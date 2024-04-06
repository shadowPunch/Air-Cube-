from cube import Rubic_Cube
from threading import Thread
import cv2
import mediapipe as mp
import numpy as np
import time
import pyautogui as pg





def open_tracking():
    hand_detector = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils
    cap = cv2.VideoCapture(0)
    array ,array_l , array_u ,array_d= [],[],[],[]
    length,length_u,length_d,length_l = -1,-1,-1,-1
    array_w_l , array_w_u = [] , []
    length_w_l,length_w_u=-1,-1
    c , v  = pg.size()
    g = c/1920 
    i = v/1080 
    while True:
        _ , Frame = cap.read()
        Frame = cv2.flip(Frame , 1)
        rgb_frame = cv2.cvtColor(Frame , cv2.COLOR_BGR2RGB)
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks
        frame_height , frame_width , _ = Frame.shape
        h , w = frame_height , frame_width
        cv2.line(Frame, (int(frame_width/6),int(frame_height/6)), (int(5*frame_width/6),int(frame_height/6)), (0,255,0), 2)
        cv2.line(Frame, (int(frame_width/6),int(5*frame_height/6)), (int(5*frame_width/6),int(5*frame_height/6)), (0,255,0), 2)
        cv2.line(Frame, (int(frame_width/6),int(frame_height/6)), (int(frame_width/6),int(5*frame_height/6)), (0,255,0), 2)
        cv2.line(Frame, (int(5*frame_width/6),int(frame_height/6)), (int(5*frame_width/6),int(5*frame_height/6)), (0,255,0), 2)
        cv2.line(Frame, (int(frame_width/2),int(0)), (int(frame_width/2),int(frame_height)), (0,0,255), 1)
        cv2.line(Frame, (int(0),int(frame_height/2)), (int(frame_width),int(frame_height/2)), (0,0,255), 1)
        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(Frame ,hand)
                landmark = hand.landmark
                for id , landmark in enumerate(landmark):
                    if id == 4:
                        thumb_coord = np.array([int(landmark.x*frame_width), int(landmark.y*frame_height)])
                    if id == 8:
                        index_coord = np.array([int(landmark.x*frame_width), int(landmark.y*frame_height)])

                    #Rightmost Layer
                        if  w/2 <= thumb_coord[0] <= 5*w/6 and h/2 <= thumb_coord[1] <= 5*h/6 and w/2 <= index_coord[0] <= 5*w/6 and h/6 <= index_coord[1] <= h/2:
                            if len(array) == 0:
                                array.append('R1')
                            if array[-1] != 'R1':
                                array.append('R1')
                            if len(array) >= 2:
                                if array[-1] == 'R1' and array[-2] == 'R2' and len(array) != length:
                                    pg.click(g*124,i*632)
                                    length = len(array)
                                if array[-1] == 'R2' and array[-2] == 'R1' and len(array) != length:
                                    print('Rightmost_layer_up')
                                    pg.click(g*89,i*632)
                                    length = len(array)
                        elif  w/2 <= index_coord[0] <= 5*w/6 and h/2 <= index_coord[1] <= 5*h/6 and w/2 <= thumb_coord[0] <= 5*w/6 and h/6 <= thumb_coord[1] <= h/2:
                            if len(array) == 0:
                                array.append('R2')
                            if array[-1] != 'R2':
                                array.append('R2')
                            if len(array) >= 2:
                                if array[-1] == 'R1' and array[-2] == 'R2' and len(array) != length:
                                    pg.click(124*g,632*i)
                                    cv2.imshow('Video' ,Frame)
                                    length = len(array)
                                if array[-1] == 'R2' and array[-2] == 'R1' and len(array) != length:
                                    print('Rightmost_layer_up')
                                    pg.click(89*g,632*i)
                                    length = len(array)
                        elif thumb_coord[0] < w/2 or thumb_coord[0] > 5*w/6 or thumb_coord[1] < h/6 or thumb_coord[1] > 5*h/6 or index_coord[0] < w/2 or index_coord[0] > 5*w/6 or index_coord[1] < h/6 or index_coord[1] > 5*h/6:
                            array = []
                       
                    #Leftmost Layer
                   
                        if  w/6 <= thumb_coord[0] <= w/2 and h/2 <= thumb_coord[1] <= 5*h/6 and w/6 <= index_coord[0] <= w/2 and h/6 <= index_coord[1] <= h/2:
                            if len(array_l) == 0:
                                array_l.append('L1')
                            if array_l[-1] != 'L1':
                                array_l.append('L1')
                            if len(array_l) >= 2:
                                if array_l[-1] == 'L1' and array_l[-2] == 'L2' and len(array_l) != length_l:
                                    print('Leftmost_layer_down')
                                    pg.click(221*g,i*632)
                                    length_l = len(array_l)
                                if array_l[-1] == 'L2' and array_l[-2] == 'L1' and len(array_l) != length_l:
                                    print('Leftmost_layer_up')
                                    pg.click(252*g,632*i)
                                    length_l = len(array_l)
                        elif  w/6 <= index_coord[0] <= w/2 and h/2 <= index_coord[1] <= 5*h/6 and w/6 <= thumb_coord[0] <= w/2 and h/6 <= thumb_coord[1] <= h/2:
                            if len(array_l) == 0:
                                array_l.append('L2')
                            if array_l[-1] != 'L2':
                                array_l.append('L2')
                            if len(array_l) >= 2:
                                if array_l[-1] == 'L1' and array_l[-2] == 'L2' and len(array_l) != length_l:
                                    print('Leftmost_layer_down')
                                    pg.click(221*g,632*i)
                                    length_l = len(array_l)
                                if array_l[-1] == 'L2' and array_l[-2] == 'L1' and len(array_l) != length_l:
                                    print('Leftmost_layer_up')
                                    pg.click(252*g,632*i)
                                    length_l= len(array_l)
                        elif thumb_coord[0] > w/2 or thumb_coord[0] < w/6  or thumb_coord[1] < h/6 or thumb_coord[1] > 5*h/6 or index_coord[0] > w/2 or index_coord[0] < w/6 or index_coord[1] < h/6 or index_coord[1] > 5*h/6:
                            array_l = []


                    #Topmost Layer
                        if  w/2 <= thumb_coord[0] <= 5*w/6 and h/6 <= thumb_coord[1] <= h/2 and w/6 <= index_coord[0] <= w/2 and h/6 <= index_coord[1] <= h/2:
                            if len(array_u) == 0:
                                array_u.append('U1')
                            if array_u[-1] != 'U1':
                                array_u.append('U1')
                            if len(array_u) >= 2:
                                if array_u[-1] == 'U1' and array_u[-2] == 'U2' and len(array_u) != length_u:
                                    print('Topmost_layer_right')
                                    pg.click(323*g,632*i)
                                    length_u = len(array_u)
                                if array_u[-1] == 'U2' and array_u[-2] == 'U1' and len(array_u) != length_u:
                                    print('Tompost_layer_left')
                                    pg.click(291*g,632*i)
                                    length_u = len(array_u)
                        elif  w/2 <= index_coord[0] <= 5*w/6 and h/6 <= index_coord[1] <= h/2 and w/6 <= thumb_coord[0] <= w/2 and h/6 <= thumb_coord[1] <= h/2:
                            if len(array_u) == 0:
                                array_u.append('U2')
                            if array_u[-1] != 'U2':
                                array_u.append('U2')
                            if len(array_u) >= 2:
                                if array_u[-1] == 'U1' and array_u[-2] == 'U2' and len(array_u) != length_u:
                                    print('Topmost_layer_right')
                                    pg.click(323*g,632*i)
                                    length_u= len(array_u)
                                if array_u[-1] == 'U2' and array_u[-2] == 'U1' and len(array_u) != length_u:
                                    print('Topmost_layer_left')
                                    pg.click(291*g,632*i)
                                    length_u = len(array_u)
                        elif thumb_coord[0] > 5*w/6 or thumb_coord[0] < w/6  or thumb_coord[1] < h/6 or thumb_coord[1] > h/2 or index_coord[0] > 5*w/6 or index_coord[0] < w/6 or index_coord[1] < h/6 or index_coord[1] > h/2:
                            array_u = []
                    #Bottommost Layer
                        if  w/6 <= thumb_coord[0] <= w/2 and h/2 <= thumb_coord[1] <= 5*h/6 and w/2 <= index_coord[0] <= 5*w/6 and h/2 <= index_coord[1] <= 5*h/6:
                            if len(array_d) == 0:
                                array_d.append('L1')
                            if array_d[-1] != 'L1':
                                array_d.append('L1')
                            if len(array_d) >= 2:
                                if array_d[-1] == 'L1' and array_d[-2] == 'R1' and len(array_d) != length_d:
                                    print('Bottommost_layer_left')
                                    pg.click(387*g,632*i)
                                    length_d = len(array_d)
                                if array_d[-1] == 'R1' and array_d[-2] == 'L1' and len(array_d) != length_d:
                                    print('Bottommost_layer_right')
                                    pg.click(360*g,i*632)
                                    length_d = len(array_d)
                        elif  w/6 <= index_coord[0] <= w/2 and h/2 <= index_coord[1] <= 5*h/6 and w/2 <= thumb_coord[0] <= 5*w/6 and h/2 <= thumb_coord[1] <= 5*h/6:
                            if len(array_d) == 0:
                                array_d.append('R1')
                            if array_d[-1] != 'R1':
                                array_d.append('R1')
                            if len(array_d) >= 2:
                                if array_d[-1] == 'L1' and array_d[-2] == 'R1' and len(array_d) != length_d:
                                    print('Bottommost_layer_left')
                                    pg.click(387*g,i*632)
                                    length_d = len(array_d)
                                if array_d[-1] == 'R1' and array_d[-2] == 'L1' and len(array_d) != length_d:
                                    print('Bottommost_layer_right')
                                    pg.click(360*g,i*632)
                                    length_d = len(array_d)
                        elif thumb_coord[0] > 5*w/6 or thumb_coord[0] < w/6  or thumb_coord[1] < h/6 or thumb_coord[1] > h/2 or index_coord[0] > 5*w/6 or index_coord[0] < w/6 or index_coord[1] < h/6 or index_coord[1] > h/2:
                            array_d = []
                        # WHole Cube
                        if np.sqrt((thumb_coord[0] - index_coord[0])**2 + (thumb_coord[1] - index_coord[1])**2 ) <=  20:
                       
                            if w/2 <= thumb_coord[0] <= 5*w/6 and h/6 <= thumb_coord[1] <= 5*h/6 :
                           
                                if len(array_w_l) == 0:
                                    array_w_l.append('R')
                               
                                if array_w_l[-1] != 'R':
                                    array_w_l.append('R')
                               
                                if len(array_w_l) >= 2:
                                    if array_w_l[-1] == 'L' and array_w_l[-2] == 'R' and len(array_w_l) != length_w_l:
                                        print('Whole_cube_left')
                                        length_w_l = len(array_w_l)
                                    if array_w_l[-1] == 'R' and array_w_l[-2] == 'L' and len(array_w_l) != length_w_l:
                                        print('Whole_cube_right')
                                        length_w_l = len(array_w_l)
                            elif w/6 <= thumb_coord[0] <= w/2 and h/6 <= thumb_coord[1] <= 5*h/6 :
                                if len(array_w_l) == 0:
                                    array_w_l.append('L')
                               
                                if array_w_l[-1] != 'L':
                                    array_w_l.append('L')
                               
                                if len(array_w_l) >= 2:
                                    if array_w_l[-1] == 'L' and array_w_l[-2] == 'R' and len(array_w_l) != length_w_l:
                                        print('Whole_cube_left')
                                        length_w_l = len(array_w_l)
                                    if array_w_l[-1] == 'R' and array_w_l[-2] == 'L' and len(array_w_l) != length_w_l:
                                        print('Whole_cube_right')
                                        length_w_l = len(array_w_l)
                                elif thumb_coord[0] > 5*w/6 or thumb_coord[0] < w/6  or thumb_coord[1] < h/6 or thumb_coord[1] > 5*h/6:
                                    array_w_l=[]
                           
                               
                               
                                               

                       

                       

        cv2.imshow('Video',Frame)
        if cv2.waitKey(10) == ord(' '):  
            break
    cv2.destroyAllWindows()
cube = Rubic_Cube()
Thread(target = open_tracking).start()
cube.start()
