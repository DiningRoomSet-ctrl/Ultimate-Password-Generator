import random
from tkinter import*
import string
import os

c="#ebece4"
ht='#2986cc'

base=string.ascii_lowercase + string.ascii_uppercase + string.digits

root= Tk()
root.title("Ultimate Password Generator by Edvin Pandzic")
root.geometry("800x600")
root.resizable(width= FALSE, height= FALSE)
root.config(bg=c)

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'passwords.txt')

psswrd_list= open(filename, 'a')
dt= open(filename, 'r')
data= dt.readlines()

generator_page= Frame(root, bg=c)
passwrd_list_page= Frame(root, bg=c)

generator_page.grid(row=0, column=0, sticky=NSEW)
passwrd_list_page.grid(row=0, column=0, sticky=NSEW)

generator_page.tkraise()
pagenumber = 0

paswrd= StringVar()
paswrd.set('Generated Password Here')

def generate():
    dan = int(cle.get())
    pan = ''.join(random.choice(base)for _ in range(dan))

    generated_text.config(state="normal")
    generated_text.delete(0, END)
    generated_text.insert(0,pan)
    generated_text.config(state="readonly", readonlybackground=c, justify='center')

def save_details():
    
    psswrd_list.write(spe.get())
    psswrd_list.write(' - ')
    psswrd_list.write(uee.get())
    psswrd_list.write(' - ')
    psswrd_list.write(generated_text.get() + '\n')


def update(data):
    
    pl.delete(0, END)

    for item in data:
        pl.insert(END, item)

def check(e):
    srch=pse.get()

    if srch == '':
        liss=data
    else:
        liss=[]
        for item in data:
            if srch.lower() in item.lower():
                liss.append(item)

    update(liss)

#Big title
btlf= LabelFrame(generator_page, bg=c, borderwidth=0)
btlf.grid(row=0, column=0)

btl= Label(btlf,text="Ultimate Password Generator", anchor=N, bg=c, font="Ariel 20 bold")
btl.grid(row=0, column=1)

cred= Label(btlf, text="By: Edvin Pandzic", bg=c, font="Helvetica 10")
cred.grid(row=1, column=1)

#Service provider entry
spa= LabelFrame(generator_page, bg=c, borderwidth=2)
spa.grid(row=1, column=0, pady=20, padx= 11)

spl= Label(spa, text="Service Name:", bg=c, font='Helvetica 10 bold')
spl.grid(row=0, column=0, padx= 10, pady=5)

spe= Entry(spa,width=35, borderwidth=2, font=("Ariel", 10))
spe.grid(row=1, column=0, padx= 10, pady=5)

#Username//Email entry
uel= Label(spa,text="Username//Email:", bg=c, font='Helvetica 10 bold')
uel.grid(row=0, column=1, padx= 10, pady=5)

uee= Entry(spa, width= 50, borderwidth= 2, font=("Ariel 10"))
uee.grid(row=1, column=1, padx= 10, pady=5)

#Char limit spinbox
cll= Label(spa,text="Character Limit:", bg=c, font='Helvetica 10 bold')
cll.grid(row=0, column=2, padx= 10, pady=5)

cle= Spinbox(spa, borderwidth=2, from_=1, to=25, width= 2)
cle.grid(row=1, column=2, padx= 10, pady=5)

#password list button
plblf= LabelFrame(generator_page, bg=c, borderwidth=0)
plblf.grid(row=2,column=0)

plbl= Label(plblf, bg=c,)
plbl.grid(row=0, column=0)

plb=Button(plbl, text="Password List", font='Ariel 10', bg=c, fg=ht, borderwidth=0,
            command=lambda:passwrd_list_page.tkraise())
plb.grid(row=0, column=0, padx= 30, pady= 30)

#Generate password button
gpbl= Label(plbl, bg=c)
gpbl.grid(row=0, column= 1, padx= 50, pady= 20)

gpb= Button(gpbl, bg="#cbd5dc", text="Generate Password", 
            font="Ariel 10 bold", command=generate)
gpb.grid(row=0, column=1, padx= 50, pady= 20)

#save login details button
sldl= Label(plblf, bg=c)
sldl.grid(row=0, column=2, padx= 0, pady= 0)

sld= Button(sldl,bg="#cbd5dc", text="Save Login Details",
            font="Ariel 10 bold", command=save_details)
sld.grid(row=0, column=2, padx= 0, pady= 0)

#generated password
generated_text = Entry(generator_page,bg=c,font=("ariel", 35),width = 30, bd= 0,textvariable= paswrd,
                       state="readonly",readonlybackground=c,justify= 'center')
generated_text.grid(row=3, pady=80)

#password search
pslf= LabelFrame(passwrd_list_page, bg=c, borderwidth=0)
pslf.grid(row=0, column=0)

psl= Label(pslf, bg=c, text='Password Search:', font='Ariel 10 bold', anchor=W)
psl.grid(row=1, column=0, pady=10)

pse= Entry(pslf, width=100)
pse.grid(row=2, column=0)

pse.bind("<KeyRelease>", check)

#password list
pllf= LabelFrame(passwrd_list_page,bg=c,borderwidth=0)
pllf.grid(row=1)

pll= Label(pllf, bg=c)
pll.grid(row=2, column=1)

pl= Listbox(pll, width=126, height=30, borderwidth=5)
pl.grid(padx=15, pady=10)

for x in open(filename):
    pl.insert(END,x)

    print("file is closed")
psswrd_list.close


#back button
bb= Button(pslf,text="Back", command=lambda:generator_page.tkraise(), bg=c, fg=ht, borderwidth=0)
bb.grid(row=0, column=0)


root.mainloop()