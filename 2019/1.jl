using Printf

# define a function to calculate the fuel required for a mass
function get_fuel(mass)
	return floor(mass/3) - 2
end

# initialise variables
tot = 0
tot2 = 0

for line in eachline("1-data")		# read the file line by line
	mass = parse(UInt32, line)	# get a mass
	fuel = get_fuel(mass)		# get the fuel required for that mass
	global tot += fuel		# add the fuel to the total (part 1)
	
	# recursively add the fuel required to carry fuel (part 2)
	while fuel > 0
		global tot2 += fuel
		fuel = get_fuel(fuel)
	end
	
end

@printf "%i %i \n" tot tot2
