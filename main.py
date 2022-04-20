from tkinter import *
from tkinter import filedialog 
from PIL import Image, ImageTk
import cv2
import imutils
 

def visualizar():
    global cap
    ret, frame = cap.read() 
    if ret == True:
        frame = imutils.resize(frame, width=720)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        im = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=im)

        lbl_video.configure(image=img)
        lbl_video.image = img
        lbl_video.after(10, visualizar)

def elegirVideo():
    global cap
    video_path = filedialog.askopenfilename(filetypes= [
        ("all video format", ".mp4"),
        ("all video format", ".avi")])
    if len(video_path) > 0:
        lbl_info_video_path.configure(text=video_path)
        cap = cv2.VideoCapture(video_path)
        visualizar()
    else:
        lbl_info_video_path.configure(text="Aun no se ha seleccionado un video")



cap = None

root = Tk()

btn_visualizar_video = Button(root, text="Elegir y visualizar video", command=elegirVideo)
btn_visualizar_video.grid(column=0, row=0, padx=5, pady=5, columnspan= 3)

lbl_info_video = Label(root, text = "Video de entrada: ")
lbl_info_video.grid(column=0, row=1)

lbl_info_video_path = Label(root, text = "Aun no se ha seleccionado un video")
lbl_info_video_path.grid(column=1, row=1)



lbl_video = Label(root)
lbl_video.grid(column=0, row=2, columnspan=2)

"""
lbl_info_jugadores = Label(root, text = "A continuacion se muestran los jugadores")
lbl_info_jugadores.grid(column=0, row=3)

lbl_jugadores = Label(root)
lbl_jugadores.grid(column=0, row=4)
"""

root.mainloop()