S= input()
value = 0
for i in range(97, 123):
    sum = S.count(chr(i))
    if value < sum:
        value = S.count(chr(i))
        text = chr(i)
        
print(text)
