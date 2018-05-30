# -*- coding: utf-8 -*-
from scipy.io import arff
from io import StringIO

def read_arf(path):
    with open(path) as f:
        content = f.read()
        d = StringIO(content)
        data, meta = arff.loadarff(d)
        
    return data, meta

def get_hour_fragment(data, hour):
    return list(filter(lambda x: int(x) == hour, data))




if __name__ == '__main__':
    print(read_arf('powersupply.arff'))
