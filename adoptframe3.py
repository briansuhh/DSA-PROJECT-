from tkinter import *
from tkinter import messagebox
import subprocess


from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\adoption3_frame")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def back_button_clicked():
    window.destroy()
    subprocess.Popen(["python", "adoptframe2.py"])
def next_button_clicked():
    if save_input():
        window.destroy()
        subprocess.Popen(["python", "adoptframe4.py"])

def close_window():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        window.destroy()

def save_input():
    if not all([q7.get(), question1_textbox.get(), question2_textbox.get(), question3_textbox.get()]):
        messagebox.showerror("Error", "Please fill up all fields.")
        return False
    else:
        messagebox.showinfo("Success", "Please proceed to the next set of questions.")
        q7input = q7.get()
        inputs = [question1_textbox.get(), question2_textbox.get(), question3_textbox.get()]
        with open("data/adopt3_data.txt", "w") as f:
            f.write(q7input + '\n')
            f.write('\n'.join(inputs) + '\n')
        
        return True
        

def read_input():
    # read the inputted data from the file and display it
    try:
        with open("data/adopt3_data.txt", "r") as f:
            q7.set(f.readline().strip())
            question1_textbox.insert(0, f.readline().strip())
            question2_textbox.insert(0, f.readline().strip())
            question3_textbox.insert(0, f.readline().strip())
    except FileNotFoundError:
        with open("data/adopt3_data.txt", "w") as f:
            pass

    

window = Tk()

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the protocol for the window close event
window.protocol("WM_DELETE_WINDOW", close_window)

# Calculate the x and y coordinates for the window to be centered
x = (screen_width - 820) // 2
y = (screen_height - 500) // 2

window.geometry(f"820x500+{x}+{y}")
window.configure(bg="#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 500,
    width = 820,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    225.0,
    128.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    394.0,
    171.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    394.0,
    264.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    394.0,
    366.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    253.0,
    53.0,
    image=image_image_5
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    100.0,
    90.0,
    image=image_image_7
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    215.0,
    90.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    341.0,
    221.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    341.0,
    323.0,
    image=image_image_11
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
back_button = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=back_button_clicked,
    relief="flat"
)
back_button.place(
    x=535.0,
    y=407.0,
    width=112.89242553710938,
    height=39.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
next_button = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=next_button_clicked,
    relief="flat"
)
next_button.place(
    x=657.0,
    y=407.0,
    width=112.89242553710938,
    height=39.0
)
question1_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
question1_textbox.place(
    x=62.0,
    y=157.0,
    width=665.0,
    height=31.0
)
question2_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
question2_textbox.place(
    x=62.0,
    y=249.0,
    width=665.0,
    height=31.0
)
question3_textbox = Entry(
    font=("Inter", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
question3_textbox.place(
    x=62.0,
    y=351.0,
    width=665.0,
    height=31.0
)

# Are any members of your household allergic to animals? 
q7 = StringVar()

dot_image = PhotoImage(file=relative_to_assets("dot.png"))
black_dot_image = PhotoImage(file=relative_to_assets("black_dot.png"))
black_dot_small_image = PhotoImage(file=relative_to_assets("black_dot_small.png"))
pink_dot_image = PhotoImage(file=relative_to_assets("pink_dot.png"))
yes2_radio = Radiobutton(
    variable=q7,
    value='yes',
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    bd=0,
    indicatoron=False,
    image=dot_image,
    selectimage=pink_dot_image,
)
yes2_radio.place(
    x=55,
    y=79
)
no2_radio = Radiobutton(
    variable=q7,
    value='no',
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    bd=0,
    indicatoron=False,
    image=dot_image,
    selectimage=pink_dot_image,
)
no2_radio.place(
    x=173,
    y=79
)

read_input()

window.resizable(False, False)
window.mainloop()
