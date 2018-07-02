def max2(a,n):
    scores = a.split()
    scores=[int(i) for i in scores]
    maxi = max(scores)
    mini = -1000
    for i in scores :
        if i < maxi and i > mini:
            mini = i
    return mini
        
if __name__ == '__main__':
    n = int(input())
    a=input()
    print(max2(a,n))
        
    
