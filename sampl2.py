import csv
with open('trial.csv','r') as f_obj:
    csvreader=csv.reader(f_obj)
    for row in csvreader:
        print(row)
