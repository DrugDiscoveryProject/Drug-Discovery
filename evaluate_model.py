import argparse
import pickle
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split

# Function to load the trained model
def load_model(model_path):
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    return model

# Function to evaluate the model
def evaluate_model(model, X_test, y_test):
    # Predict the target variable on the test data
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')

    return accuracy, precision, recall, f1

# Main function
def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Evaluate a trained machine learning model.')
    parser.add_argument('--model', type=str, required=True, help='Path to the trained model file (Pickle format).')
    parser.add_argument('--data', type=str, required=True, help='Path to the evaluation data file (numpy format).')
    parser.add_argument('--output', type=str, required=True, help='Path to output the evaluation results.')
    
    args = parser.parse_args()
    
    # Load the model
    model = load_model(args.model)
    
    # Load the evaluation dataset (assuming it's a numpy file with X and y)
    data = np.load(args.data)
    X = data['X']  # Features
    y = data['y']  # Labels
    
    # Split the data into training and test sets (if not already split)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Evaluate the model
    accuracy, precision, recall, f1 = evaluate_model(model, X_test, y_test)
    
    # Print the results
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")
    
    # Save the results to a file
    with open(args.output, 'w') as f:
        f.write(f"Accuracy: {accuracy:.4f}\n")
        f.write(f"Precision: {precision:.4f}\n")
        f.write(f"Recall: {recall:.4f}\n")
        f.write(f"F1 Score: {f1:.4f}\n")
    
if __name__ == "__main__":
    main()
