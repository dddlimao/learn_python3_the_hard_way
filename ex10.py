# 打印转义字符，因为字符串中有特殊字符,如\n表示换行，那如果我们就要打出\n就需要转义

tabby_cat = "\tI'm tabbled in"
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
