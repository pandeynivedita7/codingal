from federated.edge_client import local_train
from federated.server import fedavg
from ultralytics import YOLO
import os

# Edge datasets
edges = [
    "data/edge1.yaml",
    "data/edge2.yaml",
    "data/edge3.yaml"
]

weights = []

print("🚀 Starting Federated Training")

for edge_data in edges:
    print(f"Training on {edge_data}")
    w = local_train("yolov8n.pt", edge_data)
    weights.append(w)

print("🔗 Aggregating weights using FedAvg")
global_weights = fedavg(weights)

global_model = YOLO("yolov8n.pt")
global_model.model.args["nc"] = 1

global_model.model.load_state_dict(global_weights, strict=False)


global_model.save("global_fed_yolo.pt")

print("✅ Global Federated Model Saved: global_fed_yolo.pt")
