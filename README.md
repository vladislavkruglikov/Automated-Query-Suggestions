# Automated Query Suggestions
Automated Query Suggestions with top k topic related suggestions depending on search query and 
text correction algorithm was developed to face misspelling in search query

## How to start
```python
python main.py
```

```
>>> Купет

Поиск: Купет
Возможно вы имелли ввиду: купер 

Результаты:
купер фильмы смотреть онлайн бесплатно
купер фильмы онлайн 2016 смотреть
купер фильмы 2016 смотреть бесплатно
купер фильмы онлайн бесплатно

```

```
>>> Игры
Поиск: Игры
Результаты:
игры
игры для
игры онлайн
игры для девочек
игры для детей
```

```
>>> филмы
Поиск: филмы
Возможно вы имелли ввиду: фильмы 

Результаты:
фильмы
фильмы 2016
фильмы онлайн
фильмы смотреть
фильмы 2016 смотреть
```