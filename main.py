#!/usr/bin/python
import os, sys

file_name = {"zsh_config":".zshrc .oh-my-zsh"}


def plus(item, direct):
	if(direct == '1'):
		sou_dir = ' '.join(map(lambda foo:"./"+item+"/"+foo, file_name[item].split()))
		des_dir = "$HOME/"
	else:
		sou_dir = ' '.join(map(lambda foo:"$HOME/"+foo, file_name[item].split()))
		des_dir = item+"/"
	return (sou_dir, des_dir)

def copy(dirs):
	try:
		if(os.path.exists(dirs[1])):
			print("delete the original %s..." %dirs[1])
			os.system("sudo rm -rf " + dirs[1])
		if(not os.path.exists(dirs[1])):
			os.system("mkdir " + dirs[1])
		print("copy %s to %s..." %(dirs[0], dirs[1]))
		os.system("sudo cp -r %s %s" %(dirs[0], dirs[1]))
	except:
		print("no such directory!")
	print("Done!")

class Parser(object):
	def __init__(self):
		self.argv = sys.argv
	def solve(self):
		if(self.argv[1][1] not in ('i', 'b')):
			try:
				raise Argv_error(0)
			except Argv_error as e:
				print("unrecognized arguments!")
				exit(0)
		elif(self.argv[1][1] == 'i'):
			return 1
		else:
			return 2
	def par(self):
		if(len(self.argv) > 2):
			try:
				raise Argv_error(len(self.argv))
			except Argv_error as e:
				print("%i arguments are commited, 1 are required!" %(e.value-1))
				exit(0)
		elif(len(self.argv) == 1):
			print("welcome to auto_config tools\n\n")
			print("Do you want to install or backup?\n")
			print("# 1.install")
			print("# 2.backup")
			direct = input("choice:")
			if(direct in ('1', '2')):
				return direct
			else:
				try:
					raise Argv_error(0)
				except Argv_error as e:
					print("unrecognized arguments!")
					exit(0)
		else:
			return self.solve()

class Argv_error(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)



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
	parser = Parser()
	direct = parser.par()
	for item in file_name:
		Ask_to_do(item).deal_with(Ask_to_do(item).do_or_not(), direct)
	print("All done! enjoy!")



if __name__ == '__main__':
	main()
