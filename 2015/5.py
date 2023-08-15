import re

def rules1(s):
    if len(re.findall(r'[aeiou]',s)) < 3:
        return False
    if not re.search(r'(\w)\1',s):   # need the r to make sure Python doesn't try to interpret the \ before regex
        return False
    if re.search(r'ab|cd|pq|xy',s):
        return False
    return True
    
def rules2(s):
    if not re.search(r'(\w{2}).*\1',s):
        return False
    if not re.search(r'(\w).\1',s):
        return False
    return True

with open('5-data','r') as f:
    data = [line.strip() for line in f.readlines()]
    
nice1 = 0
nice2 = 0
for line in data:
    if rules1(line):
        nice1 += 1
    if rules2(line):
        nice2 += 1
print(nice1)
print(nice2)
