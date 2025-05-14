# Spezifikation

## Funktion und Umfang.
Es soll eine leichtgewichtige Anwendung erstellt werden, die eine eingegebene Telefonnummer in einzelne Bestandteile zerlegt und die Bestandteile, sowie eine einheitlich formatierte Version der Nummer anzeigt.

Eine eingegebene Nummer wird aufgeteilt in die Bestandteile Ländervorwahl, Ortskennzahl / Anbietercode, Nummer und Durchwahl. Bei Festnetznummern wird die Ortskennzahl erkannt und bei Handynummern Informationen über den Anbieter. Zusätzlich wird die Nummer im standardisierten Format E.164 ausgegeben. Zur Installation muss nur die exe-Datei heruntergeladen werden.

## Detaillierte Anforderungen
- **Erlaubte Zeichen:** Ziffern von 0-9, Leerzeichen und die Zeichen `. - / ( ) [ ] +` können eingegeben werden.
- **Ländervorwahl:** Die Ländervorwahl wird durch ein vorhergehendes + oder 00 erkannt.
- **Klammern:** Klammern können optional verwendet werden um die Ortsvorwahl zu markieren, sie soll allerdings auch ohne Klammern erkannt werden.
- **Trennzeichen:** Die Trennzeichen `. + / -` können als Trennzeichen verwendet werden, sind aber optional.
- **Durchwahl:** Wenn sich 3 oder weniger Ziffern nach dem letzten Trennzeichen befinden, werden sie als Durchwahl erkannt.
- **Standardvorwahl:** Wenn keine Ländervorwahl angegeben wird, wird die Standardvorwahl (DE) verwendet.
- **Formatierung:** Telefonnummern werden einheitlich formatiert in E.164 formatiert angezeigt.

## Akzeptanzkriterien
- Beim Drücken des Knopfes "Analysiere", wird die Nummer aufgeteilt in die Bestandteile und die Textfelder werden ausgefüllt.
- Eine Durchwahl wird erkannt und separat angezeigt.
- Für nicht eindeutige Eingaben werden aller erkennbaren Bestandteile eingetragen und der Rest leer gelassen.
- Ungültige Eingaben geben eine hilfreiche Fehlermeldung.


