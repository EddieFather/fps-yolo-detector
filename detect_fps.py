import time
import cv2
import torch

# 加载预训练的YOLOv5模型
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # 使用yolov5s模型，适合实时检测

# 打开视频流（例如打开摄像头或者视频文件）
cap = cv2.VideoCapture(0)  # 0代表默认摄像头，如果使用视频文件可以传入路径

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# 获取视频流的帧率
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"FPS of the video stream: {fps}")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # 记录开始时间
    start_time = time.time()

    # 使用YOLOv5模型进行检测
    results = model(frame)

    # 获取检测结果，绘制检测框
    results.render()  # 绘制结果到原始图像
    annotated_frame = results.imgs[0]  # 获取带注释的图像

    # 计算FPS
    elapsed_time = time.time() - start_time
    current_fps = 1.0 / elapsed_time

    # 在图像上显示FPS
    cv2.putText(annotated_frame, f'FPS: {current_fps:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # 显示处理后的图像
    cv2.imshow('YOLOv5 FPS Detection', annotated_frame)

    # 按'q'键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
