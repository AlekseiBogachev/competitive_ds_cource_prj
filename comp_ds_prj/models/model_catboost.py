# -*- coding: utf-8 -*-
"""Работа с Catboost."""

import logging
from pathlib import Path

import click

from comp_ds_prj import setup_logging_to_file

logger: logging.Logger = setup_logging_to_file()
project_dir: Path = Path(__file__).resolve().parents[2]


@click.command()
@click.option(
    '-i', '-input', 'input_filepath',
    default=Path.joinpath(project_dir, 'data', 'processed', 'train.csv'),
    type=click.Path(exists=True),
    help='Имя файла с подготовленным датасетом. Значение по умолчанию'
         '<project_dir>/data/processed/train.csv',
)
@click.option(
    '-o', '--output', 'output_filepath',
    default=Path.joinpath(project_dir, 'models', 'catboost.joblib'),
    type=click.Path(),
    help='Имя файла в который будет сохранена модель. Значение по умолчанию'
         '<project_dir>/data/processed/catboost.joblib',
)
def train(input_filepath: str, output_filepath: str) -> None:
    """Обучает и сохраняет модель в файл.

    Parameters
    ----------
    input_filepath : str
        Имя файла с подготовленным датасетом. Значение по умолчанию
        <project_dir>/data/processed/train.csv
    output_filepath : str
        Имя файла в который будет сохранена модель. Значение по умолчанию
        <project_dir>/data/processed/catboost.joblib
    """
    pass

    return None


if __name__ == '__main__':
    train()
