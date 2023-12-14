from tkinter import *
from tkinter import messagebox
import subprocess


from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"forms\adoption2_frame")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def back_button_clicked():
    window.destroy()
    subprocess.Popen(["python", "adoptframe1.py"])
def next_button_clicked():
    window.destroy()
    subprocess.Popen(["python", "adoptframe3.py"])

def close_window():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        window.destroy()

# def var1():
#     ()

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

# ------------------------- questionnaire title ------------------------- #
image_image_21 = PhotoImage(
    file=relative_to_assets("image_21.png"))
image_21 = canvas.create_image(
    126.0,
    47.0,
    image=image_image_21
)

# ------------------------- first question ------------------------- #
image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    76.0,
    82.0,
    image=image_image_14
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    108.0,
    124.0,
    image=image_image_15
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    200.0,
    122.0,
    image=image_image_17
)

image_image_19 = PhotoImage(
    file=relative_to_assets("image_19.png"))
image_19 = canvas.create_image(
    299.0,
    122.0,
    image=image_image_19
)

# ------------------------- second question ------------------------- #
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    197.0,
    161.0,
    image=image_image_1
)


image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    114.0,
    196.0,
    image=image_image_3
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    233.0,
    196.0,
    image=image_image_5
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    359.0,
    196.0,
    image=image_image_7
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    481.0,
    198.0,
    image=image_image_9
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    603.0,
    196.0,
    image=image_image_11
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    711.0,
    196.0,
    image=image_image_13
)

# ------------------------- third question ------------------------- #
image_image_22 = PhotoImage(
    file=relative_to_assets("image_22.png"))
image_22 = canvas.create_image(
    182.0,
    237.0,
    image=image_image_22
)

image_image_24 = PhotoImage(
    file=relative_to_assets("image_24.png"))
image_24 = canvas.create_image(
    123.0,
    273.0,
    image=image_image_24
)

image_image_26 = PhotoImage(
    file=relative_to_assets("image_26.png"))
image_26 = canvas.create_image(
    226.0,
    273.0,
    image=image_image_26
)

image_image_28 = PhotoImage(
    file=relative_to_assets("image_28.png"))
image_28 = canvas.create_image(
    327.0,
    273.0,
    image=image_image_28
)

image_image_30 = PhotoImage(
    file=relative_to_assets("image_30.png"))
image_30 = canvas.create_image(
    451.0,
    273.0,
    image=image_image_30
)

# ------------------------- fourth question ------------------------- #
image_image_31 = PhotoImage(
    file=relative_to_assets("image_31.png"))
image_31 = canvas.create_image(
    614.0,
    237.0,
    image=image_image_31
)

image_image_33 = PhotoImage(
    file=relative_to_assets("image_33.png"))
image_33 = canvas.create_image(
    615.0,
    273.0,
    image=image_image_33
)

image_image_35 = PhotoImage(
    file=relative_to_assets("image_35.png"))
image_35 = canvas.create_image(
    723.0,
    273.0,
    image=image_image_35
)

# ------------------------- fifth question ------------------------- #
image_image_36 = PhotoImage(
    file=relative_to_assets("image_36.png"))
image_36 = canvas.create_image(
    132.0,
    321.0,
    image=image_image_36
)

image_image_38 = PhotoImage(
    file=relative_to_assets("image_38.png"))
image_38 = canvas.create_image(
    124.0,
    358.0,
    image=image_image_38
)

image_image_40 = PhotoImage(
    file=relative_to_assets("image_40.png"))
image_40 = canvas.create_image(
    228.0,
    358.0,
    image=image_image_40
)

image_image_42 = PhotoImage(
    file=relative_to_assets("image_42.png"))
image_42 = canvas.create_image(
    337.0,
    357.0,
    image=image_image_42
)

image_image_44 = PhotoImage(
    file=relative_to_assets("image_44.png"))
image_44 = canvas.create_image(
    456.0,
    357.0,
    image=image_image_44
)

image_image_46 = PhotoImage(
    file=relative_to_assets("image_46.png"))
image_46 = canvas.create_image(
    602.0,
    357.0,
    image=image_image_46
)

# ------------------------- sixth question ------------------------- #
image_image_51 = PhotoImage(
    file=relative_to_assets("image_51.png"))
image_51 = canvas.create_image(
    117.0,
    399.0,
    image=image_image_51
)

image_image_48 = PhotoImage(
    file=relative_to_assets("image_48.png"))
image_48 = canvas.create_image(
    146.0,
    438.0,
    image=image_image_48
)

image_image_50 = PhotoImage(
    file=relative_to_assets("image_50.png"))
image_50 = canvas.create_image(
    325.0,
    438.0,
    image=image_image_50
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


# ------------------------- RADIO BUTTONS ------------------------- #
# STATUS
q1 = IntVar()

single_radio = Radiobutton(
    variable=q1,
    value=1,
    bg="#FFFFFF",
    activebackground="#FFFFFF", 
)
single_radio.place(
    x=54,
    y=111
)

married_radio = Radiobutton(
    variable=q1,
    value=2,
    bg="#FFFFFF",
    activebackground="#FFFFFF",
)
married_radio.place(
    x=141,
    y=111
)

others_radio = Radiobutton(
    variable=q1,
    value=3,
    bg="#FFFFFF",
    activebackground="#FFFFFF",  
)
others_radio.place(
    x=245,
    y=111
)

# What prompted you to adopt from PAWS?
q2 = IntVar()

friends_radio = Radiobutton(
    variable=q2,
    value=1,
    bg="#FFFFFF",
    activebackground="#FFFFFF",  
)
friends_radio.place(
    x=54,
    y=185
)

website_radio = Radiobutton(
    variable=q2,
    value=2,
    bg="#FFFFFF",
    activebackground="#FFFFFF",  
)
website_radio.place(
    x=173,
    y=185
)

social_radio = Radiobutton(
    variable=q2,
    value=3,
    bg="#FFFFFF",
    activebackground="#FFFFFF",  
)
social_radio.place(
    x=284,
    y=185
)

family_radio = Radiobutton(
    variable=q2,
    value=4,
    bg="#FFFFFF",
    activebackground="#FFFFFF",  
)
family_radio.place(
    x=427,
    y=185
)

partner_radio = Radiobutton(
    variable=q2,
    value=5,
    bg="#FFFFFF",
    activebackground="#FFFFFF",  
)
partner_radio.place(
    x=545,
    y=185
)

others2_radio = Radiobutton(
    variable=q2,
    value=6,
    bg="#FFFFFF",
    activebackground="#FFFFFF",  
)
others2_radio.place(
    x=656,
    y=185
)

# What type of building do you live in?
q3 = IntVar()

apartment_radio = Radiobutton(
    variable=q3,
    value=1,
    bg="#FFFFFF",
    activebackground="#FFFFFF",  
)
apartment_radio.place(
    x=54,
    y=262
)

house_radio = Radiobutton(
    variable=q3,
    value=2,
    bg="#FFFFFF",
    activebackground="#FFFFFF",  
)
house_radio.place(
    x=172,
    y=262
)

condo_radio = Radiobutton(
    variable=q3,
    value=3,
    bg="#FFFFFF",
    activebackground="#FFFFFF",  
)
condo_radio.place(
    x=272,
    y=262
)

others3_radio = Radiobutton(
    variable=q3,
    value=4,
    bg="#FFFFFF",
    activebackground="#FFFFFF",  
)
others3_radio.place(
    x=396,
    y=262
)
# Do you rent?
q4 = IntVar()
yes_radio = Radiobutton(
    variable=q4,
    value=1,
    bg="#FFFFFF",
    activebackground="#FFFFFF",  
)
yes_radio.place(
    x=570,
    y=262
)
no_radio = Radiobutton(
    variable=q4,
    value=2,
    bg="#FFFFFF",
    activebackground="#FFFFFF",  
)
no_radio.place(
    x=681,
    y=262
)
#Who do you live with?
q5 = IntVar()
living_radio = Radiobutton(
    variable=q5,
    value=1,
    bg="#FFFFFF",
    activebackground="#FFFFFF",  
)
living_radio.place(
    x=54,
    y=346
)
spouse_radio = Radiobutton(
    variable=q5,
    value=2,
    bg="#FFFFFF",
    activebackground="#FFFFFF",  
)
spouse_radio.place(
    x=173,
    y=346
)
relatives_radio = Radiobutton(
    variable=q5,
    value=3,
    bg="#FFFFFF",
    activebackground="#FFFFFF",  
)
relatives_radio.place(
    x=273,
    y=346
)
parents_radio = Radiobutton(
    variable=q5,
    value=4,
    bg="#FFFFFF",
    activebackground="#FFFFFF",  
)
parents_radio.place(
    x=397,
    y=346
)
roommate_radio = Radiobutton(
    variable=q5,
    value=5,
    bg="#FFFFFF",
    activebackground="#FFFFFF",  
)
roommate_radio.place(
    x=525,
    y=346
)
# How old are they?
q6 = IntVar()

below_radio = Radiobutton(
    variable=q6,
    value=1,
    bg="#FFFFFF",
    activebackground="#FFFFFF",  
)
below_radio.place(
    x=54,
    y=427
)
over_radio = Radiobutton(
    variable=q6,
    value=2,
    bg="#FFFFFF",
    activebackground="#FFFFFF",  
)
over_radio.place(
    x=237,
    y=427
)

window.resizable(False, False)
window.mainloop()


