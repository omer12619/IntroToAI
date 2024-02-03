from pancake.pancake_state import pancake_state


def base_heuristic(_pancake_state):
    current_state = _pancake_state.get_state_str().split(',')

    goal_state = pancake_state(sort_string(_pancake_state.get_state_str())).get_state_str().split(',')

    # Ensure both states have the same length
    assert len(current_state) == len(goal_state), "Mismatch in state lengths"

    # Calculate Manhattan distance as the heuristic
    heuristic = sum(abs(int(curr) - int(goal)) for curr, goal in zip(current_state, goal_state))

    return heuristic

def advanced_heuristic(_pancake_state):
    return 0


def sort_string(input_string):
    # Split the string into a list of integers
    numbers = [int(num) for num in input_string.split(',')]

    # Sort the list in descending order
    numbers.sort(reverse=True)

    # Convert the sorted list back to a string
    sorted_string = ','.join(map(str, numbers))

    return sorted_string