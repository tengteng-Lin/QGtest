import json

db_ipaddress = "114.212.190.189"
db_username = "xxwang"
db_password = "xxwang"
db_dbname = "dataset_search_2018nov"
# dataset_path = 'D:/Study_Work/NJU/System/20191015Datasets/data_gov_datasets'
index_path = './db_index_3/'
store_path = './db_index_3/'
info_file = '../Confs/database.json'
# stf_nlp = './QueryParseFiles/stanford-corenlp-full-2018-02-27'
stf_nlp = 'en_core_web_sm'
model_path = './QueryParseFiles/model_bilstm_crf_35_256_64'

total_documents = 100000 # temp for debug
average_field_length = { # temp for debug
    'title': 10,
    'notes': 30,
    'org_title': 5,
    'org_name': 10
}

Has_Initialized = False
parsematch = {}
parsematch_spe = {}

def read_json(file):
    with open(file, 'r', encoding='utf8') as f:
        ret = json.load(f)
        f.close()
    return ret

def Initialize():
    global parsematch
    global parsematch_spe
    parsematch = read_json('ParseMatch_norange.json')
    parsematch_spe = read_json('ParserMatch_spe.json')

def get_parsematch():
    global Has_Initialized
    global parsematch

    if Has_Initialized is True:
        return parsematch
    Initialize()
    Has_Initialized = True


def get_parsematch_spe():
    global Has_Initialized
    global parsematch_spe

    if Has_Initialized is True:
        return parsematch_spe
    Initialize()
    Has_Initialized = True