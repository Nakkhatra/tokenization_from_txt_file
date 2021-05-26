class txt_tokenize:
    def __init__(self):
        pass
    def txt_regex(self, filename): # filename=filepath here # This method is much faster!!
        import re
        text = (open(filename).read()).lower()
        text = re.sub(r'\s',r'\n',text) # replacing all whitespaces with new lines
        text = re.sub(r'\n{2,}','\n', text)
        text = re.sub(r'[^a-zA-Z\n]',"", text) # removing all empty lines with r'\n{2,} and all symbols
                                               # (Keeping only alphabetical and new lines) with [^a-zA-Z\n]
        text = sorted(set(text.split("\n")))
        text = " ".join(text).split()          #" ".join, joins all the words seperated by whitespaces in the string with a single space among those
        return text                            # and .split() seperates by whitespace and uses new line as separator for all the words 

    def txt_split_pd(self,filename):
        import pandas as pd
        text = (open(filename).read()).lower()              #opening the txt file as all alphabet in lowercase
        text = pd.Series(text.split())                         #splitting the txt file we read which is a python string now, by whitespaces into new lines so that we get only a single word in each line. Then turned it into pandas series
        text = text.str.replace(r'[^a-zA-Z\n]','',regex=True)  #removing the symbols and digits from the pandas series
        text =list(text.sort_values(axis=0, ascending=True).dropna().unique())  #sorting the words in alphabetically ascending order and dropping null values and duplicate values
        text = " ".join(text).split()               #doing this again in case we got several words in the same line after removing symbols. i.e.: fake-shot will turn into fake shot after line 19, so we need to take these two words into separate lines to make a word_index of unique words
        return text


reg = txt_tokenize()
pd_txt = txt_tokenize()
stateMent1 = lambda: reg.txt_regex("E:\Machine Learning\Dataset Mcbeth.txt")     #I used my filepath in local machine, use your filepath for the .txt file
stateMent2 = lambda: pd_txt.txt_split_pd("E:\Machine Learning\Dataset Mcbeth.txt")

def main():
# if __name__ == "__main__":
    import timeit
    number_of_executions = 500     #Since my computer is slow I took the time for 500 executions, you can do it for like 10000 times for more accurate results for comparison if you have a faster pc
    time1 = timeit.timeit(stmt = stateMent1, number = number_of_executions)
    time2 = timeit.timeit(stmt = stateMent2, number = number_of_executions)
    print("Time required for txt_regex = {}".format(time1))
    print("Time required for txt_split_pd = {}".format(time2))

main()

#My results for 500 times: 
#Time required for txt_regex = 7.263566300000093                (Much faster!)
#Time required for txt_split_pd = 17.4469024
