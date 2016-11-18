#python homework; test average test score and grade!
def main():
	t1=int(input('Enter first test score'))
	t2=int(input('Enter second test score'))
	t3=int(input('Enter third test score'))
	t4=int(input('Enter fourth test score'))
	t5=int(input('Enter fifth test score'))

#calculating the average and printing the average
	average=Calc_average(t5,t4,t3,t2,t1)
	print('average',average)
	
	#calculating the letter grade for each test score and printing the letter grade
	for x in [t1,t2,t3,t4,t5]:
			determine_grade(x)
			
#Calc_average: taking the scores and gives the averages
def Calc_average(n5,n4,n3,n2,n1):
	result=(n5+n4+n3+n2+n1)/5
	return result
	
	#finfing grade with percentage
def determine_grade(testS):
	if testS>=90:
		letter_grade='A'
	elif testS>=80:
		letter_grade='B'
	elif testS>=70:
		letter_grade='C'
	elif testS>= 60:
		letter_grade='D'
	else:
		letter_grade='F'
			
	print('letter grade',letter_grade)
		
		
#prints average and letter grade
main()