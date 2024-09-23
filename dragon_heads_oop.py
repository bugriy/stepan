
class Rotation:

    def __init__(self,  direction, duration):

        self.direction = direction
        self.duration = duration


class Head:

    def __init__(self, head_number):
        self.number = head_number
        self.rotations = []


class Dragon:

    def __init__(self, heads_count):
        self.head_count = heads_count
        self.heads = []

        for i in range(heads_count):
            self.heads.append(Head(i))

    def rotate(self, head_number: int,
               r: Rotation):
        self.heads[head_number].rotations.append(r)

    def calculate_minutes_same_direction(self):

        all_heads_rotations = []

        for head in self.heads:

            head_positions = []

            for rotation in head.rotations:
                for _ in range(rotation.duration):
                    head_positions.append(rotation.direction)

            all_heads_rotations.append(head_positions)

        min_positions_count = min([len(x) for x in all_heads_rotations ])

        count = 0

        for pos in range (min_positions_count):

            all_equal = True
            pos1= all_heads_rotations[0][pos]

            for h in all_heads_rotations[1:]:
                if h[pos] != pos1:
                    all_equal = False

            if all_equal:
                count = count + 1

        return count


if "__main__" == __name__:

    dragon_1 = Dragon(heads_count = 3)

    rotations_list = [
        {'head_number': 1, 'direction': 'N', 'duration': 5},
        {'head_number': 1, 'direction': 'S', 'duration': 3},
        {'head_number': 1, 'direction': 'W', 'duration': 4},
        {'head_number': 1, 'direction': 'E', 'duration': 6},
        {'head_number': 1, 'direction': 'S', 'duration': 1},

        {'head_number': 2, 'direction': 'N', 'duration': 4},
        {'head_number': 2, 'direction': 'W', 'duration': 7},
        {'head_number': 2, 'direction': 'S', 'duration': 2},
        {'head_number': 2, 'direction': 'S', 'duration': 1},
        {'head_number': 2, 'direction': 'E', 'duration': 3},

        {'head_number': 3, 'direction': 'N', 'duration': 5},
        {'head_number': 3, 'direction': 'S', 'duration': 1},
        {'head_number': 3, 'direction': 'W', 'duration': 4},
        {'head_number': 3, 'direction': 'S', 'duration': 3},
        {'head_number': 3, 'direction': 'E', 'duration': 5}
    ]

    for r in rotations_list:
        dragon_1.rotate( r['head_number']-1, Rotation( direction=r['direction'], duration=r['duration']) )

    print(dragon_1.calculate_minutes_same_direction())