fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

with open ('input.txt', 'r') as infile:
    everyLine = ''.join([line for line in infile])

passports = [p.replace('\n',' ') for p in everyLine.split('\n\n')]
print(f"Solution to part 1 is: {len([p for p in passports if all(f in p for f in fields)])}")

#Part 2:

hexChars = 'abcdef0123456789'
eyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def validatePassport(passport):
    if all(f in passport for f in fields) and \
        isInt(passport['byr']) and 1920 <= int(passport['byr']) <= 2002 and \
        isInt(passport['iyr']) and 2010 <= int(passport['iyr']) <= 2020 and \
        isInt(passport['eyr']) and 2020 <= int(passport['eyr']) <= 2030 and \
        any( ['cm' in passport['hgt'] and isInt(passport['hgt'][:-2]) and 150 <= int(passport['hgt'][:-2]) <= 193, \
              'in' in passport['hgt'] and isInt(passport['hgt'][:-2]) and 59 <= int(passport['hgt'][:-2]) <= 76]) and \
        passport['hcl'][0] == '#' and all([(p in hexChars) for p in passport['hcl'][1:]]) and \
        passport['ecl'] in eyeColors and \
        isInt(passport['pid']) and len(passport['pid']) == 9 and 0 <= int(passport['pid']) <= 10**9 :
        return True
    else:
        return False

def prettyPrintPassport(passport):
    for k in passport:
        print(f"{k}:\t{passport[k]}")

ppp = prettyPrintPassport

with open('input.txt', 'r') as infile:
    everyLine = ''.join([line for line in infile])

passports = [p.replace('\n',' ') for p in everyLine.split('\n\n')]
passports = [p.split(' ') for p in passports]
splitList = list()

#Generate a list of dictionaries; each dictionary is a single passport with keys being field names and values being field values
for p in passports:
    tempDict = dict()
    for field in p:
        k, v = field.split(':')
        tempDict[k] = v
    splitList.append(tempDict)

sum = 0

for passport in splitList:
    if validatePassport(passport):
        sum += 1
        print("---VALID---")
    else:
        print("---INVALID---")
    ppp(passport)
    print('')

print(f"Solution to part 2 is: {sum}")