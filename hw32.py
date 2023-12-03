def same_row(i,j): return (i//4 == j//4)
def same_col(i,j): return (i-j) % 4 == 0
def same_block(i,j): return (i//8 == j//8 and i%4//2 == j%4//2)

def solveSudoku(board):
    ans = []
    idx = board.index('0') if '0' in board else -1
    if idx == -1: #解完了
        return board
    exclude = {board[j] for j in range(16) if same_row(idx,j) or same_col(idx,j) or same_block(idx,j)}
    for m in set('1234')-exclude:
        ans += solveSudoku(board[:idx]+[m]+board[idx+1:])
    return ans
data=[]
for i in range(4):
    data+=input().split()
ans=solveSudoku(data)
temp=0
for i in ans:
    temp+=1
    if(temp==5):
        temp=1
        print()
    print(i,end=" ")