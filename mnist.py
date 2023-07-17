import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
import pickle

# выгрузка данных
df_train = pd.read_csv('mnist_train.csv')
df_test = pd.read_csv('mnist_test.csv')

# отделение целевой переменной
X_train = df_train.drop(['label'], axis=1).to_numpy()
X_test = df_test.drop(['label'], axis=1).to_numpy()

y_train = df_train.label.to_numpy()
y_test = df_test.label.to_numpy()

# выбор и обучение модели (параметры подобраны заранее)
knn_tuned = KNeighborsClassifier(n_neighbors=4, weights='distance', leaf_size=25, metric='cosine')
knn_tuned.fit(X_train, y_train)

y_pred = knn_tuned.predict(X_test)
print(classification_report(y_test, y_pred))

# сохранение обученной модели
with open('model.pkl', 'wb') as f:
    pickle.dump(knn_tuned, f)




# подбор данных для обучения

# from sklearn.model_selection import RandomizedSearchCV
#
# # выбор классификатора
# clf = KNeighborsClassifier()
#
# # параметры для настройки
# parametrs = {'n_neighbors': range(1,20),
#              'weights': ['uniform', 'distance'],
#              'leaf_size': range(20, 60)}
#
# # подбор наиболее подходящих параметров
# randomized_search_cv_clf = RandomizedSearchCV(clf, parametrs, cv=3, scoring="accuracy")
# randomized_search_cv_clf.fit(X_train, y_train)
#
# # отбор лучшей модели
# knn_tuned = randomized_search_cv_clf.best_estimator_