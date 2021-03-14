from ctypes import *
import sys
'''
파이썬에서의 list는 queue와 동일하게 사용된다. 
append() -> 데이터를 뒤에 추가 
pop(0) -> 0번째 인덱스를 가져온다.
'''


time = 0
pos = "L"
_left = list()
_right = list()
finalTime = list()

class DataSet(Structure):
    _fields_ = [("time", c_int), ("position", c_wchar_p), ("index", c_int)]
    
def init(): #입력받을 데이터들을 여기서 셋팅해준다. input()
    for idx in range(M):
        split = request[idx].split()

        item = DataSet(int(split[0]), split[1], idx)
        print("tiem={0}, position={1}, index={2}".format(item.time, item.position, item.index))
        if item.position == "left":
            _left.append(item)
        else:
            _right.append(item)
        
def size(lists):
    return len(lists)

def pop(lists):
    del lists[0]

def front(lists):
    return lists[0]

N, t, M = map(int, input().split())
request = [input() for _ in range(M)]

init()

while size(_left) + size(_right) != 0:
    flag = 0
    if(size(_left) != 0 and front(_left).time <= time):
        flag = 1
        if pos == "L":
            pos = "R"
            count = 0
            while size(_left) != 0 and front(_left).time <= time and count < M:
                finalTime.insert(front(_left).index, time + t)
                pop(_left)
                count = count + 1
            time += t
        else:
            time += t
            count = 0
            while size(_left) != 0 and front(_left).time <= time and count<M:
                finalTime.insert(front(_left).index, time + t)
                pop(_left)
                count = count + 1
            time += t
    
    if size(_right) != 0 and front(_right).time <= time:
        flag = 1
        if pos == "R":
            pos = "L"
            count = 0
            while size(_right) != 0 and front(_right) <= time&count<M:
                finalTime.insert(front(_right).index, time + t)
                pop(_right)
                count = count + 1
            time += t
        else:
            time += t
            count = 0
            while size(_right) != 0 and front(_right).time <= time & count < M:
                finalTime.insert(front(_right).index, time + t)
                pop(_right)
                count = count + 1
    if flag == 0:
        time = time +1 

for i in range(len(finalTime)):
    print(finalTime[i])

