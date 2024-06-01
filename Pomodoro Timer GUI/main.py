from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    if reps%8==0:
        label.config(text="Break", fg=RED)
        countdown(LONG_BREAK_MIN*60)
    
    elif reps%2==0:
        label.config(text="Break", fg=RED)
        countdown(SHORT_BREAK_MIN*60)
    
    else:
        label.config(text="Work")
        countdown(WORK_MIN*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    mins = math.floor(count/60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{mins}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            mark+="✓"
        check.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

check = Label(text="", bg=YELLOW, fg=GREEN)
check.grid(column=1, row=3)

label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
label.grid(column=1, row=0)


window.mainloop()