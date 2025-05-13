# Software‑Design‑Dokument (Kurzform) – Phone Number Optimizer

**Version:** 1.0  
**Datum:** 13. Mai 2025  
 2und2**Autor:**

---

## 1 Kontext & Ziele
Der Phone Number Optimizer ist ein Desktop‑Client, der eine eingegebene Rufnummer **validiert, zerlegt und formatiert** und zusätzlich Informationen zum **Land, zur Region bzw. zum Carrier** anzeigt. Eine Datenbank oder Netzwerkzugriffe sind **nicht** Bestandteil des Scopes.

## 2 Architekturübersicht

```text
┌────────────┐                      ┌─────────────┐
│     UI     │ ◀──────────────────▶ │   Parser    │
│ (Tk/ttk)   │     (public API)     │ (Service)   │
└────────────┘                      └─────────────┘
      ▲                                    ▲
      │ nutzt                              │ nutzt
      ▼                                    ▼
┌────────────┐                    ┌─────────────────┐
│   config   │                    │  phonenumbers   │
└────────────┘                    └─────────────────┘
```

### 2.1 Komponenten
| Komponente | Zweck |
|------------|-------|
| `ui.py` | Präsentation & Interaktion |
| `parser.py` | Service mit allen F‑Regeln + Mobil‑Aufspaltung |
| `config.py` | Globale Defaults |
| extern | `phonenumbers` (einzige Drittanbieter‑Abhängigkeit) |

## 3 Designentscheidungen

| ID | Entscheidung | Begründung | Konsequenz |
|----|--------------|------------|------------|
| D‑01 | Entkopplung UI ↔ Parser | Testbarkeit & Wiederverwendbarkeit | dünne UI, reiner Funktions‑Service – 100 % unit‑testbar |
| D‑02 | Keine Persistenz | MVP‑Scope | Spätere Erweiterung via Repository möglich |
| D‑03 | Land/Region/Carrier über Bibliotheks‑Tabellen | Wartungsfrei | Genauigkeit variiert |
| D‑04 | Aufspaltung über Bibliothek | Wartungsfrei, große Wissensbasis, hohe Korrektheit | Nicht alle Edge‑Cases abfangbar |

## 4 Parser‑Service‑API

```python
def parse_phone_number(raw: str, default_country: str = "DE") -> dict[str, str]
```

| Schlüssel | Beispiel | Beschreibung |
|-----------|----------|--------------|
| `country_code` | `+49` | E.164‑Ländercode |
| `area_code` | `1520` / `201` | Mobil‑Präfix oder Ortsvorwahl |
| `local_number` | `8596633` | Teilnehmernummer |
| `country_name` | Deutschland | Ländername |
| `area_desc` | Essen | Leer bei Mobilnummern |
| `carrier_name` | Telefónica Germany | Leer bei Festnetznummern |
| `human` | `+49 (0)1520 8596‑633` | Menschlich lesbares Format |