# 📋 TOR Checklist — GDCC Open Data 2569

> **งานจ้างเหมาบริการสนับสนุนโครงการบริการระบบคลาวด์กลางภาครัฐ (GDCC)**
> สำหรับระบบงานทั่วไปหรือบริการข้อมูลเปิด (Open Data) ประจำปีงบประมาณ 2569
> **ผู้ว่าจ้าง:** บริษัท โทรคมนาคมแห่งชาติ จำกัด (มหาชน)

---

## 📁 Repository Structure

```
tor-checklist-gdcc/
├── docs/
│   ├── TOR_Checklist_GDCC_OpenData.md      ← Obsidian / Markdown checklist
│   └── TOR_Checklist_GDCC_OpenData.xlsx    ← Excel checklist (TH SarabunPSK)
├── source/
│   ├── TOR_GDCC_OpenData_2569.pdf          ← TOR ต้นฉบับ
│   ├── NT_ใบเสนอราคา_ตกลงราคา.pdf
│   ├── NT_หนังสือรับทราบนโยบาย.pdf
│   └── NT_เงื่อนไขแนบท้ายเชิญชวน.pdf
├── scripts/
│   └── export_xlsx.py                      ← Re-generate Excel from scratch
├── CHANGELOG.md                            ← Version history log
├── .gitignore
└── README.md
```

---

## 🏢 Companies Covered

| # | บริษัท | สถานะ |
|---|--------|--------|
| 1 | บริษัท เรด พัมพ์กิ้น จำกัด | ✅ ใช้งาน |
| 2 | บริษัท อินคอคนิโตแล็บ จำกัด | ✅ ใช้งาน |
| 3 | บริษัท ไอคอนเนื่กท์ จำกัด | ✅ ใช้งาน |

---

## 🚀 Quick Start

### Option A — Use the files directly
1. Clone this repo (see instructions below)
2. Open `docs/TOR_Checklist_GDCC_OpenData.md` in **Obsidian**
3. Open `docs/TOR_Checklist_GDCC_OpenData.xlsx` in **Microsoft Excel** or **LibreOffice Calc**

### Option B — Re-generate the Excel file
```bash
pip install openpyxl
python scripts/export_xlsx.py
```
Output will be saved to `docs/TOR_Checklist_GDCC_OpenData.xlsx`

---

## 📌 TOR Sections Covered

| ส่วน | หัวข้อ | จำนวนข้อ |
|------|--------|-----------|
| ส่วนที่ 1 | ข้อกำหนดทั่วไป (General Requirements) | 48 ข้อ |
| ส่วนที่ 2 | ข้อกำหนดด้านเทคนิค (Technical Specifications) | 5 ข้อ |
| ส่วนที่ 3 | รายการของงาน | 1 ข้อ |

---

## 🔖 Versioning Convention

This repo uses **Semantic Versioning** adapted for documents:

```
v[MAJOR].[MINOR].[PATCH]
  │        │       └─ Typo fixes, formatting corrections
  │        └───────── Content edits, new rows, company changes
  └────────────────── Major TOR revision or new fiscal year
```

**Examples:**
- `v1.0.0` — Initial release
- `v1.1.0` — Added new company column
- `v1.1.1` — Fixed typo in item 9.5
- `v2.0.0` — TOR revised for FY 2570

Tag each release:
```bash
git tag -a v1.0.0 -m "Initial release — TOR GDCC Open Data FY2569"
git push origin v1.0.0
```

---

## 🤝 Contributing / Updating Documents

1. Create a new branch named after what you're changing:
   ```bash
   git checkout -b update/add-company-4
   ```
2. Make your edits to the files in `docs/`
3. Update `CHANGELOG.md` with a summary of changes
4. Commit with a clear message:
   ```bash
   git add .
   git commit -m "feat: add บริษัท X as 4th company column"
   ```
5. Push and open a Pull Request for review

---

## 📜 License

Internal use only — บมจ. โทรคมนาคมแห่งชาติ จำกัด (มหาชน)
