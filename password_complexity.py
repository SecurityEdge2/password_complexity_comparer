import sys
import locale
locale.setlocale(locale.LC_ALL, '')

complexity_subjects = dict(english_lower='qwertyuiopasdfghjklzxcvbnm',
	english_upper='QWERTYUIOPASDFGHJKLZXCVBNM',
	russia_lower = 'ёйцукенгшщзхъфывапролджэячсмитьбю',
	russia_upper = 'ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ',
	numbers = '1234567890',
	symbols = """~`!@#$%^&*({[\\|/;;'",<.>/?№]})""",
	spaces  = ' 	')


	
i = -1
def get_complexity(password):
	global i
	def check_symbol(password, name, chars):
		for char in chars:
			if char in password:
				return True
		return False
		
	degree = 0
	symbols = []
	for name, chars in complexity_subjects.items():
			if check_symbol(password, name, chars):
				degree += len(chars)
				symbols.append(name)
	complexity = degree**len(password)
	complexity_str = "{0:n}".format(complexity).replace(',',' ')
	i+=1
	return (i,complexity, password, degree, symbols, complexity_str)

passwords = sys.argv
passwords = passwords[1:]
values = {}
sorted_set = []
sorted_values = []
for item in passwords:
	result = get_complexity(item)
	values.update( {result[1]:result })
	sorted_set.append(result[1])
sorted_set.sort()
for item in sorted_set:
	sorted_values.append(values[item])


import pprint
for item in sorted_values:
	print('[!] Password is: {}'.format(item[2]))
	print(' -> alphabet is {}'.format(' '.join(item[4])))
	print(' -> count char in alphabet is {}'.format(item[3]))
	print(' -> password len is {}'.format(len(item[2])))
	print(' -> number of combinations: {0}, ({1} digits)'.format(item[5], len(str(item[1]))))

