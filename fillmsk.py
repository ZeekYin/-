# Copyright (c) Zeek Yin. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.
# Also read README.md. IF you use this code, it means you agree everything in README and LICENSE
#v1.2

from transformers import pipeline
import re
import copy
unmasker=pipeline('fill-mask', model='bert-base-uncased')
continu=''
global wds,mx_sc,cd_ls,q_num
wds=[]
mx_sc=0
visit={}
tmp=[]
def dfs(qn, sum):
    global mx_sc,wds,cd_ls,q_num
    if qn >= q_num:
        if sum > mx_sc:
            mx_sc = sum
            #print(sum)
            #print(tmp)
            wds = copy.copy(tmp)
    else:
        for wp in cd_ls[qn]:
            wd = wp['token_str']
            if not visit[wd]:
                visit[wd]=True
                tmp[qn]=wd
                sum=sum + wp['score']
                dfs(qn + 1, sum)
                sum = sum - wp['score']
                visit[wd] = False

while continu == '':
    md = input("Running mode?\n0:normal mode\n1: 4 to 1quiz mode\n2:mul to mul mode\n")
    if md == '0':
        sentence = input("type your question, replace _blanc_ to [MASK]\n")
        try:
            ls = unmasker(sentence)
            candidate_num = input("number of candidates\n")
            candidate_num = int(candidate_num)

            candidates = []
            for i in range(candidate_num):
                candidate = input("input candidate\n")
                candidates.append(candidate)
        except Exception as e:
            print("Unexpected input")
            md=0


    if md=="1":
        try:
            candidate_num = input("number of candidates\n")
            candidate_num = int(candidate_num)
            sentence = input("type your question\n")
            # print(len(ls))
            sentence = re.sub(r'_+', '[MASK]', sentence)
            candidates = []
            b = input()
            for i in range(candidate_num):
                b = input()
                b = input()
                candidate = input()
                candidate=candidate.strip(" ")
                candidates.append(candidate)
            ls = unmasker(sentence)
        except Exception as e:
            print("Unexpected input")
            md=0


    if md=="2":#multi to multi
        try:
            q_num = input("number of questions\n")
            # candidate_num = input("number of candidates\n")
            q_num = int(q_num)
            q = []
            for i in range(0, q_num):
                tx = input()
                tx = tx.replace("空白", "[MASK]")
                print(tx)
                q.append(tx)
                tx = input()
            rw_opt = input()
            candidates = rw_opt.split(" ")
            print(candidates)
            print("*")
            opts = []
            cd_ls = []

            for i in range(0, q_num):
                ls = unmasker(q[i])
                opts.append(ls)
                cds = []
                for wordp in ls:
                    word = wordp['token_str']
                    if word in candidates:
                        cds.append(wordp)
                cd_ls.append(cds)
            #print(cd_ls)
            for wd in candidates:
                visit[wd] = False
            for i in range(0, q_num):
                tmp.append("")
            dfs(0, 0)
            print(mx_sc)
            print(wds)
        except Exception as e:
            print("Unexpected input")
            md=0

###----------------------------------------###
    if md=="1" or md=="0":
        cands = []
        num = 0
        for wordp in ls:
            word = wordp['token_str']
            if word in candidates:
                cands.append(wordp)
                num += 1
        for cand in cands:
            word = cand['token_str']
            score = str(cand['score'])
            print(word + " " + score + "\n")
        if num != candidate_num:
            print("other answers:\n")
            num = 0
            for num in range(10):
                cand = ls[num]
                word = cand['token_str']
                score = str(cand['score'])
                print(word + " " + score + "\n")
        tg = input("continue? Y/N\n")
        if tg == 'N':
            continu = 1

