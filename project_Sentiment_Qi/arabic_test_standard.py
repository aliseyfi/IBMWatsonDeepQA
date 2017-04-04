from sklearn import datasets
tweet = datasets.load_files("Twitter")
tweet_data = tweet.data
tweet_label = tweet.target
print(len(tweet_label),len(tweet_data))
from repustate import Client
client = Client(api_key='5c2851d06291b3bf883a8903f8090e3d3d2c6faf', version='v3')
count = 0
base = 0
num = 400
for i in range(base, base + num):
    f = client.sentiment(tweet.data[i], "ar")
    #print(f['score'])
    #print(tweet.filenames[i])
    if f['score']==0:
        num = num - 1
    else:
        if tweet_label[i] == 1:
            # print("Positive")
            if f['score']>0:
                count = count + 1
        else:
                #print("Negative")
            if f['score']<0:
                count = count + 1
print(count/num)