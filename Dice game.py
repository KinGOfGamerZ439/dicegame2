  from tkinter import*
  from PIL import ImageTk,Image
  import random
  root=Tk()
  root.title(" Dice Game ")
  root.geometry("600x600")

  root.configure(background="OrangeRed2")
  
  
  img=ImageTk.PhotoImage(Image.open("dc.jpg"))
  
  player1=Label(root, text=" PLAYER 1", bg="cyan", fg="blue4")
  player1.place(relx=0.1, rely=0.3, anchor=CENTER)
  
  player2=Label(root, text=" PLAYER 2", bg="cyan", fg="blue4")
  player2.place(relx=0.9, rely=0.3, anchor=CENTER)
  
  player1score=Label(root, bg="mint cream", fg="black")
  player1score.place(relx=0.1, rely=0.4, anchor=CENTER)
  
  player2score=Label(root, bg="mint cream", fg="black")
  player2score.place(relx=0.9, rely=0.4, anchor=CENTER)
  
  randomdc=Label(root, bg="yellow", fg="gray9")
  randomdc.place(relx=0.5, rely=0.5, anchor=CENTER)
  
  p1score=0
  def elle():
      global p1score
      randomnumber=random.randint(1,6)
      randomdc["text"]="Player 1 dice random number is:"+str(randomnumber)
      p1score=p1score+randomnumber
      player1score["text"]=str(p1score)
  p1btn=Button(root, image=img, command=elle)
  p1btn.place(relx=0.1, rely=0.6, anchor=CENTER)
  
  p2score=0
  def elle18():
      global p2score
      randomnumber=random.randint(1,6)
      randomdc["text"]="Player 2 dice random number is:"+str(randomnumber)
      p2score=p1score+randomnumber
      player2score["text"]=str(p2score)
  p2btn=Button(root, image=img, command=elle18)
  p2btn.place(relx=0.9, rely=0.6, anchor=CENTER)
  
  root.mainloop()
