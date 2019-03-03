us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Importing libraries to work with CSV file
import os
import csv
import datetime

# file with data is in the same folder (employee_data1.csv and employee_data2.csv weren't provided so worked with what's been available on GitLab)
file_path = 'employee_data.csv'
output_path = 'output.csv'

# Opening file as CSV to read data from 
with open(file_path, 'r' , encoding = 'utf-8-sig', errors = 'ignore') as csvfile:
    file_data = csv.reader(csvfile, delimiter=',')

    # Reading headers
    csv_header = next(file_data)
    
    # Opening file to write data into
    with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        
        # Writing new custom headers
        csvwriter.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
        
        # Iterating for the amount of rows in original file we read
        for line in file_data:
            
            # Declaring new list, this will be "one record at the time" we write into output file
            output_str = []
            
            # Employee ID stays the same
            output_str.append(line[0])

            # Splitting First and Last names into separate list and adding them to output list
            output_str.extend(str.split(line[1]))

            # Using library datetime we change format of the date and add it to output list
            output_str.append(datetime.datetime.strptime(line[2], '%Y-%m-%d').strftime('%m/%d/%Y'))

            # Masking SSN numbers using string with asterisks and dashes, adding last 4 numbers as wild card
            output_str.append("***-**-" + line[3][-4:])
            
            # Appending state abbreviation using dictionary
            output_str.append(us_state_abbrev[line[4]])            
            
            # Writing curent list into output file
            csvwriter.writerow(output_str)
        print ('Conversion completed successfully! Please open output.csv file.')