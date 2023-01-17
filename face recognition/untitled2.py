import cv2
for i in range(0,1000):
    im=cv2.imread(r"C:\Users\MUJEEB\Desktop\open\test1/"+str(i)+".jpg",1)
    imresize=cv2.resize(im,(200,200))#,interpolation=cv2.INTER_NEAREST)
    cv2.imwrite(r"C:\Users\MUJEEB\Desktop\open\test1/"+str(i)+".jpg",imresize)