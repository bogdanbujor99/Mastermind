from typing import Sequence
import numpy as np

steps = 0
initialState = []
all_chosen_sequence = []
n = 5
m = 3
k = 3

class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueChosenTooManyTimes(Error):
    """Raised when the input value is chosen too many times"""
    pass

class ValueNotExist(Error):
    """Raised when the input value does not exist"""
    pass

def random_choice() :
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

def compare_states(state) :
    return np.sum(np.array(state) == np.array(initialState))

def initialization() :
    global steps 
    steps = 0
    return random_choice()

def checkIsFinal(state) :
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

def chosen_sequence():
    global all_chosen_sequence
    sequence = []
    i=1
    while i <= k :
        try:
            color = int(input('Choose a color:'))
            if color > n or color < 1:
                raise ValueNotExist
            elif sequence.count(color) == m :
                raise ValueChosenTooManyTimes
            else :
                sequence.append(color)
        except ValueError :
            i -= 1
            print("Is not a number. Choose again!")
        except ValueNotExist :
            i -= 1
            print("Wrong color. Choose again!")
        except ValueChosenTooManyTimes :
            i -= 1
            print("The color was choosen too many times. Choose again!")
        i += 1
    all_chosen_sequence.append(sequence)

def game():
    global steps
    global initialState
    steps = 1
    initialState = initialization()
    print(initialState)
    while steps <= 2*n :
        chosen_sequence()
        if checkIsFinal(all_chosen_sequence[-1]) == -1 :
            print("Number of matches "+str(compare_states(all_chosen_sequence[-1])))
            print("Your choices:")
            for choice in all_chosen_sequence :
                print(choice)
            steps = steps + 1
        else :
            print("Your choices:")
            for choice in all_chosen_sequence :
                print(choice)
            print(checkIsFinal(all_chosen_sequence[-1]))
            break


game()