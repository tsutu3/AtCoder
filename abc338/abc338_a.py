S = input()
if 1<= len(S) <= 100:
  if S.istitle():
    print("Yes")
  else:
    print("No")
else:
  print("No")