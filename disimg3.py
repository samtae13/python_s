import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def disp_Photo(path):
    newImage = PIL.Image.open(path)
    gimage = PIL.Image.open(path).convert("L")
    mywidth = 300
    sizefac = mywidth / newImage.size[0]
    myheight = int(newImage.size[1] * sizefac)
    print(newImage.size)
    print(mywidth, myheight)
    newImage = newImage.resize((mywidth, myheight))

    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

    gimageData = PIL.ImageTk.PhotoImage(newImage.convert("L"))
    gimageLabel.configure(image=gimageData)
    gimageLabel.image = gimageData

def open_file():
    fpath = fd.askopenfilename()

    if fpath:
        disp_Photo(fpath)

root = tk.Tk()
root.geometry("400x600")

btn = tk.Button(text="open", command=open_file)
imageLabel = tk.Label()
gimageLabel = tk.Label()

btn.pack()
imageLabel.pack()
gimageLabel.pack()

tk.mainloop()