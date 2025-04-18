import numpy as np
import pandas as pd
from sklear.metrics import accuracy_score, confusion_metrics
from sklearn.model_selection import train_test_split
from sklearn.neighours import KNeighboursClassifier


def main():
    iris = load_iris()
    print("Hello from prog-8!")


if __name__ == "__main__":
    main()
