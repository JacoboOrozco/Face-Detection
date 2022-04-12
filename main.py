from tkinter import *
import tkinter
from tkinter import filedialog 
from PIL import Image, ImageTk
import cv2
import imutils
 
def labelsLayout(root):
    lbl_info_video = Label(root, text = "Video de entrada: ")
    lbl_info_video.grid(column=0, row=1)

def buttonLayout(root):
    btn_visualizar_video = Button(root, text="Elegir y visualizar video")
    btn_visualizar_video.grid(column=0, row=0, padx=5, pady=5)
    labelsLayout(root)

def main():
    root = Tk()
    buttonLayout(root)
    root.mainloop()


if __name__ == "__main__":
    main()

print("Code Completed")