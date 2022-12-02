with open("2-data","r") as f:
	guide = [[char for char in line.split(" ")] for line in f.read().split("\n") if line]
	
score_1 = 0
score_2 = 0

# define a dictionary giving a score for each of the instructions on the guide, for part 1
outcomes_1 = {'X': {'A': 4, 'B': 1, 'C': 7}, 'Y': {'A': 8, 'B': 5, 'C': 2}, 'Z': {'A': 3, 'B': 9, 'C': 6}}

# do the same thing for part 2
outcomes_2 = {'X': {'A': 3, 'B': 1, 'C': 2}, 'Y': {'A': 4, 'B': 5, 'C': 6}, 'Z': {'A': 8, 'B': 9, 'C': 7}}

# read each round and add the correct scores to the respective totals
for round in guide:
	score_1 += outcomes_1[round[1]][round[0]]
	score_2 += outcomes_2[round[1]][round[0]]
	
# print the final scores
print(score_1)
print(score_2)
