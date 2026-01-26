from ultralytics import YOLO
import torch

def local_train(model_path, data_yaml, epochs=1):
    model = YOLO(model_path)
    model.train(data=data_yaml, epochs=epochs, imgsz=640, verbose=False)
    return model.model.state_dict()
