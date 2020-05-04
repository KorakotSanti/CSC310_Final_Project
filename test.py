import pandas as pd
import numpy as np
np.set_printoptions(formatter={'float_kind':"{:3.2f}".format})
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from assets.confint import classification_confint
from sklearn.tree import tree
from assets.treeviz import tree_print
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from joblib import dump
from sklearn.datasets import load_digits

digits = load_digits()
images = digits.data
labels = digits.target

# decision trees
model2 = DecisionTreeClassifier(random_state=1)

# grid search
param_grid = {'max_depth': list(range(1,21)), 'criterion': ['entropy','gini'] }
grid = GridSearchCV(model2, param_grid, cv=5)
grid.fit(images, labels)
print("Grid Search: best parameters: {}".format(grid.best_params_))

# accuracy of best model with confidence interval
best_model = grid.best_estimator_
predict_y = best_model.predict(images)
acc = accuracy_score(labels, predict_y)
lb,ub = classification_confint(acc,images.shape[0])
print("Accuracy: {:3.2f} ({:3.2f},{:3.2f})".format(acc,lb,ub))

dump(best_model, 'DTreeModel.joblib')

# KNN
model = KNeighborsClassifier()

# grid search
param_grid = {'n_neighbors': list(range(1,51))}
grid = GridSearchCV(model, param_grid, cv=5)
grid.fit(images, labels)
print("Grid Search: best parameters: {}".format(grid.best_params_))

# accuracy of best model with confidence interval
best_model = grid.best_estimator_
predict_y = best_model.predict(images)
acc = accuracy_score(labels, predict_y)
lb,ub = classification_confint(acc,images.shape[0])
print("Accuracy: {:3.2f} ({:3.2f},{:3.2f})".format(acc,lb,ub))

dump(best_model, 'KNN_Model.joblib')