import os
from xml.dom.minidom import parse
import xml.etree.ElementTree as ET
import pickle
import ace_filereader as fr

#遍历文件获取所有的实体 关系 文档
def get_ERDs():
    E = {}
    R = {}
    D = {}
    for root, dirs, files in os.walk("English"):
        for fn in files:
#            root_arr = root.split("\\")
#            fn_arr = fn.split(".")
            if(fn.find(".sgm")>0 and root.find("/time2norm")>0):
                f_no = fn[0:-4]
                named_entities, rels, doc = fr.get_ERD(root+"/"+f_no)
                E[f_no]=named_entities
                R[f_no]=rels
                D[f_no]=doc
    return E, R, D

def load():
    if not os.path.exists('ace.json'):
        create()
    with open('ace.json', 'rb') as f:
        data = pickle.load(f)
    return data

#创建 实体 关系 文档的数据文件
def create():
    nes, res, docs = get_ERDs()
#    texts = getText()

    with open('nes_res.pkl', 'wb') as output:
        pickle.dump({"nes":nes,"res":res, "docs":docs}, output)

def conbime_list_dic(ld):
    return dict(pair for d in ld for pair in d.items())


if __name__ == "__main__":
    datatest = load()

#     for x in rl:
#        if x =="METONYMY":
#            print x
