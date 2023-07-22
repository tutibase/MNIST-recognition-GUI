# MNIST_recognition_GUI
Программа с графическим интерфейсом для распознавания рукописных цифр. Для использования достаточно распаковать архив ```model.zip``` в общую папку и запустить ```GUI.py```


### GUI.py
Реализация графического интерфейса для работы с обученной моделью через [tkinter](https://docs.python.org/3/library/tkinter.html):
- Кнопки ```B+``` и ```B-``` изменяют размер кисти для рисования 
- Кнопка ```Clear``` очищает поле для рисования
- Кнопка ```Predict``` выводит результат работы модели в правый нижний угол
- Если нарисовать что-либо в окне, то спустя 2 секунды бездействия предсказание числа произойдет автоматически.

| <img src="https://github.com/tutibase/MNIST_recognition_GUI/assets/44751053/d5addf9e-032c-4de9-9a81-479be328862f" width="30%" height="30%" /> <img src="https://github.com/tutibase/MNIST_recognition_GUI/assets/44751053/855ee0fa-2218-4a40-8b3c-ba52214563c1" width="30%" height="30%" /> <img src="https://github.com/tutibase/MNIST_recognition_GUI/assets/44751053/b670ef72-1d12-4b75-9167-0ce2478c4f22" width="30%" height="30%" /> | 
|:--:| 
| *Интерфейс приложения* |


### img_processing.py
Функция обработки изображения из окна для рисования. Для работы с изображением используются [Pillow](https://pillow.readthedocs.io/en/stable/), [pandas](https://pandas.pydata.org/) и [NumPy](https://numpy.org/). Функция сжимает изображение, удаляет лишние данные, приводит полученное изображение к размеру 20x20, после чего добавляет рамку шириной 4 пикселя по краям. В итоге получается изображение 28x28, которое успешно обрабатывает модель.

| ![bfr_aft](https://github.com/tutibase/MNIST_recognition_GUI/assets/44751053/da271178-92ba-4313-9eea-7d27f2032dae) | 
|:--:| 
| *Изображение до и после обработки* |


### mnist.py
Обучение модели распознавания цифр через [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html) на данных из ```data.zip``` и последующая её консервация в ```model.pkl```. Приведенная модель показывает следующие результаты на тестовых данных: 

| ![model_classification_report](https://github.com/tutibase/MNIST_recognition_GUI/assets/44751053/8f505b6c-0377-4c45-9ef3-01eebac299c0) | 
|:--:| 
| *model classification report* |


### data.zip
В архиве данные [MNIST в формате csv](https://www.kaggle.com/datasets/oddrationale/mnist-in-csv) для самостоятельного обучения модели. [Описание данных на вики](https://ru.wikipedia.org/wiki/MNIST_(база_данных)).

| ![image](https://github.com/tutibase/MNIST_recognition_GUI/assets/44751053/4af2ddef-bb0a-4bcd-a4db-dfff89c159ee) | 
|:--:| 
| *Пример данных* |
