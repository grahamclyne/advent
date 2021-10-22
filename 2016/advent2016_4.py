input_raw =  open('input4.txt', 'r').read()[:-1].split('\n')
input_encrypted = list(map(lambda x : x.replace(']','').split('['), input_raw))
input = list(map(lambda x : x.replace(']','').replace('-','').split('['), input_raw))
input = [[x[0][:-3], x[0][-3:], x[1]] for x in input]
input_encrypted = [[x[0][:-3], x[0][-3:]]for x in input_encrypted]
total = 0
print(input_encrypted)

for i in input:
    buckets = {}
    for letter in i[0]:
        if letter in buckets.keys():
            buckets[letter] += 1
        else:
            buckets[letter] = 1
    xxx = sorted(buckets.items(), key=lambda x:x[0])
    y = sorted(xxx, key=lambda kv_pair: kv_pair[1], reverse=True)[:5]
    yy = sorted(y,key=lambda kv_pair: kv_pair[0], reverse=False)
    x = ''.join(list(map(lambda x : x[0],sorted(yy, key=lambda kv_pair: kv_pair[1], reverse=True))))
    if x == i[2]:
        total += int(i[1])

for i in range(len(input_encrypted)):
    for j in range(int(input_encrypted[i][1])):
        word = []
        for letter in input_encrypted[i][0]:
            if letter == '-' or letter == ' ':
                shifted = ' '
            elif ((ord(letter) + 1) > 122):
                shifted = 'a'
            else:
                shifted = chr(ord(letter)+1)
            word.append(shifted)
        input_encrypted[i][0] = ''.join(word)
    if('north' in input_encrypted[i][0]):
        print(input_encrypted[i])
