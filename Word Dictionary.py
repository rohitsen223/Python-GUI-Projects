from tkinter import *
from PyDictionary import PyDictionary
#-------------------------

root=Tk()
root.geometry("200x200")
dictionary =PyDictionary()
root.configure(bg='orange')


def SText():
  ansmeaning.configure(text=dictionary.meaning(entry.get()))
  anssynonyms.configure(text=dictionary.synonyms(entry.get()))
  ansantonyms.configure(text=entry.antonyms(entry.get()))
frame1=Frame(root)
label1=Label(frame1,text="Word Dictionary")
label2=Label(frame1,text="Enter Word Below")
entry1=Entry(frame1)
frame1.pack()
label1.pack()
label2.pack()
entry1.pack()
button=Button(frame1,text="Search",command=SText)
button.pack()
#-------frame2-------

frame2=Frame(root)
meaning=Label(frame2,text='Meaning')
ansmeaning=Label(frame2,text="")
frame2.pack()
meaning.pack()
ansmeaning.pack()
frame3=Frame(root)
synonyms=Label(frame3,text='Synonyms')
anssynonyms=Label(frame3,text="")

frame3.pack()
synonyms.pack()
anssynonyms.pack()
frame4=Frame(root)
antonyms=Label(frame4,text='Antonyms')
ansantonyms=Label(frame4,text="")
frame4.pack()
antonyms.pack()
ansantonyms.pack()
root.mainloop()
