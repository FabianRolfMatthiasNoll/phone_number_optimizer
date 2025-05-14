# Userstories

## Persona 1: Vertriebsmitarbeiter/in (häufige Nutzung von Telefonnummern)
- **Als** Vertriebsmitarbeiter/in
- **möchte ich,** dass eingegebene Telefonnummern automatisch in separate Felder für Landesvorwahl, Ortskennzahl, Nummer und Durchwahl zerlegt und diese Informationen strukturiert angezeigt werden.
- **damit ich** schnell und einfach die relevanten Informationen für Anrufe und die Pflege der Kundendaten habe.
- **Abnahmekriterien:**
    1. **Automatische Zerlegung:** Wenn ich eine vollständige Telefonnummer (mit oder ohne Leerzeichen/Sonderzeichen als Trennzeichen) in das Telefonnummernfeld eingebe, werden die Landesvorwahl, Ortskennzahl und Nummer automatisch in die entsprechenden separaten Felder extrahiert.
    2. **Erkennung der Durchwahl:** Wenn die eingegebene Nummer eine Durchwahl enthält (erkennbar z.B. durch ein "-"), wird diese automatisch im Feld "Durchwahl" gespeichert.
    3. **Strukturierte Anzeige:** Die zerlegten Informationen (Landesvorwahl, Ortskennzahl, Nummer, ggf. Durchwahl) werden in einem übersichtlichen Format im Hauptfeld angezeigt (z.B. +[Landesvorwahl] [Ortskennzahl] [Nummer]-[Durchwahl]).
    4. **Korrektes Speichern:** Die einzelnen Komponenten der Telefonnummer (Landesvorwahl, Ortskennzahl, Nummer, Durchwahl) werden korrekt in den entsprechenden Datenbankfeldern gespeichert.
    5. **Umgang mit unvollständigen Nummern:** Wenn ich eine unvollständige Telefonnummer eingebe (z.B. nur die Ortskennzahl und Nummer), werden die entsprechenden Felder befüllt und die Anzeige im Hauptfeld erfolgt entsprechend (ohne Landesvorwahl).
    6. **Fehlerbehandlung:** Wenn ein ungültiges Format eingegeben wird, erhalte ich eine klare Fehlermeldung, die mir hilft, die Nummer korrekt einzugeben.

## Persona 2: Marketing Manager/in (Nutzung für Segmentierung und Kampagnen)
- **Als** Marketing Manager/in
- **möchte ich,** dass die Landesvorwahl der Telefonnummern separat gespeichert ist.
- **damit ich** meine Marketingkampagnen nach Ländern segmentieren und personalisieren kann.
- **Abnahmekriterien:**
    1. Separate Speicherung der Landesvorwahl: Die Landesvorwahl wird in einem eigenen, eindeutigen Feld in der Datenbank gespeichert.
    2. Filterbarkeit nach Landesvorwahl: Ich kann die Kontaktdatenbank einfach nach der Landesvorwahl filtern und segmentieren.
    3. Export mit Landesvorwahl: Beim Export von Kontaktdaten ist die Landesvorwahl als separate Spalte enthalten.

## Persona 3: Administrator/in (Verwaltung und Datenqualität)
- **Als** Administrator/in
- **möchte ich,** dass das System die korrekte Formatierung von Telefonnummern unterstützt und die Datenqualität verbessert.
- **damit** unsere Datenbank sauberer und die Kommunikation effizienter wird.
- **Abnahmekriterien:**
    1. Konsistente Formatierung: Das System stellt sicher, dass Telefonnummern im Hauptfeld immer in einem einheitlichen Format angezeigt werden.
    2. Datenvalidierung: Das System führt eine grundlegende Validierung der eingegebenen Telefonnummern durch (z.B. Mindest- und Maximalanzahl an Ziffern).
    3. Optionale Standardisierung: Es gibt idealerweise eine Option, bereits gespeicherte Telefonnummern im alten Format in das neue Format zu überführen (ggf. als Batch-Prozess).

## Persona 4: Kundenservice-Mitarbeiter/in (Identifizierung und Rückrufe)
- **Als** Kundenservice-Mitarbeiter/in
- **möchte ich,** dass die vollständige Telefonnummer schnell und deutlich angezeigt wird.
- **damit ich** Anrufer schnell identifizieren und bei Bedarf zurückrufen kann, ohne die Nummer manuell zusammensetzen zu müssen.
- **Abnahmekriterien:**
    1. Vollständige Anzeige: Die formatierte Telefonnummer (inkl. Landesvorwahl, Ortskennzahl, Nummer und ggf. Durchwahl) ist auf einen Blick im Kontaktdatenblatt sichtbar.
    2. Klick-zu-Wählen-Funktionalität (optional): Idealerweise ist die angezeigte Telefonnummer anklickbar, um direkt einen Anruf zu starten (sofern die entsprechende Software vorhanden ist).

