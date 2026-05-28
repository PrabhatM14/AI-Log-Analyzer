import os
from flask import Flask
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import IsolationForest

app = Flask(__name__)

def run_ai_analysis(file_path):
    if not os.path.exists(file_path):
        return ["Error: Log file not found."]

    with open(file_path, "r") as f:
        logs = [line.strip() for line in f.readlines() if line.strip()]
        
    if not logs:
        return ["No log entries found to analyze."]

    # Convert unstructured text to numerical vectors
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(logs)

    # Train Isolation Forest for anomaly detection
    model = IsolationForest(contamination=0.25, random_state=42)
    predictions = model.fit_predict(X)

    # Format results as a list of strings
    report = []
    for log_entry, prediction in zip(logs, predictions):
        if prediction == -1:
            report.append(f"[⚠️ ANOMALY DETECTED] -> {log_entry}")
        else:
            report.append(f"[Normal]             -> {log_entry}")
    return report

# Define the web endpoint that triggers the AI model
@app.route("/")
def home():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    log_file_path = os.path.join(current_dir, "mockServerLog.txt")
    
    # Run the machine learning engine
    analysis_results = run_ai_analysis(log_file_path)
    
    # Render the results as simple text in the browser
    output = "=== AI CLOUD LOG ANALYSIS REPORT ===\n\n" + "\n".join(analysis_results)
    return output, 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == "__main__":
    # Flask requires port binding to run in a container environment
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)