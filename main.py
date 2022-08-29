# -*- coding: utf-8 -*-
from cgitb import reset
from ctypes import resize
from doctest import OutputChecker
from unittest import result
from warnings import catch_warnings
import get_data
import calculate
import pandas as pd


FOLDER_PATH = "/home/user/Downloads/"


def calc_all(folder_path: str):
    """
    
    """

    df_income = get_data.get_df_list(folder_path, "income")
    df_outcome = get_data.get_df_list(folder_path, "outcome")

    income_result = []
    outcome_result = []

    for df in df_income:
        income_result.append(calculate.monthly_df(df, "income"))

    for df in df_outcome:
        outcome_result.append(calculate.monthly_df(df, "outcome"))
    
    result = zip(income_result, outcome_result)

    return result

def main():

    # result = calc_all(FOLDER_PATH)

    # for i in result:
    #     print()
    #     print(i[0])
    #     print()
    #     print(i[1])

    df_income = get_data.get_df_list(FOLDER_PATH, "income")
    df_outcome = get_data.get_df_list(FOLDER_PATH, "outcome")

    for i in range(0, len(df_income)):
        print(calculate.get_total(df_income[i]) - calculate.get_total(df_outcome[i]))


if __name__ == "__main__":
    main()