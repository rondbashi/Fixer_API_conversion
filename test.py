#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import unittest
from convert_USD_to_GBP import call_fixer_API, cleanup_input, convert_to_GBP 

class TestFixerAPI(unittest.TestCase):
	
	def test_rate(self):

		fixer_result = call_fixer_API()
		assert fixer_result['rates']['GBP'] >= 0


class TestCleaningup(unittest.TestCase):

	def test_standard_input(self): #This is the required input

		assert cleanup_input("100") == "100"

	def test_extra_input(self): #This is extra input with slightly different input

		assert cleanup_input("100.289") == "100.289"
		assert cleanup_input("13,000") == "13000"
		assert cleanup_input("127USD") == "127"
		assert cleanup_input("$928.2") == "928.2"

	def test_invalid_input(self): #This is to test exception with no numbers

		with self.assertRaises(ValueError):
			cleanup_input("test")


class TestConversion(unittest.TestCase):

	def test_valid_conversion(self):

		for input_val in ["100", "100.289", "13,000", "127USD", "$928.2"]:

			converted = convert_to_GBP(input_val)
			self.assertRegex(converted, "£\d+\.\d{1,2}")

	def test_invalid_conversion(self):

		with self.assertRaises(ValueError):
			convert_to_GBP("test")

if __name__ == '__main__':

	unittest.main()


