import pandas as pd
import itertools
import random
from tabulate import tabulate

def generate_dataframe(nheads:int, length = 10) -> pd.DataFrame:

    direction_dic = {0: 'N', 1: 'S', 2: 'E', 3: 'W'}

    timerange = pd.date_range("2024-09-23 09:00:000", periods=length, freq="min",
                              )
    src_dic_list = []

    for head_num in range(nheads):

        head_num_list = list(itertools.repeat(head_num+1, length))

        direction_list = [ direction_dic[random.randrange(0, 3)] for x in range(length)]

        src_dic = { 'head_number': head_num_list,
                    'direction': direction_list,
                    'dttm': timerange
        }

        df = pd.DataFrame(src_dic)

        src_dic_list.append(df)

    df = pd.concat(src_dic_list).sort_values('dttm').reset_index(drop=True)

    return df

def same_dir_or_not(group):
    values = group.to_numpy()
    result = all(values[0] == values)
    return result


if "__main__" == __name__:

    dragon_df = generate_dataframe(nheads = 3, length = 10)

    print(tabulate(dragon_df, headers='keys', tablefmt='psql'))

    dragon_df.to_csv("dragon_heads.csv")

    print(
    dragon_df.groupby('dttm')['direction'].apply(same_dir_or_not).sum()
    )

