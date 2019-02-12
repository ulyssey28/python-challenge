#import necessary packages
import os
import csv

#set relative path to csv file 
csvpath = os.path.join('employee_data.csv')

#use with statement to open the file 
with open(csvpath, newline='') as filehandle:
#use csv.reader to read the contents of the file 
    employee_data_csv = csv.reader(filehandle, delimiter=",")
#skip header to start analysis on data values 
    SkipHeader = next(employee_data_csv)
#create a list that will hold the emp ids (in order)
    Emp_Id = []
#create a list to hold First names (in order)
    First_Name = []
#create a list to hold Last names (in order)
    Last_Name = []
#create a list to hold DOBs (in order)
    DOB = []
#create a list to hold SSNs
    SSN = []
#create a list to hold new SSNs (in order)
    new_SSN = []
#-------------------------------------------------------------------------------------------------------
    State_Abrev = []
    Name = []

    us_state_abbrev = {'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR','California': 'CA','Colorado': 'CO','Connecticut': 'CT','Delaware': 'DE','Florida': 'FL','Georgia': 'GA',
    'Hawaii': 'HI','Idaho': 'ID','Illinois': 'IL','Indiana': 'IN','Iowa': 'IA','Kansas': 'KS','Kentucky': 'KY','Louisiana': 'LA','Maine': 'ME','Maryland': 'MD','Massachusetts': 'MA',
    'Michigan': 'MI','Minnesota': 'MN','Mississippi': 'MS','Missouri': 'MO','Montana': 'MT','Nebraska': 'NE','Nevada': 'NV','New Hampshire': 'NH','New Jersey': 'NJ',
    'New Mexico': 'NM','New York': 'NY','North Carolina': 'NC','North Dakota': 'ND','Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR','Pennsylvania': 'PA','Rhode Island': 'RI',
    'South Carolina': 'SC','South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX','Utah': 'UT','Vermont': 'VT','Virginia': 'VA','Washington': 'WA','West Virginia': 'WV',
    'Wisconsin': 'WI','Wyoming': 'WY',}
    for row in employee_data_csv:
#Split the contents of the SSN column by "-" and put the values into a list.
        SSN = row[3].split("-")
#Set new_ssn list equal to the concatenation of the new format and the third values in the SSN list (in order)
        new_SSN.append("***-**-" + SSN[2])
#append emp ids (in order)
        Emp_Id.append(row[0])
#append DOBs (in order)
        DOB.append(row[2])
#Split name column into a list of two items
        Name = row[1].split(" ")
#append first items of the name lists to the first name list
        First_Name.append(Name[0])
#append Last items of the name lists to the last name list
        Last_Name.append(Name[1])
        
       
#loop through the state keys in the us_state_abbrev library
#if a key matches a value in the fifth column(state column) of a row, then append abbreviation value to the state_abrev list (in order)
        for y in us_state_abbrev:
            if row[4] == y:
                State_Abrev.append(us_state_abbrev[y])
#----------------------------------------------------------------------------------------------------------------------------------------
#Dates seem to be already reformatted for me, but if they werent you could do the following to format:
    New_DOBs = []
    for i in DOB:
        date_parts = i.split("-")
        New_dates = "/".join(date_parts)
        New_DOBs.append(New_dates)





edit_data = zip(Emp_Id, First_Name, Last_Name, New_DOBs, new_SSN, State_Abrev)

output_file = os.path.join("new_employee_data.csv")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB",
                     "SSN", "State"])

    # Write in zipped rows
    writer.writerows(edit_data)

    



        


        






