"""
Redact all price-related text (¥ symbol and associated numbers) from an OCR'd PDF.
Draws white rectangles over matched text spans, then saves a flattened copy.

Usage:
    pip install pymupdf
    python redact_prices.py input.pdf output_redacted.pdf
"""

import sys
import re
import fitz  # PyMuPDF

# ── patterns ──────────────────────────────────────────────────────────────────
# Matches: ¥1,234,567  /  ¥1234567  /  ¥123  /  ￥...  /  standalone ¥
PRICE_RE = re.compile(
    r'[¥￥]\s*[\d,，．.]+(?:[,，]\d{3})*'   # ¥ followed by digits/commas
    r'|[¥￥]'                                  # standalone ¥ / ￥
)

# Also catch bare numbers that follow a ¥ on a nearby word boundary
# (OCR sometimes splits "¥" and "1,234" into separate spans)
LEADING_YEN  = re.compile(r'^[¥￥]\s*$')          # span is just the ¥ symbol
PRICE_NUMBER = re.compile(r'^[\d,，．]+(?:[,，]\d{3})*$')  # span is just a number

WHITE = (1, 1, 1)   # RGB white
EXPAND = 1.5        # px padding around each matched rect


def redact_page(page: fitz.Page) -> int:
    """Find and white-out all price text on a page. Returns count of redactions."""
    count = 0
    blocks = page.get_text("rawdict", flags=fitz.TEXT_PRESERVE_WHITESPACE)["blocks"]

    rects_to_cover: list[fitz.Rect] = []
    pending_yen_rect: fitz.Rect | None = None   # track isolated ¥ spans

    for block in blocks:
        if block.get("type") != 0:   # 0 = text block
            continue
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                text = span.get("text", "")
                bbox = fitz.Rect(span["bbox"])

                # Case 1: span contains ¥ + digits (common in well-OCR'd PDFs)
                if PRICE_RE.search(text):
                    rects_to_cover.append(bbox.expand(EXPAND))
                    pending_yen_rect = None
                    count += 1
                    continue

                # Case 2: span is just a ¥ symbol – remember it, next number gets covered too
                if LEADING_YEN.match(text.strip()):
                    pending_yen_rect = bbox
                    rects_to_cover.append(bbox.expand(EXPAND))
                    count += 1
                    continue

                # Case 3: span looks like a bare number right after a ¥ span
                if pending_yen_rect is not None and PRICE_NUMBER.match(text.strip()):
                    rects_to_cover.append(bbox.expand(EXPAND))
                    count += 1
                    pending_yen_rect = None
                    continue

                pending_yen_rect = None

    # Draw white rectangles over every matched region
    for rect in rects_to_cover:
        page.draw_rect(rect, color=WHITE, fill=WHITE, overlay=True)

    return count


def redact_pdf(src: str, dst: str) -> None:
    doc = fitz.open(src)
    total = 0
    for i, page in enumerate(doc, start=1):
        n = redact_page(page)
        total += n
        if n:
            print(f"  page {i:>4}: {n} redaction(s)")

    print(f"\nTotal redactions: {total}")
    # Save with garbage collection + deflate – flattens drawn content into page stream
    doc.save(dst, garbage=4, deflate=True, clean=True)
    doc.close()
    print(f"Saved → {dst}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python redact_prices.py input.pdf output_redacted.pdf")
        sys.exit(1)
    src, dst = sys.argv[1], sys.argv[2]
    print(f"Processing: {src}")
    redact_pdf(src, dst)
