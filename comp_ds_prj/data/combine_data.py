# -*- coding: utf-8 -*-
"""Подготовка сырого датасета к генерации новых признаков."""

import logging
from pathlib import Path

import click
import pandas as pd

from comp_ds_prj import setup_logging_to_file

logger: logging.Logger = setup_logging_to_file()
project_dir: Path = Path(__file__).resolve().parents[2]


@click.command()
@click.argument(
    'car_train_filepath',
    type=click.Path(exists=True),
)
@click.argument(
    'rides_info_filepath',
    type=click.Path(exists=True)
)
@click.option(
    '-o', '--output', 'output_filepath',
    default=Path.joinpath(project_dir, 'data', 'interim', 'raw_dataset.csv'),
    type=click.Path(),
    help='Имя файла, в который будет сохранён результирующий датасет.'
         'Значение по умолчанию <project_dir>/data/interim/raw_dataset.csv',
)
def combine_data(
    car_train_filepath: str,
    rides_info_filepath: str,
    output_filepath: str
) -> None:
    """Собирает все файлы с исходными данными в один.

    Собирает файлы с исодными данными в формате .csv в одни датафрейм тоже
    в формате .csv . Файлы с исходными данными, как правило, находятся в
    каталоге <project_dir>/data/raw, результирующий датасет по умолчанию
    сохраняется в файл <project_dir>/data/interim/raw_dataset.csv .

    CAR_TRAIN_FILEPATH - файл с описанием машин и информацией о поломках.
    Обычно файл имеет имя <project_dir>/data/raw/car_train.csv .

    RIDES_INFO_FILEPATH - файл информацией про поездки. Обычно файл имеет
    имя <project_dir>/data/raw/rides_info.csv\f

    Parameters
    ----------
    car_train_filepath : str
        Файл с описанием машин и информацией о поломках.
        Обычно файл имеет имя <project_dir>/data/raw/car_train.csv
    rides_info_filepath : str
        Файл информацией про поездки. Обычно файл имеет имя
        <project_dir>/data/raw/rides_info.csv
    output_filepath : str
        Имя файла, в который будет сохранён результирующий датасет.
        Значение по умолчанию <project_dir>/data/interim/raw_dataset.csv
    """
    logger.info('Объединение исходных в единый датафрейм')

    logger.info(
        'Читение датафрейма с описанием машин и информацией о поломках '
        f'{car_train_filepath}'
    )
    car_train: pd.DataFrame = pd.read_csv(car_train_filepath)

    logger.info(
        f'Читение датафрейма с информацией о поездках {car_train_filepath}'
    )
    rides_info: pd.DataFrame = pd.read_csv(rides_info_filepath)

    rides_df_gr: pd.DataFrame = (
        rides_info
        .groupby('car_id', as_index=False)
        .agg(
            mean_rating=('rating', 'mean'),
            istance_sum=('distance', 'sum'),
            rating_min=('rating', 'min'),
            speed_max=('speed_max', 'max'),
            user_ride_quality_median=('user_ride_quality', 'median'),
            deviation_normal_count=('deviation_normal', 'count'),
            user_uniq=('user_id', lambda x: x.nunique())
        )
    )

    logger.info('Объединение данных')
    dataset: pd.DataFrame = car_train.merge(
        rides_df_gr,
        on='car_id',
        how='left',
    )

    logger.info(f'Запись датасета в файл {output_filepath}')
    dataset.to_csv(output_filepath, index=False)

    return None


if __name__ == '__main__':
    combine_data()
