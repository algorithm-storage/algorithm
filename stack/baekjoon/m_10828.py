'''
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

total = int(input())
request = [input() for _ in range(total)]

response = list()

for idx, val in enumerate(request):
    split = val.split(' ')

    if split[0] == 'push':
        response.append(int(split[1]))

    elif split[0] == 'pop':
        if len(response) != 0:
            print(response[len(response)-1])
            response.remove(response[len(response)-1])
        else:
            print(-1)

    elif split[0] == 'size':
        print(len(response))

    elif split[0] == 'empty':
        if len(response) != 0:
            print(0)
        else:
            print(1)

    elif split[0] == 'top':
        if len(response) != 0:
            print(response[len(response)-1])
        else:
            print(-1)


'''
기본적으로 swich case 형식을 사용하여 문제풀이를 진행하였음.
더 좋은 방법이 있을까 많이 고민해보지 못함.
'''