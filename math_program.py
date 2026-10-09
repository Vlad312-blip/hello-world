def factorial(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * factorial(n - 1)

if __name__ == "__main__":
	number = 7
	result = factorial(number)
	print(f"FAKTORUAL {number} = {result}")

