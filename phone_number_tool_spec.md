Phone Number Optimizer Tool – Specification v1.1
===============================================

1  Purpose & Scope
------------------
A lightweight **desktop application** (single `.exe`, packaged via PyInstaller) that lets a user enter **one phone number** and instantly shows  
* the *split components*  
   – Country code (e.g. “+49”)  
  – Area code (e.g. “711”)  
  – Local subscriber number (e.g. “1234567”)  
  – Extension (optional, e.g. “34”)  
* one *uniform, nicely formatted* version (E.164 by default, human‑friendly variant optional).  

No installation required beyond copying the `.exe`.

2  Functional Rules
-------------------
| ID  | Rule | Notes / Skeptical Considerations |
|-----|------|----------------------------------|
| F‑01 | **Allowed characters** in user input: digits 0‑9, blanks, and `. – / ( ) [ ] +`. | Avoid hard‑coding, future‑proof. |
| F‑02 | **Country code** may start with **“+”** *or* with the *international call prefix* **“00”** (e.g. `0049` ⇒ `+49`). | Strip leading **00** and convert to `+`. |
| F‑03 | Support full **E.164** numbers (`+497111234567`), including optional ext (`;ext=34`). | Use `phonenumbers` formatting helpers. |
| F‑04 | **Parentheses** around the area code are *optional*; treat them only as hints. | Don’t rely on them exclusively. |
| F‑05 | Any of `. / -` may separate segments. None of them is mandatory. | Implement fallback parsing. |
| F‑06 | ≤3 trailing digits *after* a separator → suspect **extension**. | Beware 2‑/3‑digit mobile suffixes – provide test data. |
| F‑07 | If **no country code** is supplied, fall back to a **configurable default** (factory setting `DE`). | Exposed in a config‑file or UI drop‑down. |
| F‑08 | **Validation**: use `phonenumbers` for per‑country length checks. | Show friendly error, not raw regex. |
| F‑09 | **Consistent output**: Display E.164 (`+49 711 1234567‑34`) and a human format (`+49 (0)711 123‑4567‑34`). | Skip empty segments. |
| F‑10 | **Storage** (optional but recommended): SQLite DB with columns `country_iso, country_code, area_code, local_number, extension, raw_input, formatted`. | Enables later reuse by CRM. |

3  Acceptance Criteria
----------------------
* **AC‑1** On “Analyse” click (or focus‑leave) the number is auto‑split and fields are populated.  
* **AC‑2** An extension is detected and shown separately.  
* **AC‑3** The formatted number (E.164) appears in a read‑only field. *(Click‑to‑dial deliberately **NOT** implemented).*  
* **AC‑4** Components are stored in the SQLite DB (when user presses “Save”).  
* **AC‑5** For incomplete inputs the parser fills what it can; missing parts stay empty.  
* **AC‑6** Invalid inputs raise a conspicuous error box with guidance.  

4  Technical Framework
----------------------
| Aspect | Decision |
|--------|----------|
| **GUI** | `Tkinter` (or `PySimpleGUI` for quicker layout). |
| **Parsing** | `phonenumbers` + custom heuristics for extensions & missing country code. |
| **Packaging** | `pyinstaller --onefile --noconsole main.py`. |
| **Code Modules** | `ui.py`, `parser.py`, `storage.py`, `config.py`, `main.py`, plus `tests/`. |
| **Logging** | `error.log` in the executable’s directory. |
| **Localization** | All UI strings in German; ready for i18n (gettext). |

5  UI Sketch (ASCII)
--------------------
```
┌────────────────────────────────────────────┐
│ Telefonnummer: [____________________]      │
│ [Analysieren]                              │
├────────────────────────────────────────────┤
│ Landesvorwahl:   [+49]                     │
│ Ortskennzahl:    [711]                     │
│ Nummer:          [1234567]                 │
│ Durchwahl:       [34]                      │
├────────────────────────────────────────────┤
│ E.164 Format:    +49711123456734           │
│ Lesbares Format: +49 (0)711 123‑4567‑34    │
│ [Speichern]                                │
└────────────────────────────────────────────┘
│ Meldungsbereich / Fehlerausgabe            │
└────────────────────────────────────────────┘
```
