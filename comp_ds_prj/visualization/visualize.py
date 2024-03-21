# -*- coding: utf-8 -*-
"""Визуализации и вывод информации об объектах."""

from typing import Any

import matplotlib.pyplot as plt
import missingno as msno
import pandas as pd
import seaborn as sns
from IPython.display import display


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
        Значение по умолчанию 10.
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
    print(f"Количество повторов уникальных значений признака {name}")

    with pd.option_context(
        "display.max_columns", None, "display.max_rows", None
    ):
        display(
            df
            [[name]]
            .value_counts(dropna=False)
            .reset_index()
            .rename(
                columns={
                    name: f"Значение признака {name}",
                    0: "Количество повторений"
                }
            )
        )


def plot_hbar(
    data: pd.DataFrame, column_name: str, **kwargs: Any
) -> None:
    """Строит горизонтальную столбчатую диаграмму.

    Строит горизонтальную столбчатую диаграмму категориального признака
    column_name датафрейма data. График отрисовывается с помощью метода
    pd.DataFrame.plot(**kwargs), поэтому параметры графика можно передать,
    как именованные аргументы **kwargs.

    Parameters
    ----------
    data : pd.DataFrame
        Датафрейм, содержащий исследуемый признак.
    column_name : str
        Имя признака (столбца датафрейма data).
    **kwargs : Any, optional
        Параметры графика, корректные для метода pd.DataFrame.plot.
    """
    df: pd.Series = (
        data
        [column_name]
        .value_counts(dropna=False)
        .sort_values()
    )

    df.plot(kind="barh", **kwargs)
    plt.show()

    return None


def explore_cat_feature(
    data: pd.DataFrame, column_name: str, **kwargs: Any
) -> None:
    """Выводит информацию о количестве уникальных занчений признака.

    Функция поочередно вызывает функции count_vals() и plot_hbar() и передаёт
    им соответствующие аргумерны. Сначала, выводится таблица с количеством
    повторений каждого уникального значения признака column_name датафрейма data
    (вызов count_vals()). Затем, строится горизонтальная столбчатая диаграмма
    категориального признака column_name датафрейма data (вызов plot_hbar()),
    где график строится с помощью метода pd.DataFrame.plot(**kwargs),
    поэтому параметры графика можно передать, как именованные аргументы
    **kwargs.

    Parameters
    ----------
    data : pd.DataFrame
        Датафрейм, содержащий исследуемый признак.
    column_name : str
        Имя признака (столбца датафрейма data).
    **kwargs : Any, optional
        Параметры графика, корректные для метода pd.DataFrame.plot.
    """
    count_vals(data, column_name)
    print()
    plot_hbar(data, column_name, **kwargs)

    return None


def plot_num_feature_distibs(
    data: pd.DataFrame, column_name: str, bins: int = 23
) -> None:
    """Выводит графики, характеризующие распределение значений признака.

    Выводит на экран гистограмму с KDE, диаграмму размаха и ECDF для признака
    (столбца) с именем column_name из датафрема data.

    Parameters
    ----------
    data : pd.DataFrame
        Датафрейм, содержащий исследуемый признак.
    column_name : str
        Имя признака (столбца датафрейма data).
    bins: int
        Количество корзин на гистограмме. Значение по умолчанию 23.
    """
    fig, ax = plt.subplot_mosaic(
        [['hist', 'ecdf'], ['box',  'ecdf']],
        figsize=(12, 6),
        gridspec_kw=dict(width_ratios=[2, 1], height_ratios=[2, 1])
    )

    sns.histplot(
        data=data,
        x=column_name,
        ax=ax['hist'],
        stat='density',
        kde=True,
        bins=bins,
    )
    sns.ecdfplot(data=data, x=column_name, ax=ax['ecdf'], stat='proportion')
    sns.boxplot(data=data, x=column_name, ax=ax['box'])

    plt.suptitle(f'Распределение значений признака {column_name}')

    ax['hist'].set_title('Гистограмма и KDE')
    ax['hist'].set_ylabel('Плотность вероятноти')
    ax['hist'].set_xlabel('')

    ax['ecdf'].set_title('ECDF')
    ax['ecdf'].set_ylabel('Доля значений')
    ax['ecdf'].tick_params(axis='x', rotation=45)

    for axes in ax:
        ax[axes].grid()

    plt.tight_layout()

    plt.show()

    return None


def explore_num_feature(
    data: pd.DataFrame, column_name: str, bins: int = 23
) -> None:
    """Выводит информацию о разспределении значений количественного признака.

    Выводит информацию о разспределении значений количественного признака
    column_name датафрейма data. Сначала выводит на экран информацию о
    количестве пропусков, затем, выводит описательные статистики, затем выводит
    графики распределения значений с помощью функции plot_num_feature_distibs():
    выводит на экран гистограмму с KDE, диаграмму размаха и ECDF.

    Parameters
    ----------
    data : pd.DataFrame
        Датафрейм, содержащий исследуемый признак.
    column_name : str
        Имя признака (столбца датафрейма data).
    bins: int
        Количество корзин на гистограмме. Значение по умолчанию 23.
    """
    print(f"Признак {column_name}")
    na_counts: int = data[column_name].isna().sum()

    print(f"Количество пропусков: {na_counts}")
    print()

    print("Описательные статистики:")
    display(
        data[[column_name]].describe(percentiles=[0.1, 0.25, 0.5, 0.75, 0.9])
    )

    plot_num_feature_distibs(data, column_name, bins)

    return None


def num_vs_cat_boxplots(
    data: pd.DataFrame,
    cat_feature: str,
    num_feature: str,
    **kwargs: Any,
) -> None:
    """Строит диаграммы размаха признака num_feature в разрезе cat_feature.

    Строит диаграммы размаха признака num_feature в разрезе cat_feature и
    формирует заголовок вида "Диаграммы размаха признака {num_feature} в разрезе
    признака {cat_feature} . В функцию можно передать параметры графика,
    корректные для метода pd.DataFrame.boxplot() с помощью именованных
    аргументов **kwargs.

    Parameters
    ----------
    data : pd.DataFrame
        Датафрейм, содержащий исследуемый признак.
    cat_feature : str
        Имя категориального признака в разрезе которого будут построены
        диаграммы размаха количественного признака.
    num_feature : str
        Имя количественного признака, для которого будут построены диаграммы
        размаха.
    **kwargs : Any, optional
        Параметры графика, корректные для метода pd.DataFrame.boxplot().
    """
    data.boxplot(
        column=num_feature,
        by=cat_feature,
        **kwargs,
    )

    plt.title(
        f"Диаграммы размаха признака {num_feature} в разрезе "
        f"признака {cat_feature}"
    )

    plt.suptitle("")

    return None
