''' useless.py ; DEobfuscated manually. '''
def printfun(forget): return ''.join(str(forget))
a_list=[]
zero=0

possible_blacklist=[' ', '\t', '\n', '\r', '\x0b', '\x0c']
hex_character="\\x"
for i in range(32, 254):
	character=str(chr(i))

	for blacklisted_character in possible_blacklist:
		if character==blacklisted_character:
			zero -= 1

	if hex_character in character:
		continue
	zero+=1
	a_list.append(character)

counter=0

# counting the characters
for something in a_list:
	for something4 in possible_blacklist:
		if something == something4: 
			counter+=1
print(printfun(a_list),printfun(zero))
