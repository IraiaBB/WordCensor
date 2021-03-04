## Word Censor

The functionality of this program can be summarized in a few steps:    

1. Insert text to censore. Using `input()`, the user inserts the text. This must be written with correct punctuation because the program detects sentences by periods `"."`,
question `"?"` and exclamation `"!"` marks. Then, the list of sentences is returned.    
2. Insert words to censore. With the same basic function, forbidden words are collected in a list and then returned. When the user doesn't want to add more words,
or more text (in the previous step), just leaves the input empty and presses `Intro`.     
3. Remove sentences with censored words. With consecutive `for` loops, each sentence is analyzed by checking if the words of the list are present. If they are,
the sentence is removed from the list.     
4. Finally the text is displayed in lines. Every 40 characters the new line alert turns True and, when a space is found, that line is stored in a new list. At the end,
the result is shown in the console with a `for` an a simple `print()` statement.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
