input = [33,14,18,20,45,35,16,35,1,13,18,13,50,44,48,6,24,41,30,42]
#solution for part 1
def count(S, m,n):
    if (n==0):
        return 1
    if(S is None):
        return 0
    if(n < 0):
        return 0
    if(m <=0 and n>= 1 ):
        return 0
    return count (S, m - 1, n) + count (S[:m-1] + S[m:], m-1, n-S[m-1])

#part 2
def count1(S, m, out,n):
    if (n==0):
        return [out]
    if(S is None):
        return []
    if(n < 0):
        return []
    if(m <=0 and n>= 1 ):
        return []
    return count1(S, m-1,out, n) + count1(S[:m-1] + S[m:],m-1, out + [S[m-1]], n-S[m-1])
x = count1(input,len(input),[], 150)
y = []
for i in x:
    if(len(i) == 4):
        y.append(i)
    print(sum(i), i)
print(len(y))
#1 is not correct for part 2