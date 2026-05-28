import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import IsolationForest

def load_and_analyze_logs(file_path):
    print(f" Reading log data from {file_path}...")
    
    # Ensure the target log file exists before attempting to read
    if not os.path.exists(file_path):
        print(f"Error: The file {file_path} does not exist.")
        return

    with open(file_path, "r") as f:
        logs = [line.strip() for line in f.readlines() if line.strip()]
        
    if not logs:
        print("No log entries found to analyze.")
        return

    # Convert unstructured log text into numerical feature vectors.
    # This tokenizes strings to capture recurring keywords, IP addresses, and HTTP status codes.
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(logs)

    # Initialize an Unsupervised Isolation Forest model for anomaly detection.
    # 'contamination=0.25' specifies that we expect roughly 25% of the log traffic to be anomalous.
    model = IsolationForest(contamination=0.25, random_state=42)
    
    # Train the model on the log structure and predict outliers.
    # Returns 1 for normal statistical patterns, and -1 for structural anomalies.
    predictions = model.fit_predict(X)

    print("\n=== AI LOG ANALYSIS REPORT ===")
    for log_entry, prediction in zip(logs, predictions):
        if prediction == -1:
            print(f"[⚠️ ANOMALY DETECTED] -> {log_entry}")
        else:
            print(f"[Normal]             -> {log_entry}")

if __name__ == "__main__":
    # Resolve paths dynamically relative to the script location 
    # to maintain environment independence (crucial for containerization)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    log_file_path = os.path.join(current_dir, "mock_server_logs.txt")
    
    load_and_analyze_logs(log_file_path)