from transformers import pipeline
from transformers.pipelines import fill_mask
unmasker=pipeline('fill-mask', model='bert-base-uncased')
continu=''
while continu=='':
    sentence = input("type your question, replace _blanc_ to [MASK]\n")
    ls = unmasker(sentence)
    candidate_num = input("number of candidates\n")
    candidate_num = int(candidate_num)
    candidates = []
    for i in range(candidate_num):
        candidate = input("input candidate\n")
        candidates.append(candidate)
    cands = []
    num=0
    for wordp in ls:
        word = wordp['token_str']
        if word in candidates:
            cands.append(wordp)
            num+=1
    for cand in cands:
        word = cand['token_str']
        score = str(cand['score'])
        print(word + " " + score + "\n")
    if num!=candidate_num:
        print("other answers:\n")
        num=0
        for num in range(10):
            cand=ls[num]
            word = cand['token_str']
            score = str(cand['score'])
            print(word + " " + score + "\n")
    tg=input("contunue? Y/N\n")
    if tg=='N':
        continu=1
