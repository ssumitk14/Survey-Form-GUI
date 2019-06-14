from tkinter import *


def saveToFile():
    saveFirstName = firstNameEntry.get()
    saveLastName = lastNameEntry.get()
    saveGender = gender.get()
    saveEmail  = email.get()
    savePhone = phone.get()
    saveBirth = birth.get()
    saveCity = city.get()
    saveState = state.get()
    saveZip = zip.get()


    file = open("C:/Users/sumit/Desktop/tkinter/data.txt","a+")
    file.write(saveFirstName)
    file.write(',')
    file.write(saveLastName)
    file.write(',')
    if saveGender==1:
        file.write('M')
    elif saveGender==2:
        file.write('F')
    else:
        pass
    file.write(',')
    file.write(saveBirth)
    file.write(',')
    file.write(saveEmail)
    file.write(',')
    file.write(savePhone)
    file.write(',')
    file.write(saveCity)
    file.write(',')
    file.write(saveState)
    file.write(',')
    file.write(saveZip)
    file.write('\n')


    file.close()

    firstNameEntry.delete(0,END)
    lastNameEntry.delete(0,END)
    male.deselect()
    female.deselect()
    no.select()
    email.delete(0,END)
    phone.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    birth.delete(0,END)
    zip.delete(0,END)




root = Tk()
root.geometry("270x300")

firstName = Label(root, text='First Name: ', fg='violet')
firstName.grid(row=0,sticky='E')
lastName = Label(root,text='Last Name: ', fg='indigo')
lastName.grid(row=1,sticky='E')
birth = Label(root,text='Date of Birth:\n(dd/mm/yyyy)', fg='blue')
birth.grid(row=3,sticky='E')
email = Label(root,text='Email: ',fg='green')
email.grid(row=4,sticky='E')
phone = Label(root, text='Phone No: ', fg='magenta')
phone.grid(row=5,sticky='E')
city = Label(root, text='City: ',fg='cyan')
city.grid(row=6,sticky=E)
state = Label(root, text='State: ', fg='brown')
state.grid(row=7,sticky=E)
zip = Label(root,text='Zip Code: ',fg='olive')
zip.grid(row=8,sticky=E)

firstNameEntry = Entry()
lastNameEntry = Entry()
birth = Entry()
email = Entry()
phone = Entry()
city = Entry()
state = Entry()
zip = Entry()

firstNameEntry.grid(row=0,column=1)
lastNameEntry.grid(row=1,column=1)
birth.grid(row=3,column=1)
email.grid(row=4,column=1)
phone.grid(row=5,column=1)
city.grid(row=6,column=1)
state.grid(row=7,column=1)
zip.grid(row=8,column=1)

gender = IntVar()
male = Radiobutton(root, text='Male', variable=gender,value=1)
female = Radiobutton(root, text='Female', variable=gender,value=2)
no = Radiobutton(root, variable=gender,value=3)



male.place(x=58,y=42)
female.grid(row=2,column=1)

submitButton = Button(root,text='Submit ',command=saveToFile,bg='orange',fg='black')
submitButton.place(x=60,y=220,width=150)
#submitButton.grid(row=8,column=1,ipadx=40,ipady=10)

quitButton = Button(root, text='Quit',bg='orange',fg='black' ,command=root.quit)
quitButton.place(x=60,y=260,width=150)


root.mainloop()
