"""
written by Ben

This module was created as part of PDAB 7's Modules and packages course.

It contains one function, menu.
"""

import sys

def menu(*args):
	"""
	Present a list of string options to the user and prompt for a choice.

	Repeatedly shows the available options and asks the user to select one.
	If the user imput is not among the option, it asks again until a valid choice is made.

	Args:
		*args: Any number of string options to choose from.

	Returns:
		The chosen string from the provided options.
	"""

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

