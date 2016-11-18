#the program writes three lines of data to a filter
def main():
	# this opens the named philosophers.txt
	outfile = open('philosophers.txt', 'w')
	
	#this writes the names of the three philosphers to the file.
	outfile.write('John Locke\n')
	outfile.write('David Hume\n')
	outfile.write('Edmund Burke\n')
	
	# Close the file.
	outfile.close()
	
#Calling the main function.
main()
	