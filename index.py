print("Введите строку")
s = input()
l = len(s)
m = 0
ind = 0
count = 0
for i in range(l):
    if s[i] != ' ':
        count += 1
    else:
        if count > m:
            m = count
            ind = i - count
        count = 0

if count > m:
    m = count
    ind = i - count + 1

print(s[ind:ind+m])
input()

#Второй способ, когда в предложении 2-а  
#самое большое слово было определено в предыдущем цыкле

countNew = 0

for i in range(l):
    if s[i] != ' ':
        countNew += 1
    else:
        if countNew == m:
            print("Длинное слово")
            print(s[i - countNew + 1: i - countNew + 1 + m])
        countNew = 0

if countNew == m:
    print("Длинное слово")
    print(s[i - countNew + 1: i - countNew + 1 + m])

input()



