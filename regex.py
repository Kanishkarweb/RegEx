# search in Regular Expression 
import re

txt = "Due to Heavy Rain chances are High, Schools will be closed"
x = re.search("^Due.*Rain.*High.*closed$", txt)
if x:
  print(" Yes I have a match")
else:
  print("No match")

#Match in Regular Expression

y = re.search("e", txt)
print(y)
