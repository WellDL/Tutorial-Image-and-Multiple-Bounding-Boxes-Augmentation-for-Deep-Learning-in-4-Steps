
## Stand: 10.05.2020
## Autor: Thomas Bednarski


## Build annotations for Detectron2

import csv

with open("all_labels.csv", 'r') as infile, open('annotations.csv', 'w', newline='') as outfile:

	## Stelle die Reihenfolge nach Detectron2 Vorgaben um.
	fieldnames = ['filename', 'xmin', 'ymin', 'xmax', 'ymax', 'class']
  
	## Lege die fieldnames als Variable fest.
	writer = csv.DictWriter(outfile, fieldnames=fieldnames)
  
	## Hole die Zeilen. Einträge sind mit ',' gekennzeichnet.   
	listInfile = csv.DictReader(infile, delimiter=',')
  
	## Schreibe Datei und Spaltenkopf als outfile
	writer.writeheader()

	for row in listInfile:
         
		## Weinn xmin, ymin, xmax oder ymax None ergibt => überspringe die Zeile mit 'continue'
		if row['xmin'] == '' or row['ymin'] == '' or row['xmax'] == '' or row['ymax'] == '':
			continue

		## Einträge unter 'filename' müssen das Verzeichnis anzeigen.
		row['filename'] = row.get('filename')

		## Lösche den key 'height'
		row.pop('height')

		## Lösche den key 'width'
		row.pop('width')

		## Schreibe die eingelesene Reihe in das outfile und wiederhole den Prozess innerhalb der For-Schleife.
		writer.writerow(row)