# -*- coding: utf-8 -*-
from warnings import catch_warnings
import get_data
import calculate


FOLDER_PATH = "/home/user/Downloads/"


def main():
    df_income = get_data.get_df_list(FOLDER_PATH, "income")
    df_outcome = get_data.get_df_list(FOLDER_PATH, "outcome")

    # for i in df_outcome:
    #     print(i.loc[0][0])

    cat = set()
    for df in df_outcome:
        for i in df["Категория"]:
            cat.add(i)

    print(cat)



if __name__ == "__main__":
    main()