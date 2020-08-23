import string
from collections import Counter

import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer


 text = open('read.txt', encoding='utf-8').read()
 lower_case = text.lower()
 cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

tokenized_words = word_tokenize(cleaned_text, "english")


# removing stop words from the tokensized word list
final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)


# NLP Emotion Algorithm
# 1)check if the word in the final word list is also present in emotion.txt
#  -open the emotion file
#  -loop through each lines and clear it
#  -Extract the word and emotion using split

# 2) if word is present -> add the emotion to emotion_list
# 3) finally count each emotion in te emotion list

emotion_list = []
with open('emotion.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)


print(emotion_list)
w = Counter(emotion_list)
print(w)

def sentimental_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if neg>pos:
        print("negative sentiment")
    elif pos > neg:
        print("positive sentiments")
    else:
        print("neutral vibe")

sentimental_analyse(cleaned_text)
# plotting  the emotion on the graph

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()












