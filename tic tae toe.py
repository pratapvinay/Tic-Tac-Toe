#board=[1,2,3,
 #      4,5,6,
  #     7,8,9]
#def display():
#    print(board[0],'|',board[1],'|',board[2])
#    print('---------')
#    print(board[3],'|',board[4],'|',board[5])
#    print('---------')
#    print(board[6],'|',board[7],'|',board[8])
#display()
    
#name=input('enter first user name:')
#print('welcome to tic tac toe>>>',name)
#name2=input('enter second user name:')
#print('welcome to tic tac toe>>>',name2)
#choice=str(input("press 'X' or 'O'>>>"))






#n=int(input("Enter a number: "))
#for i in range(0,n):
#    for j in range(0,n):
#        if(i==j):
#            print("1",sep=" ",end=" ")
#        else:
#            print("0",sep=" ",end=" ")
#    print(1)


################USING TKINTER###############
from tkinter import *
from tkinter import messagebox
root=Tk()

root.title('tic tac toe')
root.geometry('450x450')
root.configure(bg='powderblue')



bclick=True

def btnclear():
    global operator
    operator=''
    text_input.set('')

def ttt(buttons):
    global bclick
    if buttons['text']=='' and bclick==True:
        buttons['text']='X'
        bclick=False
        
    elif buttons['text']=='' and bclick==False:
        buttons['text']='O'
        bclick=True
     
    elif buttons["text"]=="O" or buttons["text"] == "X":
        messagebox.showinfo("Try Again","Retry")    
        
    if   (btn1['text']=='X' and btn2['text']=='X' and btn3['text']=='X' or
          btn4['text']=='X' and btn5['text']=='X' and btn6['text']=='X' or
          btn7['text']=='X' and btn8['text']=='X' and btn9['text']=='X' or
          btn1['text']=='X' and btn4['text']=='X' and btn7['text']=='X' or
          btn2['text']=='X' and btn5['text']=='X' and btn8['text']=='X' or
          btn3['text']=='X' and btn6['text']=='X' and btn9['text']=='X' or
          btn1['text']=='X' and btn5['text']=='X' and btn9['text']=='X' or
          btn3['text']=='X' and btn5['text']=='X' and btn7['text']=='X'):
          
          messagebox.showinfo('Palyer X','Winner is X !!!')



        
    elif (btn1['text']=='O' and btn2['text']=='O' and btn3['text']=='O' or
          btn4['text']=='O' and btn5['text']=='O' and btn6['text']=='O' or
          btn7['text']=='O' and btn8['text']=='O' and btn9['text']=='O' or
          btn1['text']=='O' and btn4['text']=='O' and btn7['text']=='O' or
          btn2['text']=='O' and btn5['text']=='O' and btn8['text']=='O' or
          btn3['text']=='O' and btn6['text']=='O' and btn9['text']=='O' or
          btn1['text']=='O' and btn5['text']=='O' and btn9['text']=='O' or
          btn3['text']=='O' and btn5['text']=='O' and btn7['text']=='O'):
           
          messagebox.showinfo('Palyer O','Winner is O !!!')
    
        
                
operator=""       
buttons=StringVar()
label=Label(root,text='Tic Tac Toe',font=('aerial',20,'bold'),bd=21,relief=RIDGE).grid(columnspan=6)


btn1=Button(root,text='',font=('aerial',20,'bold'),padx=40,pady=20,command=lambda:ttt(btn1))
btn1.grid(row=1,column=0,sticky=S+E+N+W)

btn2=Button(root,text='',font=('aerial',20,'bold'),padx=40,pady=20,command=lambda:ttt(btn2))
btn2.grid(row=1,column=1,sticky=S+E+N+W)

btn3=Button(root,text='',font=('aerial',20,'bold'),padx=40,pady=20,command=lambda:ttt(btn3))
btn3.grid(row=1,column=2,sticky=S+E+N+W)

btn4=Button(root,text='',font=('aerial',20,'bold'),padx=40,pady=20,command=lambda:ttt(btn4))
btn4.grid(row=2,column=0,sticky=S+E+N+W)

btn5=Button(root,text='',font=('aerial',20,'bold'),padx=40,pady=20,command=lambda:ttt(btn5))
btn5.grid(row=2,column=1,sticky=S+E+N+W)

btn6=Button(root,text='',font=('aerial',20,'bold'),padx=40,pady=20,command=lambda:ttt(btn6))
btn6.grid(row=2,column=2,sticky=S+E+N+W)

btn7=Button(root,text='',font=('aerial',20,'bold'),padx=40,pady=20,command=lambda:ttt(btn7))
btn7.grid(row=3,column=0,sticky=S+E+N+W)

btn8=Button(root,text='',font=('aerial',20,'bold'),padx=40,pady=20,command=lambda:ttt(btn8))
btn8.grid(row=3,column=1,sticky=S+E+N+W)

btn9=Button(root,text='',font=('aerial',20,'bold'),padx=40,pady=20,command=lambda:ttt(btn9))
btn9.grid(row=3,column=2,sticky=S+E+N+W)

btnclear=Button(root,bd=8,font=('aerial',20,'bold'),bg='powder blue',fg='black',text='Clear',padx=16,command=btnclear)
btnclear.grid(row=4,column=1)

root.mainloop()



















































