# competitive_ds_cource_prj

Проект для курса [Введение в соревновательный Data Science](https://stepik.org/course/108888/info) на [Stepic](https://stepik.org/).

## Краткое описание

Для оптимизации расходов на ремонт и техническое обслуживание обслуживание автомобилей каршеринговой компании необходима модель, которая будет прогнозировать, время через которое произойдёт поломка и класс поломки.

**Цель** - построить модель, прогнозирующую время, через которое произойдёт поломка, и класс поломки.

**Целевые метрики**:
1. **ROC AUC** - для прогнозирования класса поломки (классификация)
2. **RMSLE** - для прогнозирования времени до поломки (регрессия)
$$RMSLE = \sqrt{ \frac{1}{n} \sum_{i=1}^n \left(\log (1 + \hat{y}_i) - \log (1 + y_i)\right)^2},$$  
где  
$n$ - количество наблюдений,  
$\hat{y}_i$ значение, спрогнозированное моделью для наблюдения $i$,  
$y_i$ - фактическое значение для наблюдения $i$,  
$\log$ - натуральный логарифм.

## Описание данных

### Основная информация

Данные состоят из несколько их файлов. Описание машин и информация о поломках собраны в следующих:
- [`car_train.csv`](https://raw.githubusercontent.com/a-milenkin/Competitive_Data_Science/main/data/car_train.csv) - данные для обучения моделей;
- [`car_test.csv`](https://raw.githubusercontent.com/a-milenkin/Competitive_Data_Science/main/data/car_test.csv) - данные для тестирования моделей;

Опписание столбцов из `car_train.csv`, `car_test.csv`:
- `car_id` - идентификатор машины;
- `model` - марка;
- `car_type` - класс;
- `fuel_type` - тип топлива машины;
- `car_rating` - общий рейтинг;
- `riders` - общее число поездок к концу 2021-го года;
- `year_to_start` - год выпуска машины;
- `year_to_work` - год начала работы в автопарке;
- `target_reg` - количество дней до поломки;
- `target_class` - класс поломки (9 классов).

### Дополнительная информация

Дополнительные данныесодержатся в следующих файлах:
- [`rides_info.csv`](https://raw.githubusercontent.com/a-milenkin/Competitive_Data_Science/main/data/rides_info.csv) - информация про поездки;
- [`driver_info.csv`](https://raw.githubusercontent.com/a-milenkin/Competitive_Data_Science/main/data/driver_info.csv) - информация про водителей;
- [`fix_info.csv`](https://raw.githubusercontent.com/a-milenkin/Competitive_Data_Science/main/data/fix_info.csv) - информация о ремонтах машин.

Описание столбцов `rides_info.csv`:
- `user_id` - идентификаторы водителя;
- `car_id` - id машины;
- `ride_id` - id поездки;
- `ride_date` - дата поездки;
- `rating` - рейтинг, поставленный водителем;
- `ride_duration` - длительность (время) поездки; 
- `distance` - пройденное расстояние;
- `ride_cost` - стоимость поездки;
- `speed_avg` - средняя скорость поездки;
- `speed_max` - максимальная скорости поездки;
- `stop_times` - количество остановок (паузы);
- `refueling` - флаг, была ли дозаправка;
- `user_ride_quality` - оценка манеры вождения в машины водителя, определенная скоринговой ML-системой сервиса;
- `deviation_normal` - общий показатель датчиков о состоянии машины, относительно эталонных показателей (нормы). 

Описание столбцов `driver_info.csv`:
- `user_id` - идентификатор водителя;
- `age` - возраст водителя;
- `sex` - пол водителя;
- `user_rating` - общий рейтинг пользователя за все поездки к концу 2021-го года;
- `user_rides` - общее количество поездок к концу 2021-го года;
- `user_time_accident` - число инцидентов (аварий/штрафов/эвакуаций машины);  
- `first_ride_date` - дата первой поездки.

Описание столбцов `fix_info.csv`:
- `worker_id` - идентификатор работника;
- `car_id` - идентификатор машины;
- `work_type` - тип проводимой работы;
- `work_duration` - тип и длительность (в часах) проводимой работы;
- `destroy_degree` - степень износа/повреждённости машины в случае поломки;
- `fix_date` - время начала ремонта (снятия машины с линии).
  
### Схема данных

![ER-диаграмма]('./reports/figures/er_diag.svg')

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │   |                     the creator's initials, and a short `-` delimited description, e.g.
    │   |                     `1.0-jqp-initial-data-exploration`.
    │   ├── exploratory    <- Notebooks with initial explorations.
    |   └── reports        <- More polished notebooks that can be exported as html to the reports
    |                         directory.
    |
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
