from sklearn import datasets
import json
from watson_developer_cloud import AlchemyLanguageV1

tweet = datasets.load_files("Twitter")
tweet_data = tweet.data
tweet_label = tweet.target
# print(len(tweet_data.data), len(tweet_data.target_names), len(tweet_data.filenames))

alchemy_language = AlchemyLanguageV1(
    api_key='f02ac302b062e95abb01a9d880f30bae20052f87')
'''
print(json.dumps(
    alchemy_language.language(
        text=tweet_data[0]),
    indent=2))

print(json.dumps(
    alchemy_language.sentiment(
        text=tweet_data[4]),
    indent=2))
print(tweet_data[4])
print(tweet_data[4])'''

error_with = 0
error_without = 0
unsupported = 0
num_pos = 0
num_neg = 0
num_neu = 0
for index, line in enumerate(tweet_data):
    try:
        alchemy = alchemy_language.sentiment(line)
    except:
        unsupported = unsupported + 1
    else:
        if alchemy["docSentiment"]["type"] == "positive":
            sentiment = 1
            num_pos = num_pos + 1
        elif alchemy["docSentiment"]["type"] == "negative":
            sentiment = 0
            num_neg = num_neg + 1
        elif alchemy["docSentiment"]["type"] == "neutral":
            sentiment = 2  # neutral
            num_neu = num_neu + 1
        if tweet_label[index] == sentiment:
            error_with = error_with + 1
        if (tweet_label[index] == sentiment) and (sentiment != 2):
            error_without = error_without + 1
print('unsupport:', unsupported)
print('number of positive:', num_pos)
print('number of negative:', num_neg)
print('number og neutral:', num_neu)
err_rate = error_with / (len(tweet_label) - unsupported)
print('error rate(with neutral):', err_rate)
print('number of errors(with neutral):', error_with)

err_rate = error_without / (len(tweet_label) - unsupported - num_neu)
print('error rate(without neutral):', err_rate)
print('number of errors(without neutral):', error_without)
