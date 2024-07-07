import re
text="apple,banana,mango,orange"
pattern=r","
split_result=re.split(pattern,text)
print("Split result: ",split_result)
