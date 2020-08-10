# PySort
 sorting algorithms in a nice python script / module thing
 
 # Coming soon:
 bogosort, better error hadeling( specifically in the rand_list function), optional error checking / list acuracy checking in all sorting functions(except stalin sort), ther ability to revieve a least to greatest version, a new function that reverses the order of an input list, and a C version of the script.
 
 # Documentation
 
 1. rand_list function
 	this id to generate a list containing random numbers, mainlt for testing purposes
 	ex. sort.rand_list(0, 10000, 100)
	rand_list(start, stop, total)
	start is the range which numbers will be generated (start must be greater than 0)
	stop is where the numbers will stop being generated to
	total is the total length of the list
 2. bubble function
 	used to bubble sort a list from least to greates
	ex. sort.bubble([1, 7  99, 38, 1451, 254, 23452435, 4]) || bubble(rand_list(0, 100, 100))
	bubble(x)
	x is a list of numbers (non negative)
3. selection function
	used to selection sort a list of numbers from greatest to least
	ex. sort.selection([1, 7  99, 38, 1451, 254, 23452435, 4]) || selection(rand_list(0, 100, 100))
	selection(x)
	x is a list of numbers (non negative)
4. stalin function
	Ued to selection sort a list of numbers from greatest to least using the leading sorting algorith, which also compresses the list quite 	drastically.
	ex. aort.stalin([1, 7  99, 38, 1451, 254, 23452435, 4]) || stalin(rand_list(0, 100, 100))
	stalin(x)
	x is a list of numbers (non negative)
