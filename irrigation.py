from sklearn.cross_decomposition import PLSRegression

import pandas as pd
X = pd.read_csv("dataset/input.csv")
y = pd.read_csv("dataset/output.csv")

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

plsr = PLSRegression(
    n_components=2, 
    scale=True, 
    max_iter=500, 
    tol=1e-06, 
    copy=True)

model = plsr.fit(X_train, y_train)

def analyze(X_input):
    global model
    inputs = pd.read_csv(X_input)
    pred = model.predict(inputs)
    return pred

if __name__ == "__main__":
    # predict
    predict = analyze(X_test)
    # accuracy
    from sklearn.metrics import accuracy_score
    print(accuracy_score(y_test, predict))