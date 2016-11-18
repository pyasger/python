#Exam 2 - Hands open
#by Phil Yasger

MAX = 3
COMPARE_SMALL = 50
COMPARE_LARGE = 100

def main():
	#Get the three numbers
	total = 0.0
	
	#Explain what we are doing
	print('This program calculates the sum of')
	print (MAX, 'numbers you will enter.')
	
	#Get the numbers and accumulate them.
	for counter in range(MAX):
		number = int(input('Enter a number: '))
		total = total + number
		
		# displays the total numbers.
	print('The total is' , total)
		
	# print either small, modest or large 
	if total <= COMPARE_SMALL:
		print('Your total is a small amount')
	elif total >= COMPARE_LARGE:
		print('Your total is a large amount')
	else:
			print('Your total is a modest amount')
		
# Call the main function
main()
		