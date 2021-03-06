# -*- coding: utf-8 -*-
import picamera
import picamera.array
import cv2
import pygame
import sys
import numpy
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
                    cv2.rectangle(stream.array, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), (0,0,255), thickness=2)
                    # detect Eye in face
                    eyes = eyes_cascade.detectMultiScale(gray)
                    for rect in eyes:
                        cv2.rectangl:e(stream.array,tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), (0,255,0), thickness=2)
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
