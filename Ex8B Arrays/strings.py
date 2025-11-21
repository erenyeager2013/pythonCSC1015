def indices(string_one, string_two):
   
   # To check for all occurances of combination of characters of our string_one within string_two
    occur = len(string_one)
    arr = []
    length = (len(string_two) - occur)
    for i in range (len(string_two) ) :
        if (string_two[i:(i+occur)] == string_one ):
            arr.append(i)
    print(arr)    
        
    
    """
    The function accepts two strings parameters and returns an array containing the index of each occurrance of the first in the second.
    For example, given 'ow' and 'how now brown cow', the occurrences of 'ow' are at indices 1, 5, 10, 15. 
    """
    


# teststrings.py
"""
>>> import strings
>>> strings.indices('a', '')
[]
>>> strings.indices('a', 'a')
[0]
>>> strings.indices('a', 'ha')
[1]
>>> strings.indices('a', 'abba')
[0, 3]
>>> strings.indices('e', 'eek')
[0, 1]
>>> strings.indices('you', 'did you forget?')
[4]
>>> strings.indices('bubub', 'bububub')
[0, 2]

"""

if __name__ == '__main__':
    import doctest
    doctest.testfile('strings.py', verbose=True)

