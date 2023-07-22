import numpy as np
import PIL
import pandas as pd


def processing(image):
    # изменение размера изображения и перевод в список
    resized = image.resize((140, 140))
    resized_tmp = list(resized.getdata())
    resized_tmp = [i[0] for i in resized_tmp]
    # print(resized_tmp)

    # перевод в pd.DF
    resized_tmp = np.asarray(resized_tmp)
    resized_tmp = resized_tmp.reshape(140, -1)
    resized_tmp = pd.DataFrame(data=resized_tmp)

    # удаление нулевых строк (горизонтальных линий, где нет белых пикселей)
    resized_tmp = resized_tmp.loc[~(resized_tmp == 0).all(axis=1)]

    # удаление нулевых столбцов
    nan_value = float("NaN")
    resized_tmp.replace(0, nan_value, inplace=True)
    resized_tmp.dropna(how='all', axis=1, inplace=True)
    resized_tmp = resized_tmp.fillna(0)

    # перевод в np.array и картинку для изменения размера
    resized_tmp = np.asarray(resized_tmp)
    img = PIL.Image.fromarray(resized_tmp)
    img = img.resize((20, 20))

    # округление и удаление отрицательных данных
    resized_tmp = np.round(list(img.getdata())).astype(int)
    resized_tmp = np.asarray(resized_tmp)
    resized_tmp = resized_tmp.reshape(20, -1)
    resized_tmp = pd.DataFrame(data=resized_tmp)
    resized_tmp[resized_tmp < 0] = 0

    # добавление нулей (черных полей) по краям массива (изображения)
    colsPadding = (4, 4)
    rowsPadding = (4, 4)
    resized_tmp = np.pad(resized_tmp, (rowsPadding, colsPadding), 'constant')

    resized_tmp = resized_tmp.reshape(1, -1)

    # результат - одномерный np.array на 784 (28х28) элемента
    return resized_tmp
