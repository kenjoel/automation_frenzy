# This is a sample Python script.
import csv

file = "/home/kenjoel/Downloads/thikavpn.csv"
with open(file) as csv_file:
    spread_reader = csv.reader(csv_file, delimiter='|', quotechar="|")
    for i in spread_reader:
        print(', '.join(i))
