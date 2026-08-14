import tkinter as tk
import random
import math
import os

WIDTH = 430
HEIGHT = 760

HER_NAME = "Sneha Thorat"
YOUR_NAME = "Sandeep Gupta"
PASSWORD = "143"

PHOTO_1 = "photo1.png"
PHOTO_2 = "photo2.png"
PHOTO_3 = "photo3.png"

BG = "#080309"
CARD = "#180a13"
BORDER = "#563343"
WHITE = "#fff8fb"
SOFT = "#cdb6c1"
GREY = "#907985"
PINK = "#e84f67"
LIGHT_PINK = "#ff8295"
DARK_PINK = "#762638"

root = tk.Tk()
root.title("A Little Chapter Of Us ❤️")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)
root.configure(bg=BG)

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg=BG,
    highlightthickness=0
)
canvas.pack()

widgets = []
particles = []
floating_hearts = []
loaded_images = {}


def load_image(path):
    if not os.path.exists(path):
        return None

    try:
        return tk.PhotoImage(file=path)
    except:
        return None


for image_name in [PHOTO_1, PHOTO_2, PHOTO_3]:
    loaded_images[image_name] = load_image(image_name)


for _ in range(80):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)

    item = canvas.create_oval(
        x,
        y,
        x + 2,
        y + 2,
        fill=random.choice([
            "#ffffff",
            "#6e3144",
            "#8e3e53",
            "#ff7186"
        ]),
        outline=""
    )

    particles.append({
        "item": item,
        "x": x,
        "y": y,
        "speed": random.uniform(.08, .35)
    })


def animate_particles():
    for particle in particles:
        particle["y"] -= particle["speed"]

        if particle["y"] < 0:
            particle["y"] = HEIGHT
            particle["x"] = random.randint(0, WIDTH)

        canvas.coords(
            particle["item"],
            particle["x"],
            particle["y"],
            particle["x"] + 2,
            particle["y"] + 2
        )

    root.after(30, animate_particles)


def create_heart():
    x = random.randint(15, WIDTH - 15)
    y = HEIGHT + 20

    size = random.randint(10, 22)

    item = canvas.create_text(
        x,
        y,
        text="♥",
        fill=random.choice([
            PINK,
            LIGHT_PINK,
            "#ff9aaa"
        ]),
        font=("Arial", size, "bold")
    )

    floating_hearts.append({
        "item": item,
        "x": x,
        "y": y,
        "speed": random.uniform(.6, 1.6),
        "drift": random.uniform(-.4, .4)
    })


def animate_hearts():
    if random.random() < .04:
        create_heart()

    for heart in floating_hearts[:]:
        heart["y"] -= heart["speed"]
        heart["x"] += heart["drift"]

        canvas.coords(
            heart["item"],
            heart["x"],
            heart["y"]
        )

        if heart["y"] < -30:
            canvas.delete(heart["item"])
            floating_hearts.remove(heart)

    root.after(30, animate_hearts)


def clear_page():
    canvas.delete("page")

    for widget in widgets:
        widget.destroy()

    widgets.clear()


def text(
    x,
    y,
    value,
    size,
    color=WHITE,
    family="Georgia",
    weight="normal"
):
    return canvas.create_text(
        x,
        y,
        text=value,
        fill=color,
        font=(family, size, weight),
        justify="center",
        tags="page"
    )


def glow_text(x, y, value, size):
    canvas.create_text(
        x + 5,
        y + 5,
        text=value,
        fill="#350b18",
        font=("Georgia", size + 5, "bold"),
        tags="page"
    )

    canvas.create_text(
        x + 2,
        y + 2,
        text=value,
        fill="#702236",
        font=("Georgia", size + 2, "bold"),
        tags="page"
    )

    canvas.create_text(
        x,
        y,
        text=value,
        fill=WHITE,
        font=("Georgia", size, "bold"),
        tags="page"
    )


def progress(active):
    for i in range(8):
        color = PINK if i < active else "#5a3544"

        text(
            205 + i * 25 - 85,
            30,
            "♡",
            17,
            color,
            "Arial"
        )


def card(x1, y1, x2, y2):
    canvas.create_rectangle(
        x1 + 3,
        y1 + 5,
        x2 + 3,
        y2 + 5,
        fill="#040204",
        outline="",
        tags="page"
    )

    canvas.create_rectangle(
        x1,
        y1,
        x2,
        y2,
        fill=CARD,
        outline=BORDER,
        width=1,
        tags="page"
    )


def button(title, command, y, width=220):
    b = tk.Button(
        root,
        text=title,
        command=command,
        bg=PINK,
        fg=WHITE,
        activebackground=LIGHT_PINK,
        activeforeground=WHITE,
        font=("Arial", 11, "bold"),
        relief="flat",
        bd=0,
        cursor="hand2"
    )

    b.place(
        x=(WIDTH - width) // 2,
        y=y,
        width=width,
        height=44
    )

    widgets.append(b)


def footer():
    text(
        28,
        675,
        "◎",
        26,
        WHITE,
        "Arial"
    )

    text(
        28,
        704,
        "@BHOPALIMITRA",
        9,
        WHITE,
        "Arial",
        "bold"
    )

    text(
        WIDTH // 2,
        735,
        '👇 Comment "143" & DM me source Code bhai dunga. 🚀',
        8,
        "#d7a3b2",
        "Arial"
    )


def photo_card(filename, y=120):
    card(
        35,
        y,
        WIDTH - 35,
        y + 320
    )

    image = loaded_images.get(filename)

    if image:
        canvas.create_image(
            WIDTH // 2,
            y + 160,
            image=image,
            tags="page"
        )
    else:
        text(
            WIDTH // 2,
            y + 125,
            "📷",
            42,
            PINK,
            "Arial"
        )

        text(
            WIDTH // 2,
            y + 180,
            "YOUR PHOTO",
            14,
            GREY,
            "Arial",
            "bold"
        )

        text(
            WIDTH // 2,
            y + 210,
            filename,
            10,
            GREY,
            "Arial"
        )


def opening():
    clear_page()

    # text(
    #     WIDTH // 2,
    #     105,
    #     "PoV :- Normal Proposal To",
    #     23,
    #     WHITE,
    #     "Arial",
    #     "bold"
    # )

    # text(
    #     WIDTH // 2,
    #     145,
    #     "Sab Karte Ho Tum Developer",
    #     23,
    #     WHITE,
    #     "Arial",
    #     "bold"
    # )

    # text(
    #     WIDTH // 2,
    #     185,
    #     "Ho Kya Alag Karoge...👨‍💻👩‍💻",
    #     23,
    #     WHITE,
    #     "Arial",
    #     "bold"
    # )

    canvas.create_line(
        30,
        225,
        WIDTH - 30,
        225,
        fill="#482534",
        tags="page"
    )

    text(
        WIDTH // 2,
        300,
        "❤️",
        55,
        PINK,
        "Arial"
    )

    text(
        WIDTH // 2,
        370,
        "Wait...",
        18,
        SOFT
    )

    text(
        WIDTH // 2,
        410,
        "This one is different.",
        22,
        WHITE,
        "Georgia",
        "bold"
    )

    text(
        WIDTH // 2,
        450,
        "For someone special ❤️",
        16,
        LIGHT_PINK
    )

    button(
        "Let's see... ❤️",
        password_page,
        520,
        220
    )

    footer()


def password_page():
    clear_page()

    text(
        WIDTH // 2,
        70,
        "🔐",
        42,
        WHITE,
        "Arial"
    )

    text(
        WIDTH // 2,
        105,
        "Before we begin...",
        14,
        GREY,
        "Georgia"
    )

    card(
        35,
        120,
        WIDTH - 35,
        400
    )

    glow_text(
        WIDTH // 2,
        185,
        "This little world is",
        27
    )

    glow_text(
        WIDTH // 2,
        225,
        "only for you ❤️",
        27
    )

    text(
        WIDTH // 2,
        270,
        "Enter the secret password",
        14,
        WHITE
    )

    entry = tk.Entry(
        root,
        bg="#1c1018",
        fg=WHITE,
        insertbackground=WHITE,
        font=("Arial", 17),
        justify="center",
        relief="flat",
        highlightthickness=1,
        highlightbackground="#634251",
        highlightcolor=PINK
    )

    entry.place(
        x=65,
        y=300,
        width=300,
        height=48
    )

    widgets.append(entry)

    def unlock():
        if entry.get() == PASSWORD:
            welcome()
        else:
            entry.delete(0, tk.END)
            entry.insert(0, "Wrong password")
            entry.config(fg=PINK)

            root.after(
                700,
                lambda: [
                    entry.delete(0, tk.END),
                    entry.config(fg=WHITE)
                ]
            )

    button(
        "Unlock ❤️",
        unlock,
        370,
        160
    )

    footer()


def welcome():
    clear_page()

    progress(0)

    text(
        WIDTH // 2,
        125,
        "Welcome, my favorite",
        25,
        WHITE,
        "Georgia",
        "bold"
    )

    text(
        WIDTH // 2,
        165,
        "person ❤️",
        25,
        PINK,
        "Georgia",
        "bold"
    )

    button(
        "Challenge Accepted 👨‍💻❤️",
        can_i_ask,
        535,
        260
    )

    footer()


def can_i_ask():
    clear_page()

    progress(1)

    text(
        WIDTH // 2,
        315,
        "Can I ask you",
        25,
        WHITE,
        "Georgia",
        "bold"
    )

    text(
        WIDTH // 2,
        350,
        "something?",
        25,
        WHITE,
        "Georgia",
        "bold"
    )

    button(
        "Yes, ask me 🥺",
        what_if,
        420,
        170
    )

    footer()


def what_if():
    clear_page()

    progress(2)

    card(
        30,
        330,
        WIDTH - 30,
        480
    )

    text(
        WIDTH // 2,
        365,
        "What if I told you... you're",
        17,
        WHITE,
        "Georgia",
        "bold"
    )

    text(
        WIDTH // 2,
        400,
        "one of my favourite reasons",
        17,
        WHITE,
        "Georgia",
        "bold"
    )

    text(
        WIDTH // 2,
        435,
        "to smile?",
        17,
        WHITE,
        "Georgia",
        "bold"
    )

    button(
        "Awww 🥺",
        first_question,
        500,
        150
    )

    button(
        "I already knew 😌",
        first_question,
        555,
        175
    )

    footer()


def first_question():
    clear_page()

    progress(3)

    card(
        30,
        380,
        WIDTH - 30,
        480
    )

    text(
        WIDTH // 2,
        420,
        "Do you remember the first",
        17,
        WHITE,
        "Georgia",
        "bold"
    )

    text(
        WIDTH // 2,
        450,
        "time we talked?",
        17,
        WHITE,
        "Georgia",
        "bold"
    )

    button(
        "❤️ Of course I do",
        second_question,
        510,
        170
    )

    button(
        "🥺 Maybe remind me...",
        second_question,
        565,
        190
    )

    footer()


def second_question():
    clear_page()

    progress(4)

    card(
        30,
        370,
        WIDTH - 30,
        485
    )

    text(
        WIDTH // 2,
        410,
        "If I could pause one moment",
        17,
        WHITE,
        "Georgia",
        "bold"
    )

    text(
        WIDTH // 2,
        440,
        "with you forever... would you let",
        17,
        WHITE,
        "Georgia",
        "bold"
    )

    text(
        WIDTH // 2,
        470,
        "me?",
        17,
        WHITE,
        "Georgia",
        "bold"
    )

    button(
        "Without thinking ❤️",
        memory_one,
        525,
        190
    )

    button(
        "Only if you stay too 🥺",
        memory_one,
        580,
        200
    )

    footer()


def memory_one():
    clear_page()

    progress(5)

    text(
        WIDTH // 2,
        95,
        "a little chapter of us",
        15,
        GREY,
        "Georgia"
    )

    photo_card(
        PHOTO_1,
        125
    )

    text(
        WIDTH // 2,
        470,
        "Some people enter your life quietly...",
        12,
        SOFT,
        "Georgia"
    )

    text(
        WIDTH // 2,
        495,
        "and somehow become your favourite chapter.",
        12,
        SOFT,
        "Georgia"
    )

    button(
        "One more memory →",
        memory_two,
        540,
        190
    )

    footer()


def memory_two():
    clear_page()

    progress(5)

    text(
        WIDTH // 2,
        95,
        "a little chapter of us",
        15,
        GREY,
        "Georgia"
    )

    photo_card(
        PHOTO_2,
        125
    )

    text(
        WIDTH // 2,
        470,
        "I don't remember what was so funny.",
        12,
        SOFT,
        "Georgia"
    )

    text(
        WIDTH // 2,
        495,
        "I just remember not wanting it to stop.",
        12,
        SOFT,
        "Georgia"
    )

    button(
        "One more memory →",
        memory_three,
        540,
        190
    )

    footer()


def memory_three():
    clear_page()

    progress(5)

    text(
        WIDTH // 2,
        95,
        "a little chapter of us",
        15,
        GREY,
        "Georgia"
    )

    photo_card(
        PHOTO_3,
        125
    )

    text(
        WIDTH // 2,
        470,
        "Ordinary evenings, made unreasonably good,",
        11,
        SOFT,
        "Georgia"
    )

    text(
        WIDTH // 2,
        495,
        "just because you were there.",
        11,
        SOFT,
        "Georgia"
    )

    button(
        "One more memory →",
        shayari_one,
        540,
        190
    )

    footer()


def shayari_one():
    clear_page()

    progress(5)

    text(
        WIDTH // 2,
        330,
        "for you, in my own words",
        16,
        SOFT,
        "Georgia"
    )

    text(
        WIDTH // 2,
        390,
        "तुमसे मोहब्बत करना",
        21,
        WHITE,
        "Noto Sans Devanagari"
    )

    text(
        WIDTH // 2,
        430,
        "शायद मेरी ज़िंदगी का",
        21,
        WHITE,
        "Noto Sans Devanagari"
    )

    text(
        WIDTH // 2,
        470,
        "सबसे खूबसूरत इत्तेफ़ाक़ था...",
        19,
        WHITE,
        "Noto Sans Devanagari"
    )

    text(
        WIDTH // 2,
        520,
        "और तुम्हारे साथ रहना",
        19,
        WHITE,
        "Noto Sans Devanagari"
    )

    text(
        WIDTH // 2,
        560,
        "अब मेरी सबसे प्यारी आदत है।",
        19,
        WHITE,
        "Noto Sans Devanagari"
    )

    button(
        "आगे बढ़ें →",
        shayari_two,
        620,
        150
    )

    footer()


def shayari_two():
    clear_page()

    progress(5)

    text(
        WIDTH // 2,
        300,
        "for you, in my own words",
        16,
        SOFT,
        "Georgia"
    )

    text(
        WIDTH // 2,
        360,
        "मैं वादे बहुत बड़े नहीं करूँगा,",
        19,
        WHITE,
        "Noto Sans Devanagari"
    )

    text(
        WIDTH // 2,
        405,
        "बस इतना चाहता हूँ...",
        20,
        WHITE,
        "Noto Sans Devanagari"
    )

    text(
        WIDTH // 2,
        460,
        "जब दुनिया थोड़ी मुश्किल लगे,",
        19,
        WHITE,
        "Noto Sans Devanagari"
    )

    text(
        WIDTH // 2,
        505,
        "तुम मेरे पास बैठ जाना।",
        19,
        WHITE,
        "Noto Sans Devanagari"
    )

    text(
        WIDTH // 2,
        550,
        "बाकी सब मैं संभाल लूँगा।",
        19,
        WHITE,
        "Noto Sans Devanagari"
    )

    button(
        "Next",
        last_question,
        620,
        150
    )

    footer()


def last_question():
    clear_page()

    progress(6)

    text(
        WIDTH // 2,
        335,
        "❤️",
        60,
        "#ff553e",
        "Arial"
    )

    text(
        WIDTH // 2,
        410,
        "Okay... one last question.",
        16,
        SOFT,
        "Georgia"
    )

    text(
        WIDTH // 2,
        455,
        "And this one actually matters.",
        16,
        SOFT,
        "Georgia"
    )

    root.after(
        1200,
        proposal
    )

    footer()


def proposal():
    clear_page()

    progress(6)

    text(
        WIDTH // 2,
        300,
        "❤️",
        58,
        "#ff553e",
        "Arial"
    )

    text(
        WIDTH // 2,
        400,
        "Will you be my person?",
        29,
        WHITE,
        "Georgia",
        "bold"
    )

    yes = tk.Button(
        root,
        text="❤️ YES",
        command=i_love_you,
        bg=PINK,
        fg=WHITE,
        activebackground=LIGHT_PINK,
        relief="flat",
        font=("Arial", 12, "bold")
    )

    yes.place(
        x=70,
        y=480,
        width=140,
        height=50
    )

    widgets.append(yes)

    obvious = tk.Button(
        root,
        text="Obviously 🥺",
        command=i_love_you,
        bg=BG,
        fg=WHITE,
        activebackground=CARD,
        relief="flat",
        font=("Arial", 12, "bold"),
        highlightthickness=1,
        highlightbackground=BORDER
    )

    obvious.place(
        x=220,
        y=480,
        width=140,
        height=50
    )

    widgets.append(obvious)

    footer()


def i_love_you():
    clear_page()

    progress(7)

    text(
        WIDTH // 2,
        330,
        "♥",
        35,
        PINK,
        "Arial"
    )

    text(
        WIDTH // 2,
        385,
        "I LOVE YOU. 🤍",
        28,
        WHITE,
        "Georgia",
        "bold"
    )

    text(
        WIDTH // 2,
        430,
        "Today. Tomorrow.",
        15,
        SOFT,
        "Georgia"
    )

    text(
        WIDTH // 2,
        455,
        "And in all the ordinary little moments",
        13,
        SOFT,
        "Georgia"
    )

    text(
        WIDTH // 2,
        480,
        "in between.",
        13,
        SOFT,
        "Georgia"
    )

    text(
        WIDTH // 2,
        525,
        "Will you keep choosing me?",
        16,
        WHITE,
        "Georgia",
        "italic"
    )

    button(
        "YES, ALWAYS ❤️",
        couple_page,
        570,
        190
    )

    footer()


def draw_person(x, y, female=False):
    canvas.create_oval(
        x - 8,
        y - 35,
        x + 8,
        y - 19,
        fill="#f4f1f2",
        outline="",
        tags="page"
    )

    canvas.create_line(
        x,
        y - 19,
        x,
        y + 18,
        fill="#f4f1f2",
        width=4,
        tags="page"
    )

    canvas.create_line(
        x,
        y - 8,
        x - 15,
        y + 4,
        fill="#f4f1f2",
        width=4,
        tags="page"
    )

    canvas.create_line(
        x,
        y - 8,
        x + 15,
        y + 4,
        fill="#f4f1f2",
        width=4,
        tags="page"
    )

    canvas.create_line(
        x,
        y + 18,
        x - 11,
        y + 40,
        fill="#f4f1f2",
        width=4,
        tags="page"
    )

    canvas.create_line(
        x,
        y + 18,
        x + 11,
        y + 40,
        fill="#f4f1f2",
        width=4,
        tags="page"
    )


def couple_page():
    clear_page()

    progress(7)

    text(
        WIDTH // 2,
        125,
        "you & me.",
        18,
        SOFT,
        "Georgia",
        "italic"
    )

    draw_person(
        175,
        430
    )

    draw_person(
        255,
        430,
        True
    )

    text(
        WIDTH // 2,
        520,
        "and... she said yes ❤️",
        17,
        WHITE,
        "Georgia",
        "bold"
    )

    button(
        "Continue →",
        stuck_page,
        570,
        160
    )

    footer()


def stuck_page():
    clear_page()

    progress(8)

    card(
        25,
        285,
        WIDTH - 25,
        545
    )

    text(
        WIDTH // 2,
        325,
        "There's no world.",
        15,
        SOFT,
        "Georgia",
        "italic"
    )

    text(
        WIDTH // 2,
        380,
        "You're stuck with",
        25,
        WHITE,
        "Georgia",
        "bold"
    )

    text(
        WIDTH // 2,
        420,
        "me. ❤️",
        25,
        WHITE,
        "Georgia",
        "bold"
    )

    text(
        WIDTH // 2,
        470,
        "No refunds.",
        14,
        SOFT
    )

    text(
        WIDTH // 2,
        495,
        "No cancellations.",
        14,
        SOFT
    )

    text(
        WIDTH // 2,
        520,
        "Lifetime subscription. ❤️",
        14,
        PINK_LIGHT
    )

    text(
        WIDTH // 2,
        565,
        "Thank you for being my favourite part of",
        11,
        SOFT,
        "Georgia",
        "italic"
    )

    text(
        WIDTH // 2,
        585,
        "this life.",
        11,
        SOFT,
        "Georgia",
        "italic"
    )

    footer()


opening()

animate_particles()
animate_hearts()

root.mainloop()