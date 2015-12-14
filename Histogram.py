
def Area(histogram):
	hist=[]
	max_area=0
	x=0
	end=len(histogram)-1
	while x<=end:
		if (len(hist)==0 or histogram[hist[len(hist)-1]]<=histogram[x]):
			hist.append(x)
			x+=1
		else :
			top=hist.pop()
			if(len(hist)==0):
				topArea=histogram[top]*x
			else:
				topArea=histogram[top]*(x-hist[len(hist)-1]-1)
			if max_area<topArea:
				max_area=topArea
	while len(hist)!=0:
		top=hist.pop()
		if len(hist)==0:
			topArea=histogram[top]*x
		else:
			topArea=histogram[top]*(x-hist[len(hist)-1]-1)
		if max_area<topArea:
			max_area=topArea
	return max_area




#input the histogram data and call the function
try:
	temp_str=input("Enter comma seperated values of histogram: ")
	try:
		histogram=list(temp_str)
		print histogram
		print "Maximum area is: "+str(Area(histogram))		
	except TypeError:
		print "Wrong input syntax\nUse this syntax:10,20,30"
except (SyntaxError,NameError):
	print "Wrong input syntax\nUse this syntax:10,20,30"