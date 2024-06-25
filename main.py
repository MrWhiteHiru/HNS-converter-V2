#!/usr/bin/python3
# coded by Mr_White_Hiru
# github https://github.com/MrWhiteHiru/
from core import Binary
from core import Decimal
from core import Octal
import os

# colors
r ='\033[91m' # red
g ='\033[92m' # green
b = '\033[94m' # blue
y = '\033[93m' # yellow
s_b ='\033[96m' # sky_blue
pi = '\033[35m' # pink
reset = '\033[0m' # reset
blink = "\033[5;92m" # blink

def main():
	def banner():
		os.system("cls")
		print(g+"""
██╗  ██╗   ███╗  ██╗    ██████╗    █████╗
██║  ██║   ████╗ ██║   ██╔════╝   ██╔══██╗
███████║   ██╔██╗██║   ╚█████╗    ██║  ╚═╝
██╔══██║   ██║╚████║    ╚═══██╗   ██║  ██╗
██║  ██║ # ██║ ╚███║ # ██████╔╝ # ╚█████╔╝
╚═╝  ╚═╝   ╚═╝  ╚══╝   ╚═════╝     ╚════╝ 
"""+reset)
		print(y+"                 # coded by "+g+"MR WHITE HIRU"+reset)

	banner()
	print(pi+"""       \n\n"""+y+"<-----"+g+""" FROM """+y+"""----->"""+reset+"\n\n"+s_b+"""[1] """+y+"""->"""+g+""" Binary"""+reset+"""\n"""+pi+s_b+"""[2] """+y+"""->"""+g+""" Decimal"""+reset+"\n"+s_b+"""[3] """+y+"""->"""+g+""" Octal"""+reset+"""\n"""+s_b+"""[4] """+y+"""->"""+g+""" Hexadecimal"""+reset)

	choice = int(input(y+"""
   ┌──["""+pi+"""Enter the option"""+reset+y+"""]"""+reset+"""
   """+y+"""└─ᐳ   """+g))
	print(reset)
	if choice == 1:
		banner()
		Binary.binary()
	elif choice == 2:
		banner()
		Decimal.decimal()
	elif choice == 3:
		banner()
		Octal.octal()
	elif choice == 4:
		banner()
		Hexadecimal.hexadecimal()
	else:
		print(blink+r+" Wrong Input!, try again"+reset)
try:
	main()
except:
	print(r+" Something Wrong!, try again"+reset)
