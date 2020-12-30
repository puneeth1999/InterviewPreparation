'''
.If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage
'''

# Numbers 1-9

# There is no particular pattern in the first numbers, so all we can do is spell them out and count them.

# 3 + 3 + 5 +4 + 4 +3 +5 +5 +4 = 36
# Numbers 10-19

# There is also too little pattern in the next 10 numbers that I want to make a deal out of it, so if we count those as well we get

# 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8 = 70
# Numbers 20-99

# Now a pattern starts emerging. For each period of ten numbers, we have a prefix 10 times and then the sequence 1-9, which we have already counted.  So we need to figure out how many letters the tens contain and add 8*36.

# 10*(6 + 6 + 5 + 5 + 5 + 7 + 6 + 6) + 8*36 = 748

# So if we sum that up the number 1-99 will contain 36 + 70 + 74 8= 854 letters
# Numbers 100-999

# We will use sort of the same trick here.

# If we look at one hundred and twenty two (122) and  four hundred and fifty three (453). We will see that the number 1-9 is prepended, then comes the words “hundred and” (10 letters), and last comes a number between 1 and 99.  Whole hundreds such as two hundred (200) are a special case where you have the numbers 1-9 followed by “hundred” (7 letters).

# If we break it down we have the numbers 1-9 occurring 100 times each. => 36*100 = 3600

# 1-99 occurring 9 times => 9*854 = 7686

# We have “hundred” occurring 9 times with 7 letters. => 7*9 = 63

# We have “hundred and” occurring 999 times with 10 letters => 999*10 = 8910

# So in total we have

# 3600 + 7686 + 63 + 8910= 20259
# Summing up

# We still miss one thousand which is another 11 letters, so in total we have 854 + 20259 + 11 = 21124 letters in the numbers 1-1000

# I have seen people who code it using the same analysis such as Samuel Jack over at Functional Fun, but I think I will stop it here.

# And before signing off. For those of you who celebrate Christmas, I hope you have a happy. To you who does not, I just hope you have a pleasant day with lots of good spirit 🙂