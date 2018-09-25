import csv
from collections import Counter
import sys

#a class object that both prints out the result on screen (terminal) and saves a log file
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("PyPoll_result.txt", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass    

sys.stdout = Logger()

#main code
candidate = []
vote_distribution = {}

#read the csv file
with open ("03-Python_homework_PyPoll_Resources_election_data.csv",newline="") as f:
    csvreader=csv.reader(f,delimiter=",")
    next(csvreader,None)
    for rows in csvreader:
        candidate.append(rows[2])
#calculate total number of votes
total_votes = len(candidate)

#calculate the nubmer of votes each candidate received and stored in a Counter dictionary 
vote_count=Counter(candidate)

#print out the result of total votes
print (f"""Election Results
---------------------------
Total Votes: {total_votes}
---------------------------""")
#calculate the % of votes each candidate received and appended into a dictionary
#print out the $ of votes each candidate received from the dictionary
#print out the number of votes each candidate received from the Counter dictionary

for candidate_name in vote_count:
    percentage_vote="{:.3%}".format(vote_count[candidate_name]/float(total_votes))
    vote_distribution.update({candidate_name: percentage_vote})
    print (f"""{candidate_name}: {vote_distribution[candidate_name]} ({vote_count[candidate_name]})""")

#return the candidate name who received the maximum number of votes
vote_winner=max(vote_count, key=vote_count.get)
print (f"""---------------------------
Winner: {vote_winner}
---------------------------""")