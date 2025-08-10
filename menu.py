
def menu(*args):
	while True:
		print('Available options are:')
		for arg in args:
			print(arg)

		user_choice = input('Please choose an item: ')

		if user_choice not in args:
			print('Invalid choice. Please try again')

		else:
			break

	return user_choice

