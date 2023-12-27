from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250)
        self.canvas.create_text(150, 150, text="place holder", font=("Ariel", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_image)
        self.false_button.grid(column=0, row=2)
        self.true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_image, command=self.true_button_click)
        self.true_button.grid(column=1, row=2)

        self.window.mainloop()

    def true_button_click(self):
        return "true"
        
