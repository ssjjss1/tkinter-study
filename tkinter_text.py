from tkinter import *
a=Tk()
label1=Label(a,text="안녕하세요?",bg="yellow",fg="blue",width=80,height=2)
label2=Label(a,text="파이썬을 공부합시다!",font=("궁서체",32))
label1.pack()
label2.pack()
a.mainioop()
#text:여러줄로 된 텍스트 입력받는 위젯
#font:글꼴의 폰트와 크기를 설정
#fg:foreground의 약자, 글자색
#bg:background의 약자, 배경색
