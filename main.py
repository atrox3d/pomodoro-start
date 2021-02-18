import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
#   https://colorhunt.co/
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
PINK = "#ffd880"
#   https://colorhunt.co/
CHECKMARK = "✔"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
MILLISECONDS = 1
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps

    if timer is not None:
        window.after_cancel(timer)

    canvas.itemconfig(
        timer_text,      # select canvas element to modify
        text="00:00"     # set property of element
    )

    title_label.config(
        text="Timer",
        fg=GREEN,
    )

    checkmark_label.config(text="")

    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1   # non-zero based!

    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:               # 8
        title_label.config(text="Break", fg=RED)
        count_down(long_break)
    elif reps % 2 == 0:             # 2, 4, 6
        title_label.config(text="Break", fg=PINK)
        count_down(short_break)
    else:                           # 1, 3, 7
        title_label.config(text="Work", fg=GREEN)
        count_down(work)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_mins = math.floor(count / 60)
    count_seconds = count % 60
    count_text = f"{count_mins:02d}:{count_seconds:02d}"
    # change pomodoro timer text
    canvas.itemconfig(
        timer_text,         # select canvas element to modify
        text=count_text     # set property of element
    )
    """if count <= 0 the function does not get registerd"""
    if count > 0:
        # register callback function to execute AFTER 1000 ms
        timer = window.after(
            MILLISECONDS,           # ms to wait for
            count_down,     # callback function (this function)
            count - 1,       # callback function parameter
        )
    else:
        start_timer()
        if reps % 2 == 0:
            marks = ""
            work_sessions = math.floor(reps/2)
            for _ in range(work_sessions):
                marks += CHECKMARK
            checkmark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(
    padx=100,   # window border
    pady=50,    # window border
    bg=YELLOW   # window background color
)

#   timer label
title_label = tkinter.Label(
    text="Timer",
    bg=YELLOW,
    fg=GREEN,
    font=(
        FONT_NAME,
        35,
        "bold"
    )
)
# timer_label.pack()
title_label.grid(row=0, column=1)

#   create image
photo = tkinter.PhotoImage(file="tomato.png")

#   create canvas
canvas = tkinter.Canvas(
    width=200,              # canvas width
    height=224,             # canvas height
    bg=YELLOW,              # canvas background color
    highlightthickness=0    # canvas border size (?)
)
#   add image
canvas.create_image(
    100,            # image center x
    112,            # image center y
    image=photo     # photo object
)
#   add text
timer_text = canvas.create_text(
    100,            # text center x
    130,            # text center y
    text="00:00",   # text
    fill="white",   # text color fill
    font=(
        FONT_NAME,  # font name
        35,         # font size
        "bold"      # font weight
    )
)
# canvas.pack()
canvas.grid(row=1, column=1)

#   start button
start_button = tkinter.Button(
    text="Start",           # button text
    highlightthickness=0,
    command=start_timer     # function to execute
)
# start_button.pack()
start_button.grid(row=2, column=0)

#   checkmark label
checkmark_label = tkinter.Label(
    # text=CHECKMARK,
    bg=YELLOW,
    fg=GREEN,
    font=(
        FONT_NAME,
        12,
        "bold"
    )
)
# checkmark_label.pack()
checkmark_label.grid(row=3, column=1)

#   start button
reset_button = tkinter.Button(
    text="Reset",
    highlightthickness=0,
    command=reset_timer)
# reset_button.pack()
reset_button.grid(row=2, column=2)

window.mainloop()
