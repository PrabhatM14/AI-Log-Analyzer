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
