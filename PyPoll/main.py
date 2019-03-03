# Importing libraries to work with CSV file
import os
import csv

# Setting up file path where out CSV file located
file_path = os.path.join('Resources', 'election_data.csv')

# Opening file and reading data, setting up encoding
with open(file_path, 'r' , encoding = 'utf-8-sig', errors = 'ignore') as csvfile:
    file_data = csv.reader(csvfile, delimiter=',')

    # Reading the headers in file
    csv_header = next(file_data)
    
    # Declaring dictionary we will be using to store data as "Name":number_of_votes
    candidats = {}
    
    # Variable to store number of rows or number of votes
    row_num = 0
    
    # Going throuhg each row or the file, counting amoount of rows
    # If dictionary does not contain candidat listed in curent row we add new record to dictionary with his name and one vote
    # If dictionary does have such name we simply add one more vote to that person
    for line in file_data:
        row_num += 1
        if line[2] not in candidats:
            candidats[line[2]] = 1
        else:
            candidats[line[2]] += 1 

    # Printing custom info and number of votes
    print('Election Results')
    print('---------------------')
    print(f'Total Votes: {row_num}')
    print('---------------------')
    
    # Iterating through dictionary and printing results as Name: percentage (count_of_votes)
    for key, value in candidats.items():
        print (f'{key}: {str(round(value/row_num*100,3))}% ({value})')

    print('---------------------')
    # Looking for max value in keys and printing it's key name
    print (f'Winner: {max(candidats, key=candidats.get)}')
    print('---------------------')

    # Printing same info to the file
    with open("Output.txt", "w") as text_file:
        print('Election Results', file=text_file)
        print('---------------------', file=text_file)
        print(f'Total Votes: {row_num}', file=text_file)
        print('---------------------', file=text_file)
        for key, value in candidats.items():
            print (f'{key}: {str(round(value/row_num*100,3))}% ({value})', file=text_file)
        print('---------------------', file=text_file)
        print (f'Winner: {max(candidats, key=candidats.get)}', file=text_file)
        print('---------------------', file=text_file)