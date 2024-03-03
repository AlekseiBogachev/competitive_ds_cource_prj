# -*- coding: utf-8 -*-
"""Подготовка новых признаков и удаление неинформативных."""

import logging
from pathlib import Path

import click
import pandas as pd

from comp_ds_prj import setup_logging_to_file

logger: logging.Logger = setup_logging_to_file()
project_dir: Path = Path(__file__).resolve().parents[2]


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

    Готовит признаки.\f

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

    logger.info(f'Запись датафрейма с результатом в файл {output_filepath}')
    df.to_csv(output_filepath, index=False)

    return None


if __name__ == '__main__':
    build_features()
