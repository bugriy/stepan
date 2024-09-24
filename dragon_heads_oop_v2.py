import random
import sys
import time

class Rotation:

    def __init__(self, direction, duration):
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

    def __init__(self, head_count):
        self.head_count = head_count
        self.heads = []

        for i in range(head_count):
            self.heads.append(Head(i))

    def rotate(self, head_number: int,
               r: Rotation):
        self.heads[head_number].rotations.append(r)

    def calculate_minutes_same_direction(self):

        all_heads_rotations_durations = []

        for head in self.heads:
            sum_of_durations = sum([r.duration for r in head.rotations])
            all_heads_rotations_durations.append(sum_of_durations)

        minutes_total = min(all_heads_rotations_durations)

        print(f"{minutes_total=}")

        same_dir_count = 0

        for minute_num in range(minutes_total):

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

    num_samples = int(50000 / 4.92)
    minutes_one_dir_max = 10
    head_count = 5

    direction_dic = {0: 'N', 1: 'S', 2: 'E', 3: 'W'}

    dragon_1 = Dragon(head_count=head_count)

    for head_number in range(dragon_1.head_count):

        for _ in range(num_samples):
            dragon_1.rotate(head_number, Rotation(direction=direction_dic[random.randrange(0, 3)],
                                                  duration=random.randrange(1, minutes_one_dir_max)))

    start_time = time.perf_counter()

    print(dragon_1.calculate_minutes_same_direction())

    end_time = time.perf_counter()
    print(end_time - start_time, "seconds")
