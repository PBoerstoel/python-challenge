#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


filepath = '/Users/boers/Documents/bootcamp/Python-challenge/python_challenge/PyBank/Resources/budget_data.csv' #filepath on my pc


# In[3]:


with open(filepath, newline='') as f:
    reader = csv.reader(f)
    data = list(reader) #load csv into a list, in this case it turned out to be a nested list, with each entry being a list
                        #with first (zeroth) entry being the month and the second(first) entry being the profit/loss


# In[8]:


num_months=len(data)-1 #num of rows -1 for header
total=0 
greatchange=0
lowchange=0 #define variables for total profit, greatest increase, and greatest decrease respectively
for i in range(num_months):
    total = total + int(data[i+1][1]) #for loop to add the total profit
change=[] #create empty list to fill up later with all the changes
changetot=0 #define variable for total change
for i in range(num_months-1): #num_months-1 because there will be one less grouping of two subsequent months than there are months
    change.append(int(data[i+2][1])-int(data[i+1][1])) #append change list with the change between the month and the one before it
    if change[i]>greatchange:
        greatchange = change[i]
        greatchangedate = data[i+2][0] #If statement checks if the change is greater then the previously logged greatest change,
                                        #And if so changes both the change and the corresponding date to that new change entry
    if change[i]<lowchange: 
        lowchange=change[i]
        lowchangedate = data[i+2][0] #Same as previous if statement but for lowest change
    changetot=changetot+change[i] #adds change to current change total
averagechange=changetot/(num_months-1) #Divides total change by change periods to get the average


# In[18]:


#creating strings to write to terminal and txt file
Fin_an1 = "Financial analysis \n __________ \n Total months: " + str(num_months) + "\n Total: $" + str(total)
Fin_an2 = "\n Average change : $" + str(averagechange) + "\n Greatest Increase in Profits : " + str(greatchangedate) + " $" +str(greatchange)
Fin_an3 = "\n Greatest Decrease in Profits : " + str(lowchangedate) + " $" + str(lowchange)
Fin_antot=Fin_an1+Fin_an2+Fin_an3
print(Fin_antot)


# In[19]:


txtfile=open("/Users/boers/Documents/bootcamp/Python-challenge/python_challenge/PyBank/analysis/pybank.txt","x") #print to file
txtfile.write(Fin_antot)
txtfile.close()

