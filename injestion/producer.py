import csv
import json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

topic = "credit_card_transactions"

with open("/data/raw/credit_card_transactions.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        producer.send(topic, row)

producer.flush()
print("Data ingestion completed.")
