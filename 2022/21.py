# import the monkeys in a dictionary 
monkeys = {}
with open("21-data","r") as f:
	monkeys = { line.split(": ")[0]: line.strip().split(": ")[1] for line in f.readlines()}

# do some replacements necessary for part 2
humn = monkeys['humn']					# store the original value for 'humn'
monkeys['humn'] = 'x'					# replace the value by x, which we need to find in part 2
monkeys['root'] = monkeys['root'].replace("+","=")	# replace the sum in root by an equal sign (to remember where to split the expression

while len(monkeys) > 1:										# while there are more than one unevaluated monkey
	for m in monkeys:									# loop over the remaining monkeys
		if m == 'root':									# if we are looking at 'root', skip it
			continue
		
		# now that we found a monkey 'm', we substitute its expression/value into the monkeys that use it
		for n in monkeys:								# loop over the other monkeys
			if m in monkeys[n]:							# if another monkey makes use of monkey m
				monkeys[n] = monkeys[n].replace(m,'(' + monkeys[m] + ')')	# substitute the expression of monkey m into monkey n
		del monkeys[m]									# shoot the monkey
		break										# move on to another monkey

# for part 1, we evaluate the resulting expression for root, using the original value of 'humn'
rootyell = int(eval(monkeys['root'].replace('x',humn).replace("=","+")))
print(rootyell)

# for part 2, we use a first order gradient descent with fixed step size to find the correct number to shout
x = 0							# start at 0
expr = monkeys['root'].replace("=","-")			# define the expression to minimise (the difference between the sides of the equality)
diff = abs(eval(expr))					# evaluate the difference

while diff > 0.1:					# while this difference is greater than 0.1 (arbitrary number, works for me)
	# calculate the gradient at that point
	xplus = x+1					
	diffplus = abs(eval(expr.replace('x','xplus')))
	dx = (diffplus - diff) / 1
	
	# update the value of x and the difference
	x -= diff / dx
	diff = abs(eval(expr))
	
x = int(round(x,0))			# get the closest integer to the number we found
if eval(expr):				# if it doesn't work,
	print("Minimising failed")	# tough luck
print(x)
