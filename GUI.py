from tkinter import *
from tkinter import font
from tkinter.ttk import *
from tkinter import messagebox
from time import sleep
import sys
import os


CASE_NUM = 6
file_name = None
wrong_cases = list()  
case_n = 2

window = Tk()
window.geometry('600x600')
window.resizable(False, False)
window.title(":)")


photo = PhotoImage(file="./photos/robo2.png")
img = Label(window,
            image=photo)

img.place(relx=0.5, y=130, anchor=CENTER)

greeting_message = Label(window,
                         text="Tester v1.0",
                         font=("Berlin Sans FB", 35))

greeting_message.place(relx=0.5, y=250, anchor=CENTER)


tutor = Label(window,
              text="Enter File Name")
inpt = Entry()


def submit():
    global file_name
    file_name = inpt.get()
    submit_button.place_forget()
    tutor.place_forget()
    inpt.place_forget()

    uploaded_file_name = Label(window,
                               text="Uploaded File: " + file_name)
    uploaded_file_name.place(x=17, y=10)

    


submit_button = Button(
    text="Submit",
    width=10,
    command=submit)
submit_button.place(x=140, y=28)
tutor.place(x=10, y=10)
inpt.place(x=10, y=30)


def restart_program():
    pass  # TODO


def quit_program():
    window.destroy()

def CompareFillProgram(txt_area1,txt_area2):
    
    

    flood1 = list(txt_area1.get("1.0","end-1c"))
    flood2 = list(txt_area2.get("1.0","end-1c"))
    wrong_index = list()
    wrong = 0
    row = 1
    column = 0

    if(len(flood1) > len(flood2)):
        length = len(flood2)
        parameter = True
        
    elif(len(flood1) < len(flood2)):
        length = len(flood1)
        parameter = False
    else:
        length = len(flood2)
        parameter = False
    
    for i in range(length):
        if (flood1[i] != flood2[i]):
            wrong += 1
            wrong_index.append(i)

    
    for j in range(length-1):
        if(flood1[j+1] == "\n"):
            if(j in wrong_index):
                txt_area1.tag_add("wrong",str(row)+"."+str(column),str(row)+"."+str(column+1))
                txt_area1.tag_config("wrong",background="pink",foreground="black")
            row += 1
            column = 0
        elif(flood1[j] == "\n"):
            if(j in wrong_index):
                txt_area1.tag_add("wrong",str(row)+"."+str(column),str(row)+"."+str(column+1))
                txt_area1.tag_config("wrong",background="pink",foreground="black")
        else:
            if(j in wrong_index):
                txt_area1.tag_add("wrong",str(row)+"."+str(column),str(row)+"."+str(column+1))
                txt_area1.tag_config("wrong",background="pink",foreground="black")
            column += 1
            

def compare_f():
    global case_n
    global combo_box
    
    compare_screen = Tk()
    compare_screen.geometry("900x900")
    compare_screen.resizable(False,False)
    compare_screen.title("Compare Results")

    frame1_tutor = Label(
        master = compare_screen,
        text = "Your Output",
        font = ("Ariel,25")
    )
    frame1_tutor.place(x = 18, y = 80)
    frame1 = Frame(compare_screen)
    frame1.place(relx=0.25, y=500, anchor=CENTER)

    scrollbar1 = Scrollbar(frame1,
                           orient=VERTICAL)
    scrollbar1.pack(side=RIGHT, fill=BOTH)

    txtarea1 = Text(frame1,
                   width=50,
                   height=45)
        
    frame2_tutor = Label(
        master = compare_screen,
        text = "Correct Output",
        font = ("Ariel,25")
    )
    frame2_tutor.place(x = 465, y = 80)

    frame2 = Frame(compare_screen)
    frame2.place(relx=0.75, y=500, anchor=CENTER)

    scrollbar1 = Scrollbar(frame2,
                           orient=VERTICAL)
    scrollbar1.pack(side=RIGHT, fill=BOTH)

    txtarea2 = Text(frame2,
                   width=50,
                   height=45,)
    


    case_n = combo_box.get()
    case_n = int(case_n[4:])

    file1 = open("./outputs/output"+str(case_n)+".txt", "r" )
    file2 = open("./expected_outputs/expected"+str(case_n)+".txt", "r")

    txtarea1.insert(INSERT,file1.read()) #END
    txtarea2.insert(INSERT,file2.read())
    file1.close()
    file2.close()

    txtarea1.pack(side=LEFT)
    txtarea1.config(yscrollcommand=scrollbar1.set)
    scrollbar1.config(command=txtarea1.yview)
    txtarea1.configure(state="disabled")

    txtarea2.pack(side=LEFT)
    txtarea2.config(yscrollcommand=scrollbar1.set)
    scrollbar1.config(command=txtarea2.yview)
    txtarea2.configure(state="disabled")

    CompareFillProgram(txtarea1,txtarea2)

def text_viewer():
    global combo_box

    frame = Frame(window)
    frame.place(relx=0.3, y=400, anchor=CENTER)

    scrollbar1 = Scrollbar(frame,
                           orient=VERTICAL)
    scrollbar1.pack(side=RIGHT, fill=BOTH)

    txtarea = Text(frame,
                   width=30,
                   height=16)
    txtarea.pack(side=LEFT)

    txtarea.config(yscrollcommand=scrollbar1.set)
    scrollbar1.config(command=txtarea.yview)
    txtarea.insert(END, wrong_cases)  # TODO
    txtarea.configure(state="disabled")

    tutor3 = Label(
        window,
        text = "Wrong Cases",
        font = ("Ariel",15)
    )
    tutor3.place(relx=0.28, y = 250, anchor = CENTER)
    
    combo_box = Combobox(
        values = wrong_cases,
        state = "readonly",
        justify = "center"
        )
    combo_box.place(relx = 0.7, y = 300, anchor = CENTER)
    

    box_button = Button(
        text = "Compare",
        command = compare_f)
    box_button.place(relx = 0.7, y = 350, anchor= CENTER)

    tutor2 = Label(
        window,
        text = "Please Select a Case"
    )
    tutor2.place(relx=0.7, y = 280, anchor = CENTER)
def step():
    global img
    global greeting_message
    global photo
    global wrong_cases
    
    total_n_true = 0

    if(file_name == None):
        messagebox.showwarning(
            title=None,
            message="You should enter the file name to initialize the tester!")
        return

    listdir = os.listdir(".")
    if(not(file_name in listdir)):
        messagebox.showwarning(
            title = None,
            message = "The file " + file_name + " that you specified was not found! Please restart the tester."
        )
        return
    

    img.place_forget()
    greeting_message.place_forget()

    progress_percentage = 0
    progress = Progressbar(window,
                           orient=HORIZONTAL,
                           length=250,
                           mode="determinate")

    progress.place(relx=0.5, y=210, anchor=CENTER)

    
    for i in range(1,CASE_NUM+1):

        output = open("./outputs/output"+str(i)+".txt", "r" )
        expected = open("./expected_outputs/expected"+str(i)+".txt", "r")

        if(output.read() == expected.read()):
            total_n_true += 1
        else:
            wrong_cases.append("Case"+str(i))
        
        output.close()
        expected.close()

        window.update_idletasks()
        progress_percentage += (1/CASE_NUM)*100
        progress['value'] += (1/CASE_NUM)*100
        progress_percentage_text = Label(window,
                                         text=str(round(progress_percentage, 1)) + "%")
        progress_percentage_text.place(x=120, y=200)
        sleep(0.5)

        
    photo = PhotoImage(file="./photos/robo.png")
    img = Label(window,
                image=photo)
    img.pack()
    greeting_message = Label(window,
                                text="Tester v1.0",
                                font=("Berlin Sans FB", 30))

    greeting_message.pack()

    complete_text = Label(window,
                            text="Completed!")
    complete_text.place(x=93, y=200)
    
    accuracy_= (total_n_true/CASE_NUM)*100
    if(accuracy_ == 100):
        messagebox.showinfo(None,"Well Done! Your Accuracy is 100%")
    elif(accuracy_ >= 90):
        messagebox.showinfo(None,"Great! Your accuracy is " + str(accuracy_) + "%")
    elif(accuracy_ >= 80):
        messagebox.showinfo(None,"Good! Your accuracy is " + str(accuracy_) + "%")
    elif(accuracy_ == 0):
        messagebox.showinfo(None,"Götünle mi çözdün aq accuracy: " + str(accuracy_) + "%")  #change this
    else:
        messagebox.showinfo(None,"Your accuracy is " + str(round(accuracy_,2)) + "%")
    
    
    start_button.place_forget()

    retry_button = Button(
        text="Retry",
        width=15,
        command=restart_program
    )
    retry_button.place(x=175, y=150)

    quit_button = Button(text="Quit",
                            width=15,
                            command=quit_program)
    quit_button.place(x=325, y=150)
    text_viewer()
            
        


start_button = Button(
    text="Start Tester",
    width=15,
    command=step
)
start_button.place(relx=0.5, y=330, anchor=CENTER)

sign = Label(window,
             text="Creator Arda Numanoğlu",
             font=("Cascadia Code", 10))
sign.pack(side=BOTTOM)




window.mainloop()
