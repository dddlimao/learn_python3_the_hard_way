# 结合使用，练习了如何在程序运行时就读取了一些变量以及在程序运行中需要读取的变量
from sys import argv

script, user_name = argv
prompt = ">"

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few question.")
print(f"Do you like me {user_name}?")

like = input(prompt)

print(f"Where do you live {user_name}")
live = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {like} about liking me.
You live in {live}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
