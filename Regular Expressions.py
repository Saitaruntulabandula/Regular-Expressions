#Regular expressions or RegEx is a sequence of characters mainly used to 
#find(Searching) or replace(Changing) patterns embedded in the text.
from ast import pattern
import re 

#Matches a word at the "beginning" of the String.
#re.match(pattern,string)
#The re.match function returns a match object on success and none on failure.
print("**********Match**********")
match_result = re.match('Tarun',r'Tarun is a Machine Learning Engineer')
print("Beginning word of the string is matched:",match_result)

match_result = re.match('Zeans',r'Tarun Zeans is a Machine Learning Engineer')
print("Beginning word of the string is not matched:",match_result)


#Matches the "first occurrence" of a pattern in the "entire string"(and not just at the beginning).
#re.search(pattern,string)
search_result = re.search('founded',r'Andrew NG founded Coursera. He also founded deeplearning.ai')
print(" ")
print("**********Search**********")
print("Given word is matched:",search_result)

search_result = re.search('spam',r'Andrew NG founded Coursera. He also founded deeplearning.ai')
print("Given word is not matched:",search_result)


#It will return all the occurrences of the pattern from the string.
#I would recommend you to use re.findall() always, it can work like both re.search() and re.match().
print(" ")
print("**********Find All**********")
findall_result = re.findall('founded',r'Andrew NG founded Coursera. He also founded deeplearning.ai')
print("Given word is matched",len(findall_result),"time's.")

findall_result = re.findall('spam',r'Andrew NG founded Coursera. He also founded deeplearning.ai')
print("Given word is matched",len(findall_result),"time's.")


#re.split(pattern, string, [maxsplit=0]):
#This methods helps to split string by the occurrences of given pattern.
print(" ")
print("**********Split**********")
value="Andrew NG founded Coursera. He also founded deeplearning.ai"
print(value)
split_result = re.split('n',r'Andrew NG founded Coursera. He also founded deeplearning.ai')
print(split_result)

split_result = re.split('n',r'Andrew NG founded Coursera. He also founded deeplearning.ai',maxsplit=1)
print(split_result)


#re.sub(pattern, repl, string):
#It helps to search a pattern and replace with a new sub string. 
#If the pattern is not found, string is returned unchanged.
print(" ")
print("**********Sub**********")
sub_result=re.sub("Tarun","Tharun","Sai Tarun Tulabandula")
print("Replaced pattern with given repl:",sub_result)

sub_result=re.sub("Raj","Tharun","Sai Tarun Tulabandula")
print("Pattern is not found so returned string:",sub_result)


#re.compile(pattern, repl, string):
#We can combine a regular expression pattern into pattern objects, which can be used for pattern matching. 
#It also helps to search a pattern again without rewriting it.
print(" ")
print("**********Compile**********")
pattern=re.compile("Tarun") #No need to write pattern again.
compile_result=pattern.findall("Sai Tarun Tulabandula")
compile_result1=pattern.findall("Raj Tarun Peddipaga")
print(compile_result)
print(compile_result1)

















