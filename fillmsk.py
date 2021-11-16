# Copyright (c) Zeek Yin. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.
# Also read README.md. IF you use this code, it means you agree everything in README and LICENSE
#v1.1

from transformers import pipeline
import re
from transformers.pipelines import fill_mask
unmasker=pipeline('fill-mask', model='bert-base-uncased')
continu=''
md=input("Running mode? 0:old mode 1:quiz mode")
if md=='0':
    while continu == '':
        sentence = input("type your question, replace _blanc_ to [MASK]\n")
        ls = unmasker(sentence)
        candidate_num = input("number of candidates\n")
        candidate_num = int(candidate_num)
        candidates = []
        for i in range(candidate_num):
            candidate = input("input candidate\n")
            candidates.append(candidate)
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
else:
    while continu == '':
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
            candidates.append(candidate)
        cands = []
        ls = unmasker(sentence)
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
