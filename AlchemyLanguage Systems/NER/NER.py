#!/usr/bin/env python
from get_ner import get

with open('ANERCorp', 'r') as open_file:
    corpus = open_file.readlines()
data = []
sentence = ""
tokens = []
tokens_chunk = []
num_sent = 0
number = 0
for line in corpus:
    token = line.split(' ')[0]
    if token != '.':
        sentence = sentence + ' ' + token
        tokens_chunk.append(token)
    else:
        number = number + 1
        if num_sent < 20:
            sentence = sentence + token
            num_sent = num_sent + 1
            tokens_chunk.append(token)
        elif num_sent == 20:
            sentence = sentence + token
            data.append(sentence)
            num_sent = 0
            sentence = ""
            tokens_chunk.append(token)
            tokens.append(tokens_chunk)
            tokens_chunk = []
# data.append(sentence)
print(number)
print(len(tokens))
print(tokens[-1][-2])
file_out = open("ner_data.txt", 'w')
for line in data:
    file_out.writelines(line + '\n')

print('data done!')
# print(data[-2])

output_file = []

for i, chunk in enumerate(data):
    enti_tag = get(chunk, tokens[i])
    print('*--------chunk:', i)
    for j in range(len(enti_tag)):
        output_file.append(tokens[i][j] + ' ' + enti_tag[j] + '\n')

print('len of the output file:', len(output_file))

file_out = open("output_data.txt", 'w')
for line in output_file:
    file_out.writelines(line)
