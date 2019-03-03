# Importing libraries to work with CSV file
import os
import csv

# Setting up file path where out CSV file located
file_path = os.path.join('Resources', 'budget_data.csv')

# Opening file and reading data, setting up encoding
with open(file_path, 'r' , encoding = 'utf-8-sig', errors = 'ignore') as csvfile:
    file_data = csv.reader(csvfile, delimiter=',')

    # Reading the headers in file
    csv_header = next(file_data)

    # saving all rows of the file into info list, we will get a list of lists   
    info = [line for line in file_data]
    
    # Printing Title
    print ('Financial Analysis')
    print ('-------------------------')
    # Total number of month equals number of elements in info list
    print (f'Total Months: {len(info)}')
    
    # To get Net Total we summarizing a second element of each list in main list called info
    net_total = sum([int(element[1]) for element in info])
    print (f'Total: ${net_total}')
   
    # Separating nested lists into two separate lists of dates and profits 
    list_dates = [element[0] for element in info]
    list_profits = [int(element[1]) for element in info]
    
    # New list - will contain changes in profits
    list_profit_change = []

    # Going through all elements, calculating the change and saving in new list called list_profit_change
    for i in range(len(list_profits) - 1):
        list_profit_change.append(list_profits[i+1] - list_profits[i])
    
    # Calculating what is he averige change, rounding it to 2 decimals and printing it
    averige_change = str(round(sum(list_profit_change) / len(list_profit_change),2))
    print(f'Average  Change: ${averige_change}')
            
    # Calculating max change, getting it's index number and printing info
    max_change = max(list_profit_change)
    max_change_index = list_profit_change.index(max(list_profit_change))
    print (f'Greatest Increase in Profits: {list_dates[max_change_index + 1]} (${max_change})')

    # Calculating min change, getting it's index number and printing info
    min_change = min(list_profit_change)
    min_change_index = min_change_index = list_profit_change.index(min(list_profit_change))
    print (f'Greatest Decrease in Profits: {list_dates[min_change_index + 1]} (${min_change})')

    # printing same data into text file
    with open("Output.txt", "w") as text_file:
        print(f'Financial Analysis', file=text_file)
        print(f'-------------------------', file=text_file)
        print(f'Total Months: {len(info)}', file=text_file)
        print (f'Total: ${net_total}', file=text_file)
        print(f'Average  Change: ${averige_change}', file=text_file)
        print(f'Greatest Increase in Profits: {list_dates[max_change_index + 1]} (${max_change})', file=text_file)
        print(f'Greatest Decrease in Profits: {list_dates[min_change_index + 1]} (${min_change})', file=text_file)