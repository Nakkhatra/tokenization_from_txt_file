# tokenization_from_txt_file
In this code, I have created a class with two methods, where the first one tokenizes the words in the corpus (.txt file) with regular expressions and the second one tokenizes the words by turning this into a pandas dataframe. I tried to figure out which one is faster using the timeit module and faced some challenges there. It turned out to be, the regular expressions method is faster.

Details:

In the first method, first I read the .txt file as all alphabet into lower case.
Then using regular expressions, I replaced all whitespaces with new lines to get each word in the string in a separate line
After that I replace if I found two or more new lines with a single new line, as that removes all the empty lines.
Then I removed all the symbols keeping only the alphabet
And finally 
