import os

file_path=os.path.join("election_data.txt")

with open(file_path,"r",newline="") as txtfile :
    poll_header = next(txtfile)
    
    #Create a empty dict to store election result
    summary = {}

    for rows in txtfile:
        data = rows.strip().split(",") #To split row data by "," and it will be a list

        if data[2] not in summary : #To indetify one candidate if he/she is in the summary dict.
            summary[data[2]] = 1    #If not in, it will record the candidate(key) and give one vote(value) 
        else :
            summary[data[2]] += 1   #If in, it will add another one vote to him/her.

candidate = list(summary.keys()) 
each_votes = list(summary.values())
total_votes = sum(each_votes)

winner_candidate_index = each_votes.index(max(each_votes)) #To find the index which has higest votes
winner_candidate = candidate[winner_candidate_index] #To retrieve the candidate by index

print("Election Results")
print(f"---------------------------------------")
print(f"Total votes : {total_votes}")
print(f"---------------------------------------")
print(f"{candidate[0]}: {round((each_votes[0]/total_votes)*100,3)}% ({each_votes[0]})")
print(f"{candidate[1]}: {round((each_votes[1]/total_votes)*100,3)}% ({each_votes[1]})")
print(f"{candidate[2]}: {round((each_votes[2]/total_votes)*100,3)}% ({each_votes[2]})")
print(f"{candidate[3]}: {round((each_votes[3]/total_votes)*100,3)}% ({each_votes[3]})")
print(f"---------------------------------------")
print(f"Winner: {winner_candidate}")
print(f"---------------------------------------")

#Export a txt file
result = open("PyPoll_result.txt","w")
line1 = "Election Results \n"
line2 = f"--------------------------------------- \n"
line3 = f"Total votes : {total_votes} \n"
line4 = f"--------------------------------------- \n"
line5 = f"{candidate[0]}: {round((each_votes[0]/total_votes)*100,3)}% ({each_votes[0]}) \n"
line6 = f"{candidate[1]}: {round((each_votes[1]/total_votes)*100,3)}% ({each_votes[1]}) \n"
line7 = f"{candidate[2]}: {round((each_votes[2]/total_votes)*100,3)}% ({each_votes[2]}) \n"
line8 = f"{candidate[3]}: {round((each_votes[3]/total_votes)*100,3)}% ({each_votes[3]}) \n"
line9 = f"--------------------------------------- \n"
line10 = f"Winner: {winner_candidate} \n"
line11 = f"--------------------------------------- \n"

result.write(line1)
result.write(line2)
result.write(line3)
result.write(line4)
result.write(line5)
result.write(line6)
result.write(line7)
result.write(line8)
result.write(line9)
result.write(line10)
result.write(line11)

result.close()