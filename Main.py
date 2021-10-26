import numpy as np

steps = 0
initialState = []

def random_choice(n,m,k) :
    state = []
    while True :
        state = list(np.random.randint(low=1,high=n+1,size=k))
        ok = True
        for i in state :
            if state.count(i) > m :
                ok = False
        if ok :
            break
    return state

def initialization(n,m,k) :
    global steps 
    steps = 0
    return random_choice(n,m,k)

def checkIsFinal(state,n) :
    global steps
    global initialState
    if steps == 2 * n :
        if np.array_equal(state,initialState) :
            return "Winner is B"
        else :
            return "Winner is A"
    else :
        if np.array_equal(state,initialState) :
            return "Winner is B"
        else :
            return -1



    


initialState = initialization(5,3,8)
print(initialState)
print(checkIsFinal(initialState,5))
