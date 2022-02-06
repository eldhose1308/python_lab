import csv
with open('csv.txt') as inf:
 content = csv.DictReader(inf)

 print("Department")

 for row in content:
   print(row["Department"])
    
