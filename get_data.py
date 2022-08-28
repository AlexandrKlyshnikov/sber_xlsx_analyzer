# -*- coding: utf-8 -*-

from datetime import datetime
from os import listdir
from os.path import isfile, join
import re
import pandas as pd

INCOME_PATTERN = "income_\d\d.\d\d\d\d.xlsx"
OUTCOME_PATTERN = "outcome_\d\d.\d\d\d\d.xlsx"


def get_filenames(folder_path: str, regex_pattern: str) -> list:
    """
    Search for sutable files in given folder.
    Return list of filenames.
    """

    pattern = re.compile(regex_pattern)

    all_files = [filename for filename in listdir(folder_path) if isfile(join(folder_path, filename))]
    matched_files = [filename for filename in all_files if pattern.match(filename)]
    matched_files = sorted(matched_files, key=lambda x: datetime.strptime(x, regex_pattern[:-18]+'%m.%Y.xlsx'))

    return matched_files


def get_df_list(folder_path: str, type: str) -> list:
    """
    Get first sheets from xlsx in given folder.
    """

    if "income" in type:
        filenames = get_filenames(folder_path, INCOME_PATTERN)
    elif "outcome" in type:
        filenames = get_filenames(folder_path, OUTCOME_PATTERN)
    else:
        raise TypeError("Wrong type. Expecting 'income' or 'outcome'.")

    dataframes = []
    for filename in filenames:
        dataframes.append(pd.read_excel(folder_path+filename, sheet_name = 0, usecols = "B,D,G"))

    for df in dataframes:
        df['Дата'] = (df['Дата'].str[:-7].str.replace(" января ", ".02.")
                                         .str.replace(" февраля ", ".02.")
                                         .str.replace(" марта ", ".03.")
                                         .str.replace(" апреля ", ".04.")
                                         .str.replace(" мая ", ".05.")
                                         .str.replace(" июня ", ".06.")
                                         .str.replace(" июля ", ".07.")
                                         .str.replace(" августа ", ".08.")
                                         .str.replace(" сентября ", ".09.")
                                         .str.replace(" октября ", ".10.")
                                         .str.replace(" ноября ", ".11.")
                                         .str.replace(" декабря ", ".12."))
                                                

    return dataframes
