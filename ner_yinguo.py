# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 14:29:58 2020

@author: 12894
"""
#单伟
import pandas as pd
import numpy as np
import random
import json

#def list_find1(list1, list2):
#    for i in range(len(list1)):
#        if list1[i: i + n_list2] == list2:
#            tag[i] = 'B-C'
#            tag[i+1: i + n_list2] = (n_list2 - 1)*['I-C']    
#    return tag
#
#def list_find2(list1, list2):
#    n_list2 = len(list2)
#    for i in range(len(list1)):
#        if list1[i: i + n_list2] == list2:
#            tag[i] = 'B-E'
#            tag[i+1: i + n_list2] = (n_list2 - 1)*['I-E']    
#    return tag


with open ('./Data/causality/samples_causality_add.txt', 'r', encoding = 'utf-8') as f:
    lines1 = list(set(f.readlines()))
    
with open ('./Data/causality/samples_causality_tags.txt', 'r', encoding = 'utf-8') as f:
    lines2 = list(set(f.readlines()))
 
with open ('./Data/causality/samples_causality_neg.txt', 'r', encoding = 'utf-8') as f:
    lines3 = list(set(f.readlines()))
    
with open ('./Data/causality/samples_causality_neg_add.txt', 'r', encoding = 'utf-8') as f:
    lines4 = list(set(f.readlines()))

with open ('./Data/causality/samples_shizhe_neg.txt', 'r', encoding = 'utf-8') as f:
    lines5 = list(set(f.readlines()))
    
lines_all = lines1 + lines2 + random.sample(lines3 + lines4 + lines5, len(lines1 + lines2))

random_order = list(range(len(lines_all)))
np.random.shuffle(random_order)
train_line = [lines_all[j] for i, j in enumerate(random_order) if i % 5 != 0]
test_line = [lines_all[j] for i, j in enumerate(random_order) if i % 5 == 0]

with open('./Data/causality/train_causality_line.txt', 'w', encoding = 'utf-8') as ftrain:    
    for line in train_line:
        
        if len(line.strip().split('\t')) == 1:
            sentence = line.strip()
            Len = len(sentence)
            tag = ['O']*Len
            for i in range(Len):
                ftrain.write(sentence[i] + '\t' + tag[i] + '\n')
            ftrain.write('\n')

        elif len(line.strip().split('\t')) == 3:
            sentence = line.strip().split('\t')[0]
            Len = len(sentence)
            tag = ['O']*Len
            for i in range(Len):
                ftrain.write(sentence[i] + '\t' + tag[i] + '\n')
            ftrain.write('\n')
            
        elif len(line.strip().split('\t')) == 2:
            sentence = line.strip().split('\t')[0]
            causes_ends_dic = json.loads(line.strip().split('\t')[1].replace("'", '"'))
            Len = len(sentence)
            tag = ['O']*Len
            if len(causes_ends_dic) == 1:
                causes = [value for value in causes_ends_dic.values()][0]
                tag[causes[0]:causes[1]] = ['B-S'] + (causes[1] - causes[0] - 1)*['I-S']
                for i in range(Len):
                    ftrain.write(sentence[i] + '\t' + tag[i] + '\n')
                ftrain.write('\n')
            if len(causes_ends_dic) == 2:
                causes1 = [value for value in causes_ends_dic.values()][0]
                tag[causes1[0]:causes1[1]] = ['B-C'] + (causes1[1] - causes1[0] - 1)*['I-C']
                causes2 = [value for value in causes_ends_dic.values()][1]
                tag[causes2[0]:causes2[1]] = ['B-E'] + (causes2[1] - causes2[0] - 1)*['I-E']          
                for i in range(Len):
                    ftrain.write(sentence[i] + '\t' + tag[i] + '\n')
                ftrain.write('\n')    
                
        elif len(line.strip().split('\t')) == 6:
            sentence = line.strip().split('\t')[0]
            causes_ends_dic = json.loads(line.strip().split('\t')[3].replace("'", '"'))
            Len = len(sentence)
            tag = ['O']*Len
            if len(causes_ends_dic) == 1:
                causes = [value for value in causes_ends_dic.values()][0]
                tag[causes[0]:causes[1]] = ['B-S'] + (causes[1] - causes[0] - 1)*['I-S']
                for i in range(Len):
                    ftrain.write(sentence[i] + '\t' + tag[i] + '\n')
                ftrain.write('\n')
            if len(causes_ends_dic) == 2:
                causes1 = [value for value in causes_ends_dic.values()][0]
                tag[causes1[0]:causes1[1]] = ['B-C'] + (causes1[1] - causes1[0] - 1)*['I-C']
                causes2 = [value for value in causes_ends_dic.values()][1]
                tag[causes2[0]:causes2[1]] = ['B-E'] + (causes2[1] - causes2[0] - 1)*['I-E']          
                for i in range(Len):
                    ftrain.write(sentence[i] + '\t' + tag[i] + '\n')
                ftrain.write('\n')
                
    
with open('./Data/causality/test_causality_line.txt', 'w', encoding = 'utf-8') as ftest:    
    for line in test_line:
        if len(line.strip().split('\t')) == 1:
            sentence = line.strip()
            Len = len(sentence)
            tag = ['O']*Len
            for i in range(Len):
                ftest.write(sentence[i] + '\t' + tag[i] + '\n')
            ftest.write('\n')

        elif len(line.strip().split('\t')) == 3:
            sentence = line.strip().split('\t')[0]
            Len = len(sentence)
            tag = ['O']*Len
            for i in range(Len):
                ftest.write(sentence[i] + '\t' + tag[i] + '\n')
            ftest.write('\n')
            
        elif len(line.strip().split('\t')) == 2:
            sentence = line.strip().split('\t')[0]
            causes_ends_dic = json.loads(line.strip().split('\t')[1].replace("'", '"'))
            Len = len(sentence)
            tag = ['O']*Len
            if len(causes_ends_dic) == 1:
                causes = [value for value in causes_ends_dic.values()][0]
                tag[causes[0]:causes[1]] = ['B-S'] + (causes[1] - causes[0] - 1)*['I-S']
                for i in range(Len):
                    ftest.write(sentence[i] + '\t' + tag[i] + '\n')
                ftest.write('\n')
            if len(causes_ends_dic) == 2:
                causes1 = [value for value in causes_ends_dic.values()][0]
                tag[causes1[0]:causes1[1]] = ['B-C'] + (causes1[1] - causes1[0] - 1)*['I-C']
                causes2 = [value for value in causes_ends_dic.values()][1]
                tag[causes2[0]:causes2[1]] = ['B-E'] + (causes2[1] - causes2[0] - 1)*['I-E']          
                for i in range(Len):
                    ftest.write(sentence[i] + '\t' + tag[i] + '\n')
                ftest.write('\n')
            
        elif len(line.strip().split('\t')) == 6:
            sentence = line.strip().split('\t')[0]
            causes_ends_dic = json.loads(line.strip().split('\t')[3].replace("'", '"'))
            Len = len(sentence)
            tag = ['O']*Len
            if len(causes_ends_dic) == 1:
                causes = [value for value in causes_ends_dic.values()][0]
                tag[causes[0]:causes[1]] = ['B-S'] + (causes[1] - causes[0] - 1)*['I-S']
                for i in range(Len):
                    ftest.write(sentence[i] + '\t' + tag[i] + '\n')
                ftest.write('\n')
            if len(causes_ends_dic) == 2:
                causes1 = [value for value in causes_ends_dic.values()][0]
                tag[causes1[0]:causes1[1]] = ['B-C'] + (causes1[1] - causes1[0] - 1)*['I-C']
                causes2 = [value for value in causes_ends_dic.values()][1]
                tag[causes2[0]:causes2[1]] = ['B-E'] + (causes2[1] - causes2[0] - 1)*['I-E']          
                for i in range(Len):
                    ftest.write(sentence[i] + '\t' + tag[i] + '\n')
                ftest.write('\n')


#with open('./Data/train_line.txt', 'w', encoding = 'utf-8') as ftrain:    
#    for line in train_line:
#
#        if len(line.strip().split('\t')) == 1:
#            sentence = line.strip()
#            Len = len(sentence)
#            tag = ['O']*Len
#            for i in range(Len):
#                ftrain.write(sentence[i] + '\t' + tag[i] + '\n')
#            ftrain.write('\n')
#        elif len(line.strip().split('\t')) == 2:
#            sentence = line.strip().split('\t')[0]
#            causes_ends_dic = json.loads(line.strip().split('\t')[1].replace("'", '"'))
#            Len = len(sentence)
#            tag = ['O']*Len
#            if len(causes_ends_dic) == 1:
#                causes = [value for value in causes_ends_dic.values()][0]
#                tag[causes[0]:causes[1]] = ['B-S'] + (causes[1] - causes[0] - 1)*['I-S']
#                for i in range(Len):
#                    ftrain.write(sentence[i] + '\t' + tag[i] + '\n')
#                ftrain.write('\n')
#            if len(causes_ends_dic) == 2:
#                causes1 = [value for value in causes_ends_dic.values()][0]
#                tag[causes1[0]:causes1[1]] = ['B-C'] + (causes1[1] - causes1[0] - 1)*['I-C']
#                causes2 = [value for value in causes_ends_dic.values()][1]
#                tag[causes2[0]:causes2[1]] = ['B-E'] + (causes2[1] - causes2[0] - 1)*['I-E']          
#                for i in range(Len):
#                    ftrain.write(sentence[i] + '\t' + tag[i] + '\n')
#                ftrain.write('\n')
#                
#    
#with open('./Data/test_line.txt', 'w', encoding = 'utf-8') as ftest:    
#    for line in test_line:
#
#        if len(line.strip().split('\t')) == 1:
#            sentence = line.strip()
#            Len = len(sentence)
#            tag = ['O']*Len
#            for i in range(Len):
#                ftest.write(sentence[i] + '\t' + tag[i] + '\n')
#            ftest.write('\n')
#        elif len(line.strip().split('\t')) == 2:
#            sentence = line.strip().split('\t')[0]
#            causes_ends_dic = json.loads(line.strip().split('\t')[1].replace("'", '"'))
#            Len = len(sentence)
#            tag = ['O']*Len
#            if len(causes_ends_dic) == 1:
#                causes = [value for value in causes_ends_dic.values()][0]
#                tag[causes[0]:causes[1]] = ['B-S'] + (causes[1] - causes[0] - 1)*['I-S']
#                for i in range(Len):
#                    ftest.write(sentence[i] + '\t' + tag[i] + '\n')
#                ftest.write('\n')
#            if len(causes_ends_dic) == 2:
#                causes1 = [value for value in causes_ends_dic.values()][0]
#                tag[causes1[0]:causes1[1]] = ['B-C'] + (causes1[1] - causes1[0] - 1)*['I-C']
#                causes2 = [value for value in causes_ends_dic.values()][1]
#                tag[causes2[0]:causes2[1]] = ['B-E'] + (causes2[1] - causes2[0] - 1)*['I-E']          
#                for i in range(Len):
#                    ftest.write(sentence[i] + '\t' + tag[i] + '\n')
#                ftest.write('\n')
