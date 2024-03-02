# -*- coding: utf-8 -*-
"""Подготовка новых признаков и удаление неинформативных."""

import logging
from pathlib import Path

import click
import pandas as pd

project_dir: Path = Path(__file__).resolve().parents[2]
logs_path: Path = Path.joinpath(project_dir, 'logs')
logs_path.mkdir(parents=True, exist_ok=True)

logger: logging.Logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

raw_data_handler: logging.FileHandler = logging.FileHandler(
    Path.joinpath(logs_path, f'{__name__}.log'), mode='a'
)
raw_data_fromatter: logging.Formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

raw_data_handler.setFormatter(raw_data_fromatter)
logger.addHandler(raw_data_handler)


@click.command()
@click.option(
    '-i', '--input', 'input_filepath',
    default=Path.joinpath(project_dir, 'data', 'interim', 'raw_dataset.csv'),
    type=click.Path(exists=True),
    help='Имя файла с данным для обработки. Значение по умолчанию'
         '<project_dir>/data/interim/raw_dataset.csv',
)
@click.option(
    '-o', '--output', 'output_filepath',
    default=Path.joinpath(project_dir, 'data', 'processed', 'train.csv'),
    type=click.Path(),
    help='Имя файла с результатом обработки. Значение по умолчанию'
         '<project_dir>/data/processed/train.csv',
)
def build_features(
    input_filepath: str,
    output_filepath: str,
) -> None:
    """Добавляет в датасет новые признаки и удаляет ненужные.

    Удаляет признак car_id.\f

    Parameters
    ----------
    input_filepath : str
        Имя файла с данным для обработки. Значение по умолчанию
        <project_dir>/data/interim/raw_dataset.csv
    outpur_filpath : str
        Имя файла с результатом обработки. Значение по умолчанию
        <project_dir>/data/processed/train.csv
    """
    logger.info('Подготовка признаков')

    logger.info(f'Чтение датафрейма для обработки {input_filepath}')
    df: pd.DataFrame = pd.read_csv(input_filepath)

    logger.info('Удаление признака car_id')
    df = df.drop(columns='car_id')

    logger.info(f'Запись датафрейма с результатом в файл {output_filepath}')
    df.to_csv(output_filepath, index=False)

    return None


if __name__ == '__main__':
    build_features()
