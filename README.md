# tokenization_from_txt_file
In this code, I have created a class with two methods, where the first one tokenizes the words in the corpus (.txt file) with regular expressions and the second one tokenizes the words by turning this into a pandas dataframe. I tried to figure out which one is faster using the timeit module and faced some challenges there. It turned out to be, the regular expressions method is faster.

Details:

In the first method, first I read the .txt file as all alphabet into lower case.
Then using regular expressions, I replaced all whitespaces with new lines to get each word in the string in a separate line
After that I replace if I found two or more new lines with a single new line, as that removes all the empty lines.
Then I removed all the symbols keeping only the alphabet
And finally did " ".join.split() in case we got several words in the same line after removing symbols. i.e.: fake-shot will turn into fake shot after line 19, so we need to take these two words into separate lines to make a word_index of unique words

In the second method, I read the txt file as well in lower case.
Then used .split() to separate each word into new lines and turned the result into a pandas series.
After that I used pd.replace using regex on the pandas series to get rid of the symbols and then sorted the words alphabetically and dropped null and duplicate values using dropna and unique.
and finally used " ".join.split() again like before


Then I defined a function called main() to use the timeit module as the timeit module doesn't work on class methods, I had to use lambda function to make it work. The time for execution could be calculated using only 'time' module too, but that is not good for comparing different function, as that calculates the time for executing the functions only once. And we cannot be sure of which one is faster after executing only once because the time for execution also depends on several other factors i.e. your pc config and current state.

Using timeit allows to run the functions for as many times as you want and that gives a much more accurate result for comparison as those get averaged out.

Results:
the first method using regular expressions only is way faster: (I ran it for 500 times)

Time required for txt_regex = 7.263566300000093
Time required for txt_split_pd = 17.4469024

