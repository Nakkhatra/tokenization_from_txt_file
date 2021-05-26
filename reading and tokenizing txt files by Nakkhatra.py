class txt_tokenize:
    def __init__(self):
        pass
    def txt_regex(self, filename): # filename=filepath here # Much faster!!
        import re
        text = (open(filename).read()).lower()
        text = re.sub(r'\s',r'\n',text) # replacing all whitespaces with new lines
        text = re.sub(r'\n{2,}','\n', text)
        text = re.sub(r'[^a-zA-Z\n]',"", text) # removing all empty lines with r'\n{2,} and all symbols
                                               # (Keeping only alphabetical and new lines) with [^a-zA-Z\n]
        text = sorted(set(text.split("\n")))
        text = " ".join(text).split()
        return text

    def txt_split_pd(self,filename):
        import pandas as pd
        text = (open(filename).read()).lower()
        text = pd.Series(text.split())
        text = text.str.replace(r'[^a-zA-Z\n]','',regex=True)
        text =list(text.sort_values(axis=0, ascending=True).dropna().unique())
        text = " ".join(text).split()
        return text


reg = txt_tokenize()
pd_txt = txt_tokenize()
stateMent1 = lambda: reg.txt_regex("E:\Machine Learning\Dataset Mcbeth.txt")
stateMent2 = lambda: pd_txt.txt_split_pd("E:\Machine Learning\Dataset Mcbeth.txt")

def main():
# if __name__ == "__main__":
    import timeit
    number_of_executions = 1
    time1 = timeit.timeit(stmt = stateMent1, number = number_of_executions)
    time2 = timeit.timeit(stmt = stateMent2, number = number_of_executions)
    print("Time required for txt_regex = {}".format(time1))
    print("Time required for txt_split_pd = {}".format(time2))

main()
