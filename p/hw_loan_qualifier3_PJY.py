#This program is if the person qualifies for a loan.

#Constants for minimum salary and minium years on the job
MIN_SALARY = 30000.0
MIN_YEARS = 2

def main():
#Get the customers's annual salary.
salary = float(input('Enter your annual salary: '))

#Get the number of years on the job.
years_on_job = int(input('Enter the number of ' + 'years employed: '))

#determine weather the customer qualifies.
if salary >= MIN_SALARY or years_on_job >= MIN_YEARS:
        print('You qualify for the loan.')
else:
        print('You do not qualify for this loan.')
main()