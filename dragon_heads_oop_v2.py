import sys


class Rotation:

    def __init__(self,  direction, duration):

        self.direction = direction
        self.duration = duration


class Head:

    def __init__(self, head_number):
        self.number = head_number
        self.rotations = []

    def __str__(self):
        return f'Head {self.number}'


    def get_direction_by_minute(self, minute_num):

        cumsum = 0

        for rotation in self.rotations:

            cumsum = cumsum + rotation.duration

            if minute_num < cumsum:
                return rotation.direction



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

        all_heads_rotations_durations = []

        for head in self.heads:
            sum_of_durations =sum( [r.duration for r in head.rotations] )
            all_heads_rotations_durations.append(sum_of_durations)

        min_positions_count = min(all_heads_rotations_durations)

        same_dir_count = 0

        for minute_num in range (min_positions_count):

            pos1 = self.heads[0].get_direction_by_minute(minute_num)

            all_equal = True

            for head in self.heads[1:]:

                if head.get_direction_by_minute(minute_num) != pos1:
                    all_equal = False
                    break

            if all_equal:
                same_dir_count = same_dir_count + 1

        return same_dir_count


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