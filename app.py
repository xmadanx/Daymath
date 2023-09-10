monthdict = {1:1,2:4,3:4,
			 4:0,5:2,6:5,
			 7:0,8:3,9:6,
			 10:1,11:4,12:6}

daysdict = {0:"Saturday",
			1:"Sunday",
			2:"Monday",
			3:"Tuesday",
			4:"Wednesday",
			5:"Thursday",
			6:"Friday"}

day = input("Enter the day : ")
month = input("Enter the month : ")
year = input("Enter the year : ")

def result():
	century = 6 - (2 * (int(year[:2]) % 4)) 
	yearnum = int(year[2:])
	yearcalc = yearnum // 4
	if (yearnum % 4 == 0) and (int(month) < 3):
		leap = 1
	else:
		leap = 0
	result = int(day) + monthdict[int(month)]
	result += century + yearnum + yearcalc - leap
	print(daysdict[result%7])

if __name__ == "__main__":
	result()