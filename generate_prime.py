def generate_prime(n):
	"""A function that generates prime numbers from 0 to n"""
	def is_prime(x):
		"""A function that tests the primality of x
		   Uses the efficient technique of trial divison"""
		from math import sqrt

		m = 2

		if x < 2:
			print "The first prime number is 2!"
			return False

		while True:
			if m <= sqrt(x):
				if (x % m) == 0:
					return False
				else:
					m += 1
			else:
				return True



	my_prime = []
	for i in range(2, (n + 1)):
		if is_prime(i):
			my_prime.append(i)

	return my_prime
