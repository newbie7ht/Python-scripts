import re
text="the quick brown fox"
pattern=r"quick"
match=re.match(pattern,text)
if match:
	print("match found: " ,match.group())
else:
	print("match not found")
