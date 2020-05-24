# import spacy
import csv
import re
# import ray
# import multiprocessing
from functools import partial
from tqdm import tqdm
from itertools import chain
from random import random, shuffle, randint



def generate_encoded_text(keywords,query):



    encoded_texts = []
    for _ in range(3):
        new_keywords = keywords
        shuffle(new_keywords)
        new_keywords = ";".join(
            new_keywords[:randint(0, 3)])

        encoded_texts.append("<|startoftext|>" +
                             "~@" + new_keywords +
                             "~^"+query+

                             "<|endoftext|>" + "\n")
    return encoded_texts

def encode_keywords(csv_path,

                    out_path='csv_encoded.txt',
                    ):

    data_list = []

    with open(csv_path, 'r', encoding='utf8', errors='ignore') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data_list.append(row)


    shuffle(data_list)

    out_file = open(out_path,'a')

    for d in data_list:
        # print(d['query'])
        encoded_list = generate_encoded_text(d['keywords'].split(';'),d['query'])
        print(encoded_list)
        for i in encoded_list:
            out_file.write(i)


encode_keywords("annotations.csv")



