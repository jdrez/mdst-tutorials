"""
Intro to python exercises shell code
"""

def is_odd(x):
    return x % 2 != 0


def is_palindrome(word):
   return word == word[::-1]


def only_odds(numlist):
    newList = []
    for item in numlist:
        if item % 2 != 0:
            newList.append(item)
    return newList


def count_words(text):
    words = text.split(" ")
    
    wordDict = {}
    
    for word in words:
        if word in wordDict: wordDict[word] += 1
        else: wordDict[word] = 1

    return wordDict