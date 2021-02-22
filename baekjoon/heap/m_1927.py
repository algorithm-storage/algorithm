'''
널리 잘 알려진 자료구조 중 최소 힙이 있다. 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

배열에 자연수 x를 넣는다.
배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.
'''

total = int(input())
request = [int(input()) for _ in range(total)]

response = []

for idx, val in enumerate(request):
    if val == 0:
        if len(response) != 0:
            print(min(response))
            response.remove(min(response))
        else:
            print(0)
    else:
        response.append(val)


'''
파이썬에서 제공하는 문법중 min, max 함수를 사용
리스트(튜플)에서 가장 작은값과 큰 값을 가져올 수 있다.
'''