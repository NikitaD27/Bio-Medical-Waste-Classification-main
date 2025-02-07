# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JtXGS_lVJjqG6cRSINLSU93lTRqO5eNQ
"""

!pip install torch==1.8.1+cu111 torchvision==0.9.1+cu111 torchaudio===0.8.1 -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html

!git clone https://github.com/ultralytics/yolov5

import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

model = torch.hub.load('ultralytics/yolov5', 'custom', path='/content/best.pt', force_reload=True)

!pip install gradio

import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

class_names = ["Disposable Waste","Pathological/Medicinal Waste","Sharps/Glass","Radioactive Waste"]

import gradio as gr
import torch
from PIL import Image

def med_class(im, size=640):
    g = (size / max(im.size))  # gain
    im = im.resize((int(x * g) for x in im.size), Image.ANTIALIAS)  # resize

    results = model(im)  # inference
    results.render()  # updates results.imgs with boxes and labels
    return Image.fromarray(results.ims[0])

title = "YOLOv5 Medical Waste Detection"
description = "Disposable Waste - Label(0) | Pathological/Medicinal Waste - Label(1) | Sharps/Glass - Label(2) | Radioactive Waste - Label(3)"

gr.Interface(fn=med_class,
             inputs=gr.Image(type="pil"),
             outputs=gr.Image(type="pil"),title=title, description=description,
             examples=["/content/483_jpg.rf.88d6db8096ddd8feb808bf1121e7bac1.jpg","/content/IMG_20220803_152631_jpg.rf.8660e31b8347c842cd9fa19f09b67dd8.jpg","/content/Truck384_jpg.rf.d6719bc87784cf1e2cfe830dad6c4de0.jpg","/content/mask194_jpg.rf.711e5c4cb13def988a57d3ad0cc2c8bd.jpg"]).launch(debug=True)