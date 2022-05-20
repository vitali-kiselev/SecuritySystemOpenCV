import cv2
import numpy as np
import telebot

bot = telebot.TeleBot('5380173958:AAEd9prlHbDWI5tgrgSGFUVv_DK0OKAypzs')
chat_id = 478653567
face = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

cam = cv2.VideoCapture(0)
winName = "SecuritySystem"
cv2.namedWindow(winName,cv2.WINDOW_NORMAL)
prev_frame = cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2GRAY)
current_frame  = cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2GRAY)
next_frame = cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2GRAY)

def diffImg(f0,f1,f2):
    d1 = cv2.absdiff(f2,f1)
    d2 = cv2.absdiff(f1,f0)
    res = cv2.bitwise_and(d1,d2)
    d3 = np.ravel(res)
    d4=np.count_nonzero(d3)
    return  d4,res

while True:
    frame = cam.read()[1]
    nzero,result = diffImg(prev_frame,current_frame,next_frame)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    faces = face.detectMultiScale(gray)

    if nzero > 12000 and not(np.sum(faces)==0):
        _ret,frame = cam.read()
        for(x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(frame,"GULIK",(30,40),3,1,(0,0,255))
        cv2.imshow('cam',frame)
        cv2.imwrite('1.png',frame)
        bot.send_message(chat_id, 'Moving')
        bot.send_photo(chat_id,open('1.png','rb'))
        nzero=0
    cv2.imshow(winName, result)
    prev_frame = current_frame
    current_frame = next_frame
    next_frame = cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2GRAY)

    key = cv2.waitKey(10)
    if key == 27:
        cv2.destroyWindow(winName)
        break