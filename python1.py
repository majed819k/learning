def feb(n):
  a, b = 1, 1
  for i in range(n):
    a, b = a + b, a
    yield a
   
  
print("those are first 10 number of febunacci number")
for j in feb(10):
  print(f"| {j} |")
