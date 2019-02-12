#import necessary packages
import os
import csv

#set relative path to csv file 
csvpath = os.path.join('budget_data.csv')

#use with statement to open the file 
with open(csvpath, newline='') as filehandle:
#use csv.reader to read the contents of the file 
    budget_csv = csv.reader(filehandle, delimiter=",")
#skip header to start analysis on data values 
    SkipHeader = next(budget_csv)
#Create a count to keep track of number of cells in date column that have values
    counter = 0
#Create variable that will act as the sum of the "Porfit/loss" values 
    Profit_total = 0
#create a list that we use to hold individual profit values 
    Profit_vals = []
    Date_vals =[]
    for row in budget_csv:
#This provides a count of none empty cells in the data column which logically corresponds to a "date" value.
        if len(row[0]) > 0:
            counter += 1
#This creates a list of the "date" column values (which we will use later to reference the date corresponding to the greatest increase)
            Date_vals.append(row[0]) 
#Creates a total for the "Profit/loss column"
            Profit_total += int(row[1])
#This creates a list with the elements of the "Profit/loss" column (ordered by date)
        Profit_vals.append(int(row[1])) 
#This takes the first "Profit/loss" value from our new list and set it to a variable
    Profit_loss_start = Profit_vals[0]
#This takes the last "Profit/loss" value from our new list and set it to a variable
    Profit_loss_end = Profit_vals[len(Profit_vals) - 1]
#Define the average change as the change in value over the change in number of days 
    Average_change = (Profit_loss_end - Profit_loss_start) / (counter - 1)


print("Finacial Analysis")
print("------------------------------------")
print("Total Months: " + str(counter))
print("Total: " + "${:}".format(Profit_total))
print("Average Change: " + "${:.2f}".format(Average_change))


#Create an empty list that will hold the change in values from date to date (in order)
#create an index counter to help interate 

Profit_Change = []
index_counter = 0
for i in Profit_vals:
    if index_counter >= 1:
        Profit_Change.append(Profit_vals[index_counter] - Profit_vals[index_counter - 1])
        index_counter += 1
    else:
        index_counter += 1

#Logically/ Mathematically , the index of the maximum value in the Profit_change list will corresponds to one less than the index of the "date" where the increase happens.
#Same for index of the minimum value 
Great_In_Date = Date_vals[Profit_Change.index(max(Profit_Change)) + 1]

Great_De_Date = Date_vals[Profit_Change.index(min(Profit_Change)) + 1]




print("Greatest Increase in Profits: " + Great_In_Date + " " + "(${:})".format(max(Profit_Change)))

print("Greatest Decrease in Profits: " + Great_De_Date + " " + "(${:+})".format(min(Profit_Change)))

resultpath = os.path.join('Pybank_results.txt')
with open(resultpath, 'w') as file:
    file.write("Finacial Analysis\n")
    file.write("------------------------------------\n")
    file.write(f'Total Months: {counter}\n')
    file.write(f'Total: {"${:}".format(Profit_total)}\n')
    file.write(f'Average Change:  {"${:.2f}".format(Average_change)}\n')
    file.write(f'Greatest Increase in Profits:  {Great_In_Date} {"(${:})".format(max(Profit_Change))}\n')
    file.write(f'Greatest Decrease in Profits:  {Great_De_Date} {"(${:+})".format(min(Profit_Change))}\n')
    
    