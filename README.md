# 基于 YOLOv5 的 FPS 检测

本项目演示如何使用 YOLOv5 检测视频流中的物体并计算 FPS（每秒帧数），以进行实时性能评估。

## 要求

- Python 3.x
- torch
- opencv-python
- yolov5

## 安装

clone 此版本库并安装所需的依赖项：

```bash
git clone https://github.com/EddieFather/yolo-fps-detection.git
cd yolo-fps-detection
pip install -r requirements.txt
```

## 如何运行程序：

一旦你完成了以上步骤并且有了所有文件，以下是如何在本地机器上运行该程序的详细说明：

1.安装依赖：

安装以下环境依赖:
torch
opencv-python
yolov5

```bash
pip install -r requirements.txt
```

2.运行程序：

运行 detect_fps.py 脚本：

这将启动摄像头并使用 YOLOv5 检测物体，同时在画面上显示 FPS（帧率）值。

3.退出程序：
按 q 键退出程序。
