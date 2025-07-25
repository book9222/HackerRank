# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = input().split()
n,m = int(n),int(m)
n_middle = (n//2)+1

for i in range(1,n+1):
    if i == n_middle:
        temp = "WELCOME".center(m,"-")
        print(temp)
    if i < n_middle:
        temp = (".|."*(i*2-1)).center(m,"-")
        print(temp)
    if i > n_middle:
        temp = (".|."*((n-i+1)*2-1)).center(m,"-")
        print(temp)