from tkinter import *

def AnyKey():
    print("knopka shmyaknuta")
    label.configure(text='ХА НАЕБАЛ')


# создаём оно программы
root = Tk("Моя программа")
# работаем с окном
root.geometry("1000x700")
# незя типо окно изменять
root.resizable(width=False,height=False)
# цвеот окошка
root['bg'] = 'yellow'


frame = Frame(root,padx=100,pady=10,width=200,height=100)
# настраеваем место положегие фрейма
frame.place(anchor="s", relx=0.5, rely=0.5)

frame2 = Frame(root,padx=100,pady=10,width=200,height=100)
frame2.place(anchor="n", relx=0.5, rely=0.5)
frame2['bg'] = 'red'


frame3 = Frame(root,padx=37,pady=26,width=200,height=70)
frame3.place(anchor="center", relx=0.5, rely=0.5)
frame3['bg'] = 'blue'
label = Label(frame3,text='Заголовок')
label.grid(column=0,row=0)
Button(frame3,text="служба по контракту", command=AnyKey).grid(column=0,row=1)



root.mainloop()

