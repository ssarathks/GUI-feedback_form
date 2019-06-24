from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#function that invoke when the submit button has been clicked

def submit():
    submit_message.grid(row=5,stick='w')
    post_submit_frame.grid(row=6,stick='nsew')
    post_submit_namelabel.configure(text="Name: {}".format(nameentry.get()))
    post_submit_emaillabel.configure(text="Email: {}".format(emailentry.get()))
    post_submit_commentlabel.configure(text="Comment: {}".format(commententry.get(1.0,'end')))
    messagebox.showinfo("Comment Entry","Thank you for your feedback")
    clear()

#function that invoke when clear button has been pressed

def clear():
    nameentry.delete(0,'end')
    emailentry.delete(0,'end')
    commententry.delete(1.0,'end')
#function that invoke when ok button in post submit frame is clicked
def hide_post_submit():
    post_submit_frame.grid_forget()
    submit_message.grid_forget()

root=Tk()
root.title("Feedback Form")
root.resizable(False,False)
root.configure(background='#345f24')

#creating tkinter style object

style=ttk.Style()
style.configure('TFrame',background="#7ac45c")
style.configure('TButton',background="#7ac45c")
style.configure('TEntry',background="#7ac45c")
style.configure('TLabel',background="#7ac45c")
style.configure('Header.TLabel',font=('Arial',20))
style.configure('Header.TButton',font=('Arial',20))


#following are the widgets in the header frame
headerframe=ttk.Frame(root)
headerframe.grid(row=0,column=0,stick='nsew')

logoimage=PhotoImage(file="logo.png").subsample(20,20)
logo=ttk.Label(headerframe,image=logoimage)
logo.grid(row=0,column=0,rowspan=2)

header=ttk.Label(headerframe,text="Feedback Form",style='Header.TLabel')
header.grid(row=0,column=1,stick='s')

subheader=ttk.Label(headerframe,text="Here you can give your feedback about us"
                                     "your feedbacks are valuable for us",wraplength=300)
subheader.grid(row=1,column=1,stick='nsew')

#following are the content frame and widgets in the content frame

contentframe=ttk.Frame(root)
contentframe.grid(row=1,column=0,stick='nsew')

namelabel=ttk.Label(contentframe,text='Name:')
namelabel.grid(row=0,column=0,stick='w')

emaillabel=ttk.Label(contentframe,text='Email')
emaillabel.grid(row=0,column=1,stick='w')

nameentry=ttk.Entry(contentframe)
nameentry.grid(row=1,column=0,stick='w')

emailentry=ttk.Entry(contentframe)
emailentry.grid(row=1,column=1,stick='w')

commentlabel=ttk.Label(contentframe,text='Comment')
commentlabel.grid(row=2,column=0,stick='w')

commententry=Text(contentframe,width=44,height=10)
commententry.grid(row=3,column=0,columnspan=2)

submitbutton=ttk.Button(contentframe,text="Submit",command=submit)
submitbutton.grid(row=4,column=0)

clearbutton=ttk.Button(contentframe,text="Clear",command=clear)
clearbutton.grid(row=4,column=1)

#post submit widgets

post_submit_frame=ttk.Frame(root)

post_submit_namelabel = ttk.Label(post_submit_frame)
post_submit_namelabel.grid(row=0,stick='nsew')

post_submit_emaillabel=ttk.Label(post_submit_frame)
post_submit_emaillabel.grid(row=1,stick='nsew')

post_submit_commentlabel=ttk.Label(post_submit_frame)
post_submit_commentlabel.grid(row=2,stick='nsew')

post_submit_ok_button=ttk.Button(post_submit_frame,text="Ok",command=hide_post_submit)
post_submit_ok_button.grid(row=3,stick='s')

submit_message=ttk.Label(contentframe,text="your entry has been submitted!")

# for i in range(0,2):
#     root.rowconfigure(i,weight=1)
# for i in range(0,2):
#     headerframe.rowconfigure(i,weight=1)
# for i in range(0,5):
#     contentframe.rowconfigure(i,weight=1)
# for i in range(0,2):
#     headerframe.columnconfigure(i,weight=1)
#     contentframe.columnconfigure(i,weight=1)
# root.columnconfigure(0,weight=1)

for i in headerframe.grid_slaves():
    i.grid(padx=5,pady=5)
for i in contentframe.grid_slaves():
    i.grid(padx=5,pady=5)
for i in post_submit_frame.grid_slaves():
    i.grid(padx=5,pady=5)
for i in root.grid_slaves():
    i.grid(padx=5,pady=5)


root.mainloop()