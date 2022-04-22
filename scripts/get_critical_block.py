import argparse
import os
from pprint import pprint

parser = argparse.ArgumentParser ()
parser.add_argument ('-t', '--target_path', type=str, required=True, help="targetfile path")
parser.add_argument ('-c', '--cfg_path', type=str, required=True, help="cfg files path")
args = parser.parse_args ()

tf_cfg_file_list = []
Ftarget_list = []
BBtarget_list = []

class CFG_Node:

    cfg_name = ''
    edge = []

    def __init__(self, name):
        self.cfg_name = name
    
    def creat_edge(self, edge_str):
        #Node0x55c1a7813930 -> Node0x55c1a7813ec0;
        edge_str_process = edge_str.strip('\n').strip(';')
        edge_str_process = edge_str_process.split(' -> ')
        self.edge.append(edge_str_process)


with open(args.target_path+'Ftargets.txt','r') as tf:
    #tf.readlines()
    for Ftarget in tf.readlines():
        Ftarget_list.append(Ftarget.strip('\n'))


with open(args.target_path+'BBtargets.txt','r') as tb:
    for BBtarget in tb.readlines():
        BBtarget_list.append(BBtarget.strip('\n'))
        
for root,dirs,files in os.walk(args.cfg_path):
    for file in files:
        fl = file.split('.')
        if fl[0] == 'cfg':
            if fl[1] in Ftarget_list:
                tf_cfg_file_list.append(os.path.join(root, file))

print(Ftarget_list)
print(BBtarget_list)
print(tf_cfg_file_list)

node_list = []

for path in tf_cfg_file_list:
    flag = ''
    cnt = 0
    with open(path, 'r') as cfg:
        for ln in cfg.readlines()[3:-1]:
            if flag == ln[:19]:    #get edge
                node_list[cnt-1].append(ln.strip('\n').strip('\t'))
            else:                  #get head
                flag = ln[:19]
                node_list.append([ln.strip('\n').strip('\t')])
                cnt += 1

pprint(node_list)
                
                




#提取字符串前缀，去重，根据前缀依次获取不同的的字符串        

#注意多函数匹配情况