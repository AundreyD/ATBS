# Regular Expressions
# import the module
import re

message = 'Call me 415-444-4456 tomorrow, or at 281-330-8004'

# Use raw strings because there's a lot of \ 
# Use .compile to create regex object
# Use parenthesis to group things
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# Search returns a match object
# match object has the group method on it
mo = phone_num_regex.search(message)
# You can pass through a number to match a group
print(mo.group(1))

print(phone_num_regex.findall(message))


msg = 'My number is (281)-330-8004'
phonNumberReg = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')

mobj = phonNumberReg.search(msg)
print(mobj.group())

# Use the pipe to add a suffix to search for if you know the prefix
batReg = re.compile(r'Bat(man|mobile|plane|boat)')
obj = batReg.search('Batmobile is neat')
print(obj.group())
# Use 1 for group to see what suffix was matched
print(obj.group(1))

# ? character is for something appearing 0 or 1 time
br = re.compile(r'Bat(wo)?man')
mo = br.search('Adventures of Batman')
print(mo.group())
mo = br.search('Adventures of Batwoman')
print(mo.group())

phone_num_regex = re.compile(r'(\(\d\d\d\)-)?(\d\d\d-\d\d\d\d)')
mo = phone_num_regex.search('hi, 281-330-8004')
print('With area code', mo.group())
mo = phone_num_regex.search('yo, 330-8004')
print('Match Without area code:', mo.group())

# * is 0 or more if a * is needed just escape it (same for ?)
batReg = re.compile(r'Bat(wo)*man')
mo = batReg.search('Batwowowowoman')
print('Testing out the * ', mo.group())

# + is 1 or more times
# {x} x is the amount of times you want it to appear. This is exact
# {x, y} is a range for repetitions x = min y = max
# Greedy matches matches the longest string possible ex. {3,5}
# Non greedy matches the shortest possible ex. {3,5}?
phone_num_regex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo = phone_num_regex.search('My numbers: 415-555-5555,222-330-8004,919-334-6633')
print('Exact match', mo.group())

phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# Findall finds all instances and stores the in a list
# Does not return a match object
mo = phone_num_regex.findall('281-330-8004 223-334-5567 375-559-0987')
print('Findall:', mo)

# Groups returns a list of tuples
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_num_regex.findall('281-330-8004 223-334-5567 375-559-0987')
print(mo)

# This below includes the dashes
phone_num_regex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
mo = phone_num_regex.findall('281-330-8004 223-334-5567 375-559-0987')
print(mo)

# Character classes
# \d = digits 0-9
# \D = not 0-9
# \w = any letter, numeric digit, or underscore
# \W = any character that is nor a letter, numeric digit, or underscore
# \s = Any space, tab, or newline character. (matching space characters)
# \S = Any character that is not a space, tab, or newline

lyrics = '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'
xmasReg = re.compile(r'\d+\s\w+')
mo = xmasReg.findall(lyrics)
print(mo)

# Making own classes
vowelReg = re.compile(r'[aeiouAEIOU]')

# Negative character class
# using a caret ^ in a custom class means not
vowelReg = re.compile(r'[^aeiouAEIOU]')

# ^ means the string must start with
beginsWithReg = re.compile('^Hello')
print('Correct',beginsWithReg.search('Hello there'))
print('Incorrect', beginsWithReg.search('Jenny, Hello'))

# $ at the end means ends with
endsWithRegex = re.compile(r'world$')
print('correct:', endsWithRegex.search('This is my world'))
print('Incorrect:', endsWithRegex.search('One world out of many'))

allDigitsReg  = re.compile(r'^\d+$')
print('correct:', allDigitsReg.search('987587248580'))
print('incorrect:', allDigitsReg.search('44444h4298590840'))

# . character means any character except newline
atReg = re.compile('.at')
print('correct:', atReg.findall('cat in the hat sat on a bat'))

# .* means anything
# .* uses greedy/nongreedy
nameReg = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameReg.findall('First Name: Aundrey Last Name: Drummond'))

# nongredy
serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))

# Greedy
serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*)>')
print(nongreedy.findall(serve))

prime = 'Serve public trust. \nProtect the innocent. \nUphold the law.'
dotStar = re.compile(r'.*')
# reaches the first new line, not the others
print('Correctish:',dotStar.search(prime))
# Add the second argument to get EVERYTHING
dotStar = re.compile(r'.*', re.DOTALL)
print('Correct:',dotStar.findall(prime))

# Doesn't ignore case
vowelReg = re.compile(r'[aeiou]')
print('only lowercase returned:', vowelReg.findall('I am the Only Person thAt knows AnythIng'))
# Ignores case
vowelReg = re.compile(r'[aeiou]', re.IGNORECASE)
# ^^^ can also be re.I
print('All vowels', vowelReg.findall('I am the Only Person thAt knows AnythIng'))

# sub() method
namesReg = re.compile(r'Agent \w+')
print(namesReg.findall('Agent Smith met with Agent Clark.'))
print( namesReg.sub('-NOPE-','Agent Smith met with Agent Clark.'))
namesReg = re.compile(r'Agent (\w)\w*')
print( namesReg.findall('Agent Smith met with Agent Clark.'))
print( namesReg.sub(r'Agent \1****','Agent Smith met with Agent Clark.'))

# Verbose allows you to format a regex and make it readable
# Combine verbose and ignorecase with or
re.compile(r'''
\ddd #area code
- #first dash
\d\d\d #3 digits
- #second dash
\d\d\d\d #last 4 digits
''', re.VERBOSE | re.IGNORECASE | re.DOTALL)



