from search import search, print_path
from pancake_state import pancake_state
from heuristics import *

if __name__ == '__main__':
    goal_state = "6,5,3,2,1"
    pancake_input = "1,2,5,6,3"
    pancake_state = pancake_state(pancake_input)


    search_result = search(pancake_state, base_heuristic, goal_state)
    print_path(search_result)








