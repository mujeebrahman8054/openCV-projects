import cv2

vid=cv2.VideoCapture(0)
    
   
for i in range(0,1000):
    ret,frame=vid.read()
    cv2.imshow('frame',frame)
    print(i)
    cv2.imwrite(r"C:\Users\MUJEEB\Desktop\open\test1/"+str(i)+".jpg",frame)
    

    
vid.release()
cv2.destroyAllWindows()