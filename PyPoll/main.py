#import necessary packages
import os
import csv
from collections import OrderedDict

#set relative path to csv file 
csvpath = os.path.join('election_data.csv')

#use with statement to open the file 
with open(csvpath, newline='') as filehandle:
#use csv.reader to read the contents of the file 
    election_csv = csv.reader(filehandle, delimiter=",")
#skip header to start analysis on data values 
    SkipHeader = next(election_csv)
#Creates a list of voter ids per candidate 
    Khan_voters = []
    Correy_voters = []
    Li_voters = []
    Tooley_voters = []
#creates a counter for the number of people who have voted
    Num_voters = 0 

    for row in election_csv:
        if len(row[0]) > 0:
            Num_voters += 1
        if row[2] =="Khan":
            Khan_voters.append(row[0])
        elif row[2] == "Correy":
            Correy_voters.append(row[0])
        elif row[2] == "Li":
            Li_voters.append(row[0])
        elif row[2] == "O'Tooley":
            Tooley_voters.append(row[0])

num_Khan_votes = len(Khan_voters)

num_Correy_votes = len(Correy_voters)

num_Li_votes = len(Li_voters)

num_Tooley_votes = len(Tooley_voters)



#Percents are calculated using the number of votes for a personn divided by num_voters
Khan_percent = num_Khan_votes / Num_voters
Correy_percent = num_Correy_votes / Num_voters
Li_percent = num_Li_votes/ Num_voters
Tooley_percent = num_Tooley_votes/ Num_voters


#create a dictionary with the percent values as keys matching them to the candidates 
Percent_Candidate = {}
Percent_Candidate[Khan_percent] = "Khan"
Percent_Candidate[Correy_percent] = "Correy"
Percent_Candidate[Li_percent] = "Li"
Percent_Candidate[Tooley_percent] = "O'Tooley"

Percent_list = [Khan_percent, Correy_percent, Li_percent, Tooley_percent]


print("Election Results")

print("-------------------------")

print("Total Votes: " + str(Num_voters))

print("-------------------------")

print("Khan: " + "{:.3%}".format(Khan_percent) + " " + "({:})".format(num_Khan_votes))

print("Correy: " + "{:.3%}".format(Correy_percent) + " " + "({:})".format(num_Correy_votes))

print("Li: " + "{:.3%}".format(Li_percent) + " " + "({:})".format(num_Li_votes))

print("O'Tooley: " + "{:.3%}".format(Tooley_percent) + " " + "({:})".format(num_Tooley_votes))

print("-------------------------")

print("Winner: " + Percent_Candidate[max(Percent_list)] )

print("-------------------------")


line3 = "Total Votes: " + str(Num_voters)
line5 = "Khan: " + "{:.3%}".format(Khan_percent) + " " + "({:})".format(num_Khan_votes)
line6 = "Correy: " + "{:.3%}".format(Correy_percent) + " " + "({:})".format(num_Correy_votes)
line7 = "Li: " + "{:.3%}".format(Li_percent) + " " + "({:})".format(num_Li_votes)
line8 = "O'Tooley: " + "{:.3%}".format(Tooley_percent) + " " + "({:})".format(num_Tooley_votes)
line9 = "-------------------------"
line10 = "Winner: " + Percent_Candidate[max(Percent_list)]
line11 = "-------------------------"

resultpath = os.path.join('Pypoll_results.txt')
with open(resultpath, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f'{line3}\n')
    file.write("-------------------------\n")
    file.write(f'{line5}\n')
    file.write(f'{line6}\n')
    file.write(f'{line7}\n')
    file.write(f'{line8}\n')
    file.write(f'{line9}\n')
    file.write(f'{line10}\n')
    file.write(f'{line11}\n')


