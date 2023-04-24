"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""
import tkinter
import tkinter.messagebox

# TODO 13.2 Using the tkinter Module
print("=" * 10, "Section 13.2 using tkinter", "=" * 10)
# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter. Use the class name MyGUI2


class MyGUI2:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.name_label = tkinter.label(self.main_window, text="Joe Davidson")
        self.name_label.pack()

        tkinter.mainloop()


# TODO 13.3 Adding a label widget
print("=" * 10, "Section 13.3 adding a label widget", "=" * 10)
# Add a label to MyGUI2 (above) that prints your first and last name; pack the label
# Create an instance of MyGUI2
my_gui = MyGUI2()

# TODO 13.4 Organizing Widgets with Frames
print("=" * 10, "Section 13.4 using frames", "=" * 10)
# Create a MyGUI3 class that creates a window with two frames
# In the top Frame add labels with your name and major
# In the bottom frame add labels with the classes you are taking this semester
# Create an instance of MyGUI3


class MyGUI3:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.name_label = tkinter.Label(self.top_frame, text="Joe Davidson")
        self.name_label.pack()
        self.major_label = tkinter.Label(self.top_frame, text="Design and Development")
        self.major_label.pack()

        self.classes_label = tkinter.Label(self.bottom_frame, text="Programming Logic")
        self.classes_label.pack()

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()


new_gui = MyGUI3()

# TODO 13.5 Button Widgets and info Dialog Boxes
print("=" * 10, "Section 13.5 button widgets and info dialogs", "=" * 10)
# Create a GUI that will tell a joke
# Use a button to show the punch line, which should appear in a dialog box
# Create an instance of the GUI


class JokeGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.joke_label = tkinter.Label(self.top_frame, text="Why did the chicken cross the road?")
        self.joke_label.pack()
        self.answer_button = tkinter.Button(self.bottom_frame, text="Answer", command=self.show_answer)
        self.answer_button.pack()

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_answer(self):
        tkinter.messagebox.showinfo("Answer", "To get to the other side!")


joke = JokeGUI()
print("joke")

# TODO 13.6 getting input / 13.7 Using Labels as output fields
print("=" * 10, "Section 13.6-13.7 input and output using Entry and Label", "=" * 10)
# Using the program in 13.10 kilo converter as a sample,
# create a program to convert inches to centimeters


class Converter:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame, text="Enter size in inches")
        self.prompt_label.pack()
        self.inches_entry = tkinter.Entry(self.top_frame, width=6)
        self.inches_entry.pack()

        self.convert_button = tkinter.Button(self.bottom_frame, text="Convert", command=self.convert)
        self.convert_button.pack(side="left")
        self.quit_button = tkinter.Button(self.bottom_frame, text="QUIT", command=self.main_window.destroy)
        self.quit_button.pack()

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        inches = float(self.inches_entry.get())
        centimeters = inches * 2.54
        tkinter.messagebox.showinfo("Results",
                                    str(inches) + " inches equals " +
                                    str(centimeters) + " centimeters.")


convert_gui = Converter()
print("Convert inches to centimeters")
