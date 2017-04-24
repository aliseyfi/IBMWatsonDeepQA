from watson_developer_cloud import AlchemyLanguageV1
from data import get_data

data, label = get_data()
print('len of data and label:', len(data), len(label))
print('dataLen:', len(data))

alchemy_language = AlchemyLanguageV1(
    api_key='f02ac302b062e95abb01a9d880f30bae20052f87')

error_with = 0
error_without = 0
unsupported = 0
num_pos = 0
num_neg = 0
num_neu = 0
for index, line in enumerate(data):
    try:
        alchemy = alchemy_language.sentiment(line)
    except:
        unsupported = unsupported + 1
    else:
        if alchemy["docSentiment"]["type"] == "positive":
            sentiment = "Positive"
            num_pos = num_pos + 1
        elif alchemy["docSentiment"]["type"] == "negative":
            sentiment = "Negative"
            num_neg = num_neg + 1
        elif alchemy["docSentiment"]["type"] == "neutral":
            sentiment = "Neutral"  # neutral
            num_neu = num_neu + 1
        if label[index] != sentiment:
            error = error_with + 1

print('unsupport:', unsupported)
print('number of positive:', num_pos)
print('number of negative:', num_neg)
print('number og neutral:', num_neu)
err_rate = error / (len(label) - unsupported)
print('error rate:', err_rate)
print('number of errors:', error)
