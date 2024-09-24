import sys

import pandas as pd
import itertools
import random
from tabulate import tabulate
import time

def generate_dataframe(nheads:int, length = 10, minutes_one_dir_max = 10) -> pd.DataFrame:

    direction_dic = {0: 'N', 1: 'S', 2: 'E', 3: 'W'}

    #timerange = pd.date_range("2024-09-23 09:00:000", periods=length, freq="min")

    src_dic_list = []

    for head_num in range(nheads):

        head_num_list = list(itertools.repeat(head_num+1, length))

        direction_list = [ direction_dic[random.randrange(0, 3)] for x in range(length)]

        one_dir_durations_list = [random.randrange(1, minutes_one_dir_max) for x in range(length)]

        src_dic = { 'head_number': head_num_list,
                    'direction': direction_list,
                    'duration': one_dir_durations_list
                    #'dttm': timerange
        }

        df = pd.DataFrame(src_dic)

        src_dic_list.append(df)

    df = pd.concat(src_dic_list).reset_index(drop=True)#.sort_values(by = ['dttm', 'head_number']).reset_index(drop=True)

    return df


def normalize(group):
    result = group.loc[group.index.repeat(group.duration)]
    result = result.reset_index(drop=True)

    result = result.drop(columns=['duration'])

    result['minute_number'] = result.index
    return result

def same_dir_or_not(group, head_count):
    return (len(group) == head_count) and ((group.values[0] == group.values).all())


if "__main__" == __name__:


    num_samples = int(50000 / 4.92)

    minutes_one_dir_max = 10
    head_count = 5

    dragon_df = generate_dataframe(nheads = head_count, length = num_samples, minutes_one_dir_max = minutes_one_dir_max)

    print(tabulate(dragon_df.head(5), headers='keys', tablefmt='psql'))
    print(tabulate(dragon_df.tail(5), headers='keys', tablefmt='psql'))

    start_time = time.perf_counter()

    dragon_df_n = dragon_df.groupby('head_number')[['head_number', 'direction', 'duration']].apply(normalize).reset_index(drop=True)

    print(
    dragon_df_n.groupby('minute_number')['direction'].apply(same_dir_or_not, head_count=head_count).sum()
    )

    end_time = time.perf_counter()
    print(end_time - start_time, "seconds")