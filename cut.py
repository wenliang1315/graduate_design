#encoding=utf-8
import jieba.posseg as pseg
import sys
from imp import reload
reload(sys)



cx_dict = ['ag','a','an','ng','n','nr','ns','nt','nz','vg','v','vd','vn','@','j'] # 关键词词性词典, 保留名词、动词、形容词
cx_dict_noun = ['ng','n','nr','ns','nt','nz'] # 关键词词性词典, 保留名词



stopwords = ['房东','时间','人','谢谢','房子','房间','北京','三亚','成都','广州','上海','感觉','有点','谢谢您','下线','祝您']

def cut_words(text):

    cx_terms = pseg.cut(text)
    return [term for term, cx in cx_terms if cx in cx_dict and term ]


def cut_words_noun(text):
    cx_terms = pseg.cut(text)
    return [term for term, cx in cx_terms if cx in cx_dict_noun and term not in stopwords ]



