#!/usr/bin/env python3

__author__ = "Maxim Khvatalin"
__maintainer__ = "Maxim Khvatalin"
__status__ = "Development"


from modules import function_parse

def frange(start, stop, step):
	while (stop - start) > 1e-10:
		yield start
		start += step


def EulerMethod(function, a, b, y, h):
	y_ = y
	print("EulerMethod")
	print("f(%f) = %f" % (a, y))
	for x_ in frange(a, b, h):
		y_ = y_ + h * function_parse.GetFunctionValue(function, x_, y_)
		print("f(%f) = %f" % (x_ + h, y_))

def EulerMethodMod1(function, a, b, y, h):
	y_ = y
	print("EulerMethodMod1")
	print("f(%f) = %f" % (a, y))
	for x_ in frange(a, b, h):
		x_i_05 = x_ + 0.5 * h
		y_i_05 = y_ + 0.5 * h * function_parse.GetFunctionValue(function, x_, y_)
		f_i_05 = function_parse.GetFunctionValue(function, x_i_05, y_i_05)

		y_ = y_ + h * f_i_05
		print("f(%f) = %f" % (x_ + h, y_))


def EulerMethodMod2(function, a, b, y, h):
	y_ = y
	print("EulerMethodMod2")
	print("f(%f) = %f" % (a, y))
	for x_ in frange(a, b, h):
		f_i = function_parse.GetFunctionValue(function, x_, y_)
		y_i_1_ = y_ + h * f_i
		f_i_1_ = function_parse.GetFunctionValue(function, x_ + h, y_i_1_)

		y_ = y_ + h * 0.5 * (f_i + f_i_1_)
		print("f(%f) = %f" % (x_ + h, y_))

def RungeKuttaMethod(function, a, b, y, h):
	y_ = y
	print("RungeKuttaMethod (n = 2)")
	print("f(%f) = %f" % (a, y))
	for x_ in frange(a, b, h):
		r1 = h * function_parse.GetFunctionValue(function, x_, y_)
		r2 = h * function_parse.GetFunctionValue(function, x_ + h, y_ + r1)

		y_ = y_ + 0.5 * (r1 + r2)
		print("f(%f) = %f" % (x_ + h, y_))