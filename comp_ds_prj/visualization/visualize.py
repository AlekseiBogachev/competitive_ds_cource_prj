# -*- coding: utf-8 -*-
"""Визуализации и вывод информации об объектах."""

from IPython.display import display
import matplotlib.pyplot as plt
import missingno as msno
import pandas as pd


def review_data(df: pd.DataFrame, n_rows: int = 10) -> None:
    """Вывод общей информации о датафрейме.

    Выводит количество строк и столбцов в датафрейме, его первые n_rows строк,
    общую информацию о столбцах (результат df.info()), описательные статистики
    (df.describe()) отдельно для категориальных и количественных признаков.
    При выводе на экран таблицы функция печатает все её столбцы и все строки,
    если их количество явно не ограничено одним из параметров функции.

    Parameters
    ----------
    df: pd.DataFrame
        Датафрейм с данными.
    n_rows: int
        Количество первых строк, которые будут выведены.
    """
    with pd.option_context(
        "display.max_columns", None, "display.max_rows", None
    ):
        print(f"В данных\nстрок: {df.shape[0]}\nстолбцов: {df.shape[1]}")
        print()

        print("Первые 10 строк таблицы:")
        display(df.head(n_rows))
        print()

        print("Общая информация о столбцах:")
        df.info()
        print()

        print("Доля пропусков в каждом признаке:")
        display((df.isna().sum() / len(df)).round(2))

        msno.matrix(df, figsize=(10, 5))
        plt.title("Распределение пропусков по таблице", fontsize=20)
        plt.show()

        msno.bar(df, figsize=(10, 5))
        plt.title("Количество непустых значений в каждом столбце", fontsize=20)
        plt.show()

        try:
            print("Описательные статистики для числовых признаков:")
            display(
                (
                    df
                    .describe(
                        include=["number"],
                        percentiles=[0.1, 0.25, 0.5, 0.75, 0.9]
                    )
                    .transpose())
            )
        except ValueError:
            print("Числовые признаки отсутствуют.")

        try:
            print("Описательные статистики для категориальных признаков:")
            display(df.describe(include=["object"]).transpose())
        except ValueError:
            print("Категориальные признаки отсутствуют.")

        print()

        if df.duplicated().any():
            print("В данных есть дубликаты!")
        else:
            print("Дубликаты не обнаружены.")

    return None


def count_vals(df: pd.DataFrame, name: str) -> None:
    """Выводит количество повторений уникальных значений.

    Выводит на экран количество повторений каждого уникального значения
    признака name датафрейма df.

    Parameters
    ----------
    df : pd.DataFrame
        Датафрейм, содержащий нужный признак.
    name : str
        Имя признака, количество повторений уникальных значения которого нужно
        посчитать.
    """
    print(f"Количество повторений значения признака {name}")
    display(
        df
        [[name]]
        .value_counts()
        .reset_index()
        .rename(
            columns={
                name: f"Значение признака {name}",
                0: "Количество повторений"
            }
        )
    )
