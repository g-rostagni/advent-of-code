# runs in a few seconds, could do with some optimising

# define a class that represents each monkey, with the items they hold, the operation they apply and the test they use to choose which monkey they are throwing their items at
class Monkey:
	def __init__(self,items,op,test):
		self.items = items	# the items this monkey is carrying at the start
		self.op = op		# the operation the monkey applies, as a string
		self.test = test	# the test the monkey uses, as a list of three elements
		self.handled = 0	# the amount of items the monkey handled
	
	# define what happens when the monkey throws an item
	def throw(self,item):
		self.handled += 1							# add 1 to the number of handled items
		worry_level = eval(self.op.replace("old",str(item)))			# apply the operation to the worry level (by evaluating the string expression)
		# worry_level = int(worry_level/3)					# divide the worry level by 3, (un)comment this for part 1 (2)
		worry_level %= mod_prod							# mod the worry level by a global factor to keep it in check
		if not worry_level % self.test[0]:					# if the test is satisfied:
			return self.test[1],worry_level					# return the monkey it is throwing to and the item
		else:
			return self.test[2],worry_level					# return the other monkey it can throw to if not 
		

with open("11-data","r") as f:
	monkeys_text = [block.strip().split("\n") for block in f.read().split("\n\n")]
	
# initialise the monkeys 
monkeys = []
mod_prod = 1
for monkey in monkeys_text:
	items = monkey[1].split(":")[-1].split(",")	# the items each monkey is initially carrying
	op = monkey[2].split("=")[-1]			# the operation each monkey applies on the worry level
	test = []
	test.append(int(monkey[3].split(" ")[-1]))	# the test each monkey does before throwing
	test.append(int(monkey[4].split(" ")[-1]))	# the destination if the test is satisfied
	test.append(int(monkey[5].split(" ")[-1]))	# the destination otherwise
	monkeys.append(Monkey(items,op,test))		# shove these parameters in the class to create a list of Monkey objects
	
	# the factor by which we divide the worry level to keep it from exploding
	# since the only operation that matters is mod, modding by the product of all numbers that we can take the mod with won't change the result
	mod_prod *= test[0]
	
# let the monkeys throw stuff around
rounds = 10000
for i in range(rounds):
	for m in range(len(monkeys)):				# loop over each monkey
		for item in monkeys[m].items:			# loop over each item held by a monkey
			dest,thrown = monkeys[m].throw(item)	# the monkey throws an item to another monkey
			monkeys[dest].items.append(thrown)	# the destination monkey receives it
		monkeys[m].items = []				# the monkey loses all its items after throwing them
		
# determine the number of items handled by each monkey and print the monkey business number
handled_items = sorted([monkey.handled for monkey in monkeys])
monkey_business = handled_items[-2] * handled_items[-1] 
print(monkey_business)
