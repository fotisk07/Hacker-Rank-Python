import math
def degrees(ab,bc):
    import math
    print(str(int(round(math.degrees(math.atan2(ab, bc)))))+'°')

if __name__ == "__main__":
    ab=int(input())
    bc = int(input())
    degrees(ab,bc)
    
