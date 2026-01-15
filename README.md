Batch-Processing Data Architecture for Credit Card Fraud Detection
Course: Data Engineering (DLMDSEDE02) | Student: Saurav Nakar | Matriculation no.: 10604547

1. Project Overview
This project implements a scalable microservices architecture to process large-scale historical credit card transaction data. It utilizes Docker to orchestrate Apache Kafka (Ingestion), Apache Spark (Processing), and Apache Airflow (Workflow Management).

2. Installation & Setup
Prerequisites: Docker Desktop (4GB+ RAM) and Git.

Steps:
1.  Clone the Repo: `git clone [YOUR_GITHUB_LINK]`
2.  Add Data: Place your `credit_card_transactions.csv` file into the `data/` folder.
3.  Start System: Run `docker-compose up -d --build`.

3. Usage
Ingestion: The Python service automatically buffers data to Kafka topics upon startup.
Processing: Spark jobs consume these topics to clean and aggregate data.
Verification: Check `http://localhost:8080` (Spark UI) to see active batch jobs.
