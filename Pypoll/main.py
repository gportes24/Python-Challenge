import csv


total_votes =0
candidates = []


#with open ("../PyBank/Resources/election_data.csv") as elect:
with open ("../PyBank/Resources/election_data.csv") as elect:
    data = csv.reader(elect, delimiter=",")
    csvheader = next(data)
    
    for row in data:
        total_votes += 1
        candidates.append(row[2])
        
politics = list(set(candidates))
politics.sort()
electvotes = []
for crook in politics:
    electvotes.append(candidates.count(crook))

print ("Election Results")
print ("-----------------------")
print (f" Total Votes : {total_votes}")
print ("-----------------------------")
for x in range (len(politics)):
    (politics[x],(electvotes[x]/(len(candidates))), electvotes[x])
    print (f"{politics[x]}: {'{:.2%}'.format(electvotes[x]/len(candidates))} ({electvotes[x]})")
    

winner = politics[electvotes.index(max(electvotes))]


print ("-----------------------------")
print (f" Winner: {winner}")
print("------------------------------")


pol_file = ("Analysis/Analysis.txt")
with open (pol_file, "w", newline = "") as electionresults:
    electionresults.write ("Election Results\n")
    electionresults.write ("-----------------------\n")
    electionresults.write (f" Total Votes : {total_votes}\n")
    electionresults.write ("-----------------------\n")
    electionresults.write(f"{politics[x]}: {'{:.2%}'.format(electvotes[x]/len(candidates))} ({electvotes[x]})\n")
    electionresults.write ("-----------------------\n")
    electionresults.write (f" Winner: {winner}\n")
    electionresults.write("-----------------------------")
