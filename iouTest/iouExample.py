import numpy as np
# box:[up, left, down, right]

box1 = [0, 0, 8, 6]
box2 = [2, 3, 10, 9]
def Iou(box1, box2):
    area1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
    area2 = (box2[2] - box2[0]) * (box2[3] - box2[1])
    in_h = min(box1[2], box2[2]) - max(box1[0], box2[0])
    in_w = min(box1[3], box2[3]) - max(box1[1], box2[1])
    areaInter = in_h * in_w
    areaUnion = area1 + area2 - areaInter
    Iou = areaInter / areaUnion
    return Iou

print(Iou(box1,box2))