import os

模块前缀="module_"
是否开启="" #可选择的值为"yes"或者"no"
所有的模块名字 = []
enabled = ""
file = open("custom.py","w+")
modules = os.listdir("./")

for name in modules:
	if os.path.isdir(name):
		所有的模块名字.append(name)

for name in 所有的模块名字:
	是否开启 = input("enable module:" + name + "? \n" + "please use y or n to answer.")
	if 是否开启 == "y":
		enabled = "yes"
	if 是否开启 == "n":
		enabled = "no"
	单行结果 = 模块前缀 +  name + "_enabled=" + '"' + enabled + '"'
	file.write(单行结果 + "\n")
print("custom.py have been generated!")
file.close()

#to do 特殊参数选项 all_enabled=no 关闭所有模块
#python gen_profile.py all_enabled=no