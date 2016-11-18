#setting the global constant for the RETAIL_PRICE

RETAIL_PRICE = 99.00
MIN_QUANTITY = 10

#othe variables delclared for the function

quantity = 0
fullPrice = 0 
discountRate = 0 
discountAmount = 0 
totalAmount = 0 


def main():
#getting quanity from user
	quantity= int(input('Enter quantity: '))
	
	if quantity >= MIN_QUANTITY and quantity <= 19:
		print('The discount rate is:', '20%')
		discountRate=(.20)
	elif quantity >= 20 and quantity <= 49:
		print('The discount rate is:', '30%')
		discountRate=(.30)
	elif quantity >= 50 and quantity <= 99:
		print('The discount rate is:', '40%')
	elif quantity >= 100:
		print ('The discount rate is:', '50%')
		discountRate=(.50)
		
		
	# this will calculate the discount totalAmount
	fullPrice = (quantity * RETAIL_PRICE)
	print(' Full price:', fullPrice)
		
	#Calculates the discounted totalAmount
	discountAmount = (fullPrice * discountRate)
	print(' Discount amount: $', discountAmount)
		
	#Calulates the total after the discount amount 
	totalAmount = (fullPrice - discountAmount)
	print(' Total Amount: $', totalAmount)
	
		# This is calling the main function
main()

