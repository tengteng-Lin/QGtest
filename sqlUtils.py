import pymysql,json
import Confs.conf as cf
from enchant.checker import SpellChecker
from enchant.tokenize import get_tokenizer

#type id=6

def getMetadata():
    db = pymysql.connect(cf.db_ipaddress, cf.db_username, cf.db_password, cf.db_dbname)
    cursor = db.cursor()

    cursor.execute("select * from dataset3 where local_id = 8")
    datas = cursor.fetchall()

    desc = {}
    for id, val in enumerate(cursor.description):
        desc[val[0]] = id

    with open(cf.info_file, 'r', encoding='utf8') as f:
        infos = json.load(f)
        f.close()
    for line in datas:

        for nam, typ in infos.items():
            print(nam, ":", line[desc[nam]])

def getContent():
    contentList = []

    db = pymysql.connect(cf.db_ipaddress, cf.db_username, cf.db_password, cf.db_dbname)
    cursor = db.cursor()
    cursor.execute("select label from uri_label_id3 WHERE id in (select subject from triple3 where dataset_local_id = 8 ) OR id in (select object from triple3 where dataset_local_id = 8 ) "
                   "OR id in (select predicate from triple3 where dataset_local_id = 8 )")
    datas = cursor.fetchall()

    chkr = SpellChecker("en_US")   #拼写检查
    tknzr = get_tokenizer("en_US") #分词器

#词组分词，词频抽取关键词
    for line in datas:
        chkr.set_text(line[0])


        if(len(list(chkr))==0):  #a0f4c594-1ac2-49ad-81cd-487c5960b82b  也会被认为是正确的
            print(line[0])
            #无错，则分词  (是否考虑了词组）   筛选词性、去停用词
            for w in tknzr(line[0]):
                # net_income_marshal_s_office  下划线会被清除
                print(w)
                contentList.append(w[0])

    contentKey = open("contentKey.txt","a");
    contentKey.write("\n".join(contentList))


getContent()







