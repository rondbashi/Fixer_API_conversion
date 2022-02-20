#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import requests
import json
import sys 

input_val = "100"

base_currency = "USD"
output_currency = "GBP"
output_currency_mark = "£"

API_key = "" #Please insert your own key.
fixer_call = "http://data.fixer.io/api/latest?access_key=" + API_key + "&symbols=" + output_currency 


def call_fixer_API():
    
    result = None
    while result is None:

        try:

            result = requests.get(fixer_call).json()
            return result

        except:

            pass


def convert_to_GBP(input_amount):

    cleaned_input_amount = cleanup_input(input_amount)
    fixer_result = call_fixer_API()
    rate = fixer_result['rates'][output_currency]
    output_num = round(rate*float(cleaned_input_amount),2)
    return output_currency_mark + str(output_num) 


def cleanup_input(input_amount):

    for to_delete in [",", base_currency, "$"]:

        input_amount = input_amount.replace(to_delete, "")
    
    try:
    
        float(input_amount)
    
    except ValueError:
    
        raise ValueError("This is not a number")
        sys.exit()

    return input_amount.rstrip()


if __name__ == '__main__':

    print (convert_to_GBP(input_val)) #Change the input amount here.
