QUEENS = 10

def gradient_search(board):
    state = getStates(board)

    while (calcObj(state)>0):
        obj = calcObj(state)
        new_state = neighborStates(board, obj)
        print(new_state)
        newBoard(board, new_state)
        if new_state == state:
            break
        state = getStates(board)
    print(state)
    if (calcObj(state)>0):
        return False
    else:
        return True

def newBoard(board, state):
    for i in range(0,QUEENS):
        for j in range(0,QUEENS):
            if (i,j) in state:
                board[i][j]=1
            else:
                board[i][j]=0

def getStates(board):
    state = []
    for i in range(QUEENS):
        for j in range(len(board[i])):
            if board[j][i] == 1:
                state.append((j,i))
    return state

def calcObj(state):
    issues = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[i][0] == state[j][0]:
                issues += 1
            if abs((state[i][0]-state[j][0])/(state[i][1]-state[j][1]))==1:
                issues += 1
    return issues

def neighborStates(board, objective):
    current_state = [None]*QUEENS
    current_obj = 1000
    for i in range(QUEENS):
        state_new = getStates(board)
        for j in range(QUEENS):
            state_new[i] = (j, i)
            obj = calcObj(state_new)
            if obj < current_obj:
                current_obj = obj
                for k in range(len(state_new)):
                    current_state[k] = state_new[k]

                print(str(current_state)+", "+str(current_obj))
    if current_obj < objective:
        print(current_state)
        state_f = current_state
    else:
        state_f = getStates(board)
    print(state_f)
    return state_f


