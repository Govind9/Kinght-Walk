import queue
import sys
from KnightRepository import *
        
def bf_search(start, target):
    if (not is_valid(target)) or (not is_valid(start)):
        print("Start/Target position is not valid")
        return
    Q = queue.Queue()
    Q.put(start)
    
    #breadth first search
    while not Q.empty():
        current = Q.get()
        if current == target:
            final_trail = current.trail[::]
            final_trail.append(target.name())
            print(final_trail)
            return
        positions = next_positions(current)
        for position in positions:
            Q.put(position)
 
if len(sys.argv) != 3:
    print("please provide starting and target position in arguments")
    exit(0)
starting_coordinates = Position.coordinates(sys.argv[1])
target_coordinates = Position.coordinates(sys.argv[2])

start = Position(starting_coordinates[0], starting_coordinates[1])
target = Position(target_coordinates[0], target_coordinates[1])

bf_search(start, target)