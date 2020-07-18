import csv

with open ("../PyBank/Resources/Resources_budget_data.csv") as file:
    data = csv.reader(file, delimiter = ",")
    csvheader = next(data)
    total_net = 0
    total_months= 0
    minvalues = []
    maxvalues = []
    date = []
    average_change=[]
    profit = []
    profit_change = []
    for row in data:
        total_months +=1
        minvalues.append(row)
        maxvalues.append(row)
        date.append(row[0])
        #profit.append(int(profit[row]) )- (int(profit[row-1]))
        profit.append(int(row[1]))
        total_net += int(row[1])
        average_change = sum(profit)/len(profit)
        
    for row in range (1, len(profit)):
        profit_change.append(profit[row] - profit[row-1])
        avg_profit_change = sum(profit_change)/len(profit_change)
        max_profit = max(profit_change)
        min_profit = min(profit_change)
        max_rev_date = str(date[profit_change.index(max(profit_change))])
        min_rev_date = str(date[profit_change.index(min(profit_change))])
        avg_profit_change =(round(avg_profit_change))        

print ("Financial Analysis")
print ("------------------------")
print("Total Months: " + str(total_months))
print ("Total: " + str(total_net))
print ("Average Revenue Change: " + str(round(avg_profit_change)))
#print ("increase GREAT" + str(max_rev_date))
#print (max_rev_date,"($", max_profit,")")
#print (min_rev_date, "($", min_profit,")")
print (f"Greatest Increase in Revenue", max_rev_date, "($",(max_profit), ")")


    
output_file = ("Analysis/Analysis.txt")
with open (output_file, "w", newline= "") as analysisfile:
    analysisfile.write("Financial Analysis\n")
    analysisfile.write("---------------------\n")
    analysisfile.write(f" Total Months:  {total_months}\n")
    analysisfile.write(f" Total: {total_net}\n")
    analysisfile.write(f" Average Revenue Change: {avg_profit_change}\n")
    analysisfile.write(f" Greatest Increase Revenue: {max_rev_date} ($"f" {max_profit})\n")
    analysisfile.write(f" Greatest Decrease in Revenue: {min_rev_date} ($"f"{min_profit})\n")
    
    
                       
