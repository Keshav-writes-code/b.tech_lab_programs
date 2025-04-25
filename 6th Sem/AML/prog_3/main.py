import numpy as np
import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature, self.threshold = feature, threshold
        self.left, self.right = left, right
        self.value = value
    
    def is_leaf(self): return self.value is not None

class ID3DecisionTree:
    def __init__(self, max_depth=None):
        self.max_depth, self.root = max_depth, None
        self.feature_names = None
    
    def fit(self, X, y, feature_names=None):
        self.feature_names = feature_names
        self.root = self._grow_tree(X, y)
    
    def _entropy(self, y):
        hist = np.bincount(y)
        ps = hist / len(y)
        return -np.sum([p * np.log2(p) for p in ps if p > 0])
    
    def _best_split(self, X, y):
        m, n = X.shape
        if m <= 1: return None, None
        
        parent_entropy = self._entropy(y)
        best_gain, best_feature, best_threshold = -float('inf'), None, None
        
        for feature_idx in range(n):
            for threshold in np.unique(X[:, feature_idx]):
                left_idx = X[:, feature_idx] <= threshold
                right_idx = ~left_idx
                
                if np.sum(left_idx) == 0 or np.sum(right_idx) == 0: continue
                
                # Calculate information gain
                info_gain = parent_entropy
                info_gain -= (np.sum(left_idx) / m) * self._entropy(y[left_idx])
                info_gain -= (np.sum(right_idx) / m) * self._entropy(y[right_idx])
                
                if info_gain > best_gain:
                    best_gain = info_gain
                    best_feature, best_threshold = feature_idx, threshold
                    
        return best_feature, best_threshold
    
    def _grow_tree(self, X, y, depth=0):
        n_classes = len(np.unique(y))
        
        # Stopping criteria
        if (self.max_depth is not None and depth >= self.max_depth) or n_classes == 1:
            return Node(value=Counter(y).most_common(1)[0][0])
        
        # Find the best split
        best_feature, best_threshold = self._best_split(X, y)
        if best_feature is None:
            return Node(value=Counter(y).most_common(1)[0][0])
        
        # Split and grow subtrees
        left_idx = X[:, best_feature] <= best_threshold
        left = self._grow_tree(X[left_idx], y[left_idx], depth + 1)
        right = self._grow_tree(X[~left_idx], y[~left_idx], depth + 1)
        
        return Node(feature=best_feature, threshold=best_threshold, left=left, right=right)
    
    def predict(self, X):
        return np.array([self._traverse_tree(x, self.root) for x in X])
    
    def _traverse_tree(self, x, node):
        if node.is_leaf(): return node.value
        return self._traverse_tree(x, node.left) if x[node.feature] <= node.threshold else self._traverse_tree(x, node.right)
    
    def print_tree(self, node=None, indent=""):
        if node is None: node = self.root
        if node.is_leaf():
            print(f"{indent}Predict: [{node.value}]")
            return

        feature_name = self.feature_names[node.feature] if self.feature_names else f"X[{node.feature}]"
        print(f"{indent}{feature_name} <= {node.threshold}")
        print(f"{indent}├── True:")
        self.print_tree(node.left, indent + "│   ")
        print(f"{indent}└── False:")
        self.print_tree(node.right, indent + "    ")

# Create weather dataset and run demo
def main():
    # Simple weather dataset
    data = {
        'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 
                  'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
        'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 
                      'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
        'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 
                   'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
        'Windy': ['False', 'True', 'False', 'False', 'False', 'True', 'True', 
                'False', 'False', 'False', 'True', 'True', 'False', 'True'],
        'Play': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 
               'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
    }
    
    # Feature mappings
    mappings = {
        'Outlook': {'Sunny': 0, 'Overcast': 1, 'Rain': 2},
        'Temperature': {'Cool': 0, 'Mild': 1, 'Hot': 2},
        'Humidity': {'Normal': 0, 'High': 1},
        'Windy': {'False': 0, 'True': 1},
        'Play': {'No': 0, 'Yes': 1}
    }
    
    # Convert to dataframe and encode
    df = pd.DataFrame(data)
    for col, mapping in mappings.items():
        df[col] = df[col].map(mapping)
    
    # Prepare data
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values
    feature_names = ['Outlook', 'Temperature', 'Humidity', 'Windy']
    
    # Print original dataset
    print("ID3 Decision Tree Algorithm Demonstration\n----------------------------------------")
    print("\nDataset:")
    orig_df = pd.DataFrame({col: df[col].map({v: k for k, v in mapping.items()}) 
                           for col, mapping in mappings.items()})
    print(orig_df)
    
    # Train and test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Build tree
    print("\nBuilding the decision tree...")
    tree = ID3DecisionTree(max_depth=3)
    tree.fit(X_train, y_train, feature_names=feature_names)
    
    # Print tree structure
    print("\nDecision Tree Structure:")
    tree.print_tree()
    
    # Evaluate model
    y_pred = tree.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nTest Accuracy: {accuracy:.4f}")
    
    # Test new sample
    print("\nClassifying a new sample:")
    new_sample_text = {'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Windy': 'False'}
    print(f"New Sample: {new_sample_text}")
    
    # Predict
    new_sample = np.array([mappings['Outlook'][new_sample_text['Outlook']], 
                           mappings['Temperature'][new_sample_text['Temperature']],
                           mappings['Humidity'][new_sample_text['Humidity']], 
                           mappings['Windy'][new_sample_text['Windy']]]).reshape(1, -1)
    prediction = tree.predict(new_sample)[0]
    print(f"Prediction: {'Yes' if prediction == 1 else 'No'} (Play={prediction})")

if __name__ == "__main__":
    main()
