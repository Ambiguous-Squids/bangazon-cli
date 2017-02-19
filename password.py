'''
Module for password encryption using the bcrypt library
See: https://pypi.python.org/pypi/bcrypt/3.1.0
'''

import bcrypt


class Password:

	'''
		Purpose:
			This class handles encryption process of the password

		Methods:
			__init__(self, password)
			get_hashed_password(self)

		Author:
			@asimonia

	'''

	def __init__(self, password):
		"""Takes a password as string, specified by user and initializes a hashed
		password as bytes for database storage.
		"""

		# convert the string into bytes
		self.password = str.encode(password)

		# Hash a password for the first time, with a randomly-generated salt
		self.hashed = bcrypt.hashpw(self.password, bcrypt.gensalt())

	def get_hashed_password(self):
		return self.hashed.decode('utf-8')



