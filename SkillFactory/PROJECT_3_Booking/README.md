# Exploratory Data Analysis and Feature Engineering #

## (Соревнование на Kaggle) ##

[Ссылка на соревнование](https://www.kaggle.com/competitions/sf-booking)

[Профиль на Kaggle&nbsp;&mdash; **Dredox**](https://www.kaggle.com/dredox)

### Содержание ###

[1. Смоделированная ситуация](#смоделированная-ситуация)    
[2. Описание датасета](#описание-датасета)    
[3. Требования к оформлению](#требования-к-оформлению)    
[4. Критерии оценивания](#критерии-оценивания)    
[5. Результат](#результат)    

### Смоделированная ситуация ###

Одна из проблем компании Booking&nbsp;&mdash; это нечестные отели, которые
накручивают себе рейтинг. Одним из способов обнаружения таких отелей является
построение модели, которая предсказывает рейтинг отеля. Если предсказания модели
сильно отличаются от фактического результата, то, возможно, отель ведёт себя
нечестно, и его стоит проверить. Поставлена задача создать такую модель.

Предстоит работать с датасетом, в котором содержатся сведения о 515000 отзывах
на отели Европы. Модель, которую надо обучить, должна предсказывать рейтинг
отеля по данным сайта Booking на основе имеющихся в датасете данных.

[:arrow_up: Содержание](#содержание)

----

### Описание датасета ###

**Скачиваемые файлы:**

- [**`hotels_train.csv`**](https://drive.google.com/file/d/1jFkdObrBr9UrGVRHijfHWRUNt4B1XytY/view?usp=sharing)&nbsp;&mdash;
набор данных для обучения;
- [**`hotels_test.csv`**](https://drive.google.com/file/d/1jFkdObrBr9UrGVRHijfHWRUNt4B1XytY/view?usp=sharing)&nbsp;&mdash;
набор данных для оценки качества;
- [**`submission.csv`**](https://drive.google.com/file/d/1jFkdObrBr9UrGVRHijfHWRUNt4B1XytY/view?usp=sharing)&nbsp;&mdash;
результирующий файл для Submission.

**Датасет содержит 17 полей со следующей информацией:**

1. **`hotel_address`**&nbsp;&mdash; адрес отеля;
2. **`review_date`**&nbsp;&mdash; дата, когда рецензент разместил соответствующий
отзыв;
3. **`average_score`**&nbsp;&mdash; средний балл отеля, рассчитанный на основе
последнего комментария за последний год;
4. **`hotel_name`**&nbsp;&mdash; название отеля;
5. **`reviewer_nationality`**&nbsp;&mdash; страна рецензента;
6. **`negative_review`**&nbsp;&mdash; отрицательный отзыв, который рецензент дал
отелю;
7. **`review_total_negative_word_counts`**&nbsp;&mdash; общее количество слов в
отрицательном отзыве;
8. **`positive_review`**&nbsp;&mdash; положительный отзыв, который рецензент дал
отелю;
9. **`review_total_positive_word_counts`**&nbsp;&mdash; общее количество слов в
положительном отзыве.
10. **`reviewer_score`**&nbsp;&mdash; оценка, которую рецензент поставил отелю на
основе своего опыта;
11. **`total_number_of_reviews_reviewer_has_given`**&nbsp;&mdash; количество
отзывов, которые рецензенты дали в прошлом;
12. **`total_number_of_reviews`**&nbsp;&mdash; общее количество действительных
отзывов об отеле;
13. **`tags`**&nbsp;&mdash; теги, которые рецензент дал отелю;
14. **`days_since_review`**&nbsp;&mdash; количество дней между датой проверки и
датой очистки;
15. **`additional_number_of_scoring`**&nbsp;&mdash; есть также некоторые гости,
которые просто поставили оценку сервису, но не оставили отзыв. Это число
указывает, сколько там действительных оценок без проверки;
16. **`lat`**&nbsp;&mdash; географическая широта отеля;
17. **`lng`**&nbsp;&mdash; географическая долгота отеля.

[:arrow_up: Содержание](#содержание)

----

### Требования к оформлению ###

- Результаты соревнования оцениваются по метрике MAPE.
- Результирующий файл `submission.csv`, где для каждого **id** отеля в наборе
тестовых данных нужно предсказать рейтинг отеля в переменной **reviewer_score**.
Файл должен содержать заголовок и иметь следующий формат:

```text
reviewer_score,id
1,1
```

[:arrow_up: Содержание](#содержание)

----

### Критерии оценивания ###

1. Качество кода (соблюдение стандартов оформления PEP-8, комментирование кода,
README к проекту). Оформление проекта на GitHub, Kaggle;
2. Очистка данных;
3. Исследование данных (качество визуализации, наличие идей, гипотез,
комментариев);
4. Генерация признаков;
5. Отбор признаков;
6. Преобразование признаков;
7. Качество решения: результат метрики MAPE.

[:arrow_up: Содержание](#содержание)

----

### Результат ###

[**`project-3-eda-feature-engineering-booking-reviews`**](https://www.kaggle.com/code/dredox/project-3-eda-feature-engineering-booking-reviews)&nbsp;&mdash;
Notebook на Kaggle.com.

[**`project-3-eda-feature-engineering-booking-reviews`**](project-3-eda-feature-engineering-booking-reviews.ipynb)&nbsp;&mdash; Вариант решения на Github.

[**`output/submission.csv`**](output/submission.csv, https://drive.google.com/file/d/16NZEBMb4LJ7_Odypyfimu3eJsBunI934/view?usp=sharing)&nbsp;&mdash; Файл
предсказаний.

[:arrow_up: Содержание](#содержание)

----
