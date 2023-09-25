import csv 
import random 

R=random.random()

filename = "Aleatorio.csv"
fields=['1']
rows=[R]

# writing to csv file
with open(filename, 'w') as csvfile:
    
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
     
    # writing the fields
    csvwriter.writerow(fields)
     
    # writing the data rows
    csvwriter.writerows(rows)

print(R)
