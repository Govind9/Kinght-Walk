class Position():
    def __init__(self, x, y, trail = []):
        self.x = x
        self.y = y
        self.trail = trail
    
    def name(self):
        if not is_valid(self):
            return 'XX'
        x_axis = {
            0: 'A',
            1: 'B',
            2: 'C',
            3: 'D',
            4: 'E',
            5: 'F',
            6: 'G',
            7: 'H'
        }
        y_axis = {
            0: '1',
            1: '2',
            2: '3',
            3: '4',
            4: '5',
            5: '6',
            6: '7',
            7: '8'
        }
        return x_axis[self.x] + y_axis[self.y]
        
    def coordinates(name):
        if len(name) != 2:
            return (-1, -1)
        x_axis = {
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3,
            'E': 4,
            'F': 5,
            'G': 6,
            'H': 7
        }
        y_axis = {
            '1': 0,
            '2': 1,
            '3': 2,
            '4': 3,
            '5': 4,
            '6': 5,
            '7': 6,
            '8': 7
        }
        if name[0].upper() in x_axis and name[1] in y_axis:
            return (x_axis[name[0].upper()], y_axis[name[1]])
        return (-1, -1)
        
    def __str__(self):
        return "{}({}, {}). Trail:{}".format(self.name(), self.x, self.y, self.trail)
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
def is_valid(position):
    return (position.x >= 0 and position.y >= 0 and position.x <= 7 and position.y <= 7)
        
def next_positions(position):
    if not is_valid(position):
        return []
    new_trail = position.trail[::]
    new_trail.append(position.name())
    all_positions = [
        Position(position.x + 1, position.y + 2, new_trail),
        Position(position.x - 1, position.y + 2, new_trail),
        Position(position.x + 1, position.y - 2, new_trail),
        Position(position.x - 1, position.y - 2, new_trail),
        
        Position(position.x + 2, position.y + 1, new_trail),
        Position(position.x - 2, position.y + 1, new_trail),
        Position(position.x + 2, position.y - 1, new_trail),
        Position(position.x - 2, position.y - 1, new_trail)
    ]
    valid_positions = []
    for pos in all_positions:
        if is_valid(pos):
            valid_positions.append(pos)
    return valid_positions