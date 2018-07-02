if __name__ == '__main__':
    lowest=[]
    secondLowest=[]
    for _ in range(int(input())):
        name=input()
        score=float(input())
        if len(lowest)==0:
    
            lowest=[ [name,score] ]
        elif score < lowest[0][1]:
            secondLowest=lowest
            lowest=[ [name,score] ]
        elif score == lowest[0][1]:
            lowest.append( [name,score] )
        elif len(secondLowest)==0:
            secondLowest=[ [name,score] ]
        elif score < secondLowest[0][1]:
            secondLowest=[ [name,score] ]
        elif score == secondLowest[0][1]:
            secondLowest.append( [name,score] )
    names=[item[0] for item in secondLowest]
    for name in sorted(names):
        print (name)
    
