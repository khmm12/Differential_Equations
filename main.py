def main():
	from modules import DiffEquationMethods
	import re

	Methods = [DiffEquationMethods.EulerMethod, DiffEquationMethods.EulerMethodMod1,
	DiffEquationMethods.EulerMethodMod2, DiffEquationMethods.RungeKuttaMethod]


	print("Avalible methods: ")
	for i in range(len(Methods)):
		print("%d) -" % i, Methods[i].__name__)
	chosen_methods = input("chosen methods: ")
	chosen_methods = [int(i) for i in re.findall(r'\d+', chosen_methods)]

	function = input("function: ")
	a = float(input("a: "))
	b = float(input("b: "))
	h = float(input("h: "))
	y = float(input("y0: "))



	for i in chosen_methods:
		print()
		try:
			Methods[i](function, a, b, y, h)
			print()
		except IndexError:
			pass


if __name__ == "__main__":
	print()
	main()
	print()
	input()