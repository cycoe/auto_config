#!/usr/bin/python
import os

file_name = {"zsh_config":".zshrc .oh-my-zsh"}


def plus(item, direct):
	if(direct == '1'):
		sou_dir = ' '.join(map(lambda foo:"./"+item+"/"+foo, file_name[item].split()))
		des_dir = "$HOME/"
	else:
		sou_dir = ' '.join(map(lambda foo:"$HOME/"+foo, file_name[item].split()))
		des_dir = item+"/"
		if(not os.path.exists(des_dir)):
			os.system("mkdir "+ des_dir)
	return (sou_dir, des_dir)

def copy(dirs):
	try:
		print("copy %s to %s..." %(dirs[0], dirs[1]))
		os.system("sudo cp -r %s %s" %(dirs[0], dirs[1]))
	except:
		print("no such directory!")
	print("Done!")



class Ask_to_do(object):
	def __init__(self, item):
		self.item = item
	def do_or_not(self):
		if(input("Do you want to deal with %s(y/n):" %self.item) == "y"):
			return True
	def deal_with(self, do_or_not, direct):
		if do_or_not:
			print("\nfetching infomation about %s..." %self.item)
			copy(plus(self.item, direct))

def main():
	print("welcome to auto_config tools\n\n")
	print("Do you want to install or backup?\n")
	print("# 1.install")
	print("# 2.backup")
	direct = input("choice:")
	for item in file_name:
		Ask_to_do(item).deal_with(Ask_to_do(item).do_or_not(), direct)
	print("All done! enjoy!")



if __name__ == '__main__':
	main()
