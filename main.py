import torch
import cv2
import numpy as np
import pathlib

if __name__ == '__main__':
    temp = pathlib.PosixPath
    pathlib.PosixPath = pathlib.WindowsPath
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='./best.pt', force_reload=True)
    cap = cv2.VideoCapture(0)
    print("Starting Live Detections")
    while cap.isOpened():
        ret, frame = cap.read()

        # Make detections
        results = model(frame)

        cv2.imshow('Disposable Waste - 0 | Pathological/Medicinal Waste - 1 | Sharps/Glass - 2 | Radioactive Waste - 3 ', np.squeeze(results.render()))

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

