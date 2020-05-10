
## Stand: 02.05.2020
## Autor: Thomas Bednarski


## Build txt files for YOLOv3

import csv

## Funktion wird definiert.
def main():

	## Input Datei aus Data Augmentation
	all_labels_file = r"all_labels.csv"

	## classes.txt Datei
	classes_file = r"classes.txt"

	## Output Verzeichnis
	output_dir = "Output yolo txt/"
	class_list = []

	## Konvertiert die Namen der Klassen in classes.txt zu Zahlen (Anfang: 0) nach YOLO-Vorgabe.
	with open(classes_file,"r") as file:
		for line in file: class_list.append(line.strip())
	with open(all_labels_file, "r") as file:
		csvf = csv.reader(file)
		data = list(csvf)
		img_file = data[1][0]

		## Separiere den Inhalt der TXT-Dateien nach Bildnamen nach YOLO-Vorgabe.
		unique_images = set([x[0] for x in data[1:]])

		for image in unique_images:
      
			## Einlesen von Dateinamen ohne Dateiendung.
			fname = image.split(".",-1)[0]+'.txt'
      
			## Speichere Bildnamen in data
			found = [x for x in data if x[0]==image]
			to_save = ""
			for r in found:
				print(r)

				## Wenn xmin, ymin, xmax oder ymax aus vorheriger Data Augmentation (Assertion Error) None ergibt => Überspringe diese Zeile.
				if r[4] == '' or r[5] == '' or r[6] == '' or r[7] == '': continue
        
				## Hole Klasse aus vierter Spalte (r[3]).
				class_n = class_list.index(r[3])

				## Konvertiere xmin, ymin, xmax, ymax nach YOLO-Vorgaben um.
				xcenter = round((float(r[4])+(float(r[6])-float(r[4]))/2)/float(r[1]), 6)
				ycenter = round((float(r[5])+(float(r[7])-float(r[5]))/2)/float(r[2]), 6)
				width_bbox = round((float(r[6])-float(r[4]))/float(r[1]), 6)
				height_bbox = round((float(r[7])-float(r[5]))/float(r[2]), 6)

				## Speichere die Variablen in der Reihenfolge nach YOLO-Vorgabe.
				to_save += "{} {} {} {} {}\n".format(class_n,xcenter,ycenter,width_bbox,height_bbox)

			with open(output_dir+fname, "w") as ofile:
				## Speichere die Datei ab. Ende des Codes.
				ofile.write(to_save)

## Funktion wird ausgeführt.
if __name__=="__main__":
    main()
