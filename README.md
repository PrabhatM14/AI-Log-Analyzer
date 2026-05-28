
# AI-Powered Cloud Log Analyzer

A containerized, cloud-deployed Python microservice that utilizes an unsupervised Machine Learning model to execute real-time anomaly detection and security threat classification on raw server traffic logs. 

---

## 🚀 System Architecture & Overview

Instead of relying on rigid, hardcoded string matching or `if/else` statements to parse server output, this project applies an **Isolation Forest** algorithm to detect structural deviations in log data. It identifies potential security vulnerabilities, brute-force attempts, and unexpected server states by analyzing the statistical isolation of tokenized log lines.

* **Backend Engine:** Python 3.11 with `Flask` for lightweight web routing.
* **Machine Learning:** `scikit-learn` utilizing `CountVectorizer` for text tokenization and `IsolationForest` for unsupervised anomaly detection.
* **DevOps & Infrastructure:** Fully containerized via `Docker` and deployed to a rolling, production-grade cloud environment on `Render`.

---

## 🛠️ Tech Stack & Key Competencies

* **Languages:** Python
* **Libraries:** scikit-learn, pandas, numpy, Flask
* **Tools & Cloud:** Docker, Render Cloud, Git/GitHub
* **Architectural Concepts:** Microservices, Containerization, Outlier Detection, CI/CD Pipelines, Environment Variable Injection

---

## 📦 Local Setup and Installation

### Prerequisites
* Docker Desktop installed and running
* Git

### Clone and Run Locally (Without Docker)
1. Clone the repository:
   ```bash
   git clone [https://github.com/PrabhatM14/ai-cloud-log-analyzer.git](https://github.com/PrabhatM14/ai-cloud-log-analyzer.git)

```

2. Navigate into the project directory:
```bash
cd ai-cloud-log-analyzer

```


3. Install dependencies:
```bash
pip install -r requirements.txt

```


4. Execute the server:
```bash
python analyzer.py

```


5. Open `http://localhost:10000` in your web browser.

### Run via Docker Container

To replicate the exact production-level isolation used in cloud hosting:

1. Build the Docker image:
```bash
docker build -t ai-log-analyzer .

```


2. Run the container:
```bash
docker run --rm -p 10000:10000 ai-log-analyzer

```


3. Navigate to `http://localhost:10000` to view the engine's output.

---

## ☁️ Cloud Deployment Configuration

This microservice is configured for continuous deployment on **Render Cloud**. It utilizes a multi-stage execution layer defined in the `Dockerfile` to preserve a minimal memory footprint.

### Injected Environment Variables

To ensure secure, environment-independent operations, the following production configurations are actively enforced:

* `PORT`: Binds the Flask socket layer dynamically to the container service mapping (`10000`).
* `FLASK_ENV`: Enforces a secure `production` runtime execution state.
* `FLASK_DEBUG`: Explicitly disabled (`false`) to eliminate verbose stack traces and mitigate directory exposure vulnerabilities.

```

```
