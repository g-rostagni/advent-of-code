# a function to read the number of winning numbers for each card from the data
function number_of_wins(f)
	nwins = Vector{Int64}()					# define a vector that will contain the numbers of winning nos
	for line in eachline(f)					# loop over each card
		card = split(line, [':','|'])
		winning_nums = split(card[2])			# retrieve the winning numbers
		my_nums = split(card[3])			# retrieve our numbers
		num = count(n->(n in winning_nums), my_nums)	# count how many of our numbers are also winning numbers
		push!(nwins, num)				# add that number to the vector
	end
	return nwins
end

# main function
function main()
	# create an array containing the number of winning numbers we have in each card
	nwins = number_of_wins("4-data")

	score = 0				# define the score (part 1)
	ncards = ones(Int64, length(nwins))	# create an array with the number of each card that we have (part 2)

	for i in 1:length(nwins)			# loop over all the cards
		wins = nwins[i]				# get the number of winning numbers we got on that card
		if wins == 0				# if there are none do nothing
			continue
		end
	
		score += 2^(wins - 1)			# add the score of the card to the total
		for j in 1:wins				
			ncards[i+j] += ncards[i]	# add the number of copies that we won to the following cards
		end
	end
	
	println(score)
	println(sum(ncards))	# add up all the cards

	return 0
end

main()
