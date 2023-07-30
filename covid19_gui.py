#!/usr/bin/env python
# coding: utf-8

import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
import customtkinter

from PIL import ImageTk, Image  
from IPython import get_ipython

import tensorflow as tf
import numpy as np

customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Covid-19 Prediction")
        self.geometry(f"{580}x{600}")

        def prediction(img_path):
            img = tf.keras.utils.load_img(img_path, target_size=(224, 224))
            img = tf.keras.utils.img_to_array(img)
            img = np.expand_dims(img,axis=0)
            results = model.predict(img)
            return results

        def open_file():
            image_path = filedialog.askopenfilename(initialdir="/", title="Choose an image",
                                                filetypes=(("all files", "*.*"), ("png files", "*.png")))
            if not image_path:
                return
        
            im = Image.open(image_path)
            resized_image2 = im.resize((200,200))
            image2 = ImageTk.PhotoImage(resized_image2)
            lung_img.configure(image=image2)
            #lung_img.image = image2
            return image_path

        def final():
            path = open_file()
            results = prediction(path)
            #print(results)
            result_label.configure(text="")
            if results[0][0] == 0:
                result_label.configure(text='Positive For Covid-19')
            else:
                result_label.configure(text='Negative For Covid-19')
        
        get_ipython().run_line_magic('store', '-r  model')

        self.logo_image = customtkinter.CTkImage(Image.open("covidbg.png"), size=(240, 150))
        self.logo_image_label = customtkinter.CTkLabel(self, text="", image=self.logo_image)
        self.logo_image_label.pack(padx=20, pady=30)

        title_label = customtkinter.CTkLabel(self,text="Covid-19 Prediction using \n Chest X-Ray Images",
                            font=customtkinter.CTkFont(size=25, weight="bold"))
        title_label.pack(padx=20, pady=10)

        button1 = customtkinter.CTkButton(master=self, text = "Upload Chest X-Ray Image",
                                        font=customtkinter.CTkFont(size=15, weight="bold"),command=final)
        button1.pack(padx=20, pady=20)

        lung_img = customtkinter.CTkLabel(self, text="")
        lung_img.pack(padx=50, pady=25, side=tk.LEFT)

        result_label = customtkinter.CTkLabel(self,text="",
                            font=customtkinter.CTkFont(size=20, weight="bold"))
        result_label.pack(padx=50, pady=25, side=tk.LEFT)

if __name__ == "__main__":
    app = App()
    app.mainloop()