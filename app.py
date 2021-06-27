import tkinter as tk
import tkinter.font as fnt
from tkinter import END
from scrapers import linkedIn_scraper
from tkinter.scrolledtext import ScrolledText
import time



def get_jobs(job, loc):
    lower_label.insert(END, '\tParsing jobs\n\n')
    main_url = linkedIn_scraper.get_exact_link(job, loc)
    lower_label.insert(END, 'The website being parsed is ' + str(main_url)+ '\n')
    lower_label.insert(END, '\nGetting links from the website')
    links = linkedIn_scraper.get_links(main_url)
    lower_label.insert(END,'\ndone')

HEIGHT = 500
WIDTH = 800

root = tk.Tk()
root.title("Job Parsing Portal")

canvas = tk.Canvas(root, height = HEIGHT, width= WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='bg-image.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

label = tk.Label(root, text = "Scrape job Postings", bg = '#f2fcbd', font = fnt.Font(size = 25))
label.place(relx=0.5, rely=0.025,  relheight= 0.15, relwidth=0.30, anchor='n')

frame = tk.Frame(root, bg = '#b0d9b3', bd=5)
frame.place(relx = 0.5, rely = 0.2, relwidth=0.75, relheight= 0.3, anchor='n')

entry = tk.Entry(frame, bg = '#fcffeb', font = fnt.Font(size = 20), bd=2)
entry.place(relx = 0.025, rely = 0.05, relwidth=0.65, relheight=0.4)

entry2 = tk.Entry(frame, bg = '#fcffeb', font = fnt.Font(size = 20), bd=2)
entry2.place(relx = 0.025, rely = 0.55, relwidth= 0.65, relheight= 0.4)

button = tk.Button(frame, text = "Find Jobs", fg ='#3bb1cc', font = fnt.Font(size = 22), command = lambda: get_jobs(entry.get(),entry2.get()))
button.place(relx = 0.7, rely = 0.25, relheight=0.45, relwidth = 0.27)

lower_frame = tk.Frame(root, bg = '#b0d9b3', bd = 10)
lower_frame.place(relx = 0.5, rely = 0.55, relheight=0.35, relwidth= 0.75, anchor='n')

lower_label = ScrolledText(lower_frame, bg = '#fcffeb', wrap=tk.CHAR, font = fnt.Font(size = 17))
lower_label.place(relx = 0.5, rely = 0.02, relwidth= 0.95, relheight= 0.95, anchor ='n')

root.mainloop()
