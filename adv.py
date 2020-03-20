from room import Room
from player import Player
from world import World
from graph import Graph
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n','n']
# traversal_path = ['n','n','s','s','w','w','e','e','s','s','n','n','e','e']
# traversal_path = ['w','w','s','s','s','e','e','n','n','n','n','s','s','e','e']
# traversal_path = ['w','w','s','s','e','e','n','n','e','e','w','w','n','n','s','w','w','n','s','e','e','e','e','n']
traversal_path = []

# Traversal Algorithm
player.current_room.print_room_description(player)
print(f'room id: {player.current_room.id}')
print(f'room exits: {player.current_room.get_exits()}')
print(f'player.travel(direction)')


def dft(self, starting_vertex):
    s = Stack()
    s.push(starting_vertex)
    visited = set()
    while s.size() > 0:
        v = s.pop()
        if v not in visited:
            print(v)
            visited.add(v)
            for room_exit in player.current_room.get_exits():
                s.push(player.current_room.get_room_in_direction(room_exit))




# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
        print(f'room id: {player.current_room.id}')
        # print(f'room in direction: {player.current_room.get_room_in_direction("n").id}')
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")