#!/usr/bin/python
sou = {"zsh_config":"./zsh/.zshrc"}
des = {"zsh_config":"$HOME/.zshrc"}

class Ask_to_do(object):
	def __init__(self, item):
		self.item = item
	def do_or_not(self):
		if(input("Do you want to deal with %s(y/n):" %self.item) == "y"):
			return True
	def deal_with(self, item):
		print("fetching infomation...")
		sou_dir = sou["item"]
		des_dir = des["item"]

	def do(self, do_or_not):
		if do_or_not:
			self.deal_with(self.item)
			print("Done!")

def main():
	print("welcome to auto_config tools\n\n")
	items = ("zsh_config", "system_update")
	for item in items:
		Ask_to_do(item).do(Ask_to_do(item).do_or_not())


if __name__ == '__main__':
	main()
