# a function to read the hand
function read_hand(hand,p)
	cards = Dict()								# a dictionary that tells us how many of each card we have
	for card in hand	
		card in keys(cards) ? cards[card] += 1 : cards[card] = 1	# if we already have the card, add one to the number of that card
	end
	
	nJ = (p == 2 && get(cards, 'J', 5) != 5) ? pop!(cards, 'J') : 0		# if we are in part 2 (and we don't have a hand of 5 jokers), remove the jokers from the list of the cards and store their number
	
	ncards = sort(collect(values(cards)))					# sort the hand in terms of the number of each card
	ncards[end] += nJ							# add the jokers to the card we have the most of
	
	return get(hands, ncards, 0)						# return the score of that hand
end

# a function to get the score of a hand and its cards
function get_score(hand,card_vals,p)
	# return the value of the hand, plus the sum of the values of each individual card (for ties)
	return read_hand(hand,p) * 15^5 + sum([card_vals[hand[i]] * 15^(5-i) for i in 1:5])
end

# a function to get the total score of all the hands
function tot_score(data,card_vals,p)
	p == 2 && (card_vals['J'] = 1)					# if we are on part 2, set the value of the joker to 1
	sort!(data, by = i -> get_score(i[1],card_vals,p))		# sort the hands accoring to their value
	return sum([i*parse(Int64,data[i][2]) for i in 1:length(data)])	# return the total of the bid times the index of the game
end	

const data::Vector = [split(l) for l in eachline("7-data")]		# import the data
const card_vals::Dict{Char,Int64} = Dict('2'=>2,  '3'=>3,  '4'=>4,
				   	 '5'=>5,  '6'=>6,  '7'=>7,
				   	 '8'=>8,  '9'=>9,  'T'=>10,
				   	 'J'=>11, 'Q'=>12, 'K'=>13,
				   	 'A'=>14)			# define the values of the individual cards
const hands::Dict{Vector, Int64} = Dict([5] => 6,     [1,4] => 5,
					[2,3] => 4,   [1,1,3] => 3,
					[1,2,2] => 2, [1,1,1,2] => 1) 	# define the values of the different hands based on how many different cars you have

# get the total scores for parts 1 and 2
println(tot_score(data,card_vals,1))
println(tot_score(data,card_vals,2))
