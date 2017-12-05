import sys
from collections import Counter
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

class WordCount:
    def __init__(self,f1,f2):
        self.ip_file = f1
        self.ex_file =f2


    def getWords(self):
        #Get the words from input file

        with open(self.ip_file) as f:
            self.words = f.read().lower().split()
        # Get the words from exclude input file
        with open(self.ex_file) as e:
            self.ex_words = e.read().lower().split()
        # Update the words which are not in exclude file
        self.words =[x for x in self.words if x not in self.ex_words]

    def getCount(self):
        self.count_dict = Counter(self.words)
        self.count_dict_percent ={}
        count_sum = sum(self.count_dict.values())

        for k in self.count_dict.keys():
            self.count_dict_percent[k] = [self.count_dict[k],(float(self.count_dict[k])/count_sum)]

        # self.word_count = pd.DataFrame(list(self.count_dict.items()),columns=['Word','Count'])
        # self.word_count= self.word_count.sort_values('Count',ascending=False)
        #
        # self.word_count['Percent'] = (self.word_count['Count']/count_sum)*100

        print 'word', '\t', 'count', '\t', 'Percent'
        for k,v in self.count_dict_percent.items():
            print k,'\t',v[0],'\t',v[1]

    def show_cloud(self):
        wordcloud = WordCloud(width=900, height=500, max_words=1628, relative_scaling=1,\
                              normalize_plurals=False).generate_from_frequencies(frequencies=self.count_dict)
        plt.imshow(wordcloud)
        plt.axis('off')
        plt.show()

    def show_bar(self):
        centers = range(len(self.count_dict))
        plt.bar(centers, self.count_dict.values(), align='center', tick_label=self.count_dict.keys())
        plt.xlim([0, 4])
        plt.show()

if __name__ == '__main__':
    obj=WordCount(sys.argv[1],sys.argv[2])
    obj.getWords()
    obj.getCount()
    obj.show_cloud()
    obj.show_bar()