def fib(n):
	"""A function that generates the fibonacci sequence from
	zero upto and including n """
	a, b = 0, 1
	my_fib = []
	if n == a:
		my_fib.append(0)
		return my_fib
	elif n == b:
		my_fib.append(0)
		my_fib.append(1)
		return my_fib
	else:
		my_fib.append(a)
		while b <= n:
			my_fib.append(b)
			a,b = b, a + b



	return my_fib