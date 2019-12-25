group = {}

print('Welcome to iTax')
number = input ('\nHow many people do we have the pleasure to serve today? ')
	
number = int(number)
i = 1
total = 0
while i <= number:
	name = input('\nHello! What is your name? ')
	group[name] = {}
	print(group)
	age = input('\nHow old are you ' + name.title() + '? ')
	age = int(age)
	if age <= 3:
		cost = 0		
	elif  age <= 12:
		cost = 10
	else :
		cost = 15
	group[name]['age'] = age
	group[name]['cost'] = cost
	i += 1
	total += cost	

while True:	
	print(group)
	for names, info in group.items():
		first_name = names
		print('\nName : ' + names.title() +
			'\nYour ticket is $' + str(info['cost']))
		
	print('\nYour total is $' + str(total) +
			'\nEnjoy the movie at iTax')

	with open('Tickets.txt', 'w') as file_obj:
		for names, info in group.items():
			first_name = names
			file_obj.write('\nName : ' + names.title() + '\n' +
			'Your ticket is $' + str(info['cost']) + '\n')
		file_obj.write('\nYour total is $' + str(total) +
			'\nEnjoy the movie at iTax\n')
	resp = input('\n--')
	if resp == '':
		break
