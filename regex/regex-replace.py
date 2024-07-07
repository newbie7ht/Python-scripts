import re
text="the quick brown fox"
pattern=r"brown"
replacement="red"
new_text=re.sub(pattern,replacement,text)
print("nex_txt is :",new_text)

