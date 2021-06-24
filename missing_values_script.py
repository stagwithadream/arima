import csv

dataset_File=open('scrapped datasets/hyd_So2_pollution_data.csv')
dataset=csv.reader(dataset_File)

complete_list=[]
temp=0
for row in dataset:
    
    if row[1]=="NA" or row[1]=="":
        complete_list.append([row[0],str(temp)])
    else:
        complete_list.append([row[0],row[1]])
        temp=row[1]
        
        
with open('scrapped datasets/completeValues/hyd_So2_pollution_data_completeValues.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "So2"])
    writer.writerows(complete_list)