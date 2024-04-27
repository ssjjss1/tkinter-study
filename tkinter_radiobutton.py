from tkinter import *
a=Tk()
def f():
    if(x.get()==1):
        label["text"]="햄버거 선택"
    elif(x.get()==2):
        label["text"]="피자 선택"
    else:
        label["text"]="김밥 선택"
x=IntVar()
Radiobutton(a,text="햄버거",variable=x,value=1, command=f).pack()#변수 1
Radiobutton(a,text="피자",variable=x,value=2, command=f).pack()#변수 2
Radiobutton(a,text="김밥",variable=x,value=3, command=f).pack()#변수 3
label=Label(a,text="선택 안함")
label.pack()
a.mainloop()
