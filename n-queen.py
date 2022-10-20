def boardPrint():
    for i in range(0,N):
        for j in range(0,N):
            if board[i] == j:
                print(1, end="")
            else:
                print(0, end="")
        print()
    print()

    
def check(x):
    for i in range(x):
        if board[i] == board[x] or abs(board[i] - board[x]) == x - i: 
            return False
    return True 


def deepfirstsearch(x):
    global cnt

    if x != N:
        for i in range(N):
            board[x] = i
            
            if check(x):
                deepfirstsearch(x+1)
                
    else:
        cnt += 1
        if(cnt < 4):
            boardPrint()

N = int(input())
board = list()
for i in range(0,15):
    board.append(0)
    
cnt = 0
deepfirstsearch(0)
print("num = " + str(cnt))
