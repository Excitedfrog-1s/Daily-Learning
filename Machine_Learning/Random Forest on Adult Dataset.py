'''
Random Forest on Adult data set.
From https://archive.ics.uci.edu/ml/datasets/adult
This is not good format to put all code in one file...
If you want to see a good presentation version, 
please check the "Random Forest on Adult Dataset.ipynb" file.
'''

# Import Libraies
import time
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import ParameterGrid, GridSearchCV


# Loading Dataset with adding columns name
def load_data():
    train_set = pd.read_csv(
        'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data',
        header=None,
        sep=',\s*',
        engine='python')
    test_set = pd.read_csv(
        'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test',
        header=None,
        sep=',\s*',
        engine='python',
        skiprows=1)
    train_set.columns = [
        'Age', 'Workclass', 'fnlwgt', 'Education', 'Education_num',
        'Marital_status', 'Occupation', 'Relationship', 'Race', 'Sex',
        'Capital_gain', 'Capital_loss', 'Hours_per_week', 'Native_country',
        'Salary'
    ]
    test_set.columns = [
        'Age', 'Workclass', 'fnlwgt', 'Education', 'Education_num',
        'Marital_status', 'Occupation', 'Relationship', 'Race', 'Sex',
        'Capital_gain', 'Capital_loss', 'Hours_per_week', 'Native_country',
        'Salary'
    ]
    return train_set, test_set


# Data preprocessing
'''
Here are four functions for:
(1). Evaluate how many missing values in both train and test set.
(2). In test data set, there are "." at the end of salary. Delete them in order to align with training set.
(3). Delete samples which have missing values.
(4). Replace function, which will be used to replace string to number in features.
'''


def check_missing_value(data):
    num = data.shape[0]
    for i, j in zip(data.columns,
                    (data.values.astype(str) == '?').sum(axis=0)):
        if j != 0:
            percentage = float(j / num * 100)
            print('Missing value in ' + str(i) + ': ' +
                  '{0:.3f}%'.format(percentage))


def remove_period(data):
    data.replace(['<=50K.', '>50K.'], ['<=50K', '>50K'], inplace=True)
    return data


def remove_missing_value(data):
    data = data.replace({'?': None})
    data = data.dropna(axis=0)
    return data


def adult_replace(data, a, b):
    '''
    a: The feature(column) name
    b: The string which should be replaced by '1'
    Other string will be replaced to 0
    '''
    data[str(a)] = data[str(a)].map(lambda x: 1 if x == str(b) else 0)
    return data


train_set, test_set = load_data()
print('Shape of training set is:', train_set.shape)
print('Shape of test set is:', test_set.shape)
check_missing_value(train_set)
print('-----' * 10)
check_missing_value(test_set)
train_set = remove_missing_value(remove_period(train_set))
test_set = remove_missing_value(remove_period(test_set))
num_train = train_set.shape[0]
print('Shape of training set is:', train_set.shape)
print('Shape of test set is:', test_set.shape)
print('Number of training set sample is: ', num_train)
entire_set = pd.concat([train_set, test_set])
print('The shape of entire data set before preprocessing is: ',
      entire_set.shape)
entire_set.replace([
    'Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov',
    'State-gov', 'Without-pay', 'Never-worked'
], [
    'Private', 'Self_emp', 'Self_emp', 'Gov', 'Gov', 'Gov', 'Without_pay',
    'Without_pay'
],
                   inplace=True)
education_Pivot = pd.pivot_table(train_set,
                                 index='Education',
                                 values='Education_num')
education_Pivot.sort_values(by=['Education_num'])
entire_set.drop('Education', axis=1, inplace=True)
entire_set.replace([
    'Never-married', 'Divorced', 'Separated', 'Widowed',
    'Married-spouse-absent', 'Married-AF-spouse', 'Married-civ-spouse'
], [
    'no_married', 'no_married', 'no_married', 'no_married', 'no_married',
    'married', 'married'
],
                   inplace=True)
entire_set = adult_replace(entire_set, 'Marital_status', 'married')
entire_set.replace([
    'Tech-support', 'Craft-repair', 'Other-service', 'Sales',
    'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners',
    'Machine-op-inspect', 'Adm-clerical', 'Farming-Fishing',
    'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces'
], [
    'Technology', 'Craft', 'Service', 'Service', 'Management', 'Service',
    'Craft', 'Technology', 'Service', 'Craft', 'Service', 'Service', 'Service',
    'Force'
],
                   inplace=True)
entire_set.replace([
    'Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative',
    'Unmarried'
], [
    'In_relation', 'Not_in_relation', 'In_relation', 'Not_in_relation',
    'Not_in_relation', 'Not_in_relation'
],
                   inplace=True)
entire_set = adult_replace(entire_set, 'Relationship', 'In_relation')
entire_set = adult_replace(entire_set, 'Sex', 'Male')
num_us_train = train_set.apply(pd.value_counts)
print(num_us_train)
print('-----' * 20)
num_us_test = test_set.apply(pd.value_counts)
print(num_us_test)
entire_set = adult_replace(entire_set, 'Native_country', 'United-States')
entire_set = adult_replace(entire_set, 'Salary', '>50K')
dummy_class = ['Workclass', 'Race', 'Occupation']
without_dummy_class = [
    'Age', 'fnlwgt', 'Education_num', 'Marital_status', 'Relationship', 'Sex',
    'Capital_gain', 'Capital_loss', 'Hours_per_week', 'Native_country',
    'Salary'
]
dummy = pd.get_dummies(entire_set[dummy_class])
entire_set = pd.concat([entire_set[without_dummy_class], dummy], axis=1)
salary = entire_set['Salary'].values
entire_set.drop(['Salary'], axis=1, inplace=True)
standardised_feature = [
    'Age', 'fnlwgt', 'Education_num', 'Capital_gain', 'Capital_loss',
    'Hours_per_week'
]
entire_set[standardised_feature] = entire_set[standardised_feature].apply(
    lambda x: (x - np.mean(x)) / np.std(x))
entire_set = np.array(entire_set)
x_train = entire_set[0:num_train, :]
y_train = salary[0:num_train]
x_test = entire_set[num_train:]
y_test = salary[num_train:]
print('The shape of training data after preprocessing is: ', x_train.shape)
print('The shape of training label after preprocessing is: ', y_train.shape)
print('The shape of test data after preprocessing is: ', x_test.shape)
print('The shape of test label after preprocessing is: ', y_test.shape)
# Training
train_start_time = time.time()
rf = RandomForestClassifier()
rf.fit(x_train, y_train)
train_end_time = time.time()
print('Training time is: ' + str(round(train_end_time - train_start_time, 4)) +
      's')

# Prediction
test_start_time = time.time()
print('Accuracy is: ', rf.score(x_test, y_test))
test_end_time = time.time()
print('Prediction time is: ' + str(round(test_end_time - test_start_time, 4)) +
      's')

# Confusion Matrix
pred = rf.predict(x_test)
matrix = confusion_matrix(y_test, pred)
print('Confusion Matrix is\n{}'.format(matrix))

# 10-Fold Cross Validation
rf_scores = cross_val_score(rf, x_train, y_train, cv=10, scoring='accuracy')
print('10-fold CV accuracy: %.4f +/- %.4f' %
      (np.mean(rf_scores), np.std(rf_scores)))

# Precision, recall, etc
print(classification_report(y_test, pred))
rf.get_params()
param_grid = {
    'min_samples_leaf': [1, 5, 10, 15, 20, 25],
    'max_features': ['sqrt', 'log2', 0.5, 0.6, 0.7],
    'max_depth': [10, 20, 30, 50, 100],
    'n_estimators': [10, 20, 50, 70, 100],
    'n_jobs': [-1],
}
param_list = ParameterGrid(param_grid)
cv = GridSearchCV(rf, param_grid)
rf_cv = cv.fit(x_train, y_train)
print('Grid in progress:\n')
means = rf_cv.cv_results_['mean_test_score']
stds = rf_cv.cv_results_['std_test_score']
for mean, std, params in zip(means, stds, rf_cv.cv_results_['params']):
    print("%0.3f (+/-%0.03f) when %r" % (mean, std * 2, params))
print('The best choice is: ', rf_cv.best_params_)
# Training
train_start_time = time.time()
rf_new = RandomForestClassifier(max_depth=100,
                                max_features='sqrt',
                                min_samples_leaf=5,
                                n_estimators=100,
                                n_jobs=-1)
rf_new.fit(x_train, y_train)
train_end_time = time.time()
print('Training time is: ' + str(round(train_end_time - train_start_time, 4)) +
      's')

# Prediction
test_start_time = time.time()
print('Accuracy is: ', rf_new.score(x_test, y_test))
test_end_time = time.time()
print('Prediction time is: ' + str(round(test_end_time - test_start_time, 4)) +
      's')

# Confusion Matrix
pred_new = rf_new.predict(x_test)
matrix_new = confusion_matrix(y_test, pred)
print('Confusion Matrix is\n{}'.format(matrix))

# 10-Fold Cross Validation
rf_new_scores = cross_val_score(rf_new,
                                x_train,
                                y_train,
                                cv=10,
                                scoring='accuracy')
print('10-fold CV accuracy: %.4f +/- %.4f' %
      (np.mean(rf_new_scores), np.std(rf_new_scores)))

# Precision, recall, etc
print(classification_report(y_test, pred_new))
