#!/bin/python

#importing
import sys #system function and parameter

from datetime import datetime

print(datetime.now())

#Importing using alias
from datetime import datetime as dt
print(dt.now())

#Advance strings
sent = "This is a sentence."
print("The last word is "+ sent[-9:])

# Splitting the sentence 
sent_split = sent.split()
print(sent_split)	
sent_join = " ".join(sent_split) # space as delimiter
print(sent_join)	

# Escaping or quoteception 
quote = "this is an \"example of quoteception\" "
print(quote)

#Boolean	
letter = "A"
word = "Apple"
print(letter in word)

letter = "a"
word = "Apple"
print(letter.upper() in word)

#strip uses delimiter space as default.
stripalike = "		hello buddy 	"
print(stripalike.strip())

#Replace
my_name = "Nikhil Pra"
print(my_name.replace("Pra","Pratik"))

print(my_name.find("Pra"))

movie = "The Exorcist"
print("The horror film i ever saw was {} in {} ".format(movie,2014))

# Dictionaries and print Dictionaries are keys and values 
branches = { "IT": ["Nikhil","Pratik"],
	     "CSE" :["Durga"]
		}
# print(branches)
branches["IT"].append("Rohit")
branches["Mech"] = ["Biswajit"]
print(branches)

# Other way to add new keys to dictionary
branches.update({"ETC" : ["Himansh","Abhisekh"]})
print(branches)

print(branches.get("ETC"))

## Converting List into  Dictionary
movie = ["KGF","Andhadhun"]
actor = ["Yash","Ayushman"]
combined = zip(movie,actor)
dic_combined = {key:value for key ,value in combined}
print(dic_combined)
















