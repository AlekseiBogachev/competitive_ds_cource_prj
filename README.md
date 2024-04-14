# competitive_ds_cource_prj

Проект для курса
[MLOps и production в DS исследованиях 3.0](https://ods.ai/tracks/mlops3-course-spring-2024)
и курса [Введение в соревновательный Data Science](https://stepik.org/course/108888/info)
на [Stepic](https://stepik.org/).

> [!IMPORTANT]
> **Разработка проекта ведётся по методологии GitHub-flow. Подробенне в
> [CONTRIBUTING.md](/CONTRIBUTING.md).**

> [!WARNING]
> **Проект и документация в стадии разработки.**

## Краткое описание проекта

Для оптимизации расходов на ремонт и техническое обслуживание автомобилей
каршеринговой компании необходима модель, которая будет прогнозировать, время
через которое произойдёт поломка и класс поломки.

**Цель** - построить модель (или модели), прогнозирующую время, через которое
произойдёт поломка, и класс поломки.

**Целевые метрики**:

1. **ROC AUC** - для прогнозирования класса поломки (классификация)
2. **RMSLE** - для прогнозирования времени до поломки (регрессия)
$$RMSLE = \sqrt{ \frac{1}{n} \sum_{i=1}^n \left(\log (1 + \hat{y}_i) - \log (1 + y_i)\right)^2},$$  
где  
$n$ - количество наблюдений,  
$\hat{y}_i$ значение, спрогнозированное моделью для наблюдения $i$,  
$y_i$ - фактическое значение для наблюдения $i$,  
$\log$ - натуральный логарифм.

## Документация

Документация и отчёты разделены на несколько разделов, размещённых в отдельных файлах:

- Отчёты содержат подробное описание исследования и моделей и собраны в каталоге
  [reports](/reports/)
- Документация, содержащая описание данных и техническую информацию, собрана в
каталоге [docs](/docs/):
  - [Описание исходных данных](/docs/data_description.md)
  - [Среда разработки](/docs/development_environment.md) - Сборка и запуск
  среды разработки.
  - [CI/CD конвейер GihHub Actions](/docs/ci_cd_gh_actions.md) - Сборка,
  запуск и регистрация
  [self-hosted runner для GitHub Actions](https://docs.github.com/en/actions/hosting-your-own-runners).

## Структура репозитория

    ├── comp_ds_prj                   <- Каталог с python-модулями проекта.
    │   ├── data                      <- Скрипты для загрузки и обработки данных.
    │   ├── features                  <- Скрипты, создающие из сырых данных признаки, пригодные для передачи модели.
    │   ├── logs                      <- Каталог с модулями для организации и настройки логирования.
    │   ├── models                    <- Модули, реализующие работу с разными моделями. Для каждой модели свой модуль.
    │   └── visualization             <- Скрипты для генерации графиков.
    |
    ├── data
    │   ├── external                  <- Данные, полученные из внешних источников, например открытых API в интернете.
    │   ├── interim                   <- Промежуточные данные, полученные после предобработки сырых данных и данных из
    |   |                                внешних источников, а также данные, полученные после промежуточных шагов
    |   |                                обработки.
    │   ├── processed                 <- Подготовленные данные, пригодные для отправки модели.
    │   ├── raw                       <- Сырые исходные данные, полученные из первоисточника.
    │   └── submissions               <- Прогнозы (сабмиты) для отправки на Kaggle.
    |
    ├── docs                          <- Документация проекта.
    │   └── figures                   <- Иллюстрации для документации.
    |
    ├── .dvc                          <- Временные файлы и настройки DVC, в том числе и данные для доступа ко внешнему 
    |   |                                хранилищу.
    │   ├── config                    <- Глобальные настройки.
    │   └── config.local              <- Локальные настройки.
    ├── .gdrive
    │   └── credentials.json          <- Токен для подключения DVC к внешнему хранилищу данных на Google Drive.
    |
    ├── gh_actions_runner             <- Каталог со скриптами и файлами для работы с self-hosted runner
    |   |                                (GitHub Actions).
    │   ├── build_runner.sh           <- Скрипт, собирающий образ контейнера с ранером из Dockerfile в этом же каталоге.
    │   ├── Dockerfile                <- Dockerfile для сборки контейнера с ранером.
    │   ├── remove_runner.sh          <- Скрипт анулирует регистрацию ранера в GitHub Actions, что вызывает остановку
    |   |                                работающего ранера.
    │   ├── .secret_token             <- Временный токен для регистрации ранера в GitHub Actions. 
    │   └── start_runner.sh           <- Скрипт, запускающий контейнер с ранером. После запуска контейнера Скрипт
    |                                    также регистрирует и запускает ранер.
    ├── .github
    │   └── workflows                 <- Каталог с описанием CI/CD конвейеров GitHub Actions в формате yaml.
    |
    ├── logs                          <- Каталог для логов.
    |
    ├── models                        <- Каталог с сохранёнными обученными моделями.
    |
    ├── notebooks                     <- Каталог с тетрадками Jupyter
    │   ├── exploratory               <- Notebook-и с первичными исследованиями и экспериментами. 
    |   |                                В них допустимо большое количество кода.
    │   └── reports                   <- Более тщательно оформленные тетрадки, служащие основой для отчётов.
    |
    ├── references                    <- Дополнительные сторонние материалы и руководства.
    │   └── baseline_by_authors.ipynb <- Baseline-решение от авторов
    |                                    [курса](https://stepik.org/course/108888/info).
    |
    ├── reports                       <- Каталог с отчётами. Отчёты содержат информацию об основных этапах
    |                                    исследования, разработке модели и полученных результатах. Для остальных
    |                                    разделов, например описания окружения разработки и процесса его
    |                                    развёртывания есть документация (каталог docs).
    |
    ├── build.sh                      <- Скрипт, собирающий образ контейнера с окружением разработки из Dockerfile.
    ├── Dockerfile                    <- Dockerfile базового контейнера.
    ├── Dockerfile_dev_env            <- Dockerfile контейнера со средой разработки.
    ├── .dockerignore                 <- Аналог .gitignore для Docker. Docker не будет копировать и обрабатывать всё,
    |                                    что перечислено в этом файле.
    ├── .dvcignore                    <- Аналог .gitignore для DVC. DVC не будет обрабатывать всё, что перечислено в
    |                                    этом файле.
    ├── dvc.lock                      <- Файл с метаданными о каждом шаге workflow, описанного в dvc.yaml и выполняемого
    |                                    DVC. Файл позволяет DVC определить какие шаги нужно выполнить.
    ├── dvc.yaml                      <- Описание workflow DVC в формате yaml.
    ├── .env                          <- Файл с переменными окружения, которые могут быть импортированы в среду
    |                                    разработки.
    ├── .flake8                       <- Файл с параметрами Flake8. Flake8 не поддерживает pyproject.toml, поэтому его
    |                                    параметры вынесены в отдельный файл.
    ├── .gitignore
    ├── jupyter.sh                    <- Скрипт для запуска контейнера среды разработки с запущенным сервером
    |                                    Jupyter Notebook.
    ├── LICENSE                       <- лицензия MIT.
    ├── poetry.lock                   <- Файл с зафиксированными зависимостями Poetry.
    ├── pyproject.toml                <- Файл с описанием пакетов, устанавливаемых в виртуальное окружение, и
    |                                    параметрами линтеров и автоформатеров.
    ├── requirements.txt              <- Файл с зафиксированными зависимостями Poetry, экспортированный в формате для
    |                                    других менеджеров пакетов.
    ├── README.md                     <- README.md верхнего уровня, отображающийся на заглавной странице репозитория.
    ├── CONTRIBUTING.md               <- Описание для новых участников проекта.
    └── start.sh                      <- Скрипт для запуска контейнера среды разработки. Предоставляет доступ к
                                         /bin/bash в контейнере.
