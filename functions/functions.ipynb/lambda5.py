x = list(range(1,1001))

x35 = list(filter(lambda j: j % 3 == 0 and j % 5== 0,x))
print(x35)