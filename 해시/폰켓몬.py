from collections import Counter

def solution(nums):
    #counter로 갯수를 세서 dictionary 형태로 만듬
    nums_map = Counter(nums)
    
    #리턴 가능한 최대 배열 수를 셈
    cnt = len(nums) / 2
    
    #포켓몬 종류 개수를 셈
    kinds = len(list(nums_map))
    
    #포켓몬종류수보다 리턴 가능한 길이가 길면 길이리턴, 아니면 포켓몬종류리턴
    if kinds > cnt:
        return cnt
    else:
        return kinds