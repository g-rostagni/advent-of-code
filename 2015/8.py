import re

with open('8-data','r') as f:
	data = [line.strip() for line in f.readlines()]
	
diff = 0
diff2 = 0
for line in data:
	x = re.sub(r'\\x[a-f0-9]{2}','X',line)	# replace the ASCII codes
	x = re.sub(r'\\\W','X',x)		# replace the escaped characters
	diff += len(line) - (len(x)-2)		# -2 because we ignore the quotes
	
	y = re.sub(r'\W','XX',line)		# replace any non-alphanumeric character
	diff2 += len(y)+2 - len(line)		# +2 because we haven't added quotes

print(diff)
print(diff2)
