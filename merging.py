import csv

dataset_1 = []
dataset_2 = []

with open("bright_stars.csv", "r") as f:
    c = csv.reader(f)
    for i in c :
        dataset_1.append(i)

with open("stars.csv", "r") as f:
    c = csv.reader(f)
    for i in c :
        dataset_2.append(i)
        
header1  = dataset_1[0]
star_data_1  = dataset_1[1:]

header2  = dataset_2[0]
star_data_2  = dataset_2[1:]

header = header1 + header2
final_star_data = []

for i in star_data_1:
    final_star_data.append(i)
    
for i in star_data_2:
    final_star_data.append(i)
    
with open("final_data.csv","w") as f:
    c = csv.writer(f)
    c.writerow(header)
    c.writerows(final_star_data)