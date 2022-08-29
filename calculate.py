import calendar
from datetime import date
from nis import cat
from unicodedata import category
import pandas as pd

INCOME_CATEGORY =  ("Зарплата", 
                    "От других людей", 
                    "Внесение наличных", 
                    "Возврат", 
                    "Прочие поступления")

OUTCOME_CATEGORY = ("Супермаркеты", 
                    "Рестораны и кафе", 
                    "Транспорт", 
                    "Онлайн-маркеты", 
                    "Все для дома", 
                    "ЖКХ, связь, интернет ", 
                    "Детские товары", 
                    "Одежда и аксессуары", 
                    "Питомцы", 
                    "Развлечения и хобби", 
                    "Здоровье и красота", 
                    "Другим людям",
                    "Погашение кредитов", 
                    "Комиссия",
                    "Снятие наличных",
                    "Налоги, штрафы, взыскания",
                    "Прочие расходы")


def monthly_df(dataframe: pd.DataFrame, type: str):
    """
    
    """
    if "income" in type:
        category = INCOME_CATEGORY
    elif "outcome" in type:
        category = OUTCOME_CATEGORY
    else:
        raise TypeError("Wrong type. Expecting 'income' or 'outcome'.")

    days_in_month = calendar.monthrange(int(dataframe["Дата"][0][6::]), int(dataframe["Дата"][0][3:5]))[1]

    days = []
    for day in range(1, days_in_month+1):
        days.append(str(day).zfill(2))

    result = pd.DataFrame(0, columns = days, index = category)

    for index, row in dataframe.iterrows():
        result[row["Дата"][0:2]][row["Категория"]] += row["Сумма в рублях"]

    return result


def get_total(dataframe: pd.DataFrame):
    """
    
    """

    sum = dataframe["Сумма в рублях"].sum()

    return sum

