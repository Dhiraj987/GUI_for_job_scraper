import tkinter as tk

HEIGHT = 500
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width= WIDTH)
canvas.pack()

label = tk.Label(root, text = "Scrape job Postings", bg = 'white')
label.place(relx=0.5, rely=0.05,  relheight= 0.1, relwidth=0.25, anchor='n')

frame = tk.Frame(root, bg = '#80c1ff', bd=5)
frame.place(relx = 0.5, rely = 0.2, relwidth=0.75, relheight= 0.3, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(rely = 0.05, relwidth=0.65, relheight=0.4)

entry2 = tk.Entry(frame, font = 40)
entry2.place(rely = 0.55, relwidth= 0.65, relheight= 0.4)

button = tk.Button(frame, text = "Test Button", font = 40)
button.place(relx = 0.68, rely = 0.25, relheight=0.5, relwidth = 0.3)

lower_frame = tk.Frame(root, bg = '#80c1ff', bd = 10)
lower_frame.place(relx = 0.5, rely = 0.55, relheight=0.35, relwidth= 0.75, anchor='n')

lower_label = tk.Label(lower_frame)
lower_label.place(relx = 0.5, rely = 0.02, relwidth= 0.95, relheight= 0.95, anchor ='n')

root.mainloop()