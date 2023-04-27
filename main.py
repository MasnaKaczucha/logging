import logging
from tkinter import *
import csv
import tkinter


def f_validation(file_name):

    col1 = []
    col2 = []
    try:
        with open(file_name, 'r') as f:
            read_file = f.readlines()
            for row in read_file:
                x = row.split(",")
                col1.append(x[0])
                col2.append(x[1].strip('\n'))
    except FileNotFoundError as a:
        logging.fatal(a)
        label.config(text="file not found")

    for x, y in zip(col1, col2):
        try:
            z = int(x) / int(y)
            logging.info(f"{x} / {y} = {z}")

        except ZeroDivisionError:
            logging.error("You can't divide with 0")
            label.config(text="division by 0")

        except Exception as e:
            logging.error(e)
            label.config(text="error")
        else:
            print("no errors")
            label.config(text="no errors")

# logging.basicConfig(filename=f"{time.time()}.log", filemode="a")
# the least 10 (debug msg), highest 50 (fatal error msg)
# displays messages from the given level and up


fmt = "%(asctime)s :: %(levelname)-8s :: %(message)s"
logging.basicConfig(format=fmt, level=10)

root = Tk()
root.geometry('500x500')
f_label = Label(root, text="File Name:")
f_label.pack()
f_info = StringVar()
f_name = Entry(root, textvariable=f_info)
f_name.pack()
label = Label(root)
label.pack()
Button(root, text="import", command=lambda: f_validation(f_name.get())).pack()
root.mainloop()
# backwards compatibility

