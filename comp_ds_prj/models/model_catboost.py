# -*- coding: utf-8 -*-
"""Работа с Catboost."""

import logging
from pathlib import Path
from typing import List

import click
import numpy as np
import pandas as pd
from catboost import CatBoostClassifier
from joblib import dump
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from comp_ds_prj import setup_logging_to_file

logger: logging.Logger = setup_logging_to_file()
project_dir: Path = Path(__file__).resolve().parents[2]


@click.group()
def cli() -> None:
    """Создаёт группу комманд интерфейса коммандной строки."""
    pass


@click.command()
@click.option(
    "-i",
    "-input",
    "input_filepath",
    default=Path.joinpath(project_dir, "data", "processed", "train.csv"),
    type=click.Path(exists=True),
    help="Имя файла с подготовленным датасетом. Значение по умолчанию"
    "<project_dir>/data/processed/train.csv",
)
@click.option(
    "-o",
    "--output",
    "output_filepath",
    default=Path.joinpath(project_dir, "models", "catboost.joblib"),
    type=click.Path(),
    help="Имя файла в который будет сохранена модель. Значение по умолчанию"
    "<project_dir>/models/catboost.joblib",
)
def train(input_filepath: str, output_filepath: str) -> None:
    """Обучает и сохраняет модель в файл.

    Обучает модель на тренировочном датасете (по умолчанию
    <project_dir>/data/processed/train.csv) и сохраняет её в файл (по умолчанию
    <project_dir>/data/processed/catboost.joblib).\f

    Parameters
    ----------
    input_filepath : str
        Имя файла с подготовленным датасетом. Значение по умолчанию
        <project_dir>/data/processed/train.csv
    output_filepath : str
        Имя файла в который будет сохранена модель. Значение по умолчанию
        <project_dir>/data/processed/catboost.joblib
    """
    logger.info("Обучение Catboost")

    logger.info(f"Чтение датафрейма с обучающими данными {input_filepath}")
    train: pd.DataFrame = pd.read_csv(input_filepath)

    targets: List[str] = ["target_class", "target_reg"]
    X = train.drop(columns=targets, errors="ignore")
    y = train["target_class"]

    target: str = str(y.name)
    cat_features: List[str] = ["car_type", "fuel_type", "model"]
    num_features: List[str] = [
        item for item in train.columns.to_list() if item not in cat_features
    ]

    logger.info(f"Целевой признак: {target}")
    logger.info(f"Категориальные признаки: {cat_features}")
    logger.info(f"Количественные признаки: {num_features}")

    data: List[np.ndarray] = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    X_train, X_test, y_train, y_test = data

    logger.info(
        f"Количество наблюдений в обучающем множестве {len(X_train)}. "
        f"Количество наблюдений в валидациооном множества {len(X_test)}."
    )

    logger.info('Инициализация классификатора')

    clf = CatBoostClassifier(cat_features=cat_features)

    logger.info("Обучение модели")

    clf.fit(
        X_train,
        y_train,
        eval_set=(X_test, y_test),
        verbose=150,
        plot=False,
    )

    accuracy: float = accuracy_score(clf.predict(X_test), y_test)
    logger.info(f"Модель обучена. Accuracy: {accuracy}")

    logger.info(f"Сохранение модели в файл {output_filepath}")
    dump(clf, output_filepath)

    return None


@click.command()
@click.option(
    "-i",
    "--input",
    "input_filepath",
    default=Path.joinpath(
        project_dir, "data", "processed", "submission_features.csv"
    ),
    type=click.Path(exists=True),
    help="Имя файла с подготовленными признаками по которым надо подготовить "
    "прогноз. Значение по умолчанию <project_dir>/data/processed"
    "/submission_features.csv",
)
@click.option(
    "-m",
    "--model",
    "model_filepath",
    default=Path.joinpath(
        project_dir, "model", "catboost.joblib",
    ),
    type=click.Path(exists=True),
    help="Имя файла с сохраненной моделью. Значение по умолчанию"
    "<project_dir>/models/catboost.joblib",
)
@click.option(
    "-o",
    "--output",
    "output_filepath",
    default=Path.joinpath(
        project_dir, "data", "submissions", "submission.scv",
    ),
    help="Имя файла с подготовленным прогнозом. Значение по умолчанию"
         "<project_dir>/data/submissions/submission.scv",
)
def predict(
    input_filepath: str,
    model_filepath: str,
    output_filepath: str,
) -> None:
    """Готовит прогноз для загрузки на Kaggle.

    Готовит прогноз для загрузки на Kaggle. Функция принимает путь к
    подготовленному датасетом для подготовки прогноза для Kaggle (submission),
    который должен уже быть очищен и содержать все необходимые признаки (функция
    только готовит прогноз, остальные шаги уже должны быть выполнены), путь
    к файлу, в который сохранена модель, и путь к файлу в который будет сохранён
    результат. Результат представляет из себя датафрейм, сохранённый в формате
    .csv и состоящий из двух столбцов car_id и target_class\f

    Parameters
    ----------
    input_filepath : str
        Имя файла с подготовленными признаками по которым надо подготовить
        прогноз. Значение по умолчанию <project_dir>/data/processed
        /submission_features.csv
    model_filepath : str
        Имя файла с сохраненной моделью. Значение по умолчанию
        <project_dir>/models/catboost.joblib
    output_filepath : str
        Имя файла с подготовленным прогнозом. Значение по умолчанию
        <project_dir>/data/submissions/submission.scv
    """
    logger.info(
        "Подготовка прогноза для Kaggle. "
        f"Модель: {model_filepath}. Признаки {input_filepath}."
    )

    logger.info(f"Сохранение результата в {output_filepath}.")
    (
        pd
        .DataFrame(columns=["car_id", "target_class"])
        .to_csv(output_filepath, index=False)
    )

    return None


cli.add_command(train)
cli.add_command(predict)

if __name__ == "__main__":
    cli()
