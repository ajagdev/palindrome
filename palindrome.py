import re

def strip(str):
	pattern = '[a-zA-z]'
	return ''.join(re.findall(pattern,str))

def is_palindrome(str):

	org = strip(str)
	rev = org[::-1]

	if org.lower() == rev.lower():
		print  '"%s" is a palindrome sentence' % str.replace('\n', '')
	else:
		print  '"%s" is not palindrome sentence' % str.replace('\n', '')

if __name__ == '__main__':
	print "---Starting Program---\n"

	for line in open("input.txt" , "r").readlines():
		is_palindrome(line)

	print "\n---finished running---"	