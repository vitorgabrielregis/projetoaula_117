import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frame = cv2.imread(images[0])
#altura, largura e canais
height, width, channels = frame.shape
#tamanho da imagem (tupla)
size = (width,height)

out = cv2.VideoWriter('project1.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 27, size)

#criando por do sol
#for i in range(0,count-1):

#criando nascer do sol
for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    out.write(frame)

out.release() #liberando o vídeo gerado
print("Concluido")