import os
import cv2

path = "Images"
images = []

for file in os.listdir(path):
    name,ext = os.path.splitext(file)
    if ext in ['.gif','.png','.jpg','.jpeg','jfif']:
        file_name = path+"/"+file
        print(file_name)
        images.append(file_name)

print(len(images))
frame = cv2.imread(images[0])
width,height,channels = frame.shape
size = (width,height)
print(size)

save = cv2.VideoWriter("video.mp4",cv2.VideoWriter_fourcc(*'DIVX'),30,size)
for i in range(0,10):
    frame = cv2.imread(images[i])
    cv2.imshow("Video",frame)
    if cv2.waitKey(50) == 32:
        break
    save.write(frame)

save.release()
print("Done!")