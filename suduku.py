from tkinter import *
import sys
###########################
w = '#FFFFFF'
g = '#9fe665'
lg ='#DCF2F0'
gr='#778899'
r = '#e37b76'
entries=[]
timer=-1
st={(0,3):'6',(0,6):'4',(1,0):'7',(1,5):'3',(1,6):'6',(2,4):'9',(2,5):'1',(2,7):'8',(4,1):'5',(4,3):'1',(4,4):'8',(4,8):'3',(5,3):'3',
    (5,5):'6',(5,7):'4',(5,8):'5',(6,1):'4',(6,3):'2',(6,7):'6',(7,0):'9',(7,2):'3',(8,1):'2',(8,6):'1'}
sol=['581672439','792843651','364591782','438957216','256184973','179326845','845219367','913768524','627435198']

###########
root=Tk()
root.title('Sudoku solver')
root.geometry('600x400')
root.config(bg=w, relief='solid', bd=2)
root.resizable(False,False)

##################function
def QUIT():
    sys.exit()
def check():
    global  sudukuframe, sudukuframe,entrytext,button,entrybox,timelabel
    button.destroy()
    timelabel.destroy()
    done = divmod(timer, 60)
    m=0
    for i in range(9):
        for j in range(9):
            if sol[i][j]==entrytext[i][j].get().strip() and (i,j) not in st.keys():
                m+=1
                entrybox[i][j].config(bg=g)
            elif (i,j) not in st.keys():
                entrybox[i][j].config(bg=r)

    label = Label(root, text='TOTAL TIME:'+str(done[0])+'.'+str(done[1])+' min.', justify='center', bg=gr, font='Courier 13')
    label.pack(pady=10)
    label = Label(root, text='YOU ENTERED '+str(m)+' BOXES CORRECTLY', justify='center', bg=gr,
                  font='Courier 13')
    label.pack(pady=10)
    button = Button(root, text='QUIT', bg=gr, justify='center', bd=1, relief='solid', font='Courier 13 ',
                    command=QUIT)
    button.pack(pady=3)









def time():
    global timelabel,timer
    timer+=1
    p=divmod(timer,60)
    timelabel.config(text='TIME:'+str(p[0])+'.'+str(p[1])+' min.')
    timelabel.after(1000, time)
def createEntrytext():
    global entrytext,sudukuframe,st
    for i in range(9):
        #mt=[]
        for j in range(9):
            entrytext[i][j] = StringVar()
            entrytext[i][j].set(' ')

            #print(type(entrytext[i][j]))
            #mt.append(entrytext[i][j])
        #entries.append(mt)
def createEntry():
    global entrybox, sudukuframe,entrytext,st
    for i in range(9):
        sm=[]
        for j in range(9):
            if (i,j) in st.keys():
                E=Label(sudukuframe,text=st[(i,j)],justify='center', width=3, font='BOLD 15',bd=1,relief='solid',bg=lg)
                E.grid(row=i, column=j)
                entrytext[i][j].set(st[(i,j)])
                sm.append(E)
            else:
                E = Entry(sudukuframe,text=entrytext[i][j], width=3, font='BOLD 15',bd=1,relief='solid',justify='center')
                E.grid(row=i, column=j)
                sm.append(E)
        entrybox.append(sm)

def start():
    global sudukuframe, entrytext, entrybox,b1,l2,l3,timelabel,button
    b1.destroy();l2.destroy();l3.destroy()
    sudukuframe = Frame(root)
    sudukuframe.config(bg=w, bd=1, relief='solid', height='450', width='450')  # , relief='solid', bd=3)
    sudukuframe.pack()
    entrytext = [['0'] * 9 for k in range(9)]
    entrybox=[]
    createEntrytext()
    createEntry()
    timelabel=Label(root,text='TIME:'+str(timer), justify='center', bg=gr, font='Courier 13 ',bd=1, relief='solid')
    timelabel.pack(pady=3)
    button= Button(root, text='SUBMIT', bg=gr, justify='center', bd=1, relief='solid', font='Courier 13 ', command=check)
    button.pack(pady=3)
    time()


    #E.place(x=i, y=j, height=20, width=25)

########################main
global b1,l2,l3
label1=Label(root,text='--SUDOKU SOLVER--', justify='center', bg=w, font='Courier 13 underline')
label1.pack()
l2=Label(root,text='Read The Rules And\nClick Start Once You Are Ready.',background='white',font='Courier 13 ',justify='center')
l2.pack()
mt='1.Only use the numbers 1 to 9,\n2. Avoid trying to guess the solution to the puzzle,\n3.Only use each number once in each row,column,&grid,\n' \
   '4.Use the process of elimnation as a tactic.'
l3=Label(root,width=100,text=mt,background=g,font='Courier 13 ')
l3.pack()
b1=Button(root,text='Start',bg=gr,width=10,bd=1,relief='solid',font='Courier 13 ',command=start)
b1.pack(pady=10)



root.mainloop()
