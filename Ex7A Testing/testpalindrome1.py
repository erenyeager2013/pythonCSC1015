# A program for a doctest script, suitable for execution within Wing IDE to tests for a Python function that cumulatively achieve path coverage.
# Vincent T Mukwevo MKWVIN004
# 11/04/2024

'''
>>> import palindrome
>>> palindrome.is_palindrome('')
True
>>> palindrome.is_palindrome('madam')
True
>>> palindrome.is_palindrome('V')
True
>>> palindrome.is_palindrome('program')
False
>>> palindrome.is_palindrome('abBa')
False

'''
import doctest
doctest.testmod(verbose= True)