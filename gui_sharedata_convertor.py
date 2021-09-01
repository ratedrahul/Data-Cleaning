from tkinter import * 
import os

os.chdir("F:\\share_data")
dloc = os.listdir()
os.chdir("F:\\new_share_data")
files = os.listdir()
file = files.reverse()
window= Tk()

font1 = ('LED',22,'bold')
font2 = ('LED',14,'bold')
window.config(bg = '#990000')
window.geometry('600x800')
window.title('Share Data Cleaning')

k = Label(window,text = 'Convert Share Data',font = font1)
k.pack()
k = Label(window,text = 'unreadable files into readable CSV files',font = font2)
k.pack()
# k.grid(row = 0, column = 0)
from functools import partial

# def sh(days = 2):
# 	print('here doing for days ',days)
# 	for i in files[:days]:
# 		j = "F:\\new_share_data\\"+i[:10]+'.csv'
# 		with open(i,'r+') as rf:
# 			with open(j,'w+') as wf:
# 				for i in rf:
# 					if i.count(',') == 6:
# 						wf.write(i)

# 	os.chdir("F:\\new_share_data")
# 	name_k.config(text = os.listdir()[-1])

def sh1(days=2):
	print('here doing for days ',days)
	dloc.reverse()
	count = 0
	for i in dloc[:days]:
		j = "F:\\new_share_data\\"+i[:10]+'.csv'
		i = 'F:\\share_data\\'+i
		# print(i)
		count+=1
		# print(j)
		with open(i,'r+') as rf:
			with open(j,'w+') as wf:
				for i in rf:
					if i.count(',') == 6:
						wf.write(i)

	os.chdir("F:\\new_share_data")
	name_k.config(text = os.listdir()[-1])

l = Label(window,text = 'Convert',font = font1,bg = 'brown')
# l.grid(row =2,column = 0)
l.place(x = 100, y = 100)


kk = Button(window,text = 'Latest File',command = partial(sh1,1),font = font2,bg = 'green')
# kk.grid(row = 2, column = 3)
kk.place(x = 300, y = 100)
kk = Button(window,text = '2 Days',bg = 'green',command = partial(sh1,2),font = font2)
# kk.grid(row = 2, column = 3)
kk.place(x = 50, y = 300)
kk = Button(window,text = '3 Days',bg = 'green',command = partial(sh1,3),font = font2)
# kk.grid(row = 2, column = 3)
kk.place(x = 200, y = 300)
kk = Button(window,text = '4 Days',bg = 'green',command = partial(sh1,4),font = font2)
# kk.grid(row = 2, column = 3)
kk.place(x = 350, y = 300)

k = Label(window,text =' Last available file',font = ('LED',14,'bold'),bg = 'gray')
k.place(x = 0, y = 200)
name_k = Label(window,text = dloc[-1],font = ('LED',12,'bold'))
name_k.place(x = 250, y = 200)

k = Label(window,text =' Multiple n Days ',font = ('LED',14,'bold'))
k.place(x = 0, y = 500)

st = IntVar()
e1 = Entry(window, width = 6,font = font2, textvariable = st)
e1.place(x = 250, y = 500)
 # print(file)
					# break 
					
def ndays(event = None):
	e = int(e1.get())

	# print(e,type(e))
	sh1(days = e)
k = Button(window,text = 'Enter',bg = 'green', font = font2,command = ndays)
k.place(x = 410 , y = 500)


exi = Button(window,text = 'EXIT (Khatm- Tata- Bye Bye)',font = ('LED',14,'bold'),bg = 'red',fg = 'blue',command = window.destroy)
exi.pack(side = BOTTOM,fill = X)
window.mainloop()