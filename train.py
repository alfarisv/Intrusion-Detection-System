# Description: This file is used to train the model using the dataset

import pandas as pd
import numpy as np

# Importing ML libraries for classification using Decision Tree
from sklearn import tree

from sklearn.model_selection import train_test_split
from sklearn import metrics

# Label encoding
from sklearn.preprocessing import LabelEncoder

# Using SVM
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# Using Random Forest
from sklearn.ensemble import RandomForestClassifier

import pickle
import time

# ====== FLAG PENTING ======

debug = False # Gunakan ini untuk debugging
use_svm = False # Gunakan ini untuk menggunakan SVM
print_z_scores = False # Gunakan ini untuk print z_scores

# ==========================

# Load the data
df = pd.read_csv('Dataset/UNSW-NB15_4.csv',encoding="ISO-8859-1")

# Load features from NUSW-NB15_features.csv
df_features = pd.read_csv('Dataset/NUSW-NB15_features.csv',encoding="ISO-8859-1")

# Apply features to the dataset
df.columns = df_features['Name'].values

# Making columns names more lower case, removing spaces
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

# train_test_split
X = df.drop(columns=['label'])
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)


print("Total Null values in X_train before filter:", X_train.isnull().sum().sum())

# Print Null values in X_train
if debug:
    print(X_train.isnull().sum())

# Fill null values in attack_cat column with 'normal'
X_train['attack_cat'] = X_train['attack_cat'].fillna('normal')
X_test['attack_cat'] = X_test['attack_cat'].fillna('normal')

# Fill null values in ct_flw_http_mthd column with 0
X_train['ct_flw_http_mthd'] = X_train['ct_flw_http_mthd'].fillna(0)
X_test['ct_flw_http_mthd'] = X_test['ct_flw_http_mthd'].fillna(0)

# Fill null values in is_ftp_login column with 0
X_train['is_ftp_login'] = X_train['is_ftp_login'].fillna(0)
X_test['is_ftp_login'] = X_test['is_ftp_login'].fillna(0)

print("Total Null values in X_train after filter:", X_train.isnull().sum().sum())

print(" ")

print("X_train shape before high corr filter:", X_train.shape)

# Finding dan Remove high correlation features
corr_mat = X_train.corr(method='pearson')
columns = corr_mat.columns
for i in range(corr_mat.shape[0]):
    for j in range(i+1, corr_mat.shape[0]):
        if corr_mat.iloc[i, j] >= 0.9:
            if debug:
                print(f"High corr: {columns[i]:20s} {columns[j]:20s} {corr_mat.iloc[i, j]}")

            # Dropping high correlation features
            if columns[j] in X_train.columns:
                X_train = X_train.drop(columns=[columns[j]])
            
            if columns[j] in X_test.columns:
                X_test = X_test.drop(columns=[columns[j]])

print("X_train shape after high corr filter:", X_train.shape)

print(" ")

print("Using Label Encoder to convert object to float...")

# Label encoding
le = LabelEncoder()

# Using loop to encode all the columns with object datatype to float 
for i in X_train.columns:
    if X_train[i].dtypes=='object':
        if debug:
            print(f"Encoding: {i}")
        X_train[i]=le.fit_transform(X_train[i])

for i in X_train.columns:
    if X_test[i].dtypes=='object':
        X_test[i]=le.fit_transform(X_test[i])


print(" ")

print("Using StandardScaler to scale the data...")

# Get standard deviation 
if print_z_scores:
    z_scores = X_train.std()
    print(z_scores)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

if debug:
    print(f"Data after scaling:\n{X_train}")

print(" ")

print("Training...")

start_time = time.time()
# Train using random forest
random_forest_clf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
random_forest_clf.fit(X_train, y_train)
end_time = time.time()
print("Training time taken (Random Forest): ", end_time - start_time)

# Test and get accuracy, precision, recall
y_pred = random_forest_clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("Precision:",metrics.precision_score(y_test, y_pred, average='weighted'))
print("Recall:",metrics.recall_score(y_test, y_pred, average='weighted'))
cm = metrics.confusion_matrix(y_test, y_pred)
print(cm)

print(" ")

start_time = time.time()
decision_tree_clf = tree.DecisionTreeClassifier()
decision_tree_clf.fit(X_train, y_train)
end_time = time.time()
print("Training time taken (Decision Tree): ", end_time - start_time)

# Test and get accuracy, precision, recall
y_pred = decision_tree_clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("Precision:",metrics.precision_score(y_test, y_pred, average='weighted'))
print("Recall:",metrics.recall_score(y_test, y_pred, average='weighted'))
cm = metrics.confusion_matrix(y_test, y_pred)
print(cm)

if not use_svm:
    exit()



time_start = time.time()

# Using SVM
clf = SVC(kernel='linear', random_state=0)
clf.fit(X_train, y_train)

time_end = time.time()
print("Training time taken: ", time_end - time_start)

# Predicting the test set results
y_pred = clf.predict(X_test)

# Accuracy
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# Precision
print("Precision:",metrics.precision_score(y_test, y_pred, average='weighted'))

# Recall
print("Recall:",metrics.recall_score(y_test, y_pred, average='weighted'))

# Making the confusion matrix
cm = metrics.confusion_matrix(y_test, y_pred)
print(cm)

# Save the model
pickle.dump(clf, open('svm_clf_lagi.pkl', 'wb'))











########### Tidak usah dijalankan ###########
exit()

mode_dict = pickle.load(open('svm_clf_banyak.pkl', 'rb'))

# Using SVM
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Predicting the test set results
y_pred = mode_dict.predict(X_test)

# Making the confusion matrix
cm = metrics.confusion_matrix(y_test, y_pred)
print(cm)





