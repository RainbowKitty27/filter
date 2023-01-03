import csv
rows=[]
with open("final.csv","r") as f:
  csvreader=csv.reader(f)
  for row in csvreader:
    rows.append(row)
headers=rows[0]
data_rows=rows[1:]
print(headers)
print(data_rows[2])
import enum
temp_data_rows=list(data_rows)
for data in temp_data_rows:
  if data[1].lower()=="hd 100546 b":
    data_rows.remove(data)
  if data[4].lower()=="0":
    data_rows.remove(data)
  if data[3].lower()=="40 + 39 +\xa0?":
    data_rows.remove(data)

masses=[]
radii=[]
names=[]
for data in data_rows:
  masses.append(data[3])
  radii.append(data[4])
  names.append(data[1])
star_gravity=[]
for index,name in enumerate(names):
  gravity=(float(masses[index])*1.989e+30)/((float(radii[index])*6.957e+8)*float(radii[index])*6.957e+8)*6.674e-11
  star_gravity.append(gravity)
filter=[]
if gravity>=150 and gravity<=350:
  if data[2]<=100:
    filter.append(rows[index])
print(len(filter))