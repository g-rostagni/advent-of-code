f = open('6-data','r')

data = []
questions = []

for line in f:
	line = line.strip().split()
	if line:
		questions.append(line[0])
	else:
		data.append(questions)
		questions = []
		
if questions:
	data.append(questions)

Nans = 0

for questions in data:
	Qans = []
	for let in questions[0]:
		miss = 0
		for question in questions:
			if not let in question:
				miss = 1
				break
		if not miss:
			Qans.append(let)
	print(Qans,questions)
	Nans += len(Qans)
	
print(Nans)