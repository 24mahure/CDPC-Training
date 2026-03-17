t=int(input())

for i in range(t):
    n,k=map(int, input().split())
    arr=list(map(int,input().split()))

    k=k%n
    
    result = arr[-k:]+arr[:-k]
    
    print(*result)