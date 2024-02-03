

class pancake_state:

    def __init__(self, state_str):
        self.state_str = state_str
        self.Backtrakcost=0;





    #returns an array of tuples of neighbor states and the cost to reach them: [(pancake_state1, cost1), (pancake _state2, cost2)...]
    def get_neighbors(self):
        neighbors = []
        print("start node:", self.state_str)
        for i in range(1, len(self.state_str.split(',')) + 1):
            stack_parts = self.state_str.split(',')
            flipped_stack_parts = stack_parts[:i][::-1] + stack_parts[i:]
            cost = self.calculate_changed_places_sum(stack_parts, flipped_stack_parts)
            flipped_stack = ','.join(flipped_stack_parts)

            neighbor_state = pancake_state(flipped_stack)

            # Check for duplicate neighbors before adding
            if neighbor_state.state_str != self.state_str:
                neighbors.append((neighbor_state, cost))
            else:
                print("Duplicate neighbor:", neighbor_state.state_str)
        print(neighbors)
        return neighbors


    #you can change the body of the function if you want
    def __hash__(self):
        return hash(self.state_str)

    #you can change the body of the function if you want
    def __eq__(self, other):
        return self.state_str == other.state_str


    def get_state_str(self):
        return self.state_str

    def calculate_changed_places_sum(self,arr1, arr2):
        # Make sure both arrays have the same length
        if len(arr1) != len(arr2):
            raise ValueError("Both arrays must have the same length")

        # Convert the elements of the arrays to integers
        int_arr1 = list(map(int, arr1))
        int_arr2 = list(map(int, arr2))

        # Initialize the sum of numbers that change places
        changed_places_sum = 0

        # Iterate through the elements of both arrays
        for num1, num2 in zip(int_arr1, int_arr2):
            # Check if the numbers change places
            if num1 != num2:
                changed_places_sum += num1 + num2

        return changed_places_sum
