"""
This module was created as part of PDAB 7's  Modules and packages course.

It contains one function, menu.
"""

import sys

def menu(*args):
	while True:
		print('Available options are:')
		for arg in args:
			print(f'- {arg}')

		user_choice = input('Please choose an item: ')

		if user_choice not in args:
			print('Invalid choice. Please try again')

		else:
			break

	return user_choice

if __name__ == "__main__":
	menu(*sys.argv[1:])

