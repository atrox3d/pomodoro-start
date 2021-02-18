import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
#   https://colorhunt.co/
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
#   https://colorhunt.co/
CHECKMARK = "✔"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(
    padx=100,   # window border
    pady=50,    # window border
    bg=YELLOW   # window background color
)

#   timer label
timer_label = tkinter.Label(
    text="Timer",
    bg=YELLOW,
    fg=GREEN,
    font=(
        FONT_NAME,
        35,
        "bold"
    )
)
timer_label.pack()

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
canvas.create_text(
    100,                # text center x
    130,                # text center y
    text="00:00",       # text
    fill="white",       # text color fill
    font=(
            FONT_NAME,  # font name
            35,         # font size
            "bold"      # font weight
    )
)
canvas.pack()

#   start button
start_button = tkinter.Button(text="Start")
start_button.pack()

#   checkmark label
checkmark_label = tkinter.Label(
    text=CHECKMARK,
    bg=YELLOW,
    fg=GREEN,
    font=(
        FONT_NAME,
        35,
        "bold"
    )
)
checkmark_label.pack()

#   start button
reset_button = tkinter.Button(text="Reset")
reset_button.pack()

window.mainloop()
