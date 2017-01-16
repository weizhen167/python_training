import re

'''
Notes on Regular Expressions:
[] denotes a set of applicable characters i.e. [abc] means it will match if it encounts a, b, or c, but not anything else
[a-b] denotes  the set of characters between a and b in ASCII i.e. [a-z] will match any lowercase letter
Can combine ranges in one bracket i.e. [a-zA-Z] matches any lowercase or uppercase characters
^ denotes negation i.e. [^abc] will match any character except a, b, or c
. will match any character. If you want to match a literal '.', you must use [.] or \. escape character
? will match 0 or 1 occurences of the preceding match i.e. [abc]? will match 'a', 'b', 'c', '', but not anything else
* will match 0 or more occurences of the preceding match i.e. [abc]* will match any number of a, b, and c characters, including the empty string
+ will match 1 or more occurences of the preceding match i.e. [abc]+ will match a, b, c, ababababc, but the empty string will not match
{d} will must match the preceding match exactly d times i.e. [abc]{3} will match 'aaa', 'aba', but not 'aa' or 'aaaa'
{n,m} will match between n and m occurences of the preceding match. If n is left blank, it is 0. If m is left blank, it is infinity. i.e. [abc]{2,10} will match 'ab', 'aaaaab', but not 'a'
\d is any numerical character. shorthand for [0-9] (does not work in Designer user variables, use [0-9] instead)
\w is any word character, which is a letter, number or underscore
a|b will match if either a or b is matched
\Z can be put at the end of the regex to guarantee that this regex matches with the end of the string (\z in rubular)
\A can be put at the beginning of the regex to guarantee that this regex matches with the beginning of the string
'''

#first and last name, at least 1 letter, a space, then at least 1 letter

#first and last name, Capitalized first letters, the rest are lowercase

#Time of day: HH:MM:SS AM/PM where 1 <= HH <= 12 (not zero padded), 00 <= MM <= 59 (zero padded), 00 <= SS <= 59 (zero padded) and followed by AM or PM

#Date: MM/DD/YYYY, Month and day will be 0-padded to always be 2 characters, Year will always be 4. Can accept 00 as month or day (\/ is the escape character for the / character).
#Date: mm/dd/yyyy -- Month, day, and year are not 0 padded, will not accept 00 as month or day (Does not catch invalid dates i.e. 2/30/2017)

#email address - <base_name>@<domain_name>.<ext>
#base_name is 3-20 alphanumeric or underscore characters
#domain_name is 2-10 alpha characters
#ext must be in the set {com, org, edu}


#re python module

my_reg = r'a(bc)*'
#match

my_match =  re.match(my_reg,'abcbca')
#search
my_match_2 = re.search(my_reg, 'dsgfdgfdsgfdsgfdabc')

#group
print my_match_2.group(0)
#print my_match.group(0)

#sub
print re.sub(my_reg, 'sub_text', 'dsgfdgfdsgfdsgfdabc')

#findall
print re.findall(my_reg,'dsgfdgfdsgfdsgfdabc')

#split
print re.split(r'[ae1]','sefas123')


#Good references for RegEx:
#http://rubular.com/
#https://docs.python.org/2/library/re.html


#bonus points: make a regex to recognize proper IP addresses in IPv4 format (4 '.' deliminated values between 0 and 255)
#bonus points 2: make a regex to recognize proper IP addresses in IPv6 format (8 groups of 4 hexidecimal characters [0-9 and a-f in lowercase], with leading 0s in each group eliminated. Groups are : deliminated)
