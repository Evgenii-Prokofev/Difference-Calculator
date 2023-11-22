### Hexlet tests and linter status:
[![Actions Status](https://github.com/Evgenii-Prokofev/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Evgenii-Prokofev/python-project-50/actions)
[![Actions Status](https://github.com/Evgenii-Prokofev/python-project-50/actions/workflows/python_test_and_linter.yml/badge.svg)](https://github.com/Evgenii-Prokofev/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/13a63bb08bb4b3b44ee3/maintainability)](https://codeclimate.com/github/Evgenii-Prokofev/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/13a63bb08bb4b3b44ee3/test_coverage)](https://codeclimate.com/github/Evgenii-Prokofev/python-project-50/test_coverage)

Вычислитель отличий – программа, определяющая разницу между двумя структурами данных. Это популярная задача, для решения которой существует множество онлайн-сервисов типа  http://www.jsondiff.com/. Подобный механизм, например, используется при выводе тестов или при автоматическом отслеживании изменений в конфигурационных файлах.

Установка:

Для установки и запуска проекта вам потребуется Python версии 3.10 и выше 
и инструмент для управления зависимостями Poetry.

Для установки выполните следующие шаги:

1. Склонируйте репозиторий с проектом на ваше локальное устройство:
git clone git@github.com:Evgenii-Prokofev/python-project-50.git
2. Перейдите в директорию проекта:
cd python-project-50
3. Установите необходимые зависимости с помощью Poetry:
poetry install

Поддерживаемые форматы файлов

Проект поддерживает следующие форматы файлов для поиска отличий:

• YAML (.yaml, .yml)
• JSON (.json)

Как найти различия между двумя файлами:

• gendiff path/to/file_1 path/to/file_2 - команда для поиска различий в формате stylish (по умолчанию)
 
• gendiff --format plain path/to/file_1 path/to/file_2 - команда для поиска различий в формате plain

• gendiff --format json path/to/file_1 path/to/file_2 - команда для поиска различий в формате json


Пример работы программы при сравнении различий в двух файлах json-формата:
https://asciinema.org/a/ctOGZFxCWC7WqAqZr4w5N9ZaN

Пример работы программы при сравнении различий в двух файлах yaml-формата:
https://asciinema.org/a/tC5rJaLiBetPCXMutdJO1FdMU

Пример работы программы при сравнении различий в двух файлах с вложенной структурой:
https://asciinema.org/a/mOaBOK7neCFkk2tBIqdN2yEdL

Пример работы программы при сравнении различий в двух файлах и вывод результата в плоском формате:
https://asciinema.org/a/OUDFKNBZvI2kE3Gq4sqsXU5Tr

Пример работы программы при сравнении различий в двух файлах и вывод результата в формате json:
https://asciinema.org/a/MAlxjluK95AeSCVs3xELvgiM9

