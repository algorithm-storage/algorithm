'''
상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 
설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 
예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.
상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.
'''


def division(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

def solution():
    response = 0

    a, b = division(request, 5)
    if b == 0:
        print(a)
        return

    req = request
    while(req > 0):
        req -= 3
        response += 1

        a,b = division(req, 5)
        if b == 0:
            print(response + a)
            return
        else:
            continue
    
    a, b = division(request, 3)
    if b == 0:
        print(a)
        return
    
    print(-1)
    return
    
    
request = int(input())
if 3 > request:
    print(-1)
elif 5000 < request:
    print(-1)
else: 
    solution()



'''
가장 적은 횟수를 구하는 것임으로 while에서 
3씩 제외하고 5로 나눴을 때 떨어지는 수가 해당 반복문 안에서 구할 수 있는 제일 적은 횟수
'''
