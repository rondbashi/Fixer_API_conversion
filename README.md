# Fixer_API_conversion
Currency conversion Python programme using Fixer API (https://fixer.io/).

----------------------------------------------------------------------

About convert_USD_to_GBP.py

This script converts the amount in certain currency into another currency. For example 100 USD --> 83.28 GBP.

Set inside convert_USD_to_GBP.py,
- the input value. The default value is "100".
- base currency inside. The default value is "USD".
- output currency. The default value is "GBP"
- output currency mark optionally. The default value is "£"
- API key. It's set empty to submit. You need your own API key from https://fixer.io/ and set inside the code.
- API call paramater if you need.

----------------------------------------------------------------------

About test.py

This script tests convert_USD_to_GBP.py for various inputs.

The script tests each function separately and the last test TestConversion runs the entire conversion of currency. The test tries the required input "100" and additional inputs with slightly different numbers such as "100", "100.289", "13,000", "127USD", "$928.2", as well as invalid input "test".
