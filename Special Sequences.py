import re
from types import new_class

#Special Sequences
#These are used to extract a different kind of information from a given text
#\A
#Matches pattern only at the start of the string.
print("********Checking Staring Word********")
str="sai Tarun"
begin_result=re.findall(r"\Asai",str) #([A-Z].*?)\s
print(begin_result)

#\Z
#Matches pattern only at the end of the string.
print("********Checking Ending********")
end_result=re.findall(r"\d.*?\Z",str)
print(end_result)

#\b
#Returns a match where the specified pattern is at the beginning or at the end of a word.


#Check if there is any word that begins with "Mach"
str = r'Machine learning is the study of computer algorithms that can improve automatically through experience and by the use of data.'
print("**********Checking at begin and end**********")
print(str)
begin_result = re.findall(r"\bMach", str)
print(begin_result)

begin_result = re.findall(r"lly\b", str)
print(begin_result)


#\w
#Matches any alphanumeric character (digits and alphabets).
#Equivalent to [a-zA-Z0-9_]. By the way, underscore _ is also considered an alphanumeric
new_input=input("Enter data to check:")
#^[A-Za-z-0-9]  {8,}$  we can use \w also for alphanumeric chars.
match=re.search("^\w{8,}$",new_input)
if match:
    print(match)
else:
    print("Invalid Data")


#\W
#Matches any non-alphanumeric character. Equivalent to [^a-zA-Z0-9_]
new_input1=input("Enter data to check:")
#[^A-Za-z-0-9]  {8,}$  we can use \w also for non-alphanumeric chars.
match=re.search("[^a-zA-Z0-9_]{5,}$",new_input)
if match:
    print(match)
else:
    print("Invalid Data")
