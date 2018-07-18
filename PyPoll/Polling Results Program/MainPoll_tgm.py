


##### Program Start - Import File 
import os
import csv

# Establish path to data file
election_results = os.path.join("..", "Resources", "election_data.csv")

##### Open and read csv data file
with open(election_results, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    ##### Read the header row first (skip this part if there is no header)
    #next(csvreader)
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    tot_votes = 0
    candidate_list = 0
    candidate_vote_count = 0
    candidate_vote_share = 0
    winning_candidate = 0

    ##### Read through each row of data after the header
    for row in csvreader:
        #   * The total number of votes cast
        tot_votes = tot_votes + 1

    print("A total of " + str(tot_votes) + " votes were cast in the election")

# Counter is used for the bonus solution
from collections import Counter

        ## Paths
        ## resume_path = os.path.join(".", 'resume.md')

        ## Skills to match
        ## REQUIRED_SKILLS = {"excel", "python", "mysql", "statistics"}
        ## DESIRED_SKILLS = {"r", "git", "html", "css", "leaflet"}


        ## def load_file(filepath):

            ## Helper function to read a file and return the data.
            ## with open(filepath, "r") as resume_file_handler:
            ##return resume_file_handler.read().lower().split()


# Grab the text for a Resume
word_list = load_file(resume_path)

# Create a set of unique words from the resume
resume = set()

        ## Remove trailing punctuation from words
        ## for token in word_list:
        ##    resume.add(token.split(',')[0].split('.')[0])
        ## print(resume)

        ## Remove Punctuation that were read as whole words
        ## punctuation = set(string.punctuation)
        ## resume = resume - punctuation
        ## print(resume)

        ## Calculate the Required Skills Match using Set Intersection
        ## print(resume & REQUIRED_SKILLS)

        ## Calculate the Desired Skills Match using Set Intersection
        ## print(resume & DESIRED_SKILLS)

# Bonus: Resume Word Count
# ==========================
# Initialize a dictionary with default values equal to zero
word_count = {}.fromkeys(word_list, 0)

# Loop through the word list and count each word.
for word in word_list:
    word_count[word] += 1
print(word_count)

# Bonus using collections.Counter
word_counter = Counter(word_list)
print(word_counter)

# Comparing both word count solutions
print(word_count == word_counter)

# Top 10 Words
print("Top 10 Words")
print("=============")

        ## Clean Punctuation
        ## _word_count = [word for word in word_count if word not in string.punctuation]

        ## Clean Stop Words
        ## stop_words = ["and", "with", "using", "##", "working", "in", "to"]
        ## _word_count = [word for word in _word_count if word not in stop_words]

# Sort words by count and print the top 10
sorted_words = []
for word in sorted(_word_count, key=word_count.get, reverse=True)[:10]:
    print(f"Token: {word:20} Count: {word_count[word]}")


'''
# * Your task is to create a Python script that analyzes the records to calculate each of the following:
  
#   * The total number of votes cast
#   * A complete list of candidates who received votes
#   * The percentage of votes each candidate won
#   * The total number of votes each candidate won
#   * The winner of the election based on popular vote.

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
# 
#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.


print("end of file")