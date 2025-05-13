# Deployment und Rollout

**Version:** 1.0  
**Datum:** 13. Mai 2025  
**Autor:**  2und2

## Deployment

Die Applikation wird als `.exe`-Datei bereitgestellt, die direkt ausführbar ist – ohne Installation und ohne externe Abhängigkeiten.
Der Download-Link wird mit jeder neuen Version veröffentlicht.

- Der Quellcode ist auf GitHub verfügbar
- Jede Release-Version erhält einen Git-Tag nach dem Schema `vX.Y`
- Die `.exe`-Datei wird ebenfalls auf GitHub bereitgestellt.
- Der Release enthält:
  - einen Link zur `.exe`-Datei,
  - den Source Code der jeweiligen Version
  - Changelog und Versionshinweise.

## Rollout-Plan

1. **Release veröffentlichen**
   - Neues GitHub Release mit Tag `vX.Y` bereitstellen
   - `.exe`-Datei erstellen und in Repository hochladen
   - Changelog und bekannte Änderungen beilegen

2. **Kommunikation**
   - Nutzer per E-Mail über neue Version informieren

3. **Nutzung durch Anwender**
   - Nutzer laden `.exe` herunter.
   - Ausführung direkt per Doppelklick – keine Installation, keine Abhängigkeiten.

4. **(Optional) Alte Versionen**
   - Vorherige `.exe`-Versionen zugänglich halten.
   - Archivseite oder Abschnitt mit älteren Releases im Repository pflegen.