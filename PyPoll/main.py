#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


filepath = '/Users/boers/Documents/bootcamp/Python-challenge/python_challenge/PyPoll/Resources/election_data.csv'


# In[3]:


with open(filepath, newline='') as f:
    reader = csv.reader(f)
    data = list(reader) #load csv into a list, in this case it turned out to be a nested list, with each entry being a list
                        #with zeroth entry being the Ballot id, the first entry being the County, and the second being candidate


# In[8]:


num_votes = len(data)-1 #number of votes will be number of rows - 1 for the header row
uniquecandidates=[]
candvotes=[] #create empty lists to fill with unique candidates and their number of votes
for i in range(num_votes):
    if data[i+1][2] not in uniquecandidates: #[i+1] to get that entry, and plus 1 to avoid header entry. [2] to get the candidate
        uniquecandidates.append(data[i+1][2]) #if not in list, then append list to include candidate
        candvotes.append(0) #create entry in votes list for that candidate
    for j in range(len(uniquecandidates)):
        if data[i+1][2] == uniquecandidates[j]:#checks which candidate the entry matches
            candvotes[j]=candvotes[j]+1 #adds 1 to their respective counter
for i in range(len(uniquecandidates)-1):
    if candvotes[i]>candvotes[i+1]:
        wincand=uniquecandidates[i] #checks which number in candvotes is biggest and creates variable for the winner
        
wincand


# In[10]:


totvotes=0
pvotes=[]
roundedvotes=[]
for i in range(len(candvotes)):
    totvotes=totvotes+candvotes[i] #another way to find total votes, a bit redundant
for i in range(len(candvotes)):
    pvotes.append(candvotes[i]/totvotes) #Converts raw votes to their decimal proportion of whole
    roundedvotes.append(round(pvotes[i],3)*100) #rounds and multiplies by 100 to give percent
pvotes


# In[22]:


#making strings to print to terminal and file
el_res1="Election results \n __________ \nThe total number of votes is " + str(num_votes) + "\n __________ \n"
el_res2 = ""
for i in range(len(candvotes)):
    el_res2= el_res2 + str(uniquecandidates[i]) + " recieved " + str(candvotes[i]) + " votes, which is " + str(roundedvotes[i]) + " percent of the vote! \n"
el_res3="____________ \nThe winner is " + wincand + "!"
el_restot = el_res1 + el_res2 + el_res3
print(el_restot)


# In[24]:


txtfile=open("/Users/boers/Documents/bootcamp/Python-challenge/python_challenge/PyPoll/analysis/pypoll.txt","x") #print to file
txtfile.write(el_restot)
txtfile.close()

