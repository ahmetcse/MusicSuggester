import re


str = "17.563.132 kere enesbatır"

print(re.findall(r"\d+",str))
