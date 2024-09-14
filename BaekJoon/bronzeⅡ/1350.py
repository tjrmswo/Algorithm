# 클러스터의 크기가 512바이트고, 600 바이트 파일을 저장하려고 한다면
# 두 개의 클러스터에 저장하게 됌. 두 클러스터는 파일을 공유할 수 없기 때문에
# 디스크 사용 공간은 1024바이트가 됌.
# 파일 사이즈와 클러스터의 크기가 주어질 때, 사용한 디스크 공간을 출력하는 프로그램 작성.
N = int(input())
numbers = list(map(int,input().split()))
cluster = int(input())
cnt = 0
for i in range(N):
    if numbers[i] != 0 and numbers[i] <= cluster:
        cnt += 1
    elif numbers[i] == 0:
        continue
    else:
        if numbers[i] % cluster != 0:
            cnt += (numbers[i]//cluster)+1
        else:
            cnt += (numbers[i]//cluster)
print(cluster*cnt)