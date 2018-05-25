#!/usr/bin/python3
# -*- coding=UTF-8 -*-
import os
import sys
import re 

def compare_file(f):
    matchobj = re.match("wskey_value(\w*)", f, flags=0)
    num = 0
    if matchobj:
        num = int(matchobj.group(1))
        # print(num)
    return num
def compare_file_seek(f):
    matchobj = re.match("wskey_seek_value(\w*)", f, flags=0)
    num = 0
    if matchobj:
        num = int(matchobj.group(1))
        # print(num)
    return num

def print_data(data,name):
    print(name)
    for item in data:
        print(item, end=' ')
    print()

def deal_ws_data(path,isseek):
    files = os.listdir(path)
    files.sort(key=compare_file)
    if isseek == "isseek":
        files.sort(key=compare_file_seek)
        seekrandom1=[]
        seekrandom2=[]
        for file in files:
            i = False
            f = open(path+"/"+file)
            iter_f = iter(f)
            for line in iter_f:
                matchobj = re.match("(seekrandom\s*:)\s*(\w*.\w*)\smicros/op;", line, flags=0)
                if matchobj:
                    # print(matchobj.group, ..., sep=' ', end='\n', file=sys.stdout)
                    data = matchobj.group(2);
                    if i == False:
                        seekrandom1.append(data)
                        i = True
                    else:
                        seekrandom2.append(data)
        print_data(seekrandom1,"seekrandom1")
        print_data(seekrandom2,"seekrandom2")
    else:
        fillseq=[]
        fillseq_bandwidth=[]
        fillrandom=[]
        fillrandom_bandwidth=[]
        readrandom1=[]
        readseq1=[]
        readseq1_bandwidth=[]
        compact=[]
        readrandom2=[]
        readseq2=[]
        readseq2_bandwidth=[]
        for file in files:
            # print(file)
            if os.path.isfile(path +"/"+file):
                f = open(path+"/"+file)
                iter_f = iter(f)
                i = False
                j = False
                for line in iter_f:
                    matchobj = re.match("(fillseq\s*:)\s*(\w*.\w*)\smicros/op;\s*(\w*.\w*)\sMB/s", line, flags=0)
                    if matchobj:
                        # print(matchobj.group())
                        data2 = matchobj.group(2);
                        fillseq.append(data2)
                        data3 = matchobj.group(3);
                        fillseq_bandwidth.append(data3)
                    matchobj = re.match("(fillrandom\s*:)\s*(\w*.\w*)\smicros/op;\s*(\w*.\w*)\sMB/s", line, flags=0)
                    if matchobj:
                        # print(matchobj.group())
                        data2 = matchobj.group(2);
                        fillrandom.append(data2)
                        data3 = matchobj.group(3);
                        fillrandom_bandwidth.append(data3)
                    matchobj = re.match("(readrandom\s*:)\s*(\w*.\w*)\smicros/op;", line, flags=0)
                    if matchobj:
                        data = matchobj.group(2);
                        if i == False:
                            readrandom1.append(data)
                            i = True
                        else:
                            readrandom2.append(data)
                    matchobj = re.match("(readseq\s*:)\s*(\w*.\w*)\smicros/op;\s*(\w*.\w*)\sMB/s", line, flags=0)
                    if matchobj:
                        # print(matchobj.group())
                        data2 = matchobj.group(2);
                        data3 = matchobj.group(3);
                        if j == False:
                            readseq1.append(data2)
                            readseq1_bandwidth.append(data3)
                            j = True
                        else:
                            readseq2.append(data2)
                            readseq2_bandwidth.append(data3)
                    matchobj = re.match("(compact\s*:)\s*(\w*.\w*)\smicros/op;", line, flags=0)
                    if matchobj:
                        data = matchobj.group(2);
                        compact.append(data)
        print_data(fillseq,"fillseq")
        print_data(fillseq_bandwidth,"fillseq_bandwidth")
        print_data(fillrandom,"fillrandom")
        print_data(fillrandom_bandwidth,"fillrandom_bandwidth")
        print_data(readrandom1,"readrandom1")
        print_data(readseq1,"readseq1")
        print_data(readseq1_bandwidth,"readseq1_bandwidth")
        print_data(compact,"compact")
        print_data(readrandom2,"readrandom2")
        print_data(readseq2,"readseq2")
        print_data(readseq2_bandwidth,"readseq2_bandwidth")



# print(sys.argv)
# print(len(sys.argv))
if len(sys.argv) > 2:
    deal_ws_data(sys.argv[1],sys.argv[2])
else:
    print("example:python3 dealdata dir(目录名) isseek")
