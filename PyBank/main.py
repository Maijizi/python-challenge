import csv
import statistics

total_net= 0
date = []
monthly_change= []
average_change= []

#open and read the csv file
with open ("03-Python_homework_PyBank_Resources_budget_data.csv",newline="") as f:
    csvreader=csv.reader(f,delimiter=",")
    next(csvreader,None)
    for rows in csvreader:
        date.append(rows[0]) 
        monthly_change.append(int(rows[1]))
        total_net=total_net+int(rows[1]) #calculate net
        
month_counter=len(date) #calculate number of months

#calculate change of profits or loss from previous month
for i in range(len(monthly_change)): 
    if i <len(monthly_change)-1:
        average_change.append(monthly_change[i+1]-monthly_change[i])

#calculate average monthly change and format 2 decimals
average_change_result="{0:.2f}".format(statistics.mean(average_change))

#find maximum change from previous month and return the month
max_change = max (average_change)
max_change_month = date[average_change.index(max_change)+1]
#find minimum change from previous month and return the month
min_change = min (average_change)
min_change_month = date[average_change.index(min_change)+1]

#print result
result=f"""Total month: {month_counter} 
Total: ${total_net} 
Average Change ${average_change_result} 
Greatest Increase in Profits: {max_change_month} (${max_change})
Greatest Decrease in Profits: {min_change_month} (${min_change})"""
print (result)

#write result into a text file
out = open ("PyBank_result.txt","w")
out.write(result)
out.close()
