import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#FFE17B"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = NONE
# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text ="00:00")
    timerlabel .config(text="timer")
    check.config(text=" ")
    global reps
    reps =1
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    work_time = WORK_MIN
    short_break_time = SHORT_BREAK_MIN
    long_break_time =LONG_BREAK_MIN
    if reps == 1 or reps == 3 or reps == 5:
        timerlabel.config(text= "Work")
        count_down(work_time*60)
    elif reps == 2 or reps == 4 or reps == 6:
        timerlabel.config(text= "Break")
        count_down(short_break_time*60)
    else:
        timerlabel.config(text= "Long Break")
        count_down(long_break_time*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    global reps
    count_minutes = count //60
    count_sec = count % 60
    #checking a number and hanging the type of the variable
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text =f"{count_minutes}:{count_sec}")
    if count>0:
       timer = window.after(1000,count_down,count-1)
    if count_minutes == 0 and count_sec == f"0{0}":
        reps += 1
        mark =""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
        check.config(text= mark)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)



canvas = Canvas(width=200,height=224,bg =YELLOW,highlightthickness=0)
canvas.grid(column=1,row=1)
# Load the image using PhotoImage
photo = PhotoImage(file="tomato.png")

# Get the image width and height
image_width = photo.width()
image_height = photo.height()

# Calculate the x and y coordinates to center the image on the canvas
x = canvas.winfo_reqwidth() // 2
y = canvas.winfo_reqheight() // 2

# Create the image on the canvas with the calculated x and y coordinates
canvas.create_image(x, y, image=photo)
timer_text = canvas.create_text(x,130,text="00:00",fill="white",font = (FONT_NAME,35,"bold"))


timerlabel = Label(text =" Timer" ,font =(FONT_NAME,35,"bold"),fg = GREEN,bg=YELLOW)
timerlabel.grid(column=1 ,row= 0)

start_button = Button(text = "start",highlightthickness=0,command=start_timer)
start_button.grid(column=0 ,row= 3)

check= Label(text = " ",bg=YELLOW,fg = GREEN)
check.grid(column= 1,row= 3)

reset_button = Button(text = "reset",highlightthickness=0,command=reset)
reset_button.grid(column=3 ,row= 3)


window.mainloop()
