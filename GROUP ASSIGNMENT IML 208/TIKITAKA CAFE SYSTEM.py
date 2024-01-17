from tkinter import *
from tkinter import messagebox
import random, os, tempfile, smtplib
#functionality Part

def clear ():
    watermelonsparkleEntry.delete(0,END)
    mojitolimeEntry.delete(0,END)
    coolingmintEntry.delete(0,END)
    bluemoonEntry.delete(0,END)
    popsodaberryEntry.delete(0,END)
    grasshoneyEntry.delete(0,END)
    
    caramelmacchiatoEntry.delete(0,END)
    matchalatteEntry.delete(0,END)
    berrycanoEntry.delete(0,END)
    vanillafelatteEntry.delete(0,END)
    cookiesftmochaEntry.delete(0,END)
    seasaltfecreameEntry.delete(0,END)

    cinnamonrollEntry.delete(0,END)
    croissantEntry.delete(0,END)
    croffleEntry.delete(0,END)
    macaroonEntry.delete(0,END)
    eggtartEntry.delete(0,END)
    pancakeEntry.delete(0,END)

    watermelonsparkleEntry.insert(0,0)
    mojitolimeEntry.insert(0,0)
    coolingmintEntry.insert(0,0)
    bluemoonEntry.insert(0,0)
    popsodaberryEntry.insert(0,0)
    grasshoneyEntry.insert(0,0)
    
    caramelmacchiatoEntry.insert(0,0)
    matchalatteEntry.insert(0,0)
    berrycanoEntry.insert(0,0)
    vanillafelatteEntry.insert(0,0)
    cookiesftmochaEntry.insert(0,0)
    seasaltfecreameEntry.insert(0,0)

    cinnamonrollEntry.insert(0,0)
    croissantEntry.insert(0,0)
    croffleEntry.insert(0,0)
    macaroonEntry.insert(0,0)
    eggtartEntry.insert(0,0)
    pancakeEntry.insert(0,0)

    refreshertaxEntry.delete(0,END)
    coffeetaxEntry.delete(0,END)
    desserttaxEntry.delete(0,END)

    refresherpriceEntry.delete(0,END)
    coffeepriceEntry.delete(0,END)
    dessertpriceEntry.delete(0,END)

    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billnumberEntry.delete(0,END)

    textarea.delete(1.0,END)

def send_email():
    def send_gmail():
        try:
            ob=smtplib.SMTP('smpt.gmail.com', 587)
            ob.starttls()
            ob.login(senderEntry.get(),passwordEntry.get())
            message=email_textarea(1.0, END)
            ob.sendmail(senderEntry.get(),recieverEntry.get(),message)
            ob.quit()
            messagebox.showinfo('Success', 'Bill is successfully sent', parent=root1)
        except :
            messagebox.showerror('Error', 'Something went wrong, Please try again', parent=root1)

    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        root1=Toplevel()
        root.title('send gmail')
        root1.config(bg='DeepPink3')
        root1.resizable(0,0)

        senderFrame=LabelFrame(root1, text='SENDER', font=('arial', 16, 'bold'), bd=6, bg='DeepPink3', fg='white')
        senderFrame.grid(row=0, column=0, padx=40, pady=20)

        senderLabel=Label(senderFrame,text="Sender's Email", font=('arial', 14, 'bold'),bg='DeepPink3', fg='white')
        senderLabel.grid(row=0, column=0, padx=10, pady=8)

        senderEntry=Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        senderEntry.grid(row=0, column=1, padx=10, pady=8)

        passwordLabel=Label(senderFrame,text="Password", font=('arial', 14, 'bold'),bg='DeepPink3', fg='white')
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)

        passwordEntry=Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE, show='*')
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        recipientFrame=LabelFrame(root1, text='RECIPIENT', font=('arial', 16, 'bold'), bd=6, bg='DeepPink3', fg='white')
        recipientFrame.grid(row=1, column=0, padx=40, pady=20)

        recieverLabel=Label(recipientFrame,text="Email Address", font=('arial', 14, 'bold'),bg='DeepPink3', fg='white')
        recieverLabel.grid(row=0, column=0, padx=10, pady=8)

        recieverEntry=Entry(recipientFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        recieverEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel=Label(recipientFrame,text="Message", font=('arial', 14, 'bold'),bg='DeepPink3', fg='white')
        messageLabel.grid(row=1, column=0, padx=10, pady=8)

        email_textarea=Text(recipientFrame, font=('arial', 14, 'bold'), bd=2, relief=SUNKEN,
                            width=42, height=11)
        email_textarea.grid(row=2, column=0, columnspan=2)
        email_textarea.delete(1.0, END)
        email_textarea.insert(END, textarea.get(1.0, END).replace('=','').replace('-','').replace('\t\t\t', '\t'))

        sendButton=Button(root1, text='SEND', font=('arial', 16, 'bold'), width=15, command=send_gmail)
        sendButton.grid(row=3, column=0, pady=20)

        root1.mainloop()


def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0, END))
        os.startfile(file, 'print')


def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billnumberEntry.get():
            f=open(f'bills/{i}', 'r')
            textarea.delete(1.0, END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
    else:
        messagebox.showerror('Error', 'Invalid Bill Number')

if not os.path.exists('bills'):
    os.mkdir('bills')

def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm', 'Do you want to save the bill?')
    if result: 
        bill_content=textarea.get(1.0, END)
        file=open(f'bills/{billnumber}.txt', 'w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success', f'bill number{billnumber} is saved successfully')
        billnumber = random.randint (500,1000)


billnumber=random.randint(500,1000)

def bill_area():
    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error', 'Customer Details Are Required')
    elif refresherpriceEntry.get()=='' and coffeepriceEntry.get()=='' and dessertpriceEntry.get()=='':
        messagebox.showerror('Error', 'No Product Are Selected')
    elif refresherpriceEntry.get()=='RM 0' and coffeepriceEntry.get()=='RM 0' and dessertpriceEntry.get()=='RM 0':
        messagebox.showerror('Error', 'No Products Are Selected')
    else:
        textarea.delete(1.0, END)
    
        textarea.insert(END, '\t\t\t**WELCOME CUSTOMER**\n')
        textarea.insert(END, f'\nBill Number : {billnumber}\n')
        textarea.insert(END, f'\nCustomer Name : {nameEntry.get()}\n')
        textarea.insert(END, f'\nPhone Number : {phoneEntry.get()}\n')
        textarea.insert(END, '\n===================================================================')
        textarea.insert(END, 'Product\t\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END, '\n===================================================================')
        if watermelonsparkleEntry.get()!='0':
       
            textarea.insert(END, f'\nWatermelon Sparkle\t\t\t\t{watermelonsparkleEntry.get()}\t\t\tRM{melonprice}')
        if mojitolimeEntry.get()!='0':
            textarea.insert(END, f'\nMojito Lime\t\t\t\t{mojitolimeEntry.get()}\t\t\tRM{mojitoprice}')
        if coolingmintEntry.get()!='0':
            textarea.insert(END, f'\nCooling Mint\t\t\t\t{coolingmintEntry.get()}\t\t\tRM{mintprice}')
        if bluemoonEntry.get()!='0':
            textarea.insert(END, f'\nBlue Moon\t\t\t\t{bluemoonEntry.get()}\t\t\tRM{blueprice}')
        if popsodaberryEntry.get()!='0':
            textarea.insert(END, f'\nPop Soda Berry\t\t\t\t{popsodaberryEntry.get()}\t\t\tRM{popsodaprice}')
        if grasshoneyEntry.get()!='0':
            textarea.insert(END, f'\nGrass Honey\t\t\t\t{grasshoneyEntry.get()}\t\t\tRM{grassprice}')

        if caramelmacchiatoEntry.get()!='0':
            textarea.insert(END, f'\nCaramel Macchiato\t\t\t\t{caramelmacchiatoEntry.get()}\t\t\tRM{caramelprice}')
        if matchalatteEntry.get()!='0':
            textarea.insert(END, f'\nMatcha Latte\t\t\t\t{matchalatteEntry.get()}\t\t\tRM{matchaprice}')
        if berrycanoEntry.get()!='0':
            textarea.insert(END, f'\nBerry Cano\t\t\t\t{berrycanoEntry.get()}\t\t\tRM{canoprice}')
        if vanillafelatteEntry.get()!='0':
            textarea.insert(END, f'\nVanilla Latte\t\t\t\t{vanillafelatteEntry.get()}\t\t\tRM{vanillaprice}')
        if cookiesftmochaEntry.get()!='0':
            textarea.insert(END, f'\nCookies Ft Mocha\t\t\t\t{cookiesftmochaEntry.get()}\t\t\tRM{cookiesprice}')
        if seasaltfecreameEntry.get()!='0':
            textarea.insert(END, f'\nSea Salt Creame\t\t\t\t{seasaltfecreameEntry.get()}\t\t\tRM{seasaltprice}')

        if cinnamonrollEntry.get()!='0':
            textarea.insert(END, f'\nCinnamon Roll\t\t\t\t{cinnamonrollEntry.get()}\t\t\tRM{cinnamonprice}')
        if croissantEntry.get()!='0':
            textarea.insert(END, f'\nCroissant\t\t\t\t{croissantEntry.get()}\t\t\tRM{croissantprice}')
        if croffleEntry.get()!='0':
            textarea.insert(END, f'\nCroffle\t\t\t\t{croffleEntry.get()}\t\t\tRM{croffleprice}')
        if macaroonEntry.get()!='0':
            textarea.insert(END, f'\nMacaroon\t\t\t\t{macaroonEntry.get()}\t\t\tRM{macaroonprice}')
        if eggtartEntry.get()!='0':
            textarea.insert(END, f'\nEgg Tart\t\t\t\t{eggtartEntry.get()}\t\t\tRM{eggtartprice}')
        if pancakeEntry.get()!='0':
            textarea.insert(END, f'\nPancake\t\t\t\t{pancakeEntry.get()}\t\t\tRM{pancakeprice}')
        textarea.insert(END, '\n-------------------------------------------------------------------')

        if refreshertaxEntry.get()!='RM 0.0' :
            textarea.insert(END, f'\nRefresher Tax\t\t\t\t\t\t\t{refreshertaxEntry.get()}')
        if coffeetaxEntry.get()!='RM 0.0' :
            textarea.insert(END, f'\nCoffee Tax\t\t\t\t\t\t\t{coffeetaxEntry.get()}')
        if desserttaxEntry.get()!='RM 0.0' :
            textarea.insert(END, f'\nDessert Tax\t\t\t\t\t\t\t{desserttaxEntry.get()}')
        textarea.insert(END, '\n===================================================================')
        textarea.insert(END, f'\n\nTotal Bill \t\t\t\t\t\t\tRM{totalbill}')
        textarea.insert(END, '\n===================================================================')
        save_bill()



def total():
    global melonprice, mojitoprice, mintprice, blueprice, popsodaprice, grassprice
    global caramelprice, matchaprice, canoprice, vanillaprice, cookiesprice, seasaltprice
    global cinnamonprice, croissantprice, croffleprice, macaroonprice, eggtartprice, pancakeprice
    global totalbill


    #refresher price calculation
    melonprice=int(watermelonsparkleEntry.get())*15
    mojitoprice=int(mojitolimeEntry.get())*10
    mintprice=int(coolingmintEntry.get())*10
    blueprice=int(bluemoonEntry.get())*20
    popsodaprice=int(popsodaberryEntry.get())*25
    grassprice=int(grasshoneyEntry.get())*20

    totalrefresherprice= melonprice+mojitoprice+mintprice+blueprice+popsodaprice+grassprice
    refresherpriceEntry.delete(0,END)
    refresherpriceEntry.insert(0,'RM' + str(totalrefresherprice))
    refreshertax=totalrefresherprice*0.4
    refreshertaxEntry.delete(0, END)
    refreshertaxEntry.insert(0,'RM' + str( refreshertax))

    #coffee price calculation
    caramelprice=int(caramelmacchiatoEntry.get())*20
    matchaprice=int(matchalatteEntry.get())*35
    canoprice=int(berrycanoEntry.get())*15
    vanillaprice=int(vanillafelatteEntry.get())*15
    cookiesprice=int(cookiesftmochaEntry.get())*30
    seasaltprice=int(seasaltfecreameEntry.get())*38

    totalcoffeeprice= caramelprice+matchaprice+canoprice+vanillaprice+cookiesprice+seasaltprice
    coffeepriceEntry.delete(0,END)
    coffeepriceEntry.insert(0,'RM'+ str(totalcoffeeprice))
    coffeetax=totalcoffeeprice*0.4
    coffeetaxEntry.delete(0, END)
    coffeetaxEntry.insert(0,'RM' + str( coffeetax))

    #dessert price calculaation
    cinnamonprice=int(cinnamonrollEntry.get())*10
    croissantprice=int(croissantEntry.get())*15
    eggtartprice=int(eggtartEntry.get())*6
    macaroonprice=int(macaroonEntry.get())*5
    croffleprice=int(croffleEntry.get())*20
    pancakeprice=int(pancakeEntry.get())*20

    totaldessertprice= cinnamonprice+croissantprice+eggtartprice+macaroonprice+croffleprice+pancakeprice
    dessertpriceEntry.delete(0,END)
    dessertpriceEntry.insert(0, 'RM' + str(totaldessertprice))
    desserttax=totaldessertprice*0.4
    desserttaxEntry.delete(0, END)
    desserttaxEntry.insert(0,'RM' + str( desserttax))

    totalbill=totalrefresherprice+totalcoffeeprice+totaldessertprice+refreshertax+coffeetax+desserttax


#GUI Part
root = Tk()
root.title('Tiki Taka Cafe System')
root.geometry('1600x900')
headingLabel=Label(root, text = 'Tiki Taka Cafe', font=('times new roman', 30, 'bold')
                   , bg = 'DeepPink3', fg='gold',bd=12, relief=GROOVE)
headingLabel.pack(fill=X, pady=10)

customer_details_frame=LabelFrame(root, text='CUSTOMER DETAILS', font=('times new roman', 15, 'bold'),
                                  fg='gold', bd=8, relief=GROOVE, bg='DeepPink3')
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame, text='Name', font=('times new roman', 15, 'bold'),
                fg='black')
nameLabel.grid(row=0, column=0, padx=20)

nameEntry=Entry(customer_details_frame, font=('arial', 15) , bd=7, width=18)
nameEntry.grid(row=0, column=1, padx=8)

phoneLabel=Label(customer_details_frame, text='Phone Number', font=('times new roman', 15, 'bold'),
                fg='black')
phoneLabel.grid(row=0, column=2, padx=20, pady=2)

phoneEntry=Entry(customer_details_frame, font=('arial', 15) , bd=7, width=18)
phoneEntry.grid(row=0, column=3, padx=8)

billnumberLabel=Label(customer_details_frame, text='Bill Number', font=('times new roman', 15, 'bold'),
                fg='black')
billnumberLabel.grid(row=0, column=4, padx=20, pady=2)

billnumberEntry=Entry(customer_details_frame, font=('arial', 15) , bd=7, width=18)
billnumberEntry.grid(row=0, column=5, padx=8)

searchButton=Button(customer_details_frame, text='SEARCH', 
                    font=('arial', 12, 'bold'), bd=7, width=10, command=search_bill)
searchButton.grid(row=0, column=6, padx=20, pady=8)

productsFrame=Frame(root)
productsFrame.pack(pady=10)

refresherFrame=LabelFrame(productsFrame, text='REFRESHERs',font=('times new roman', 15, 'bold'),
                                  fg='gold', bd=8, relief=GROOVE, bg='DeepPink3')
refresherFrame.grid(row=0, column=0)

watermelonsparkleLabel=Label(refresherFrame, text='Watermelon Sparkle',font=('times new roman', 15, 'bold'),
                                  fg='white', bd=8, bg='DeepPink3')
watermelonsparkleLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

watermelonsparkleEntry= Entry(refresherFrame, font=('times new roman', 15, "bold"), width=10, bd=5)
watermelonsparkleEntry.grid(row=0, column=1, pady=9, padx=10)
watermelonsparkleEntry.insert(0,0)

mojitolimeLabel=Label(refresherFrame, text='Mojito Lime',font=('times new roman', 15, 'bold'),
                                  fg='white', bd=8, bg='DeepPink3')
mojitolimeLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

mojitolimeEntry= Entry(refresherFrame, font=('times new roman', 15, "bold"), width=10, bd=5)
mojitolimeEntry.grid(row=1, column=1, pady=9, padx=10)
mojitolimeEntry.insert(0,0)

coolingmintLabel=Label(refresherFrame, text='Cooling Mint',font=('times new roman', 15, 'bold'),
                                  fg='white', bd=8, bg='DeepPink3')
coolingmintLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

coolingmintEntry= Entry(refresherFrame, font=('times new roman', 15, "bold"), width=10, bd=5)
coolingmintEntry.grid(row=2, column=1, pady=9, padx=10)
coolingmintEntry.insert(0,0)

bluemoonLabel=Label(refresherFrame, text='Blue Moon',font=('times new roman', 15, 'bold'),
                                  fg='white', bd=8, bg='DeepPink3')
bluemoonLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

bluemoonEntry= Entry(refresherFrame, font=('times new roman', 15, "bold"), width=10, bd=5)
bluemoonEntry.grid(row=3, column=1, pady=9, padx=10)
bluemoonEntry.insert(0,0)

popsodaberryLabel=Label(refresherFrame, text='Pop Soda Berry',font=('times new roman', 15, 'bold'),
                                  fg='white', bd=8, bg='DeepPink3')
popsodaberryLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

popsodaberryEntry= Entry(refresherFrame, font=('times new roman', 15, "bold"), width=10, bd=5)
popsodaberryEntry.grid(row=4, column=1, pady=9, padx=10)
popsodaberryEntry.insert(0,0)

grasshoneyLabel=Label(refresherFrame, text='Grass Honey',font=('times new roman', 15, 'bold'),
                                  fg='white', bd=8, bg='DeepPink3')
grasshoneyLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

grasshoneyEntry= Entry(refresherFrame, font=('times new roman', 15, "bold"), width=10, bd=5)
grasshoneyEntry.grid(row=5, column=1, pady=9, padx=10)
grasshoneyEntry.insert(0,0)

coffeeFrame=LabelFrame(productsFrame, text='COFFEEs',font=('times new roman', 15, 'bold'),
                                  fg='gold', bd=8, bg='DeepPink3')
coffeeFrame.grid(row=0, column=1)

caramelmacchiatoLabel=Label(coffeeFrame, text='Ca Macci',font=('times new roman', 15, 'bold'),
                                  fg='white', bd=8, bg='DeepPink3')
caramelmacchiatoLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

caramelmacchiatoEntry= Entry(coffeeFrame, font=('times new roman', 15, "bold"), width=10, bd=5)
caramelmacchiatoEntry.grid(row=0, column=1, pady=9, padx=10)
caramelmacchiatoEntry.insert(0,0)

matchalatteLabel=Label(coffeeFrame, text='Matcha Whimp',font=('times new roman', 15, 'bold'),
                                  fg='white', bd=8, bg='DeepPink3')
matchalatteLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

matchalatteEntry= Entry(coffeeFrame, font=('times new roman', 15, "bold"), width=10, bd=5)
matchalatteEntry.grid(row=1, column=1, pady=9, padx=10)
matchalatteEntry.insert(0,0)

berrycanoLabel=Label(coffeeFrame, text='Berry Cano',font=('times new roman', 15, 'bold'),
                                  fg='white', bd=8, bg='DeepPink3')
berrycanoLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

berrycanoEntry= Entry(coffeeFrame, font=('times new roman', 15, "bold"), width=10, bd=5)
berrycanoEntry.grid(row=2, column=1, pady=9, padx=10)
berrycanoEntry.insert(0,0)

vanillafelatteLabel=Label(coffeeFrame, text='Vanilla Fe Te',font=('times new roman', 15, 'bold'),
                                  fg='white', bd=8, bg='DeepPink3')
vanillafelatteLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

vanillafelatteEntry= Entry(coffeeFrame, font=('times new roman', 15, "bold"), width=10, bd=5)
vanillafelatteEntry.grid(row=3, column=1, pady=9, padx=10)
vanillafelatteEntry.insert(0,0)

cookiesftmochaLabel=Label(coffeeFrame, text='Cookies Moc',font=('times new roman', 15, 'bold'),
                                  fg='white', bd=8, bg='DeepPink3')
cookiesftmochaLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

cookiesftmochaEntry= Entry(coffeeFrame, font=('times new roman', 15, "bold"), width=10, bd=5)
cookiesftmochaEntry.grid(row=4, column=1, pady=9, padx=10)
cookiesftmochaEntry.insert(0,0)

seasaltfecreameLabel=Label(coffeeFrame, text='Seasalt Fe',font=('times new roman', 15, 'bold'),
                                  fg='white', bd=8, bg='DeepPink3')
seasaltfecreameLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

seasaltfecreameEntry= Entry(coffeeFrame, font=('times new roman', 15, "bold"), width=10, bd=5)
seasaltfecreameEntry.grid(row=5, column=1, pady=9, padx=10)
seasaltfecreameEntry.insert(0,0)

dessertFrame=LabelFrame(productsFrame, text='DESSERTs',font=('times new roman', 15, 'bold'),
                                  fg='gold', bd=8, bg='DeepPink3')
dessertFrame.grid(row=0, column=2)

cinnamonrollLabel=Label(dessertFrame, text='Moni Roll',font=('times new roman', 15, 'bold'),
                                  fg='white', bd=8, bg='DeepPink3')
cinnamonrollLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

cinnamonrollEntry= Entry(dessertFrame, font=('times new roman', 15, "bold"), width=10, bd=5)
cinnamonrollEntry.grid(row=0, column=1, pady=9, padx=10)
cinnamonrollEntry.insert(0,0)

croissantLabel=Label(dessertFrame, text='Croissant',font=('times new roman', 15, 'bold'),
                                  fg='white', bd=8, bg='DeepPink3')
croissantLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

croissantEntry= Entry(dessertFrame, font=('times new roman', 15, "bold"), width=10, bd=5)
croissantEntry.grid(row=1, column=1, pady=9, padx=10)
croissantEntry.insert(0,0)

macaroonLabel=Label(dessertFrame, text='Macaroon',font=('times new roman', 15, 'bold'),
                                  fg='white', bd=8, bg='DeepPink3')
macaroonLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

macaroonEntry= Entry(dessertFrame, font=('times new roman', 15, "bold"), width=10, bd=5)
macaroonEntry.grid(row=2, column=1, pady=9, padx=10)
macaroonEntry.insert(0,0)

eggtartLabel=Label(dessertFrame, text='Egg Tart',font=('times new roman', 15, 'bold'),
                                  fg='white', bd=8, bg='DeepPink3')
eggtartLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

eggtartEntry= Entry(dessertFrame, font=('times new roman', 15, "bold"), width=10, bd=5)
eggtartEntry.grid(row=3, column=1, pady=9, padx=10)
eggtartEntry.insert(0,0)

croffleLabel=Label(dessertFrame, text='Croffle',font=('times new roman', 15, 'bold'),
                                  fg='white', bd=8, bg='DeepPink3')
croffleLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

croffleEntry= Entry(dessertFrame, font=('times new roman', 15, "bold"), width=10, bd=5)
croffleEntry.grid(row=4, column=1, pady=9, padx=10)
croffleEntry.insert(0,0)

pancakeLabel=Label(dessertFrame, text='Pancake',font=('times new roman', 15, 'bold'),
                                  fg='white', bd=8, bg='DeepPink3')
pancakeLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

pancakeEntry= Entry(dessertFrame, font=('times new roman', 15, "bold"), width=10, bd=5)
pancakeEntry.grid(row=5, column=1, pady=9, padx=10)
pancakeEntry.insert(0,0)

billframe= Frame(productsFrame, bd=8, relief=GROOVE)
billframe.grid(row=0, column=3, padx=10)

billareaLabel=Label(billframe,text='Bill Area',font=('times new roman', 15, "bold"), bd=7, relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
textarea=Text(billframe,height=20, width=67, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root, text='BILL MENU',font=('times new roman', 15, 'bold'),
                                  fg='gold', bd=8, relief=GROOVE, bg='DeepPink3')
billmenuFrame.pack(fill=X)

refresherpriceLabel=Label(billmenuFrame, text='Refresher Price',font=('times new roman', 16, 'bold'),
                                  fg='white', bd=8, bg='DeepPink3')
refresherpriceLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

refresherpriceEntry= Entry(billmenuFrame, font=('times new roman', 16, "bold"), width=10, bd=5)
refresherpriceEntry.grid(row=0, column=1, pady=9, padx=10)

coffeepriceLabel=Label(billmenuFrame, text='Coffee Price',font=('times new roman', 16, 'bold'),
                                  fg='white', bd=8, bg='DeepPink3')
coffeepriceLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

coffeepriceEntry= Entry(billmenuFrame, font=('times new roman', 16, "bold"), width=10, bd=5)
coffeepriceEntry.grid(row=1, column=1, pady=9, padx=10)

dessertpriceLabel=Label(billmenuFrame, text= 'Dessert Price',font=('times new roman', 16, 'bold'),
                                  fg='white', bd=8, bg='DeepPink3')
dessertpriceLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

dessertpriceEntry= Entry(billmenuFrame, font=('times new roman', 16, "bold"), width=10, bd=5)
dessertpriceEntry.grid(row=2, column=1, pady=9, padx=10)

refreshertaxLabel=Label(billmenuFrame, text='Refresher Tax',font=('times new roman', 16, 'bold'),
                                  fg='white', bd=8, bg='DeepPink3')
refreshertaxLabel.grid(row=0, column=2, pady=9, padx=10, sticky='w')

refreshertaxEntry= Entry(billmenuFrame, font=('times new roman', 16, "bold"), width=10, bd=5)
refreshertaxEntry.grid(row=0, column=3, pady=9, padx=10)

coffeetaxLabel=Label(billmenuFrame, text='Coffee Tax',font=('times new roman', 16, 'bold'),
                                  fg='white', bd=8, bg='DeepPink3')
coffeetaxLabel.grid(row=1, column=2, pady=9, padx=10, sticky='w')

coffeetaxEntry= Entry(billmenuFrame, font=('times new roman', 16, "bold"), width=10, bd=5)
coffeetaxEntry.grid(row=1, column=3, pady=9, padx=10)

desserttaxLabel=Label(billmenuFrame, text= 'Dessert Tax',font=('times new roman', 16, 'bold'),
                                  fg='white', bd=8, bg='DeepPink3')
desserttaxLabel.grid(row=2, column=2, pady=9, padx=10, sticky='w')

desserttaxEntry= Entry(billmenuFrame, font=('times new roman', 16, "bold"), width=10, bd=5)
desserttaxEntry.grid(row=2, column=3, pady=9, padx=10)

buttonFrame=Frame(billmenuFrame, bd=8, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=3)

totalButton=Button(buttonFrame, text='Total', font=('arial', 16, 'bold'), bg='DeepPink3', fg='white' , 
                   bd=5, width=11, pady=10, command=total)
totalButton.grid(row=0, column=0, pady=20, padx=5)

billButton=Button(buttonFrame, text='Bill', font=('arial', 16, 'bold'), bg='DeepPink3', fg='white' , 
                   bd=5, width=11, pady=10, command=bill_area)
billButton.grid(row=0, column=1, pady=20, padx=5)

emailButton=Button(buttonFrame, text='Email', font=('arial', 16, 'bold'), bg='DeepPink3', fg='white' , 
                   bd=5, width=11, pady=10, command=send_email)
emailButton.grid(row=0, column=2, pady=20, padx=5)

printButton=Button(buttonFrame, text='Print', font=('arial', 16, 'bold'), bg='DeepPink3', fg='white' , 
                   bd=5, width=11, pady=10, command=print_bill)
printButton.grid(row=0, column=3, pady=20, padx=5)

clearButton=Button(buttonFrame, text='Clear', font=('arial', 16, 'bold'), bg='DeepPink3', fg='white' , 
                   bd=5, width=11, pady=10, command=clear)
clearButton.grid(row=0, column=4, pady=20, padx=5)

root.mainloop()