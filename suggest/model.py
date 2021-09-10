import math
class Model():
    def __init__(self):
        pass

    #用户余弦相似度
    def cos_simularity(sele,A:set,B:set):
        w= len(A & B) / math.sqrt(len(A)*len(B))
        return w

