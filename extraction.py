from pathlib import Path
import csv
import os

# get CSV file path
directry = Path(str(Path.home()) + r"\*****")
csv_list = list(directry.glob("***.csv"))

# open CSV file
csv_file = open("./*****.csv",'r')

# get row
a_list = []
for row in csv.reader(csv_file):
    a_list.append(row[10]) # specified row number (0 start) you want

# remove head row
del a_list[0]

# make text data to write to text data
a_text = ""
for a in reversed(a_list):
    a_text += a
    a_text += "\n"

# write text file
a_file = open("./*****.txt", "w")
a_file.writelines(a_text)
a_file.close()