#8 line: Command line arguments, exception handling

#Thie program adds up integers in the command line
import sys
try:
	total = sum(int(arg) for arg in sys.argv[1:])
	print 'sum =', total
except ValueError:
	print 'Please supply integer argumnets'
