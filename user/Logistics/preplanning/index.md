# Planungsübersicht
Bei der Planungübersicht handelt es sich um ein Dispositionstool, das für die Erstellung und Verwaltung von Touren zuständig ist. Hier können Sendungen auf ein bestimmtes Fahrzeug innerhalb eines bestimmtes Tages disponiert werden.  
## Wo finde ich das Modul
Das Modul ist Teil des Logistics PlugIns und ist unter **Disposition>Planungsübersicht** auffindbar. 

## Erklärung
In der Auftragsübersicht befinden sich die Sendungen, die per Drag&Drop auf das jeweilige Feld von Tag und Fahrzeug gezogen werden können, um Touren zu erstellen. 
### Begrifflichkeiten 
#### Tour:
Eine Tour ist eine Ansammlung von Sendungen, die ein Start und Enddatum aufzeigt und eine bis mehrere Sendungen enthalten kann sowie immer einer Fahrzeugressource zugewiesen ist.
#### Sendung:
Eine Sendung ist eine Fahrt von A nach B.
#### Kontextmenü
Das Kontextmenü listet mehrere Funktionen auf das durch Rechtsklick auf einer Sendung erscheint. 

## Funktionen
#### Tag ändern
Die angezeigten Tage in der Planungsübersicht können, durch das Ändern der Eigenschaften **von** und **bis** angepasst werden.

### Sendungen
#### - Sendungen filtern
Um nach bestimmten Sendungen zu suchen, kann das Suchfeld über der Auftragsübersicht genutzt werden. Es werden alle Sendungen aufgelistet, die den Suchtext enthalten.
#### - Sendungen aktualisieren

Über die linke Schaltfläche **⟳** lassen sich die Sendungen der Auftragsübersicht aktualisieren. Um die gesamte Planungsübersicht zu aktualisieren, wird die rechte Schaltfläche **🗘** gewählt. 

#### - Sendungen vertouren
Um eine Sendung zu vertouren, wird diese aus der Auftragsübersicht gewählt und per Drag and Drop auf das gewünschte Auftragsfeld zwischen Fahrzeug und Tag gezogen. 
#### - Freitext hinzufügen
Um einen Freitext hinzuzufügen, wird per Rechtsklick auf dem Feld zwischen Tag und Fahrzeug das Kontextmenü aufgerufen. Hier erscheint dann die Auswahlmöglichkeit **Freitext hinzufügen**.
#### - Container hinzufügen/entfernen
Container können unter dem Kontextmenü einer Sendung hinzugefügt oder entfernt werden.
#### - Reinigungsstation auswählen/entfernen
Reinigungsstationen können per Kontextmenü einer Sendung hinzugefügt oder entfernt werden.
#### - Reinigungsprozedur auswählen/entfernen
Reinigungsprozeduren können unter dem Kontextmenü einer Sendung hinzugefügt oder entfernt werden.
#### - Uhrzeiten ändern
Uhrzeiten können unter dem Kontextmenü einer Sendung geändert werden.
#### - Vertourung aufheben
Eine Vertourung kann über das Kontextmenü einer Sendung aufgehoben werden. Die Sendung wird aus der Tour entfernt und erscheint in der Auftragsübersicht.
#### - Sendung entfernen und löschen
Eine Sendung kann über das Kontextmenü einer Sendung gelöscht werden. Diese wird endgültig entfernt und erscheint nicht mehr in der Auftragsübersicht.
#### - Tour sperren
Eine Tour wird gesperrt, indem ein Häkchen neben dem Schloss im Auftragsfeld gesetzt wird. Es gibt den Sperrstatus den ein Benutzer setzen kann und den Sperrstatus der vom System selbst gesetzt wird. 
#### - Sendung in Resourcenplan überführen
Eine Sendung oder Tour kann per Drag&Drop in den Ressourcenplaner überführt werden. Die Tour wird automatisch in der Planungsübersicht gesperrt.

## Troubleshooting

#### Fehlermeldung: Neustart Vorplanung
Diese Fehlermeldung erscheint, wenn die Verbindung zum Server nicht hergestellt werden konnte. Das kann an folgenden Punkte liegen:

 - Der Applicationserver ist abgestürzt oder funktioniert nicht mehr richtig. 
		- **Potenzielle Lösung:**  Überprüfen des ApplicationServer und ggf. neu starten
- Die Planungsübersicht hat kurzzeitig die Verbindung verloren 
		- **Potenzielle Lösung:** Neustarten der Anwendung 
