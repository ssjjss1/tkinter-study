from tkinter import *
a=Tk()
a.geometry("500x200")
def f():
    label["text"]="버튼이 클릭됨"
button=Button(a,text="클릭하세요!",command=f)
button.pack()
label=Label(a,text="버튼이 클릭 안됨")
label.pack()
a.mainloop()
#Button: 버튼을 제공해줌
#f: 콜백 함수→label 값을 변경해줌
