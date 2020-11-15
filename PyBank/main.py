# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 20:49:45 2020

@author: jekor
"""

# import dependencies

import os
import csv

'''task is to create a Python script that analyzes the records to calculate each of the following:
  * The total number of months included in the dataset
  * The net total amount of "Profit/Losses" over the entire period
  * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
  * The greatest increase in profits (date and amount) over the entire period
  * The greatest decrease in losses (date and amount) over the entire period
'''
# define variables
month_total=0
net_total=0
profitloss=0
delta=0
deltatracker=0
greatestincrease=-1000000000000
greatestdecrease=10000000000000


#set file location
budget_data_csv = os.path.join("Resources","budget_data.csv")
with open(budget_data_csv,encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    #skip header
    budget_header=next(csv_file)
    #set up loop through the rows
    for row in csv_reader:
        #set up month total tracker
        month_total += 1
        #set up net total
        net_total=float(net_total) + float(row[1])
        #track change in profit/losses over period
        if profitloss != 0:
            delta= float(row[1]) - float(profitloss)
            print(f' The current change in Profit/Losses is ${float(delta)}0.')
            deltatracker= float(deltatracker) + float(delta)
            profitloss=float(row[1])
            #setup greatest increase and decrease
            if float(delta)> float(greatestincrease):
                greatestincrease= float(delta)
                greatestincreasetime=row[0]
            if float(delta)< float(greatestdecrease):
                greatestdecrease= float(delta)
                greatestdecreasetime=row[0]
        else:
            profitloss=float(row[1])
        
  

average= float(deltatracker)/(float(month_total)-float(1))
average=round(float(average), 2 )         
print(f' The total number of months included in the data set is {int(month_total)} months.')
print(f' The net total amount of Profit/Losses over the entire {int(month_total)} month period is ${float(net_total)}0.') 
print(f'The total change in Profit/Losses is ${float(deltatracker)}0.  The average change in Profit/Losses was ${average}')
print(f' The greatest increase in profits over the entire period was ${float(greatestincrease)}0 and took place in {greatestincreasetime}.')
print(f' The greatest decrease in profits over the entire period was ${float(greatestdecrease)}0 and took place in {greatestdecreasetime}.')

output_file= os.path.join("Analysis","results.txt")
with open(output_file, "w") as text_file:
    print(f' The total number of months included in the data set is {int(month_total)} months.')
    print(f' The net total amount of Profit/Losses over the entire {int(month_total)} month period is ${float(net_total)}0.',file=text_file) 
    print(f'The total change in Profit/Losses is ${float(deltatracker)}0.  The average change in Profit/Losses was ${average}',file=text_file)
    print(f' The greatest increase in profits over the entire period was ${float(greatestincrease)}0 and took place in {greatestincreasetime}.',file=text_file)
    print(f' The greatest decrease in profits over the entire period was ${float(greatestdecrease)}0 and took place in {greatestdecreasetime}.',file=text_file)

    