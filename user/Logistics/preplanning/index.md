# Planungsübersicht
Bei der Planungübersicht handelt es sich um ein Dispositionstool zur Erstellung und Verwaltung von Touren.
Dabei können Sendungen auf ein bestimmtes Fahrzeug innerhalb eines bestimmtes Tages disponiert werden. 

## Wo finde ich das Modul
Das Modul ist Teil des Logistics PlugIn. 
Es liegt im Tab **Disposition>Planungsübersicht**

## Erklärung
Auf der linken Seite befinden sich die Sendungen, die per Drag&Drop auf die Kombination zwischen Tag und Fahrzeug gezogen werden können. Dabei entstehen Touren.
### Begrifflichkeiten 
#### Tour:
 Eine Tour ist eine Ansammlung von Sendungen. Sie hat ein Start und Enddatum und kann 1 bis mehrere Sendungen enthalten. Eine Tour ist auch immer einer Fahrzeugresource zugewiesen
#### Sendung:
Eine Sendung ist eine Fahrt von A nach B.
#### Kontextmenü
Das Kontextmenü erscheint, wenn der Rechtsklick auf beispielsweise einer Sendung ausgelöst wird. 
Dabei enthält das Kontextmenü verschiedene Funktionen.

## Funktionen
#### Tag ändern
Die angezeigten Tagen in der Planungsübersicht können, durch das Ändern der Eigenschaften **von** und **bis** verändert werden. 

### Sendungen
#### - Sendungen filtern
Um nach bestimmten Sendungen zu suchen, kann das Suchfeld oben links genutzt werden. Sobald dort Text eingegeben wird, werden alle Sendungen angezeigt, die den Suchtext enthalten.
#### - Sendungen aktualisieren
Es gibt zwei Aktualisierungsmöglichkeiten. Bei der linken Schaltfläche werden nur die linken Sendungen aktualisiert. Bei der rechten Schaltfläche wird die komplette Planungsübersicht aktualisiert.
#### - Sendungen vertouren
Um eine Sendung zu vertouren, kann eine Sendung aus der linken Spalte per Drag and Drop auf ein Fahrzeug an ein bestimmten Tag gezogen werden. 
#### - Freitext hinzufügen
Um einen Freitext hinzufügen zu können, muss ein Rechtsklick auf die Kombination von Tag und Fahrzeug geklickt werden. Dann erscheint ein Kontextmenu, wo die Auswahlmöglichkeit **Freitext hinzufügen** steht.
#### - Container hinzufügen/entfernen
Container können bei Sendungen über das Kontextmenü hinzugefügt oder entfernt werden
#### - Reinigungsstation auswählen/entfernen
Reinigungsstationen können per Kontextmenü einer Sendung hinzugefügt oder entfernt werden.
#### - Reinigungsprozedur auswählen/entfernen
Reinigungsprozeduren können per Kontextmenü einer Sendung hinzugefügt oder entfernt werden.
#### - Uhrzeiten ändern
Die Uhrzeit für die Reinigungsstation kann über das Kontextmenü einer Sendung geändert werden
#### - Vertourung aufheben
Eine Vertourung kann über das Kontextmenü einer Sendung aufgehoben werden. Dabei wird die Sendung aus der Tour entfernt und erscheint dann wieder bei den verfügbaren Sendungen.
#### - Sendung entfernen und löschen
Eine Sendung kann über das Kontextmenü einer Sendung entfernt und gelöscht werden. Dabei wird die Sendung im Anschluss auch gelöscht. Somit erscheint diese Sendung nicht mehr bei den verfügbaren Sendungen.
#### - Tour sperren
Eine Tour kann gesperrt werden, indem ein Haken neben dem Schloss gesetzt wird. Dabei wird zwischen verschiedenen Sperrstatuswerten unterschieden. Es gibt den Sperrstatus den ein Benutzer setzen kann und ein Sperrstatus der vom System selbst gesetzt wird.
#### - Sendung in Resourcenplan überführen
Eine Sendung oder auch eine Tour kann per Drag&Drop in den Ressourcen - Planer überführt werden. Dabei wird die Tour automatisch vom System in der Planungsübersicht gesperrt.

## Troubleshooting

#### Fehlermeldung: Neustart Vorplanung
Bei dieser Fehlermeldung handelt es sich darum, dass die Verbindung zum Server nicht hergestellt werden konnte. Das kann an folgende Punkte liegen.

 - Der Applicationserver ist abgestürzt oder funktioniert nicht mehr richtig. 
		- **Potentielle Lösung:**  Überprüfen des ApplicationServer und ggf. neu starten
- Die Planungsübersicht hat kurzzeitig die Verbindung verloren 
		- **Potentielle Lösung:** Neustarten der Anwendung 
