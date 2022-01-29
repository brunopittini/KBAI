from collections import deque

class SemanticNetsAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    def solve(self, initial_sheep, initial_wolves):
        #Add your code here! Your solve method should receive
        #the initial number of sheep and wolves as integers,
        #and return a list of 2-tuples that represent the moves
        #required to get all sheep and wolves from the left
        #side of the river to the right.
        #
        #If it is impossible to move the animals over according
        #to the rules of the problem, return an empty list of
        #moves.

        class State():
            
            def __init__(self, sheep_left, wolves_left, sheep_right, wolves_right, boat_loc):
                self.sheep_left = sheep_left
                self.wolves_left = wolves_left
                self.sheep_right = sheep_right
                self.wolves_right = wolves_right
                self.boat_loc = boat_loc
            
            def is_goal(self):
                pass
            
            def is_valid(self):
                pass

            def generate(current_state):
                pass

            def ret_path(self):
                pass

            def BFS(self):
                initial_state = State(initial_sheep, initial_wolves, 0, 0, 0)
                if initial_state.is_goal():
                    return initial_state
                frontier = []
                frontier.append(initial_state)
                explored = set()
                while frontier:
                    state = frontier.pop(0)
                    if state.is_goal():
                        return state
                    explored.append(state)
                    children = generate(state)
                    for child in children:
                        if (child not in explored) and (child not in frontier):
                            frontier.append(child)
                return None