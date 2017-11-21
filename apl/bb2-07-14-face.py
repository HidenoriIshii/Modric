# -*- coding: utf-8 -*i
import picamera
import picamera.array
import cv2
import pygame
import sys
import numpy
import time
pygame.init()
size=(320,240)
screen = pygame.display.set_mode(size)

def pygame_imshow(array):
    b,g,r = cv2.split(array)
    rgb = cv2.merge([r,g,b])
    surface1 = pygame.surfarray.make_surface(rgb)
    surface2 = pygame.transform.rotate(surface1, -90)
    surface3 = pygame.transform.flip(surface2, True, False)
    screen.blit(surface3, (0,0))
    pygame.display.flip()
#Haar-like
face_cascade_path =  "/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml"
eyes_cascade_path = "/usr/share/opencv/haarcascades/haarcascade_eye.xml"
eyeglasses_cascade_path = "/usr/share/opencv/haarcascades/haarcascade_eye_tree_eyeglasses.xml"
face_cascade = cv2.CascadeClassifier(face_cascade_path)
eyes_cascade = cv2.CascadeClassifier(eyes_cascade_path)
eyeglasses_cascade = cv2.CascadeClassifier(eyeglasses_cascade_path)

with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        camera.resolution = (320, 240)

        while True:
            #neutral degree X-axis
            now_degree_x =475
            #neutral degree Y-axis
            now_degree_y = 325
            #moved degree X-axis
            move_degree_x = 0
            #moved degree Y-axis
            move_degree_y = 0
            # stream.arrayにBGRの順で映像データを格納
            camera.capture(stream, 'bgr', use_video_port=True)
            # 映像データをグレースケール画像grayに変換
            gray = cv2.cvtColor(stream.array, cv2.COLOR_BGR2GRAY)
            # grayから顔を探す
            # To get the coordinates
            facerect = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=2, minSize=(30,30), maxSize=(150,150))

            if len(facerect) > 0:
                for rect in facerect:
                    # 元の画像(system.array)の顔がある位置赤い四角を描画
                    # rect[0:2]:長方形の左上の座標, rect[2:4]:長方形の横と高さ
                    # rect[0:2]+rect[2:4]:長方形の右下の座標
                    img_x = rect[0]+rect[2]/2
                    img_y = rect[1]+rect[3]/2
                    print('pt1',rect[0:2])
                    print('pt2',rect[0:2]+rect[2:4])
                    print('img_x,y:',img_x,img_y)
                    #the left and right center:160 = 320 /2
                    #gap of the left and right center = img_x - 160
                    gap_x = img_x -160
                    # サーボモータX軸移動量 = gap_x * 比例定数A
                    # 比例定数Aは、実際のサーボモータの動きから調整した値を定数化する
                    # サンプルでは3としている
                    move_x = gap_x * 3
                    move_degree_x = now_degree_x - (img_x-160)*0.4
                    #the up and down the center:120 = 240 /2
                    #gap of the up and down center = img_y - 120
                    gap_y = img_y-120
                    # サーボモータY軸移動量 = gap_x * (-比例定数A)
                    # 比例定数Aは、実際のサーボモータの動きから調整した値を定数化する
                    # サンプルでは3としている
                    move_degree_y = now_degree_y - (img_y-120)*0.4
                    print('mov_deg:',int(move_degree_x),int(move_degree_y))
                    # Pwm moved degree X-axis
                    # Pwm moved degree Y-axis
                    time.sleep(0.1)
                    now_degree_x = now_degree_x + move_degree_x
                    now_degree_y = now_degree_y + move_degree_y
                    print('now_deg:',int(now_degree_x),int(now_degree_y))
                    cv2.circle(stream.array,(int(img_x),int(img_y)),3,(255,255,255),-1)
                    #img:image
                    #pt1:vertex of the rectangle
                    #pt2: vertex of the rectangle opposite to  pt1
                    #color:color of the rectangle
                    #thickness: thcikness of lines that make up the rectangle.
                    #line type:
                    #shift:decimal places of vertex
                    cv2.rectangle(stream.array, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), (0,0,255), thickness=2)
                    # detect Eye in face
                    eyes = eyes_cascade.detectMultiScale(gray)
                    for rect in eyes:
                        cv2.rectangle(stream.array,tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), (0,255,0), thickness=2)
                    '''
                    # detect Eyeglasses in face
                    eyeglasses = eyeglasses_cascade.detectMultiScale(gray)
                    for rect in eyeglasses:
                        print 'detect glasses'
                        cv2.rectangle(stream.array,tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), (255,255,0), thickness=2)
                    '''
            # pygameで画像を表示
            pygame_imshow(stream.array)

            # "q"を入力でアプリケーション終了
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

            # streamをリセット
            stream.seek(0)
            stream.truncate()
