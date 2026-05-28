FROM python:3.11-slim
WORKDIR /app
COPY reqs.txt .
RUN pip install --no-cache-dir -r reqs.txt
COPY analyzer.py .
COPY mockServerLog.txt .

# Expose Flask's default port 
EXPOSE 10000

CMD ["python", "analyzer.py"]