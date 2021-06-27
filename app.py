import tkinter as tk
import tkinter.font as fnt
from tkinter import END
from scrapers import for_both



def get_jobs( job, loc):
    lower_label.config(text = "Parsing Job Postings")
    return for_both.run(job, loc)

root = tk.Tk()
root.title("Job Parsing Portal")

canvas = tk.Canvas(root, height = 500, width= 800)
canvas.pack()

background_image = tk.PhotoImage(file='bg-image.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

label = tk.Label(root, text = "Scrape job Postings", fg = '#3bb1cc', font = fnt.Font(size = 25))
label.place(relx=0.5, rely=0.025,  relheight= 0.15, relwidth=0.30, anchor='n')

frame = tk.Frame(root, bg = '#b0d9b3', bd=5)
frame.place(relx = 0.5, rely = 0.2, relwidth=0.75, relheight= 0.3, anchor='n')

entry = tk.Entry(frame, bg = '#fcffeb', font = fnt.Font(size = 20), bd=2)
entry.place(relx = 0.025, rely = 0.05, relwidth=0.65, relheight=0.4)

entry2 = tk.Entry(frame, bg = '#fcffeb', font = fnt.Font(size = 20), bd=2)
entry2.place(relx = 0.025, rely = 0.55, relwidth= 0.65, relheight= 0.4)

button = tk.Button(frame, text = "Find Jobs", fg ='black', font = fnt.Font(size = 22), command = lambda: get_jobs(entry.get(),entry2.get()))
button.place(relx = 0.7, rely = 0.25, relheight=0.45, relwidth = 0.27)

lower_frame = tk.Frame(root, bg = '#b0d9b3', bd = 10)
lower_frame.place(relx = 0.5, rely = 0.55, relheight=0.35, relwidth= 0.75, anchor='n')

lower_label = tk.Label(lower_frame, bg = '#fcffeb', font = fnt.Font(size = 17), justify="center")
lower_label.place(relx = 0.5, rely = 0.02, relwidth= 0.95, relheight= 0.95, anchor ='n')


root.mainloop()
