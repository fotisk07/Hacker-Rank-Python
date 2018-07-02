def Weird_Meter(N):
    if (N==2 or N==4) or (N%2 == 0 and N>20):
        print("Not Weird")
    else:
        print("Weird")

if __name__ == '__main__':
    N = int(input())
    Weird_Meter(N)
    
