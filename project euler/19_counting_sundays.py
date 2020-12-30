months = { "January": 31,
        "February" : 28,
        "March" : 31,
        "April" : 30,
        "May" : 31,
        "June" : 30,
        "July" : 31,
        "August" : 31,
        "September" : 30,
        "October" : 31,
        "November" : 30,
        "December" : 31}


for month in months:
	print(months[month])


tuesday_count = 0
day = 0 
extra_days = 0
for year in range(1901, 2001):
	days_in_the_year = 0
	for month in months:
		day += months[month]
		days_in_the_year += months[month]

		if( year % 4 == 0 and month == 'February'):
				if (year % 100 != 0):
					extra_days += 1
					days_in_the_year += 1
					day += 1
				elif(year % 100 ==0 and year % 400 ==0):
					extra_days += 1
					days_in_the_year += 1
					day += 1
		if( (day) % 7  == 0):
				tuesday_count += 1
	print('No. of days in the year',year,'are',days_in_the_year)

print('No. of Tuesdays counted so far is  =', tuesday_count)
print('The number of extra_days because of the leap years are:',extra_days)
# print('extra_days % 7 =', '25 % 7 =', extra_days % 7)
print('So, there were', extra_days // 7, 'extra_no_of_weeks left that we haven\'t considered. After that, it\'s followed by --wed, thu, fri and sat (we don\'t need to consider that).\n So, the total number of Tuesdays are', tuesday_count+3 )

tuesday_count += 3

print('This means only 2 Sundays that have followed')
sunday_count = tuesday_count - 1
print('Since, 1901 Jan1 would be a Tuesday, we need to subract one from the total number of Sundays\n So, the total number of sundays are:', )
sunday_count=sunday_count-1
print(sunday_count)


# def countingSundays():
#     day = 0	
#     sunday_count = 1

#     for year in range(1901,2001):
#         days_in_the_year = 0
#         for m in months:

#             day += months[m]
#             days_in_the_year += months[m]

#             # print(day)
#             if( year % 4 == 0 and m == "February"):
#                 if (year % 100 != 0):
#                 	day += 2
#                 elif(year % 100 ==0 and year % 400 ==0):
#                 	day += 2
#             if day % 7 == 0:
#                 sunday_count += 1
#         print(days_in_the_year)
#     print ("Sundays:", sunday_count)

# countingSundays()