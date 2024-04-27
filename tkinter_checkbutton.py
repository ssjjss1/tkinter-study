from tkinter import *
a=Tk()
a.geometry("500x200")
def f():
    if(var1.get()==1):
        label["text"]="체크 박스 1번 선택"
    else:
        label["text"]="체크 박스 1번 선택 해제"
var1=IntVar()#IntVar():정수형 변수를 동적으로 생성
k=Checkbutton(a,text="햄버거",variable=var1,command=f)
k.pack()
#Checkbutton:체크 버튼 생성
#variable:체크 할 때 변수를 계속 변경해줌(1또는 0)
label=Label(a,text="선택 안됨")
label.pack()
a.mainloop()
