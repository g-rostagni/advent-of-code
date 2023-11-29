# put the main loop in a function since we will need to run it twice for part 2
# it can be given a value as an argument
def main(a=0):
	
	# define a function to read the inputs, check whether they are number and if not check whether the variable is already defined
	def readvar(i):
		try:
			return int(i)
		except ValueError:
			if i in wires:
				return wires[i]	# if the variable has been defined previously, read it
			else:
				return 'skip'	# if not, we will skip this instruction
				
	# read the data
	with open('7-data','r') as f:
		data = f.read().split('\n')[:-1]	# exclude the last empty line
	
	wires = {}					# define a dictionary that will contain all our variables

	# we loop over the instructions, skipping the ones we can't do, and executing then deleting the ones we can
	i = 0
	while data:					# while we still have things to do
		i %= len(data)				# no overflow
		l = data[i].split(' ')
			
		if len(l) == 5:				# if the instruction takes two arguments
			# read both arguments, if one of them is a variable that we haven't yet defined, we skip this instruction
			if (x := readvar(l[0])) == 'skip' or (y := readvar(l[2])) == 'skip':
				i += 1 
				continue
			
			# do the bitwise operation using Python's built-in operators
			if l[1] == 'AND':
				wires[l[-1]] = x & y
			elif l[1] == 'OR':
				wires[l[-1]] = x | y
			elif l[1] == 'LSHIFT':
				wires[l[-1]] = x << y
			elif l[1] == 'RSHIFT':
				wires[l[-1]] = x >> y
			
		elif len(l) == 4:			# if the instruction takes a single argument (NOT)
			if (x := readvar(l[1])) == 'skip':
				i += 1
				continue
				
			wires[l[-1]] = ~x % 65536	# mod the result to make sure it is unsigned

		else:					# if the instruction is a simple assignment
			if (x := readvar(l[0])) == 'skip':
				i += 1
				continue
				
			wires[l[-1]] = x
			
		# if we passed a value as an argument, override the assignment to wire 'b'
		if a and l[-1] == 'b':
			wires['b'] = a
			
		data.pop(i)				# delete the instruction we just executed
	
	return wires['a']				# return the value of wire 'a' when we're done
	
# print the result of the function with no value for 'a', and then run it again with the output of the first run as an argument
print(a := main())
print(main(a))
