#############################################################################
## PHASE ONE - Convert MetaData to a CSV file with just the Tile Coordinates
#############################################################################
# Step One: Import the Libraries needed
import xml.etree.ElementTree as ET
import csv
import os
import pandas as pd

#Step Two: Point to the right folders and files
metafolder = "/Volumes/Carl_Friedrich_Gauss/HET3_Whole_Depot/Metadata/3_RT_9b/"
arborfolder = "/Volumes/Carl_Friedrich_Gauss/HET3_Whole_Depot/Arborization_Quantification/"
metaname = "RT_9b.lif_RT_9b_tilescan.xml"
arborfile = "9b_Arborization.csv"
csvfile = "9b_metadata.csv"
tilefile = "9b_TilePositions.csv"
finalfile = "9b_HeatMapFinal.csv"
####
metapath = os.path.join(metafolder, metaname)
csvpath = os.path.join(metafolder, csvfile)
arborpath = os.path.join(arborfolder, arborfile)
tilepath = os.path.join(arborfolder,tilefile)
finalpath = os.path.join(arborfolder,finalfile)

# Step Three: Parse the XML document and get the root
tree = ET.parse(metapath)
root = tree.getroot()

# Step Four: Create and open a csv file
csv_output_file = open(csvpath, 'w')

# Step Five: Create a variable to write into our csv file
csvwriter = csv.writer(csv_output_file)

# Step Six: Loop for each node we want to parse
count = 0
for element in tree.findall('.//Tile'):
	List_nodes = []

	# Step Seven: Get the child nodes
	PosX = element.attrib.get('PosX')
	List_nodes.append(PosX)
	PosY = element.attrib.get('PosY')
	List_nodes.append(PosY)

	# Step Eight: Write List_nodes to csv
	csvwriter.writerow(List_nodes)

# Step Nine: Close the csv file
csv_output_file.close()

#############################################################################
## PHASE TWO - Take CSV and place tile numbers in their geometric locations
#############################################################################

# Step Ten: Read in the csv file we just made and open the arborization file
data = open(csvpath)
data = csv.reader(data, delimiter=',')
arbor = open(arborpath)
arbor = csv.reader(arbor, delimiter=',')

# Step Eleven: Declare three lists that we will fill with values from our csv file
listx = []
listy = []
listxy = []

# Step Twelve: Run a for loop that assigns the x coordinates to listx and y coordinates to listy
for row in data:
    listxy.append(row)
    valuex = row[0]
    valuey = row[1]
    if valuex in listx:
        listx = listx
    else:
        listx.append(valuex)
    if valuey in listy:
        listy = listy
    else:
        listy.append(valuey)

# Step Thirteen: Nested for loops to create a list of lists of x and y values
listofrowlists = []
for i in listy:
    listbyrow = []*len(listx)
    for j in listxy:
        if i in j:
            listbyrow.append(j[0])
    listofrowlists.append(listbyrow)

# Step Fourteen: Begin the process of composing the geometric list of tiles
myData = []
myTile = []
Length = len(listx)
ArborList = []
for row in arbor:
	ArborList.append(row[0])
Count = 0
for i in range(len(listy)):
	var = listofrowlists[i]
	listas = ['']*Length
	lists = ['']*Length
	for j in var:
		t = 0
		for m in listx:
			if float(m) < float(j):
				t += 1
		listas[t] = Count
		lists[t] = ArborList[Count]
		Count += 1
	myData.append(lists)
	myTile.append(listas)

# Step Fifteen: Write out the final file into a csv file of the tiles in their geometric position
myFile = open(finalpath, 'w')
myFile2 = open(tilepath, 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
with myFile2:
	writer = csv.writer(myFile2)
	writer.writerows(myTile)
