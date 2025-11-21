# Code for a doctest script, suitable for execution within Wing IDE to tests for a Python function that cumulatively achieve path coverage.
# Vincent T Mukwevo MKWVIN004
# 08/04/2024
'''
>>> import numberutil
>>> numberutil.aswords(934)
'nine hundred and thirty four'
>>> numberutil.aswords(100)
'one hundred'
>>> numberutil.aswords(60)
'sixty'
>>> numberutil.aswords(29)
'twenty nine'
>>> numberutil.aswords(0)
'zero'
>>> numberutil.aswords(19)
'nineteen'
>>> numberutil.aswords(111)
'one hundred and eleven'
>>> numberutil.aswords(150)
'one hundred and fifty'

'''
import doctest
doctest.testmod(verbose=True)