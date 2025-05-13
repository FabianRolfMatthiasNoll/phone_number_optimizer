# Testplan – Phone Number Optimizer

**Version:** 1.1  
**Datum:** 13. Mai 2025
**Autor:** 2und2

---

## 1 Ziele
* Nachweis der Einhaltung der Funktionsregeln F‑01 … F‑09  
* Validierung der Mobil‑Aufspaltung und Zusatzinformationen  
* Basis‑Smoke‑Test der UI‑Integration  
* Automatisierte Reports (Unit-Test & Coverage‑HTML) pro Release‑Build

## 2 Testobjekte
* `parser.py` – **Unit‑Ebene**  
* `ui.App` – **Smoke‑Ebene**

## 3 Strategie
| Ebene | Technik | Werkzeug |
|-------|---------|----------|
| Unit | parametrisierte Assertions | `pytest` |
| Integration | GUI‑Smoke (Parser ↔ UI) | manuell |
| Reporting | JUnit XML + HTML‑Coverage | `pytest --junitxml` + `pytest-cov` |

## 4 Abdeckungskriterien
* erlaubte / unerlaubte Zeichen (F‑01)  
* 00‑Prefix‑Regel (F‑02)  
* Durchwahl‑Parsing (F‑06)  
* Mobil‑Split‑Präfixe 15xx / 16xx / 17xx  
* Fehlerfälle: UK‑ & IN‑Beispiele  
* **Coverage‑Ziel:** ≥ 90 % Lines in `parser.py`

## 5 Testumgebung
* Python 3.12  
* phonenumbers ≥ 8.13  
* OS: Windows 10 & macOS 14  
* Zusatz‑Pakete: `pytest`, `pytest-cov`, optional `pytest-html`, `pytest-qt`

## 6 Ausführungs‑ & Reporting‑Workflow

```bash
# 1. Install test deps
pip install -r requirements.txt pytest pytest-cov pytest-html

# 2. Run complete suite with reports
pytest -q   --junitxml build/test-results.xml   --html build/report.html --self-contained-html   --cov=phone_number_optimizer --cov-report=html --cov-report=xml
```

* `build/test-results.xml` → CI‑Server importiert als Testreport  
* `build/report.html`    → menschenlesbarer Überblick  
* `htmlcov/`         → interaktive Coverage‑Ansicht (`index.html`)

## 7 Erfolgs‑/Fehlschlagkriterien
* **Alle** Unit‑ und Smoke‑Tests sind grün.  
* Coverage ≥ 90 % (hard threshold im CI).  
* Keine ungefangenen Tracebacks bei manueller GUI‑Smoke.

## 8 Risiken
* Carrier‑Daten können nach Rufnummernmitnahme veraltet sein.  
* Geocoder liefert bei kleinen Orten nur das Bundesland.

## Coverage-Ergebnisse (Stand 13 Mai 2025)

| Modul                     | Statements | Fehlende | Abdeckung |
|---------------------------|-----------:|---------:|----------:|
| `parser.py`               | 55         | 4        | **93 %** |
| `tests/test_parser.py`    | 12         | 0        | 100 % |
| **Gesamt**                | 67         | 4        | **94 %** |

*Die angestrebte Mindestabdeckung von 90 % wurde erreicht.*  
Der Threshold in der CI kann somit auf `--cov-fail-under=90` gesetzt bleiben.
