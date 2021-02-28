# Компьютерная графика. Лабораторная работа №2
Солодуха Дмитрий, 13 группа
## Задание
Написать приложение/веб-приложение, считывающее из графического файла/файлов основную информацию об изображении:
- имя файла;
- размер изображения;
- разрешение;
- глубина цвета;
- сжатие.

## Реализация
Реализация представлена в виде скрипта на языке `Python` с использованием библиотеки [`PIL`](https://pillow.readthedocs.io/en/stable/). Основная работа в скрипте выполняется с помощью библиотеки `PIL`, которая в свою очередь считывает нужные нам метаданные из специальных частей в файле изображений: `Exif`, `XMP`, `IPTC`. 

Пример работы можно видеть ниже:
![Example](screenshots/example-1.png)

Пользователь имеет возможность передать папку используя аргумент `--directory [DIR]`

## Скачать и запустить
Если установлен интерпретатор `Python`, то можно просто скормить скрипт ему:
```cmd
git clone https://github.com/sMeDDveD/ComputerGraphicsLab2.git
cd ComputerGraphcisLab2
python -m venv env && venv\bin\Scripts\activate
python extractor.py --directory directory
```

Если интерпретатор нет, то нужно скачать статически скомпилрованный `.exe`-файл [отсюда](). 
