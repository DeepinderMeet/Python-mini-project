# python project 

# VOTING MANAGEMENT SYSTEM

candidates = {} # for storing the information of the candidates -> id,party

voting = {} # for storing the information of the votes -> id,votes

voter_ids = {-1} # set with inital value to avoid the interfernce with the dictionary


# function to register all the candidates
def register_candidates():

    n = (int(input("Enter the Number of Candidates to be Registered: ")))
    for i in range(0,n):

        print("Enter the Candidate id: ")
        id = (int(input()))

        print("Enter the Candidate Party: ")
        party = input()

        # store it in the dictionary of the candidates
        candidates[id] = party


    print("All the Candidates Are Registered!")

    # loop to intialise all the candidates in the voting dictionary
    for id in candidates.keys():
        voting[id] = 0


# function to print all the candidates 
def print_candidates():

    print("All the Candidates are:")

    for id,party in candidates.items():
        print(f"Candidate party {party} , Candidate id {id}")

    
# function to cast the votes
def cast_votes():
    # run this function only for one time no iterations are needed

    voter_id = int(input("Enter the Voter ID: "))
    voters_name = (input("Enter the Voter's Name : "))

    if(voter_id not in voter_ids):
        # then the voter has not voted so consider it's vote
        
        candidate_id = (int(input("Enter the Candidate id")))
        
        if(candidate_id not in candidates.keys()):
            print("The Candidate ID entered is NOT VALID")
            return

        # store this candidate id in the voting dictionary
        voting[candidate_id] = voting[candidate_id] + 1

        # add the voter id to the set of voters
        voter_ids.add(voter_id)

    else:
        print("You have Already voted!")


# function to show the voting results
def show_results():

    print("VOTING RESULTS : ")

    for k,v in sorted(voting.items,key =lambda x:x[1],reverse=True):
        print(f"Candidate_id: {k}, Votes: {v}")

    
# function to declare the winner
def declare_winner():
    
    print("VOTING RESULTS")

    highest_votes =max( sorted(voting.values())[0]) # this takes the highest votes

    for k,v in sorted(voting.values()):

        if(v == highest_votes):
            print(f"Candidate id : {k}, Candidate Votes : {highest_votes}")



# main function
while(True):
    print()
    print("The Options Available are ")
    print("1. Register Candidates")
    print("2. Display Candidates")
    print("3. Cast Vote")
    print("4. Show Results")
    print("5. Declare Winner")
    print("6. Exit")

    choice = (int(input("Enter your choice: ")))

    match choice:
        case 1:
            register_candidates()
        case 2:
            print_candidates()
        case 3 :
            cast_votes()
        case 4 :
            show_results()
        case 5:
            declare_winner()
        case _:
            print ("Exiting!")
            exit()