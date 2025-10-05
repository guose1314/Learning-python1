# Untitled - By: lenovo - 周五 8月 9 2019

import sensor, image, time
from pid import PID
from pyb import Servo

pan_servo=Servo(1) # P7
distance_servo=Servo(2) # P8
mid_Xangel = -10 #X舵机给定初始转向
mid_Yangel = 15 #Y舵机给定初始转向

Aim_threshold = (66, 83, 17, 29, -11, 5)     #(76, 87, 18, 42, -16, 4)
red_threshold  = (67, 77, 11, 32, -20, -6)
pixels_threshold  = 10   #像素的阈值
K= 4840           #the value should be measured
distance_angelvalue = []

#pan_pid = PID(p=0.07, i=0, imax=90) #脱机运行或者禁用图像传输，使用这个PID
#distance_pid = PID(p=0.05, i=0, imax=90) #脱机运行或者禁用图像传输，使用这个PID
pan_pid = PID(p=0.1, i=0, imax=90)#在线调试使用这个PID
distance_pid = PID(p=0.1, i=0, imax=90)#在线调试使用这个PID

sensor.reset() # Initialize the camera sensor.
sensor.set_pixformat(sensor.RGB565) # use RGB565.
sensor.set_framesize(sensor.QVGA) # use QQVGA for speed.
sensor.skip_frames(10) # Let new settings take affect.
sensor.set_auto_whitebal(False) # turn this off.
clock = time.clock() # Tracks FPS.
pan_servo.angle(mid_Xangel)# 摆正水平舵机
distance_servo.angle(mid_Yangel) # 摆正竖直舵机

def find_max(blobs):
    max_size=0
    for blob in blobs:
        if blob[2]*blob[3] > max_size:
            max_blob=blob
            max_size = blob[2]*blob[3]
    return max_blob
while(True):
    clock.tick() # Track elapsed milliseconds between snapshots().

    img = sensor.snapshot() # Take a picture and return the image.
    blobs = img.find_blobs([Aim_threshold],pixels_threshold  = pixels_threshold)
    if blobs:
        max_blob = find_max(blobs)

        # 计算距离值
        Dm = (max_blob[2]+max_blob[3])/2
        length = K/Dm
        print("Center X:",max_blob[5]) # cx坐标值（debug调试测值用）
        print("像素直径值：",Dm)#(像素点直径长度)（debug调试测值用）
        print("length:",length)#(距离长度)（debug调试测值)

        # 转换到对应发射角度（可用列表方式解决）
        shot_angel = length * 1

        pan_error = max_blob.cx()-img.width()/2 # 计算X偏差
        distance_error = max_blob.cy()-img.height()/2 # 计算距离角度调整误差
        # distance_error = length - 250
        print("distance_error:",distance_error)
        # distance_error = shot_angel-img.height()/2 # 计算距离角度调整误差

        print("pan_error: ", pan_error)

        img.draw_rectangle(max_blob.rect()) # rect
        img.draw_cross(max_blob.cx(), max_blob.cy()) # cx, cy

        pan_output = pan_pid.get_pid(pan_error,1)/2 # 尽量除以2，抖动幅度明显减少
        distance_output = distance_pid.get_pid(distance_error,1)/2

        print("pan_output",pan_output)
        print("distance_output:",distance_output)
        pan_servo.angle(pan_servo.angle()-pan_output)
        distance_servo.angle(distance_servo.angle()+distance_output)
