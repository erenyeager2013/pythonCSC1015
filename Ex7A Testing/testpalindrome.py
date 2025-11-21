# Set of tests for a Python function that cumulatively achieve statement coverage. A palindrome function.
# Mukwevo T Vincent MKWVIN004
# 08/01/2024

'''
>>> import palindrome
>>> palindrome.is_palindrome('a')
True
>>> palindrome.is_palindrome('pop')
True
>>> palindrome.is_palindrome('True')
False
>>> palindrome.is_palindrome('')
True
>>> palindrome.is_palindrome('abBa')
False

'''
import doctest
doctest.testmod(verbose=True)