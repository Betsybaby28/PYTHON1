import csv
with open('trial.csv','w',newline='') as f_obj:
    csvwriter=csv.writer(f_obj)
    header=['name','age','address']
    csvwriter.writerow(header)
    data=[['Anu',20,'EKM'],['Tom',28,'KTM']]
    csvwriter.writerows(data)