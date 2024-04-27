from tkinter import *
a=Tk()
def f():
    label["text"]=entry.get()+"가 입력됨"
entry=Entry(a,fg="black",bg="yellow",width=28)
entry.pack()
button=Button(a,text="입력 후 클릭해주세요",command=f)
button.pack()
label=Label(a,text="아무 것도 입력 안됨")
label.pack()

a.mainloop()
#entry:입력한 내용을 전달하는 위젯
#get():입력 불러오기
