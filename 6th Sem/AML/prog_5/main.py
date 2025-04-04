import pandas as pd
from sklearn.naive_bayes import CategoricalNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score


def main():
    ## Step 1: Read Dataset
    df = pd.read_csv("data.csv")

    ## Step 2: Lets Encode Categorical Features into numberical values
    label_encoder = {}
    for c in df.columns:
        le = LabelEncoder()
        df[c] = le.fit_transform(df[c])
        label_encoder[c] = le

    ## Step 3: Split Dataset into Features and Target Variables
    x = df.drop("play", axis=1)
    y = df["play"]

    ## Step 4: Train and test split
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=2
    )

    ## Step 5: Train NB
    model = CategoricalNB()
    model.fit(x_train, y_train)

    ## Step 6: Test
    y_pred = model.predict(x_test)

    ## Step 7: Test Accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(accuracy)


if __name__ == "__main__":
    main()
