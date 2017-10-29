from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def quit_app():
    root.quit() #built in function

def show_about(event=None):
    print("Help menu coming")
    messagebox.showwarning(
    "About",
    "Dylan made this in 2017"
)

def show_info(event=None):
    print("Showing info in msgbox")
    messagebox.showinfo(
        "Title",
        "info"
    )

root = Tk()
# root.title("Play project")
the_menu = Menu(root)



# --- file menu ----
# lets create a fixed menu on top fo the screen
file_menu = Menu(the_menu, tearoff=0)
#add submenus
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_command(label="Save as...")
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit_app)
# make them all pulldown from menu name
the_menu.add_cascade(label="File", menu=file_menu)

# --- font menu ----



text_font = StringVar()
text_font.set("Times")

def change_font(event=None):
    print("Font picked: ", text_font.get())

font_menu = Menu(the_menu, tearoff=0)

font_menu.add_radiobutton(label="Times",
                          variable=text_font,
                          command=change_font)

font_menu.add_radiobutton(label="Courier",
                          variable=text_font,
                          command=change_font)

font_menu.add_radiobutton(label="Monospace",
                          variable=text_font,
                          command=change_font)

# --- view menu ----
view_menu = Menu(the_menu, tearoff=0)
#lets toggle line numbers on and off
line_numbers = IntVar()
line_numbers.set(1) # set as true?

view_menu.add_checkbutton(label="Line Numbers",
                          variable=line_numbers)
# this is a submenu
view_menu.add_cascade(label="Fonts", menu=font_menu)
the_menu.add_cascade(label="View", menu=view_menu)

# --- help menu ----

help_menu = Menu(the_menu, tearoff=0)
#this indicates a keyboard shortcut
help_menu.add_command(label="About",
                      accelerator="option-A",
                      command=show_about)

the_menu.add_cascade(label="help", menu=help_menu)
#bind the commands
root.bind('<Option-A>', show_about)
root.bind('<Option-a>', show_about)

root.config(menu=the_menu)

# the form

Label(root, text="Description").grid(row=0, column=0, sticky=W)
Entry(root, width=50).grid(row=0, column=1)
Button(root, text="Suit", command=show_info).grid(row=0, column=8)


Label(root, text="Quality").grid(row=1, column=0, sticky=W)
Radiobutton(root, text="New", value=1).grid(row=2, column=0, sticky=W)
Radiobutton(root, text="Good", value=2).grid(row=3, column=0, sticky=W)
Radiobutton(root, text="Poor", value=3).grid(row=4, column=0, sticky=W)
Radiobutton(root, text="Bad", value=4).grid(row=5, column=0, sticky=W)

Label(root, text="Benefits").grid(row=1, column=1, sticky=W)
Checkbutton(root, text="Free Shipping").grid(row=2, column=1, sticky=W)
Checkbutton(root, text="Bonus Gift").grid(row=3, column=1, sticky=W)

root.mainloop()




