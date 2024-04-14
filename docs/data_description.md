# Описание данных

## Основная информация

Данные состоят из нескольких файлов. Описание машин и информация о поломках собраны в следующих таблицах:

- [`car_train.csv`](https://raw.githubusercontent.com/a-milenkin/Competitive_Data_Science/main/data/car_train.csv) - данные для обучения моделей;
- [`car_test.csv`](https://raw.githubusercontent.com/a-milenkin/Competitive_Data_Science/main/data/car_test.csv) - данные для подготовки прогноза для соревнования;

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

## Дополнительная информация

Дополнительные данные содержатся в следующих файлах:

- [`rides_info.csv`](https://raw.githubusercontent.com/a-milenkin/Competitive_Data_Science/main/data/rides_info.csv) - информация о поездках;
- [`driver_info.csv`](https://raw.githubusercontent.com/a-milenkin/Competitive_Data_Science/main/data/driver_info.csv) - информация о водителях;
- [`fix_info.csv`](https://raw.githubusercontent.com/a-milenkin/Competitive_Data_Science/main/data/fix_info.csv) - информация о ремонтах машин.

Описание столбцов `rides_info.csv`:

- `user_id` - идентификатор водителя;
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
- `work_duration` - длительность проводимой работы в часах;
- `destroy_degree` - степень износа/повреждения машины в случае поломки;
- `fix_date` - время начала ремонта (снятия машины с линии).
  
## Схема данных

![ER-диаграмма](/docs/figures/er_diag.svg)
