# 2007년 1월 1일 월요일. 2007년 x월 y일은 무슨 요일일까
# 9 2
# 1 1 월 (3) => 2 1 목 (-1) => 3 1 수 (3) => 4 1 토 (2) => 5 1 월 (3)
# => 6 1 목 => 7 1 토 (3) => 8 1 화 3 => 9 1 => 금  9 2 토
Day = 0
arrList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekList = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]

x,y = map(int,input().split())

for i in range(x-1):
    Day = Day + arrList[i]
Day = (Day + y) % 7

print(weekList[Day])
