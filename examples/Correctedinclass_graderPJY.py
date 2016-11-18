#
#
#
A_SCORE = 100
B_SCORE = 50
C_SCORE = 20
D_SCORE = 10
def main():
	#
	score = int(input('Please enter your quantity: '))
	
	#
	if score >= A_SCORE:
			print('Take a 50% discount.')
	elif score >= B_SCORE:
			print('Take a 40% discount.')
	elif score >= C_SCORE:
			print('Take a 30% discount.')
	elif score >= D_SCORE:
			print('Take a 20% discount. ')
	else:
			print('sorry, no discount. ')
#
main()