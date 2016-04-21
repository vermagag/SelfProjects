#!/usr/bin/python

list=[]

def post(a):
	global list
	list.append(a)
	if len(list) == 5:
		check()
	else:
		pass


def check():
|	i=0
	count = 0
	while i!=4:
		if list[i] == list[i+1]:
			count = count+1
		i=i+1

	if count >3:
		print 'yes'
	else:
		print 'no'



def main():
	i=0
	while i!=5:
		value = raw_input('Enter a values :')
		post(value)
		i=i+1

if __name__ == '__main__':
	main()

