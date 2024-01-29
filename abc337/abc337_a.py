N = int(input())
Takahashi = 0
Aoki = 0
for i in range(N):
    s = input().split()
    Takahashi += int(s[0])
    Aoki += int(s[1])
if Takahashi > Aoki:
    print ("Takahashi")
elif Aoki > Takahashi:
    print ("Aoki")
else:
    print("Draw")