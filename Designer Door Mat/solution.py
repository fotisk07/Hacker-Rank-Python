h, w = map(int, input().split())
number_of_layers = (h-1) // 2
wh = w - 3

for i in range(0,number_of_layers):
    a, b=int(wh/2), 1 + 2*i
    print(a*"-" + b*".|." + a*"-")
    wh = wh - 6

alpha = int((w-7) / 2)
print(alpha* "-" + "WELCOME" + alpha* "-")
wh =6

for i in range(number_of_layers , 0, -1):
    a, b = int(wh/2), 2*i - 1
    print(a*"-" + b*".|." + a*"-")
    wh = wh + 6
