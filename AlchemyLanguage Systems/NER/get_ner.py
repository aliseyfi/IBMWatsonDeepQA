#!/usr/bin/env python
from watson_developer_cloud import AlchemyLanguageV1


def get(chunk, tokens):
    alchemy_language = AlchemyLanguageV1(
        api_key='f02ac302b062e95abb01a9d880f30bae20052f87')
    al = alchemy_language.entities(text=chunk, model='ar-news', max_items=200)
    enti = al['entities']
    entities = []
    for e in enti:
        if e['type'] == 'Person' or 'Organization' or 'GeopoliticalEntity' or 'TitleWork':
            entities.append(e)

    index = 0

    enti_tag = []
    for i in range(len(tokens)):
        enti_tag.append('O')

    for e in entities:
        enti_token = e['text'].split(' ')
        type = e['type']
#        print('*---entity:' + e['text'])
#        print('type:' + e['type'])
        for index, token in enumerate(tokens):
            if (token == enti_token[0]) and (enti_tag[index] == 'O'):
                flag = 0
#                print('len enti_token:', len(enti_token))
#                print('len tokens:', len(tokens))
#                print(tokens[-1])
                for i in range(1, len(enti_token)):
                    #                    print('index:', index)
                    #                    print('i:', i)
                    if index + i <= len(tokens) - 1:
                        if (tokens[index + i] == enti_token[i]) and (enti_tag[index + i] == 'O'):
                            flag = flag + 1
                if flag == len(enti_token) - 1:
                    if type == 'Person':
                        enti_tag[index] = 'B-PERS'
#                        print('start PERS:' + token)
                        for i in range(1, len(enti_token)):
                            enti_tag[index + i] = 'I-PERS'
#                            print('body PERS:' + tokens[index + i])
                    elif type == 'Organization':
                        enti_tag[index] = 'B-ORG'
#                        print('start ORG:' + token)
                        for i in range(1, len(enti_token)):
                            enti_tag[index + i] = 'I-ORG'
#                            print('body ORG:' + tokens[index + i])
                    elif type == 'GeopoliticalEntity':
                        enti_tag[index] = 'B-LOC'
#                        print('start LOC:' + token)
                        for i in range(1, len(enti_token)):
                            enti_tag[index + i] = 'I-LOC'
#                            print('body LOC:' + tokens[index + i])
    return enti_tag
