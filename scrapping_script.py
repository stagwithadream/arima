import csv

dataset_File=open('pollution_dataset.csv')
dataset=csv.reader(dataset_File)
list_so2=[]
list_no2=[]
list_rspm=[]
list_spm=[]
list_pm25=[]

for row in dataset:
    
    if row[3]=="Hyderabad"and row[5]=="Residential, Rural and other Areas":
        list_so2.append([row[12],row[6]])
        list_no2.append([row[12],row[7]])
        list_rspm.append([row[12],row[8]])
        list_spm.append([row[12],row[9]])
        list_pm25.append([row[12],row[11]])



with open('hyd_So2_pollution_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "So2"])
    writer.writerows(list_so2)
    
    
    
with open('hyd_No2_pollution_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "No2"])
    writer.writerows(list_no2)

with open('hyd_rspm_pollution_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Rspm"])
    writer.writerows(list_rspm)
    
with open('hyd_spm_pollution_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Spm"])
    writer.writerows(list_spm)
    
with open('hyd_pm2.5_pollution_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Pm2.5"])
    writer.writerows(list_pm25)