participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
answer = ''

# 딕셔너리를 이용한 풀이법1
"""
def solution(participant, completion):
    answer = ''
    p = {participant[x] : 0 for x in range(len(participant))}   # {참가자이름:수} 형식으로 딕셔너리p 생성
    for i in participant:
        p[i] += 1

    for i in completion:        # completion을 key로 p의 value 감소
        p[i] -= 1

    for i, j in p.items():      # value가 남아있을 경우 key를 출력
        if j == 1:
            answer = i
            break
            
    return answer
    
print(solution(participant, completion))
    """

#해시 함수를 이용한 풀이법
"""def solution(participant, completion):
    h = {}
    temp = 0
    for p in participant:   # participant의 해시값을 key로 하여 딕셔너리에 key(해시값):value(참가자)의 형태로 저장한다.
        h[hash(p)] = p
        temp += hash(p)     # participant를 순회하며 해시의 값을 temp에 더해준다.
    for c in completion:
        temp -= hash(c)     # completion을 돌며 해시의 값을 temp에서 빼주면 completion에 없는 participant 의 해시값만이 temp에 남는다. 
    return(h[temp])         # 그 해시값을 키값으로 딕셔너리에서 값을 서치하면 완주하지 못한 participant의 이름이 나온다.
print(solution(participant, completion))"""


# 딕셔너리를 이용한 풀이법2
"""def solution(participant, completion):
    dict = {}
    for p in participant:
        dict[p] = dict.get(p, 0) + 1    # p의 디폴트 값을 0으로 초기화한 후 1을 더해 사람의 숫자를 표현

    for i in completion:
        dict[i] -= 1

    for k in dict:
        if dict[k]:
            return k
print(solution(participant, completion))
"""

# zip을 이용한 풀이법
"""def solution(participant, completion):
    answer = ''
    participant.sort()                          #participant와 completion을 정렬
    completion.sort()
    for i,j in zip(participant, completion):    # zip을 통해 participant, completion의 각원소를 비교
        if i != j:                              
            return i
    return participant[-1]
print(solution(participant, completion))"""


# Collections 모듈을 사용한 풀이법
# collections.Counter는 class, dict내 아이템의 발생빈도를 카운트하여 저장한다.
# Counter({'mislav': 2, 'stanko': 1, 'ana': 1}) 와 같은 형태의 결과값이 나온다.

"""import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return(list(answer.keys())[0])

print(solution(participant, completion))
"""


