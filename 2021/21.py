def update_possible_scores(scores):
	newscores = {}
	for score in scores:
		for pn in scores[score]:
			pos = pn
			mult = scores[score][pn]
			for i in range(3, 10):
				newpos = pos+i
				newmult = mult * roll3pos[i]
				if newpos > 10:
					newpos -= 10
				newscore = score+newpos
				if not newscore in newscores:
					newscores[newscore] = {}
				if not newpos in newscores[newscore]:
					newscores[newscore][newpos] = 0
				newscores[newscore][newpos] += newmult
	return newscores
	
def check_win(scores):
	won = 0
	scoresnew = scores.copy()
	for score in scores:
		if score >= 21:
			for pn in scores[score]:
				won += scores[score][pn]
			scoresnew.pop(score)
	return scoresnew,won
	
def get_total_mult(scores):
	mult = 0
	for score in scores:
		for pn in scores[score]:
			mult += scores[score][pn]
	return mult
	
def get_winners(turn,scoresA,scoresB,universes_won):
	scoresA = update_possible_scores(scoresA)
	scoresA,won = check_win(scoresA)
	universes_won[turn%2] += won * get_total_mult(scoresB)
	return scoresA,scoresB,universes_won
			

# input: p1 starts at 4, p2 starts at 2	
startpos1 = 4
startpos2 = 2

roll3pos = [0, 0, 0, 1, 3, 6, 7, 6, 3, 1]

scores1 = {0: {startpos1: 1}}
scores2 = {0: {startpos2: 1}}
universes_won = [0,0]
turn = 0
while get_total_mult(scores1) or get_total_mult(scores2):
	if not turn%2:
		scores1,scores2,universes_won = get_winners(turn,scores1,scores2,universes_won)
	else:
		scores2,scores1,universes_won = get_winners(turn,scores2,scores1,universes_won)
	turn += 1

print(max(universes_won))
