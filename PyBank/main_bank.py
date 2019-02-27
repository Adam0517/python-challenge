import os
import csv

file_path=os.path.join("budget_data.csv")

with open(file_path,newline="") as cvsfile :
    budget = csv.reader(cvsfile, delimiter=",")
    budget_header=next(budget)

#Create two empty list to store each row data
    month_cost = []
    every_date = []
    
    for row in budget:
        every_date.append(row[0])
        month_cost.append(int(row[1]))

#Total number of months
total_num = len(every_date)

#Net total amount of Profit/Losses
total_amount = sum(month_cost)

#Average of the changes in Profit/Losses
#Create a past_cost to store last month profits/losses
past_cost = [0]
past_cost.extend(month_cost)
past_cost = past_cost[0:total_num]

month_change = []
sum_changes = 0

#To calculate the difference between current_month and last month profits/losses
for i in range(1,total_num) :
    month_change.append(month_cost[i]-past_cost[i])
    sum_changes += month_change[i-1]

average_change = sum_changes/(total_num-1)

#Find Greate Increase and Decrease in profits/losses
G_increase = max(month_change)
G_decrease = min(month_change)

print("Financial Analysis")
print(f"--------------------------------------")
print(f"Total Months : {total_num}")
print(f"Total : ${total_amount}")
print(f"Average Change : ${round(average_change,2)}")
print(f"Greatest Increase in Profits : {every_date[month_change.index(G_increase)+1]} (${G_increase})")
print(f"Greatest Decrease in Profits : {every_date[month_change.index(G_decrease)+1]} (${G_decrease})")

#Export a txt file
result = open("PyBank_result.txt","w")
line1 = "Financial Analysis \n"
line2 = f"-------------------------------------- \n"
line3 = f"Total Months : {total_num} \n"
line4 = f"Total : ${total_amount} \n"
line5 = f"Average Change : ${round(average_change,2)} \n"
line6 = f"Greatest Increase in Profits : {every_date[month_change.index(G_increase)+1]} (${G_increase}) \n"
line7 = f"Greatest Decrease in Profits : {every_date[month_change.index(G_decrease)+1]} (${G_decrease}) \n"

result.write(line1)
result.write(line2)
result.write(line3)
result.write(line4)
result.write(line5)
result.write(line6)
result.write(line7)
result.close()
