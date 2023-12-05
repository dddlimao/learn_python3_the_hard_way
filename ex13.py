from sys import argv
# read the WYSS selection for how to run this
# 这里其实就是读参数值并将这些参数值赋值给变量，方便后面我们使用，注意第一外script表示脚本名
script, first, second, third = argv

print("This script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
