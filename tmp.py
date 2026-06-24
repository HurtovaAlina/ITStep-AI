import numpy
import cv2
import ultralytics
import torch
import langchain
import langgraph
import torch

# мак
print(torch.mps.is_available())

import onnxruntime as ort

import numpy as np

print("ONNX Runtime version:", ort.__version__)

# Create a fake session just to test backend availability

providers = ort.get_available_providers()

print("Available providers:", providers)

# Create dummy input

x = np.random.randn(1, 3, 224, 224).astype(np.float32)

print("Input shape:", x.shape)

print("ONNX Runtime is working correctly ✅")
