# a function to do the hashing of a string
function hash_str(s)
	v = 0
	for c in s
		v = ((v + Int(c)) * 17) % 256 # Int(c) converts a char to its ASCII value
	end
	return v
end

# a function to read an instruction and apply it to the boxes
function read_instr(s)
	boxcode = match(r"[a-z]+", s).match			# get the box/lens code
	boxid = hash_str(boxcode) + 1				# get the index corresponding to that code
	if '-' in s						# if we have a subtract instruction
		filter!(i -> i[1] != boxcode, boxes[boxid])	# remove the lens from the box
	else 							# if we have an equal instruction
		n = parse(Int64, match(r"\d+", s).match)	# read the focal length
		for l in boxes[boxid]				# loop over the lenses in the box
			if l[1] == boxcode			# if we find the lens in the instruction
				l[2] = n			# update it
				return 0
			end
		end
		push!(boxes[boxid], [boxcode, n])		# otherwise add the lens to the box
	end
	return 0
end

# a function to get the score of a box
function get_box_score(box)
	isempty(box) ? 0 : sum(l -> l*box[l][2], 1:length(box))		# return 0 if the box is empty, calculate the score otherwise
end

data = split(strip(read("15-data", String)), ',')			# read the data

boxes::Vector{} = [[] for i = 0:255]					# define the array of boxes
map(read_instr, data)							# apply all the instructions to the boxes

sum(hash_str, data) |> println						# sum the hashes from the input (part 1)
sum(i -> i*get_box_score(boxes[i]), 1:length(boxes)) |> println		# sum the scores of each box (part 2)
