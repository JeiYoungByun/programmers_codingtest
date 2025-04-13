# Counter로 배열의 갯수를 세서 dictionary를 만들고 숫자를 비교한다. set으로 key의 순서를 무시하는게 point.
from collections import Counter

def solution(participant, completion):
    p_map = Counter(participant)
    c_map = Counter(completion)
    
    p_lst = set(p_map)
    c_lst = set(c_map)
    
    if p_lst != c_lst:
        for p in p_lst:
            if p not in c_lst:
                return p
    else:
        for a in p_map:
            if p_map[a] != c_map[a]:
                return a
            
# answer(best code)

# from collections import Counter

# def solution(participant, completion):
#     answer = Counter(participant) - Counter(completion)
#     return list(answer.keys())[0]
