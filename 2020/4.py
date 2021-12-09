import re

f = open('4-data','r')

passports = []
passport = {}
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
eyecolors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

for line in f:
	if line == '\n':
		passports.append(passport)
		passport = {}
	else:
		line2 = line.rstrip().split()
		for entry in line2:
			val = entry.split(':')
			passport[val[0]] = val[1]		
if passport:
	passports.append(passport)

invalid = 0

for passport in passports:
	for field in fields:
		try:
			entry = passport[field]
			match field:
				case 'byr':
					if not 1920 <= int(entry) <= 2002:
						raise KeyError
				case 'iyr':
					if not 2010 <= int(entry) <= 2020:
						raise KeyError
				case 'eyr':
					if not 2020 <= int(entry) <= 2030:
						raise KeyError
				case 'hgt':
					if 'cm' in entry:
						if not 150 <= int(entry.split('cm')[0]) <= 193:
							raise KeyError
					elif 'in' in entry:
						if not 59 <= int(entry.split('in')[0]) <= 76:
							raise KeyError
					else:
						raise KeyError
				case 'hcl':
					if not re.search("#[A-Fa-f0-9]{6}",entry):
						raise KeyError
				case 'ecl':
					if not entry in eyecolors:
						raise KeyError
				case 'pid':
					if not len(entry) == 9 and not entry[0] == '0':
						raise KeyError
		except KeyError:
			invalid += 1
			print('INVALID',field,passport)
			break

print('passports:',len(passports))
print('invalid:',invalid)
print('valid:',len(passports)-invalid)