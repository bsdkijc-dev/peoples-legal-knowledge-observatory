# Source Assessment & Verification Report (Phase 2)

**Assessment Date:** 2026-11-23  
**Status:** SAFE MODE — Preliminary Verification (`REQUIRES HUMAN APPROVAL` before publication)

## 1. Official Portal Verification Summary

| Portal | Official URL | Verification Status | Notes |
|---|---|---|---|
| **Database Peraturan BPK (JDIH BPK)** | https://peraturan.bpk.go.id/ | `VERIFIED` | Accessible; provides consolidated metadata, effective dates, repeal/amendment links, and MK judicial review notes. |
| **JDIHN (BPHN)** | https://jdihn.go.id/ | `VERIFIED` | Accessible; national legal documentation network. |
| **Mahkamah Agung RI (e-Court / Badilum / Badilag / Kepaniteraan)** | https://ecourt.mahkamahagung.go.id/ | `VERIFIED` | Accessible; official electronic court registration, Badilum, Badilag, and Kepaniteraan portals verified. |
| **Mahkamah Konstitusi RI (MKRI)** | https://www.mkri.id/ | `VERIFIED` | Accessible; official constitutional review decisions (`Putusan`) available. |
| **BPHN & SIDBANKUM** | https://bphn.go.id/ & https://sidbankum.kemenkum.go.id/ | `VERIFIED` | Accessible; lists accredited Legal Aid Organizations (OBH 2025–2027, 777 active OBH recorded). |
| **Direktori Putusan MA RI** | https://putusan3.mahkamahagung.go.id | `UNVERIFIED_IN_SESSION` | Returned empty search index results during this session; requires direct browser verification before automated extraction. |

## 2. Critical Legal Status Findings (2026)

1. **Labour Law (`LK05`)**: [UU No. 27 Tahun 2026 tentang Pelindungan Ketenagakerjaan](https://peraturan.bpk.go.id/Details/359755/uu-no-27-tahun-2026-pelindungan-ketenagakerjaan) took effect on **2026-10-28**. It explicitly **revokes** [UU No. 13 Tahun 2003](https://peraturan.bpk.go.id/Details/43013/uu-no-13-tahun-2003) and Chapter IV (Article 80(a) & Article 81) of [UU No. 6 Tahun 2023](https://peraturan.bpk.go.id/Details/246523/uu-no-6-tahun-2023), following up Constitutional Court Decision No. 168/PUU-XXI/2023. Any public guide citing UU 13/2003 as active law is outdated.
2. **Criminal Code (`LK03`)**: [UU No. 1 Tahun 2023 tentang KUHP](https://peraturan.bpk.go.id/Details/234935/uu-no-1-tahun-2023) took effect on **2026-01-02**, as amended by [UU No. 1 Tahun 2026 tentang Penyesuaian Pidana](https://peraturan.bpk.go.id/Details/337869/uu-no-1-tahun-2026) (effective **2026-01-02**).
3. **Electronic Information & Digital Rights (`LK11`)**: [UU No. 1 Tahun 2024 tentang Perubahan Kedua atas UU ITE](https://peraturan.bpk.go.id/Details/274494/uu-no-1-tahun-2024) (effective **2024-01-02**) is subject to conditional constitutional interpretations under MKRI rulings (e.g., Putusan No. 105/PUU-XXII/2024 and 115/PUU-XXII/2024). Similarly, [UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi](https://peraturan.bpk.go.id/Details/229798/uu-no-27-tahun-2022) has an MKRI ruling on Article 53(1)(b).
4. **Consumer Protection (`LK09`)**: [UU No. 8 Tahun 1999](https://peraturan.bpk.go.id/Details/45288/uu-no-8-tahun-1999) remains in force; a judicial review petition ([Putusan MK No. 235/PUU-XXIII/2025](https://s.mkri.id/public/content/persidangan/putusan/putusan_mkri_13756_1770022399.pdf)) is noted for human legal review.

## 3. Uncertainties & Human Review Flags
- Implementing regulations (`Peraturan Pelaksanaan`) for `UU No. 27 Tahun 2026` have a 1-year statutory window from promulgation (`2026-10-28`); transitional rules require human legal verification.
- Exact local court fee schedules (`panjar biaya perkara`) vary by Pengadilan Negeri/Agama and must never be hardcoded without checking the specific court's official SK.
