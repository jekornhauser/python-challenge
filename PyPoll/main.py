# -*- coding: utf-8 -*-
"""
* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:
  * The total number of votes cast
  * A complete list of candidates who received votes
  * The percentage of votes each candidate won
  * The total number of votes each candidate won
  * The winner of the election based on popular vote.
"""
# import dependencies

import os
import csv

#set file location
election_data_csv = os.path.join("Resources","election_data.csv")
with open(election_data_csv,encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    #skip header
    budget_header=next(csv_file)
    
    #establish variables
    total_votes=0
    list_of_candidates = []
    #set variables for votes each candidate won
    Khan_votes=0
    Correy_votes=0
    Li_votes=0
    OTooley_votes=0
    
    for row in csv_reader:
        #count total votes
        total_votes +=1
        #go through candidates and add new ones to list and use results to set up variables for total/percentages
        if row[2] not in list_of_candidates:
            list_of_candidates.append(row[2])
        if row[2] ==  "Khan":
            Khan_votes += 1
        if row[2] == "Li":
            Li_votes += 1
        if row[2] == "O'Tooley":
            OTooley_votes += 1
        if row[2] == "Correy":
            Correy_votes += 1
#set up percentage variable
def percentage(x,y):
    return round((x/y)*100,2)


print(f' The total number of votes cast was {int(total_votes)}.')
print(f' The complete list of candidates running was {list_of_candidates}.')
print(f" Khan had {int(Khan_votes)} votes and this was {percentage(Khan_votes,total_votes)}0% of the vote.")
print(f" Correy had {int(Correy_votes)} votes and this was {percentage(Correy_votes,total_votes)}0% of the vote.")
print(f" Li had {int(Li_votes)} votes and this was {percentage(Li_votes,total_votes)}0% of the vote.")
print(f" O'Tooley had {int(OTooley_votes)} votes and this was {percentage(OTooley_votes,total_votes)}0% of the vote.")
#winner of popular vote is highest number of votes.  Calculate this using the variables
if Khan_votes> Li_votes and Khan_votes > OTooley_votes and Khan_votes > Correy_votes:
    print(f"The winner of the election was Khan with the most votes of {int(Khan_votes)} votes.")
elif Li_votes > OTooley_votes and Li_votes > Correy_votes:
        print(f"The winner of the election was Li with the most votes of {int(Li_votes)} votes.")
elif OTooley_votes > Correy_votes:
            print(f"The winner of the election was O'Tooley with the most votes of {int(OTooley_votes)} votes.")
else: print(f"The winner of the election was Correy with the most votes of {int(Correy_votes)} votes.")

output_file= os.path.join("Analysis","results.txt")
with open(output_file, "w") as text_file:
    print(f' The total number of votes cast was {int(total_votes)}.',file=text_file)
    print(f' The complete list of candidates running was {list_of_candidates}.',file=text_file)
    print(f" Khan had {int(Khan_votes)} votes and this was {percentage(Khan_votes,total_votes)}0% of the vote.",file=text_file)
    print(f" Correy had {int(Correy_votes)} votes and this was {percentage(Correy_votes,total_votes)}0% of the vote.",file=text_file)
    print(f" Li had {int(Li_votes)} votes and this was {percentage(Li_votes,total_votes)}0% of the vote.",file=text_file)
    print(f" O'Tooley had {int(OTooley_votes)} votes and this was {percentage(OTooley_votes,total_votes)}0% of the vote.",file=text_file)
    #winner of popular vote is highest number of votes.  Calculate this using the variables
    if Khan_votes> Li_votes and Khan_votes > OTooley_votes and Khan_votes > Correy_votes:
        print(f"The winner of the election was Khan with the most votes of {int(Khan_votes)} votes.",file=text_file)
    elif Li_votes > OTooley_votes and Li_votes > Correy_votes:
        print(f"The winner of the election was Li with the most votes of {int(Li_votes)} votes.",file=text_file)
    elif OTooley_votes > Correy_votes:
            print(f"The winner of the election was O'Tooley with the most votes of {int(OTooley_votes)} votes.",file=text_file)
    else: print(f"The winner of the election was Correy with the most votes of {int(Correy_votes)} votes.",file=text_file)

