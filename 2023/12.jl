# I have no merit for this solution, I've just nicked it from Yannick

#the magic ingredient, cuts your runtime from infinity to about 3secs by memorising previous solutions
const solution_memory = Dict{Tuple{Vector{Char}, Vector{Int}, Int}, Int}()

# a function to count the solutions for a given line and list of numbers
function count_sols(l::Vector{Char}, n::Vector{Int}, c_b::Int = 0)::Int
	# look up the solution, if it doesn't exist calculate it
	get!(solution_memory, (l, n, c_b)) do

		# a subfunction to calculate the solutions by calling count_sols with a smaller fraction of the line
		function get_sols(c::Char)::Int
			if c == '#'										# if we are looking at a #
				return count_sols(l[2:end], n, c_b+1)		# add 1 to the length of the current block
			else
				if c_b == 0									# if we are not in a block
					return count_sols(l[2:end], n)			# keep going
				elseif length(n) > 0 && c_b == n[1]			# if we are at the end of a block
					return count_sols(l[2:end], n[2:end])	# move on to the next one
				else
					return 0								# otherwise the block is invalid
				end
			end
		end
	
		if length(l) == 0					# if we reached the end of the line
			if length(n) == 0 && c_b == 0	# if we completed all the numbers
				return 1					# valid
			else							# otherwise
				return 0					# not valid
			end
		end

		if l[1] == '?'								# if we are looking at a '?'
			return get_sols('#') + get_sols('.')	# consider both possibilities
		else
			return get_sols(l[1])
		end
	end
end

# a function to parse the data
function parse_data(l,p)
	ls, ns = split(l)
	ns = map(i -> parse(Int64,i), split(ns, ','))
	ls = collect(ls)
	
	# stuff for part 2
	if p == 2
		ls = [ls ; repeat(['?'; ls], 4)]
		ns = repeat(ns, 5)
	end
	
	append!(ls, '.')	# add a trailing . to make sure we actually read the whole thing and don't stop early
	return ls, ns
end

# loop over both parts
for i = 1:2
	sum(readlines("12-data")) do l
		ls::Vector{Char}, ns::Vector{Int} = parse_data(l, i)
		count_sols(ls, ns)
	end |> println
end






