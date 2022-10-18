from tkinter import *
from tkinter import font
import random
import time
from tkinter import filedialog , messagebox


root = Tk()
root.geometry('1270x690+0+0')
root.title('BAKERY')#change
root.config(bg='pink')
topFrame=Frame(root,bd=10,relief=RIDGE,bg='red')
topFrame.pack(side=TOP)
labelTitle=Label(topFrame,text="BAKER'S DELIGHT",font=('algerian',30,'bold'),fg='white',bg='firebrick',width=51,bd=9)
labelTitle.grid(row=0,column=0)
# root.mainloop()






# for reciept button
def recieptbill():
    global billnumber,date
    if cakes.get()!='' or snacks.get()!='':
            textReciept.delete(1.0,END)
            x=random.randint(100,1000)
            billnumber='BILL'+str(x)
            date=time.strftime('%d/%m/%Y')
            textReciept.insert(END,'Reciept ref:\t\t'+billnumber+'\t\t'+date+'\n')
            textReciept.insert(END,'***************************************************************\n')
            textReciept.insert(END,'ITEMS:\t\t Cost of items(Rs)\n')
            textReciept.insert(END,'***************************************************************\n')



            if eprise.get()!='0':
                textReciept.insert(END,f'chocoprize cake 1pc:\t\t\t{int(eprise.get())*75}\n\n')

            if eblack.get()!='0':
                textReciept.insert(END,f'black forest 1pc:\t\t\t{int(eblack.get())*80}\n\n')  

            if ewhite.get()!='0':
                textReciept.insert(END,f'white forest 1pc:\t\t\t{int(ewhite.get())*80}\n\n')
            
            if ered.get()!='0':
                textReciept.insert(END,f'redvelvet 1pc:\t\t\t{int(ered.get())*85}\n\n')

            if elava.get()!='0':
                textReciept.insert(END,f'lava cake 1pc:\t\t\t{int(elava.get())*75}\n\n')

            if echoco.get()!='0':
                textReciept.insert(END,f'chocolate cake 1pc:\t\t\t{int(echoco.get())*70}\n\n')

            if erain.get()!='0':
                textReciept.insert(END,f'rainbow cake 1pc:\t\t\t{int(erain.get())*90}\n\n')
            
            if eras.get()!='0':
                textReciept.insert(END,f'rasmali cake 1pc:\t\t\t{int(eras.get())*85}\n\n')

            if epinata.get()!='0':
                textReciept.insert(END,f'pinata cake 1pc:\t\t\t{int(epinata.get())*75}\n\n')

            if ebuter.get()!='0':
                textReciept.insert(END,f'buterscotch cake 1pc:\t\t\t{int(ebuter.get())*75}\n\n')

            if ecaramel.get()!='0':
                textReciept.insert(END,f'caramel cake 1pc:\t\t\t{int(ecaramel.get())*65}\n\n')



            if fprise.get()!='0':
                textReciept.insert(END,f'chocoprize cake 1/2kg:\t\t\t{int(fprise.get())*475}\n\n')

            if fblack.get()!='0':
                textReciept.insert(END,f'black forest 1/2kg:\t\t\t{int(fblack.get())*480}\n\n')  

            if fwhite.get()!='0':
                textReciept.insert(END,f'white forest 1/2kg:\t\t\t{int(fwhite.get())*470}\n\n')
            
            if fred.get()!='0':
                textReciept.insert(END,f'redvelvet 1/2kg:\t\t\t{int(fred.get())*485}\n\n')

            if flava.get()!='0':
                textReciept.insert(END,f'lava cake 1/2kg:\t\t\t{int(flava.get())*475}\n\n')

            if fchoco.get()!='0':
                textReciept.insert(END,f'chocolate cake 1/2kg:\t\t\t{int(fchoco.get())*470}\n\n')

            if frain.get()!='0':
                textReciept.insert(END,f'rainbow cake 1/2kg:\t\t\t{int(frain.get())*490}\n\n')

            if fcheese.get()!='0':
                textReciept.insert(END,f'cheese cake 1/2kg:\t\t\t{int(fcheese.get())*480}\n\n')

            if fras.get()!='0':
                textReciept.insert(END,f'rasmali cake 1/2kg:\t\t\t{int(fras.get())*485}\n\n')

            if fpinata.get()!='0':
                textReciept.insert(END,f'pinata cake 1/2kg:\t\t\t{int(fpinata.get())*475}\n\n')

            if fbuter.get()!='0':
                textReciept.insert(END,f'buterscotch cake 1/2kg:\t\t\t{int(fbuter.get())*475}\n\n')

            if fcaramel.get()!='0':
                textReciept.insert(END,f'caramel cake 1/2kg:\t\t\t{int(fcaramel.get())*365}\n\n')



            if gsam.get()!='0':
                textReciept.insert(END,f'samosa:\t\t\t{int(gsam.get())*15}\n\n')

            if gegg.get()!='0':
                textReciept.insert(END,f'egg puff:\t\t\t{int(gegg.get())*20}\n\n')

            if gveg.get()!='0':
                textReciept.insert(END,f'veg puff:\t\t\t{int(gveg.get())*15}\n\n')

            if groll.get()!='0':
                textReciept.insert(END,f'crispy roll:\t\t\t{int(groll.get())*30}\n\n')

            if gchip.get()!='0':
                textReciept.insert(END,f'choco chip:\t\t\t{int(gchip.get())*10}\n\n')

            if gdonut.get()!='0':
                textReciept.insert(END,f'donut:\t\t\t{int(gdonut.get())*50}\n\n')

            if gcold.get()!='0':
                textReciept.insert(END,f'cold cofee:\t\t\t{int(gcold.get())*35}\n\n')

            if glime.get()!='0':
                textReciept.insert(END,f'lime soda:\t\t\t{int(glime.get())*25}\n\n')
            
            if gmalai.get()!='0':
                textReciept.insert(END,f'rasmalai:\t\t\t{int(gmalai.get())*30}\n\n')

            if gpepsi.get()!='0':
                textReciept.insert(END,f'pepsi 500ml:\t\t\t{int(gpepsi.get())*35}\n\n')

            if gfro.get()!='0':
                textReciept.insert(END,f'frootie 750ml:\t\t\t{int(gfro.get())*40}\n\n')

            if gwater.get()!='0':
                textReciept.insert(END,f'water 1lt:\t\t\t{int(gwater.get())*20}\n\n')

            

            textReciept.insert(END,'***************************************************************\n')

            textReciept.insert(END,f'cost of cakes:\t\t\t{priceofcakes}Rs\n\n')
            textReciept.insert(END,f'cost of snacks:\t\t\t{priceofsnacks}Rs\n\n')

            textReciept.insert(END,f'Sub total:\t\t\t{subtotalofitems}Rs\n\n')
            textReciept.insert(END,f'Service tax:\t\t\t{servicetax}Rs\n\n')
            textReciept.insert(END,f'TOTAL:\t\t\t{total}Rs\n\n')
            textReciept.insert(END,'***************************************************************\n')
            textReciept.insert(END,'THANK YOU AND VISIT AGAIN:)\n')


    else:
            messagebox.showerror('error','no items selected')






    # for save button

def save():
    if textReciept.get(1.0,END)=='\n':
        pass
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        bill_data=textReciept.get(1.0,END)
        url.write(bill_data)
        url.close()
        messagebox.showinfo('Information','Your bill is saved succesfully')






# for send button

def send():
    if textReciept.get(1.0,END)=='\n':
        pass

    else:
        root2=Toplevel()
        root2.title("Send Bill")
        root2.config(bg='wheat1')
        root2.geometry('485x620+50+50')
        # root2.mainloop()

        numberlabel=Label(root2,text='Moblie Number',font=('ariel',18,'underline','bold'),bg='wheat1',fg='red4')
        numberlabel.pack(pady=5)
        # root2.mainloop()

        numberfeild=Entry(root2,font=('helvitica',22,'bold'),bd=3,width=24)
        numberfeild.pack(pady=5)

        billlabel=Label(root2,text='Bill Details',font=('ariel',18,'underline','bold'),bg='wheat1',fg='red4')
        billlabel.pack(pady=5)


        textarea=Text(root2,font=('ariel',12,'bold'),bd=3,width=42,height=14)
        textarea.pack(pady=5)
        textarea.insert(END,'Reciept ref:\t\t'+billnumber+'\t\t'+date+'\n\n')
        
        textarea.insert(END,f'cost of cakes:\t\t\t{priceofcakes}Rs\n\n')
        textarea.insert(END,f'cost of snacks:\t\t\t{priceofsnacks}Rs\n\n')

        textarea.insert(END,f'Sub total:\t\t\t{subtotalofitems}Rs\n\n')
        textarea.insert(END,f'Service tax:\t\t\t{servicetax}Rs\n\n')
        textarea.insert(END,f'TOTAL:\t\t\t{total}Rs\n\n')
        textarea.insert(END,'THANK YOU AND VISIT AGAIN:)\n')
        

        def see():
            if numberfeild.get()=='':
                pass
            else:
                messagebox.showinfo('Information','message sent')


        sendbutton=Button(root2,text='SEND',font=('ariel',19,'bold'),bg='red4',fg='white',bd=7,relief=GROOVE,command=see)
        sendbutton.pack(pady=5)

        root2.mainloop()





 
# for reset button
def reset():
    textReciept.delete(1.0,END)

    
    eprise.set('0')
    eblack.set('0')
    ewhite.set('0')
    ered.set('0')
    elava.set('0')
    echoco.set('0')
    erain.set('0')
    echeese.set('0')
    eras.set('0')
    epinata.set('0')
    ebuter.set('0')
    ecaramel.set('0')

    fprise.set('0')
    fblack.set('0')
    fwhite.set('0')
    fred.set('0')
    flava.set('0')
    fchoco.set('0')
    frain.set('0')
    fcheese.set('0')
    fras.set('0')
    fpinata.set('0')
    fbuter.set('0')
    fcaramel.set('0')

    gsam.set('0')
    gegg.set('0')
    gveg.set('0')
    groll.set('0')
    gchip.set('0')
    gdonut.set('0')
    gcold.set('0')
    glime.set('0')
    gmalai.set('0')
    gpepsi.set('0')
    gfro.set('0')
    gwater.set('0')

    textprise.config(state=DISABLED)
    textblack.config(state=DISABLED)
    textwhite.config(state=DISABLED)
    textred.config(state=DISABLED)
    textlava.config(state=DISABLED)
    textchoco.config(state=DISABLED)
    textrain.config(state=DISABLED)
    textcheese.config(state=DISABLED)
    textras.config(state=DISABLED)
    textpinata.config(state=DISABLED)
    textbuter.config(state=DISABLED)
    textcaramel.config(state=DISABLED)
    textprise1.config(state=DISABLED)
    textblack1.config(state=DISABLED)
    textwhite1.config(state=DISABLED)
    textred1.config(state=DISABLED)
    textlava1.config(state=DISABLED)
    textchoco1.config(state=DISABLED)
    textrain1.config(state=DISABLED)
    textcheese1.config(state=DISABLED)
    textras1.config(state=DISABLED)
    textpinata1.config(state=DISABLED)
    textbuter1.config(state=DISABLED)
    textcaramel1.config(state=DISABLED)
    textsam.config(state=DISABLED)
    textegg.config(state=DISABLED)
    textveg.config(state=DISABLED)
    textroll.config(state=DISABLED)
    textchip.config(state=DISABLED)
    textdonut.config(state=DISABLED)
    textcold.config(state=DISABLED)
    textlime.config(state=DISABLED)
    textmalai.config(state=DISABLED)
    textpepsi.config(state=DISABLED)
    textfro.config(state=DISABLED)
    textwater.config(state=DISABLED)


    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var28.set(0)
    var29.set(0)
    var30.set(0)
    var31.set(0)
    var32.set(0)
    var33.set(0)
    var34.set(0)
    var35.set(0)
    var36.set(0)
    var49.set(0)
    var50.set(0)
    var51.set(0)
    var52.set(0)
    var53.set(0)
    var54.set(0)
    var55.set(0)
    var56.set(0)
    var57.set(0)
    var58.set(0)
    var59.set(0)
    var60.set(0)


    cakes.set('')
    snacks.set('')
    sub.set('')
    tax.set('')
    tot.set('')

    




# function to activate entry feild
def a():
    if var13.get()==1:
        textprise.config(state=NORMAL)
        textprise.delete(0,END)
        textprise.focus()
    else:
        textprise.config(state=DISABLED)
        eprise.set('0')


def b():
    if var14.get()==1:
        textblack.config(state=NORMAL)
        textblack.delete(0,END)
        textblack.focus()
    else:
        textblack.config(state=DISABLED)
        eblack.set('0')

def c():
    if var15.get()==1:
        textwhite.config(state=NORMAL)
        textwhite.delete(0,END)
        textwhite.focus()
    else:
        textwhite.config(state=DISABLED)
        ewhite.set('0')

def d():
    if var16.get()==1:
        textred.config(state=NORMAL)
        textred.delete(0,END)
        textred.focus()
    else:
        textred.config(state=DISABLED)
        ered.set('0')       

def e():
    if var17.get()==1:
        textlava.config(state=NORMAL)
        textlava.delete(0,END)
        textlava.focus()
    else:
        textlava.config(state=DISABLED)
        elava.set('0')   

def f():
    if var18.get()==1:
        textchoco.config(state=NORMAL)
        textchoco.delete(0,END)
        textchoco.focus()
    else:
        textchoco.config(state=DISABLED)
        echoco.set('0')   

def g():
    if var19.get()==1:
        textrain.config(state=NORMAL)
        textrain.delete(0,END)
        textrain.focus()
    else:
        textrain.config(state=DISABLED)
        erain.set('0')         

def h():
    if var20.get()==1:
        textcheese.config(state=NORMAL)
        textcheese.delete(0,END)
        textcheese.focus()
    else:
        textcheese.config(state=DISABLED)
        echeese.set('0')         


def i():
    if var21.get()==1:
        textras.config(state=NORMAL)
        textras.delete(0,END)
        textras.focus()
    else:
        textras.config(state=DISABLED)
        eras.set('0')

def j():
    if var22.get()==1:
        textpinata.config(state=NORMAL)
        textpinata.delete(0,END)
        textpinata.focus()
    else:
        textpinata.config(state=DISABLED)
        epinata.set('0')        


def k():
    if var23.get()==1:
        textbuter.config(state=NORMAL)
        textbuter.delete(0,END)
        textbuter.focus()
    else:
        textbuter.config(state=DISABLED)
        ebuter.set('0') 

def l():
    if var24.get()==1:
        textcaramel.config(state=NORMAL)
        textcaramel.delete(0,END)
        textcaramel.focus()
    else:
        textcaramel.config(state=DISABLED)
        ecaramel.set('0') 







def m():
    if var25.get()==1:
        textprise1.config(state=NORMAL)
        textprise1.delete(0,END)
        textprise1.focus()
    else:
        textprise1.config(state=DISABLED)
        fprise.set('0')

def n():
    if var26.get()==1:
        textblack1.config(state=NORMAL)
        textblack1.delete(0,END)
        textblack1.focus()
    else:
        textblack1.config(state=DISABLED)
        fblack.set('0')

def o():
    if var27.get()==1:
        textwhite1.config(state=NORMAL)
        textwhite1.delete(0,END)
        textwhite1.focus()
    else:
        textwhite1.config(state=DISABLED)
        fwhite.set('0')

def p():
    if var28.get()==1:
        textred1.config(state=NORMAL)
        textred1.delete(0,END)
        textred1.focus()
    else:
        textred1.config(state=DISABLED)
        fred.set('0')       

def q():
    if var29.get()==1:
        textlava1.config(state=NORMAL)
        textlava1.delete(0,END)
        textlava1.focus()
    else:
        textlava1.config(state=DISABLED)
        flava.set('0')   

def r():
    if var30.get()==1:
        textchoco1.config(state=NORMAL)
        textchoco1.delete(0,END)
        textchoco1.focus()
    else:
        textchoco1.config(state=DISABLED)
        fchoco.set('0')   

def s():
    if var31.get()==1:
        textrain1.config(state=NORMAL)
        textrain1.delete(0,END)
        textrain1.focus()
    else:
        textrain1.config(state=DISABLED)
        frain.set('0')         

def t():
    if var32.get()==1:
        textcheese1.config(state=NORMAL)
        textcheese1.delete(0,END)
        textcheese1.focus()
    else:
        textcheese1.config(state=DISABLED)
        fcheese.set('0')         


def u():
    if var33.get()==1:
        textras1.config(state=NORMAL)
        textras1.delete(0,END)
        textras1.focus()
    else:
        textras1.config(state=DISABLED)
        fras.set('0')

def v():
    if var34.get()==1:
        textpinata1.config(state=NORMAL)
        textpinata1.delete(0,END)
        textpinata1.focus()
    else:
        textpinata1.config(state=DISABLED)
        fpinata.set('0')        


def w():
    if var35.get()==1:
        textbuter1.config(state=NORMAL)
        textbuter1.delete(0,END)
        textbuter1.focus()
    else:
        textbuter1.config(state=DISABLED)
        fbuter.set('0') 

def x():
    if var36.get()==1:
        textcaramel1.config(state=NORMAL)
        textcaramel1.delete(0,END)
        textcaramel1.focus()
    else:
        textcaramel1.config(state=DISABLED)
        fcaramel.set('0') 







def aa():
    if var49.get()==1:
        textsam.config(state=NORMAL)
        textsam.delete(0,END)
        textsam.focus()
    else:
        textsam.config(state=DISABLED)
        gsam.set('0')


def bb():
    if var50.get()==1:
        textegg.config(state=NORMAL)
        textegg.delete(0,END)
        textegg.focus()
    else:
        textegg.config(state=DISABLED)
        gegg.set('0')


def cc():
    if var51.get()==1:
        textveg.config(state=NORMAL)
        textveg.delete(0,END)
        textveg.focus()
    else:
        textveg.config(state=DISABLED)
        gveg.set('0')


def dd():
    if var52.get()==1:
        textroll.config(state=NORMAL)
        textroll.delete(0,END)
        textroll.focus()
    else:
        textroll.config(state=DISABLED)
        groll.set('0')


def ee():
    if var53.get()==1:
        textchip.config(state=NORMAL)
        textchip.delete(0,END)
        textchip.focus()
    else:
        textchip.config(state=DISABLED)
        gchip.set('0')

def ff():
    if var54.get()==1:
        textdonut.config(state=NORMAL)
        textdonut.delete(0,END)
        textdonut.focus()
    else:
        textdonut.config(state=DISABLED)
        gdonut.set('0')

def gg():
    if var55.get()==1:
        textcold.config(state=NORMAL)
        textcold.delete(0,END)
        textcold.focus()
    else:
        textcold.config(state=DISABLED)
        gcold.set('0')


def hh():
    if var56.get()==1:
        textlime.config(state=NORMAL)
        textlime.delete(0,END)
        textlime.focus()
    else:
        textlime.config(state=DISABLED)
        glime.set('0')

def ii():
    if var57.get()==1:
        textmalai.config(state=NORMAL)
        textmalai.delete(0,END)
        textmalai.focus()
    else:
        textmalai.config(state=DISABLED)
        gmalai.set('0')

def jj():
    if var58.get()==1:
        textpepsi.config(state=NORMAL)
        textpepsi.delete(0,END)
        textpepsi.focus()
    else:
        textpepsi.config(state=DISABLED)
        gpepsi.set('0')


def kk():
    if var59.get()==1:
        textfro.config(state=NORMAL)
        textfro.delete(0,END)
        textfro.focus()
    else:
        textfro.config(state=DISABLED)
        gfro.set('0')


def ll():
    if var60.get()==1:
        textwater.config(state=NORMAL)
        textwater.delete(0,END)
        textwater.focus()
    else:
        textwater.config(state=DISABLED)
        gwater.set('0')









# for total button
def totalcost():
    global priceofcakes,priceofsnacks,subtotalofitems, servicetax, total

    if var13.get()!=0 or var14.get()!=0 or var15.get()!=0 or var16.get()!=0 or var17.get()!=0 or var18.get()!=0 or var19.get()!=0 or var20.get()!=0 or var21.get()!=0 or\
        var22.get()!=0 or var23.get()!=0 or var24.get()!=0 or var25.get()!=0 or var26.get()!=0 or var27.get()!=0 or var28.get()!=0 or var29.get()!=0 or var30.get()!=0 or var31.get()!=0 or\
            var32.get()!=0 or var33.get()!=0 or var34.get()!=0 or var35.get()!=0 or var36.get()!=0 or var36.get()!=0 or var49.get()!=0 or var38.get()!=0 or var50.get()!=0 or var51.get()!=0 or\
                var52.get()!=0 or var53.get()!=0 or var54.get()!=0 or var55.get()!=0 or var56.get()!=0 or var57.get()!=0 or var58.get()!=0 or var59.get()!=0 or var60.get()!=0:

      item1=int(eprise.get())
      item2=int(eblack.get())
      item3=int(ewhite.get())
      item4=int(ered.get())
      item5=int(elava.get())
      item6=int(echoco.get())
      item7=int(erain.get())
      item8=int(echeese.get())
      item9=int(echeese.get())
      item10=int(eras.get())
      item11=int(epinata.get())
      item12=int(ecaramel.get())
       

      item13=int(fprise.get())
      item14=int(fblack.get())
      item15=int(fwhite.get())
      item16=int(fred.get())
      item17=int(flava.get())
      item18=int(fchoco.get())
      item19=int(frain.get())
      item20=int(fcheese.get())
      item21=int(fcheese.get())
      item22=int(fras.get())
      item23=int(fpinata.get())
      item24=int(fcaramel.get())


      item25=int(gsam.get())
      item26=int(gegg.get())
      item27=int(gveg.get())
      item28=int(groll.get())
      item29=int(gchip.get())
      item30=int(gdonut.get())
      item31=int(gcold.get())
      item32=int(glime.get())
      item33=int(gmalai.get())
      item34=int(gpepsi.get())
      item35=int(gfro.get())
      item36=int(gwater.get())


      priceofcakes=(item1*75)+(item2*80)+(item3*80)+(item4*85)+(item5*75)+(item6*70)+(item7*90)+(item8*80)+(item9*85)+(item10*75)+(item11*75)+(item12*65)+(item13*475)+(item14*480)+(item15*470)+(item16*485)+(item17*475)+(item18*470)+(item19*490)+(item20*480)+(item21*485)+(item22*475)+(item23*475)+(item24*365)

      priceofsnacks=(item25*15)+(item26*20)+(item27*15)+(item28*30)+(item29*10)+(item30*50)+(item31*35)+(item32*25)+(item33*30)+(item34*35)+(item35*40)+(item36*20)      

      cakes.set(str(priceofcakes)+'Rs')
      snacks.set(str(priceofsnacks)+'Rs')

      subtotalofitems=priceofcakes+priceofsnacks
      sub.set(str(subtotalofitems)+'Rs')

      servicetax=subtotalofitems/20
      tax.set(str(servicetax)+'Rs')
    
      total=subtotalofitems+servicetax
      tot.set(str(total)+'Rs')
    
    else:
        messagebox.showerror('error','no item selected')







#frame:
menuFrame=Frame(root,bd=10,relief=RIDGE,bg='pink')#change
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='firebrick')
costFrame.pack(side=BOTTOM)

cakeFrame=LabelFrame(menuFrame,text='CAKES                  Per pc       1/2kg',font=('ariel',19,'bold'),bd=8,relief=RIDGE,fg='red4',)  #change
cakeFrame.pack(side=LEFT)

snackFrame=LabelFrame(menuFrame,text='snacks',font=('ariel',19,'bold'),bd=8,fg='red4',relief=RIDGE)
snackFrame.pack(side=LEFT)



rightFrame=Frame(root,bd=15,relief=RIDGE,bg='red4')
rightFrame.pack(side=RIGHT)

calculaterFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='red4')
calculaterFrame.pack()

recieptFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='red4')
recieptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='red4')
buttonFrame.pack(side=BOTTOM)




# VARIABLES

# variables cakes
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()

# variables per pc

var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()

# variables for entry feild for per pc

eprise=StringVar()
eblack=StringVar()
ewhite=StringVar()
ered=StringVar()
elava=StringVar()
echoco=StringVar()
erain=StringVar()
echeese=StringVar()
eras=StringVar()
epinata=StringVar()
ebuter=StringVar()
ecaramel=StringVar()

# variables for per half kg

var25=IntVar()
var26=IntVar()
var27=IntVar()
var28=IntVar()
var29=IntVar()
var30=IntVar()
var31=IntVar()
var32=IntVar()
var33=IntVar()
var34=IntVar()
var35=IntVar()
var36=IntVar()

# variables for entry feild for half kg

fprise=StringVar()
fblack=StringVar()
fwhite=StringVar()
fred=StringVar()
flava=StringVar()
fchoco=StringVar()
frain=StringVar()
fcheese=StringVar()
fras=StringVar()
fpinata=StringVar()
fbuter=StringVar()
fcaramel=StringVar()


# variables for snacks

var37=IntVar()
var38=IntVar()
var39=IntVar()
var40=IntVar()
var41=IntVar()
var42=IntVar()
var43=IntVar()
var44=IntVar()
var45=IntVar()
var46=IntVar()
var47=IntVar()
var48=IntVar()


# variable for price of snacks

var49=IntVar()
var50=IntVar()
var51=IntVar()
var52=IntVar()
var53=IntVar()
var54=IntVar()
var55=IntVar()
var56=IntVar()
var57=IntVar()
var58=IntVar()
var59=IntVar()
var60=IntVar()



# variables for entry feild for snacks

gsam=StringVar()
gegg=StringVar()
gveg=StringVar() 
groll=StringVar()
gchip=StringVar()
gdonut=StringVar()
gcold=StringVar()
glime=StringVar()
gmalai=StringVar()
gpepsi=StringVar()
gfro=StringVar()
gwater=StringVar()

# Set 0 for per pc

eprise.set('0')
eblack.set('0')
ewhite.set('0')
ered.set('0')
elava.set('0')
echoco.set('0')
erain.set('0')
echeese.set('0')
eras.set('0')
epinata.set('0')
ebuter.set('0')
ecaramel.set('0')

# set 0 per half kg

fprise.set('0')
fblack.set('0')
fwhite.set('0')
fred.set('0')
flava.set('0')
fchoco.set('0')
frain.set('0')
fcheese.set('0')
fras.set('0')
fpinata.set('0')
fbuter.set('0')
fcaramel.set('0')

# set 0 for snacks

gsam.set('0')
gegg.set('0')
gveg.set('0')
groll.set('0')
gchip.set('0')
gdonut.set('0')
gcold.set('0')
glime.set('0')
gmalai.set('0')
gpepsi.set('0')
gfro.set('0')
gwater.set('0')


# cost frame variables

cakes=StringVar()
snacks=StringVar()
sub=StringVar()
tax=StringVar()
tot=StringVar()











# cakes
prise=Checkbutton(cakeFrame,text='chocoprize cake',font=('ariel',15,'bold'),onvalue=1,offvalue=0,variable=var1)
prise.grid(row=0,column=0,sticky=W)

black=Checkbutton(cakeFrame,text='black forest',font=('ariel',15,'bold'),onvalue=1,offvalue=0,variable=var2)
black.grid(row=1,column=0,sticky=W)

white=Checkbutton(cakeFrame,text='white forest',font=('ariel',15,'bold'),onvalue=1,offvalue=0,variable=var3)
white.grid(row=2,column=0,sticky=W)

red=Checkbutton(cakeFrame,text='red velvet',font=('ariel',15,'bold'),onvalue=1,offvalue=0,variable=var4)
red.grid(row=3,column=0,sticky=W)

lava=Checkbutton(cakeFrame,text='lava cake',font=('ariel',15,'bold'),onvalue=1,offvalue=0,variable=var5)
lava.grid(row=4,column=0,sticky=W)

choco=Checkbutton(cakeFrame,text='chocolate cake',font=('ariel',15,'bold'),onvalue=1,offvalue=0,variable=var6)
choco.grid(row=5,column=0,sticky=W)

rain=Checkbutton(cakeFrame,text='rainbow cake',font=('ariel',15,'bold'),onvalue=1,offvalue=0,variable=var7)
rain.grid(row=6,column=0,sticky=W)

cheese=Checkbutton(cakeFrame,text='cheese cake',font=('ariel',15,'bold'),onvalue=1,offvalue=0,variable=var8)
cheese.grid(row=7,column=0,sticky=W)

ras=Checkbutton(cakeFrame,text='rasmalai cake',font=('ariel',15,'bold'),onvalue=1,offvalue=0,variable=var9)
ras.grid(row=8,column=0,sticky=W)

pinata=Checkbutton(cakeFrame,text='pinata cake',font=('ariel',15,'bold'),onvalue=1,offvalue=0,variable=var10)
pinata.grid(row=9,column=0,sticky=W)

buter=Checkbutton(cakeFrame,text= 'buterscotch cake',font=('ariel',15,'bold'),onvalue=1,offvalue=0,variable=var11)
buter.grid(row=10,column=0,sticky=W)

caramel=Checkbutton(cakeFrame,text='caramel cake',font=('ariel',15,'bold'),onvalue=1,offvalue=0,variable=var12)
caramel.grid(row=11,column=0,sticky=W)






# price per pc

prise=Checkbutton(cakeFrame,text='Rs 75',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var13,command=a)
prise.grid(row=0,column=1,sticky=W)

black=Checkbutton(cakeFrame,text='Rs-80',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var14,command=b)
black.grid(row=1,column=1,sticky=W)

white=Checkbutton(cakeFrame,text='Rs-80',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var15,command=c)
white.grid(row=2,column=1,sticky=W)

red=Checkbutton(cakeFrame,text='Rs-85',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var16,command=d)
red.grid(row=3,column=1,sticky=W)

lava=Checkbutton(cakeFrame,text='Rs-75',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var17,command=e)
lava.grid(row=4,column=1,sticky=W)

choco=Checkbutton(cakeFrame,text='Rs-70',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var18,command=f)
choco.grid(row=5,column=1,sticky=W)

rain=Checkbutton(cakeFrame,text='Rs-90',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var19,command=g)
rain.grid(row=6,column=1,sticky=W)

cheese=Checkbutton(cakeFrame,text='Rs-80',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var20,command=h)
cheese.grid(row=7,column=1,sticky=W)

ras=Checkbutton(cakeFrame,text='Rs-85',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var21,command=i)
ras.grid(row=8,column=1,sticky=W)

pinata=Checkbutton(cakeFrame,text='Rs-75',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var22,command=j)
pinata.grid(row=9,column=1,sticky=W)

buter=Checkbutton(cakeFrame,text= 'Rs-75',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var23,command=k)
buter.grid(row=10,column=1,sticky=W)

caramel=Checkbutton(cakeFrame,text='Rs-65',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var24,command=l)
caramel.grid(row=11,column=1,sticky=W)



# entry feild for cakes per pc

textprise=Entry(cakeFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=eprise)
textprise.grid(row=0,column=2)

textblack=Entry(cakeFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=eblack)
textblack.grid(row=1,column=2)

textwhite=Entry(cakeFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=ewhite)
textwhite.grid(row=2,column=2)

textred=Entry(cakeFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=ered)
textred.grid(row=3,column=2)

textlava=Entry(cakeFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=elava)
textlava.grid(row=4,column=2)

textchoco=Entry(cakeFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=echoco)
textchoco.grid(row=5,column=2)

textrain=Entry(cakeFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=erain)
textrain.grid(row=6,column=2)

textcheese=Entry(cakeFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=echeese)
textcheese.grid(row=7,column=2)

textras=Entry(cakeFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=eras)
textras.grid(row=8,column=2)

textpinata=Entry(cakeFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=epinata)
textpinata.grid(row=9,column=2)

textbuter=Entry(cakeFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=ebuter)
textbuter.grid(row=10,column=2)

textcaramel=Entry(cakeFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=ecaramel)
textcaramel.grid(row=11,column=2)






# price for half kg

prise=Checkbutton(cakeFrame,text='Rs 475',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var25,command=m)
prise.grid(row=0,column=3,sticky=W)


black=Checkbutton(cakeFrame,text='Rs-480',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var26,command=n)
black.grid(row=1,column=3,sticky=W)

white=Checkbutton(cakeFrame,text='Rs-470',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var27,command=o)
white.grid(row=2,column=3,sticky=W)

red=Checkbutton(cakeFrame,text='Rs-485',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var28,command=p)
red.grid(row=3,column=3,sticky=W)

lava=Checkbutton(cakeFrame,text='Rs-475',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var29,command=q)
lava.grid(row=4,column=3,sticky=W)

choco=Checkbutton(cakeFrame,text='Rs-470',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var30,command=r)
choco.grid(row=5,column=3,sticky=W)

rain=Checkbutton(cakeFrame,text='Rs-490',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var31,command=s)
rain.grid(row=6,column=3,sticky=W)

cheese=Checkbutton(cakeFrame,text='Rs-480',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var32,command=t)
cheese.grid(row=7,column=3,sticky=W)

ras=Checkbutton(cakeFrame,text='Rs-485',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var33,command=u)
ras.grid(row=8,column=3,sticky=W)

pinata=Checkbutton(cakeFrame,text='Rs-475',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var34,command=v)
pinata.grid(row=9,column=3,sticky=W)

buter=Checkbutton(cakeFrame,text= 'Rs-475',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var35,command=w)
buter.grid(row=10,column=3,sticky=W)

caramel=Checkbutton(cakeFrame,text='Rs-365',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var36,command=x)
caramel.grid(row=11,column=3,sticky=W)



# entry feilds for half kg

textprise1=Entry(cakeFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=fprise)
textprise1.grid(row=0,column=4)

textblack1=Entry(cakeFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=fblack)
textblack1.grid(row=1,column=4)

textwhite1=Entry(cakeFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=fwhite)
textwhite1.grid(row=2,column=4)

textred1=Entry(cakeFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=fred)
textred1.grid(row=3,column=4)

textlava1=Entry(cakeFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=flava)
textlava1.grid(row=4,column=4)

textchoco1=Entry(cakeFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=fchoco)
textchoco1.grid(row=5,column=4)

textrain1=Entry(cakeFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=frain)
textrain1.grid(row=6,column=4)

textcheese1=Entry(cakeFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=fcheese)
textcheese1.grid(row=7,column=4)

textras1=Entry(cakeFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=fras)
textras1.grid(row=8,column=4)

textpinata1=Entry(cakeFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=fpinata)
textpinata1.grid(row=9,column=4)

textbuter1=Entry(cakeFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=fbuter)
textbuter1.grid(row=10,column=4)

textcaramel1=Entry(cakeFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=fcaramel)
textcaramel1.grid(row=11,column=4)








# snacks

sam=Checkbutton(snackFrame,text='samosa',font=('ariel',15,'bold'),onvalue=1,offvalue=0,variable=var37)
sam.grid(row=0,column=0,sticky=W)

egg=Checkbutton(snackFrame,text='egg puff',font=('ariel',15,'bold'),onvalue=1,offvalue=0,variable=var38)
egg.grid(row=1,column=0,sticky=W)

veg=Checkbutton(snackFrame,text='veg puff',font=('ariel',15,'bold'),onvalue=1,offvalue=0,variable=var39)
veg.grid(row=2,column=0,sticky=W)

roll=Checkbutton(snackFrame,text='crispy roll',font=('ariel',15,'bold'),onvalue=1,offvalue=0,variable=var40)
roll.grid(row=3,column=0,sticky=W)

chip=Checkbutton(snackFrame,text='choco chip',font=('ariel',15,'bold'),onvalue=1,offvalue=0,variable=var41)
chip.grid(row=4,column=0,sticky=W)

donut=Checkbutton(snackFrame,text='donut',font=('ariel',15,'bold'),onvalue=1,offvalue=0,variable=var42)
donut.grid(row=5,column=0,sticky=W)

cold=Checkbutton(snackFrame,text='cold cofee',font=('ariel',15,'bold'),onvalue=1,offvalue=0,variable=var43)
cold.grid(row=6,column=0,sticky=W)

lime=Checkbutton(snackFrame,text='lime soda',font=('ariel',15,'bold'),onvalue=1,offvalue=0,variable=var44)
lime.grid(row=7,column=0,sticky=W)

malai=Checkbutton(snackFrame,text='rasmalai',font=('ariel',15,'bold'),onvalue=1,offvalue=0,variable=var45)
malai.grid(row=8,column=0,sticky=W)

pepsi=Checkbutton(snackFrame,text='pepsi',font=('ariel',15,'bold'),onvalue=1,offvalue=0,variable=var46)
pepsi.grid(row=9,column=0,sticky=W)

fro=Checkbutton(snackFrame,text='frootie',font=('ariel',15,'bold'),onvalue=1,offvalue=0,variable=var47)
fro.grid(row=10,column=0,sticky=W)

water=Checkbutton(snackFrame,text='water bottle',font=('ariel',15,'bold'),onvalue=1,offvalue=0,variable=var48)
water.grid(row=11,column=0,sticky=W)




# price for snacks

sam=Checkbutton(snackFrame,text='Rs-15',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var49,command=aa)
sam.grid(row=0,column=1,sticky=W)

egg=Checkbutton(snackFrame,text='Rs-20',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var50,command=bb)
egg.grid(row=1,column=1,sticky=W)

veg=Checkbutton(snackFrame,text='Rs-15',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var51,command=cc)
veg.grid(row=2,column=1,sticky=W)

roll=Checkbutton(snackFrame,text='Rs-30',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var52,command=dd)
roll.grid(row=3,column=1,sticky=W)

chip=Checkbutton(snackFrame,text='Rs-10',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var53,command=ee)
chip.grid(row=4,column=1,sticky=W)

donut=Checkbutton(snackFrame,text='Rs-50',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var54,command=ff)
donut.grid(row=5,column=1,sticky=W)

cold=Checkbutton(snackFrame,text='Rs-35',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var55,command=gg)
cold.grid(row=6,column=1,sticky=W)

lime=Checkbutton(snackFrame,text='Rs-25',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var56,command=hh)
lime.grid(row=7,column=1,sticky=W)

malai=Checkbutton(snackFrame,text='Rs-30',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var57,command=ii)
malai.grid(row=8,column=1,sticky=W)

pepsi=Checkbutton(snackFrame,text='Rs-35',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var58,command=jj)
pepsi.grid(row=9,column=1,sticky=W)

fro=Checkbutton(snackFrame,text='Rs-40',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var59,command=kk)
fro.grid(row=10,column=1,sticky=W)

water=Checkbutton(snackFrame,text='Rs-20',font=('ariel',11,'bold'),onvalue=1,offvalue=0,variable=var60,command=ll)
water.grid(row=11,column=1,sticky=W)



# entry feild for snacks

textsam=Entry(snackFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=gsam)
textsam.grid(row=0,column=2)

textegg=Entry(snackFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=gegg)
textegg.grid(row=1,column=2)

textveg=Entry(snackFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=gveg)
textveg.grid(row=2,column=2)

textroll=Entry(snackFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=groll)
textroll.grid(row=3,column=2)

textchip=Entry(snackFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=gchip)
textchip.grid(row=4,column=2)

textdonut=Entry(snackFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=gdonut)
textdonut.grid(row=5,column=2)

textcold=Entry(snackFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=gcold)
textcold.grid(row=6,column=2)

textlime=Entry(snackFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=glime)
textlime.grid(row=7,column=2)

textmalai=Entry(snackFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=gmalai)
textmalai.grid(row=8,column=2)

textpepsi=Entry(snackFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=gpepsi)
textpepsi.grid(row=9,column=2)

textfro=Entry(snackFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=gfro)
textfro.grid(row=10,column=2)

textwater=Entry(snackFrame,font=('ariel',15,'bold'),bd=3,width=5,state=DISABLED,textvariable=gwater)
textwater.grid(row=11,column=2)







# cost labels and entry feilds

labelCakes=Label(costFrame,text='cost of cakes',font=('ariel',16,'bold'),bg='firebrick',fg='white')
labelCakes.grid(row=0,column=0)

textCakes=Entry(costFrame,font=('ariel',16,'bold'),bd=5,width=13,state='readonly',textvariable=cakes)
textCakes.grid(row=0,column=1,padx=41)

labelSnacks=Label(costFrame,text='cost of snacks',font=('ariel',16,'bold'),bg='firebrick',fg='white')
labelSnacks.grid(row=1,column=0)

textSnacks=Entry(costFrame,font=('ariel',16,'bold'),bd=5,width=13,state='readonly',textvariable=snacks)
textSnacks.grid(row=1,column=1,padx=41)

labelSub=Label(costFrame,text='Sub total',font=('ariel',16,'bold'),bg='firebrick',fg='white')
labelSub.grid(row=2,column=0)

textSub=Entry(costFrame,font=('ariel',16,'bold'),bd=5,width=13,state='readonly',textvariable=sub)
textSub.grid(row=2,column=1,padx=41)

labeltax=Label(costFrame,text='service tax',font=('ariel',16,'bold'),bg='firebrick',fg='white')
labeltax.grid(row=0,column=2)

texttax=Entry(costFrame,font=('ariel',16,'bold'),bd=5,width=13,state='readonly',textvariable=tax)
texttax.grid(row=0,column=3,padx=41)

labeltot=Label(costFrame,text='TOTAL',font=('ariel',16,'bold'),bg='firebrick',fg='white')
labeltot.grid(row=1,column=2)

texttot=Entry(costFrame,font=('ariel',16,'bold'),bd=5,width=13,state='readonly',textvariable=tot)
texttot.grid(row=1,column=3,padx=41)







# buttons

buttonTotal=Button(buttonFrame,text='Total',font=('ariel',14,'bold'),fg='white',bg='red4',bd=3,command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReciept=Button(buttonFrame,text='Reciept',font=('ariel',14,'bold'),fg='white',bg='red4',bd=3,command=recieptbill)
buttonReciept.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('ariel',14,'bold'),fg='white',bg='red4',bd=3,command=save)
buttonSave.grid(row=0,column=2)

buttonSend=Button(buttonFrame,text='Send',font=('ariel',14,'bold'),fg='white',bg='red4',bd=3,command=send)
buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font=('ariel',14,'bold'),fg='white',bg='red4',bd=3,command=reset)
buttonReset.grid(row=0,column=4)





# text area

textReciept=Text(recieptFrame,font=('ariel',12,'bold'),bd=3,width=42,height=14)
textReciept.grid(row=0,column=0)






# calculater

operator=''
def Buttonclick(numbers):
    global operator
    operator=operator + numbers
    calcFeild.delete(0,END)
    calcFeild.insert(END,operator)

def clear():
    global operator
    operator=''
    calcFeild.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calcFeild.delete(0,END)
    calcFeild.insert(0,result)
    operator=''




calcFeild=Entry(calculaterFrame,font=('ariel',16,'bold'),width=32,bd=4)
calcFeild.grid(row=0,column=0,columnspan=4)

button7=Button(calculaterFrame,text='7',font=('ariel',16,'bold'),fg='yellow',bg='pink3',bd=4,width=6
                ,command=lambda:Buttonclick('7'))
button7.grid(row=1,column=0)

button8=Button(calculaterFrame,text='8',font=('ariel',16,'bold'),fg='yellow',bg='pink3',bd=4,width=6,command=lambda:Buttonclick('8'))
button8.grid(row=1,column=1)

button9=Button(calculaterFrame,text='9',font=('ariel',16,'bold'),fg='yellow',bg='pink3',bd=4,width=6,command=lambda:Buttonclick('9'))
button9.grid(row=1,column=2)

buttonplus=Button(calculaterFrame,text='+',font=('ariel',16,'bold'),fg='yellow',bg='pink3',bd=4,width=6,command=lambda:Buttonclick('+'))
buttonplus.grid(row=1,column=3)

button4=Button(calculaterFrame,text='4',font=('ariel',16,'bold'),fg='yellow',bg='pink3',bd=4,width=6,command=lambda:Buttonclick('4'))
button4.grid(row=2,column=0)

button5=Button(calculaterFrame,text='5',font=('ariel',16,'bold'),fg='red4',bg='white',bd=4,width=6,command=lambda:Buttonclick('5'))
button5.grid(row=2,column=1)

button6=Button(calculaterFrame,text='6',font=('ariel',16,'bold'),fg='red4',bg='white',bd=4,width=6,command=lambda:Buttonclick('6'))
button6.grid(row=2,column=2)

buttonminus=Button(calculaterFrame,text='-',font=('ariel',16,'bold'),fg='yellow',bg='pink3',bd=4,width=6,command=lambda:Buttonclick('-'))
buttonminus.grid(row=2,column=3)

button1=Button(calculaterFrame,text='1',font=('ariel',16,'bold'),fg='yellow',bg='pink3',bd=4,width=6,command=lambda:Buttonclick('1'))
button1.grid(row=3,column=0)

button2=Button(calculaterFrame,text='2',font=('ariel',16,'bold'),fg='red4',bg='white',bd=4,width=6,command=lambda:Buttonclick('2'))
button2.grid(row=3,column=1)

button3=Button(calculaterFrame,text='3',font=('ariel',16,'bold'),fg='red4',bg='white',bd=4,width=6,command=lambda:Buttonclick('3'))
button3.grid(row=3,column=2)

buttonmulti=Button(calculaterFrame,text='*',font=('ariel',16,'bold'),fg='yellow',bg='pink3',bd=4,width=6,command=lambda:Buttonclick('*'))
buttonmulti.grid(row=3,column=3)

buttonans=Button(calculaterFrame,text='Ans',font=('ariel',16,'bold'),fg='yellow',bg='pink3',bd=4,width=6,command=answer)
buttonans.grid(row=4,column=0)

buttonclr=Button(calculaterFrame,text='Clear',font=('ariel',16,'bold'),fg='yellow',bg='pink3',bd=4,width=6,command=clear)
buttonclr.grid(row=4,column=1)

button0=Button(calculaterFrame,text='0',font=('ariel',16,'bold'),fg='yellow',bg='pink3',bd=4,width=6,command=lambda:Buttonclick('0'))
button0.grid(row=4,column=2)

buttonslash=Button(calculaterFrame,text='/',font=('ariel',16,'bold'),fg='yellow',bg='pink3',bd=4,width=6,command=lambda:Buttonclick('/'))
buttonslash.grid(row=4,column=3)


root.mainloop()
