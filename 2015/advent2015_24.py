import time
memo = {}

def f(arr, out, k):
    if(k == 0):
        # print("RESULT", out)
      #  memo[(str(arr),k)] = [out]
        return [out]
    if(len(arr) == 0 or k < 0):
        return []    
    arr1 = f(arr[1:], out + [arr[0]], k - arr[0])
    arr2 = f(arr[1:], out, k)
    if(len(arr2) > 0 and len(arr1) > 0):
        return arr2 +  arr1
    elif(len(arr2) ==0):
        return arr1
    else:
        return arr2
memo = {}

def p(arr, out, k):
    temp = []
    if(k == 0 and sorted([i for i in out]) == [1,2,3,4,5,6,7,8,9]):
        return [out]
    if(len(arr) == 0 or k < 0):
        return []
    arr2 = p(arr[1:], out, k)
    arr1 = p(arr[1:], out + [arr[0]], k - 1)
    if(len(arr2) > 0 and len(arr1) > 0):
        return arr2 + arr1
    elif(len(arr2) ==0):
        return arr1
    else:
        return arr2


if __name__ == '__main__':
    start_time = time.time()
    input=  open('input24.txt', 'r').read().replace(',','').split('\n')[:-1]
    arr = [int(x) for x in input]
  #  arr = [1,3,5,11,13,17,19,23,29,31,37,41,43,47,53,59]
    k = sum(arr)/4
    y = f(arr,[],k)
    print(k)
    # output = p(y,[],3)
    # x = set((tuple(x) for x in y))
    # for i in output:
    #     print(i)
    x = sorted(y)
    m = []
    for i in x:
        if(len(i) <= 6):
            m.append(i)
    lala = []
    for i in m:
        prod = 1
        for j in i:
            prod = prod * j
        lala.append(prod)
    print(sorted(lala))
    print("--- %s seconds ---" % (time.time() - start_time))

    #216871 possibilites that add up to len(input)/3 ? 

    #29728298883 too high
    #232530413623 too high
    #10439961859