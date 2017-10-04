#Taylor Scafe
#CSIT/Python Files/Final
#12/09/2014
#Creates the card game Blackjack.

from Deck import *
from graphics import *
from random import *

deck = Deck()
win = GraphWin("Blackjack",800,500)
cardstore = []

def table():


    #Graphics Builder
    field = Rectangle(Point(0,0),Point(800,500))
    field.setFill("Green")
    field.draw(win)

    tempbox = Rectangle(Point(100,200),Point(700,250))
    tempbox.setFill('white')
    tempbox.draw(win)

    tempbox = Rectangle(Point(250,250),Point(550,300))
    tempbox.setFill('white')
    tempbox.draw(win)

    tempbox = Rectangle(Point(550,250),Point(600,300))
    tempbox.setFill('white')
    tempbox.draw(win)

    tempbox = Rectangle(Point(725,200),Point(800,250))
    tempbox.setFill('white')
    tempbox.draw(win)

    tempbox = Rectangle(Point(725,250),Point(800,300))
    tempbox.setFill('white')
    tempbox.draw(win)

    tempbox = Rectangle(Point(700,450),Point(800,500))
    tempbox.setFill('white')
    tempbox.draw(win)
    
    temptext = Text(Point(375,275),"Place bet here     $")
    temptext.draw(win)

    temptext = Text(Point(575,275),"Bet")
    temptext.draw(win)

    temptext = Text(Point(760,225),"Hit")
    temptext.draw(win)

    temptext = Text(Point(760,275),"Stay")
    temptext.draw(win)

    moneytext = Text(Point(750,475),'$ 500')
    moneytext.draw(win)

    
    
    betrule = Text(Point(400,225),'Black Jack pays 3 to 2\nDealer must hit on 16 and stand on all 17\'s')
    betrule.draw(win)



    #Money Setup

    money = 500


    cards(win,money,moneytext)

def cards(win,money,moneytext):
    bete = Entry(Point(500,275),10)
    bete.setFill("White")
    bete.draw(win)
    moneytext.undraw()
    moneytext = Text(Point(750,475),('$',money))
    moneytext.draw(win)

    mousestart = 1
    deck = Deck()
    player = Deck()
    dealer = Deck()
    deck.buildDeck()
    deck.setName()
    deck.shuffle()


    poscount = 0
    x = 75
    y = 400

    start = 0
    skip = 0
    errorbox = Rectangle(Point(600,0),Point(800,50))
    errorbox.setFill('white')
    errorbox.draw(win)
    errortext = Text(Point(700,25),('Welcome to BlackJack'))
    errortext.draw(win)


    while mousestart == 1:
        
        
        mouse = win.getMouse()
        if mouse.getX()> 550 and mouse.getX()<600:
            if mouse.getY()>250 and mouse.getY()<300:
                bet = bete.getText()
                if bet == '':
                    errorbox = Rectangle(Point(600,0),Point(800,50))
                    errorbox.setFill('white')
                    errorbox.draw(win)
                    errortext = Text(Point(700,25),('Must enter a value'))
                    errortext.draw(win)
                else:
                    bet = eval(bet)
                    if bet <= 500:
                        if bet <= money:
                            if bet > 0:
                                start = 1
                                mousestart = 0
                                errorbox.undraw()
                                errortext.undraw()

                            else:
                                errorbox.undraw()
                                errortext.undraw()
                                errorbox = Rectangle(Point(600,0),Point(800,50))
                                errorbox.setFill('white')
                                errorbox.draw(win)
                                errortext = Text(Point(700,25),('Bet Must be \nhigher than 0'))
                                errortext.draw(win)
                        else:
                            errorbox.undraw()
                            errortext.undraw()
                            errorbox = Rectangle(Point(600,0),Point(800,50))
                            errorbox.setFill('white')
                            errorbox.draw(win)
                            errortext = Text(Point(700,25),('You do not have \nthat much money'))
                            errortext.draw(win)
                    else:
                        errorbox.undraw()
                        errortext.undraw()
                        errorbox = Rectangle(Point(600,0),Point(800,50))
                        errorbox.setFill('white')
                        errorbox.draw(win)
                        errortext = Text(Point(700,25),(' Max bet is $500'))
                        errortext.draw(win)
                
                    
    
    while start == 1:
        if len(deck.getDeck())<15:    
            deck = Deck()
            deck.buildDeck()
            deck.setName()
            deck.shuffle()
        else:
            value = 0
            card = deck.draw()
            images(card,x,y,win,skip)
            #print("You got a(n)",card.getName())
            value = value + card.getValue()
            player.add(card)
            
            card = deck.draw()
            player.add(card)
            
            #print("You got a(n)",card.getName())
            value = value + card.getValue()
            x = x + 100
            images(card,x,y,win,skip)

            if value == 21:
                #print('Black Jack!!!')
                            
                dealbox = Rectangle(Point(600,0),Point(800,50))
                dealbox.setFill('white')
                dealbox.draw(win)
                dealtext = Text(Point(700,25),('Black Jack!!!'))
                dealtext.draw
                money = money + ((3*bet)//2)
                check = 0
                dealgo = 0
                start = 0
                cardblank = Image(Point((x+100),y),'blank.gif')
                cardblank.draw(win)
            else:    
                card = deck.draw()
                dealer.add(card)
                x = 75
                y = 100
                images(card,x,y,win,skip)
                #print("Dealer got a(n)",card.getName())
                cardblank = Image(Point(x+100,y),'cardImages\\b1fv.gif')
                cardblank.draw(win)
                card = deck.draw()
                dealer.add(card)


                start = 0
                x = 175
                y = 400
                check = 1


#Hitter and Checker
            while check == 1:
                mouse = win.getMouse()
                #choice = input("Would you like to hit or stay?\n")
                #if choice == "hit":Point(725,200),Point(800,250)
                if mouse.getX()> 725 and mouse.getX()<800:
                    if mouse.getY()>200 and mouse.getY()<250:
                        #print('hit')
                        card = deck.draw()
                        #print("\nYou got a(n)",card.getName())
                        value = value + card.getValue()
                        player.add(card)
                        x = x + 100
                        images(card,x,y,win,skip)



                        if value > 21:
                            for card in player.getDeck():
                                if card.getValue() == 11:
                                    card.setValue(1)
                                    value = value - 10
                                    break
                        if value > 21:
                            #print ("You bust\n")
                            dealbox = Rectangle(Point(600,0),Point(800,50))
                            dealbox.setFill('white')
                            dealbox.draw(win)
                            dealtext = Text(Point(700,25),('You Bust'))
                            dealtext.draw
                            money = money - bet
                            check = 0
                            dealgo= 0



                if mouse.getX()> 725 and mouse.getX()<800:
                    if mouse.getY()> 250 and mouse.getY()<300:
                        #print('stay')
                        check = 0
                        dealgo= 1
                    

            
            
#Dealer Code

            

            
            
            dvalue = 0
            while dealgo== 1:
                dealgo = 0
                card = dealer.getDeck()
                card = card[1]
                x = 175
                y = 100
                images(card,x,y,win,skip)
                for card in dealer.getDeck():
                    dvalue = dvalue + card.getValue()
                    if dvalue > 21:
                        if card.getValue() == 11:
                            card.setValue(1)
                            dvalue = dvalue - 10
                            break
                while dvalue <17:
                    card = deck.draw()
                    dvalue = dvalue + card.getValue()
                    dealer.add(card)
                    x = x + 100
                    images(card,x,y,win,skip)
                    #print("Dealer got a(n)",card.getName())
                    if dvalue > 21:
                        for card in player.getDeck():
                            if card.getValue() == 11:
                                card.setValue(1)
                                dvalue = dvalue - 10
                                break


                        
                dealbox = Rectangle(Point(600,0),Point(800,50))
                dealbox.setFill('white')
                dealbox.draw(win)
                            
                if dvalue > 21:
                    dealtext = Text(Point(700,25),('Dealer Busts'))
                    #print ('Dealer Busts')                
                    money = money + bet
                elif dvalue > value:
                    #print ("You lose!")
                    dealtext = Text(Point(700,25),('You Lose'))
                    money = money - bet
                elif dvalue == value:
                    #print("You Tie")
                    dealtext = Text(Point(700,25),('You Tie'))
                else:
                    #print("You win!")
                    money = money + bet
                    dealtext = Text(Point(700,25),('You Win!'))


            dealtext.draw(win)
            player = Deck()
            dealer = Deck()
            again = 1

            againbox = Rectangle(Point(725,150),Point(800,200))
            againbox.setFill('white')
            againbox.draw(win)

            yesbox = Rectangle(Point(725,200),Point(800,250))
            yesbox.setFill('white')
            yesbox.draw(win)

            againtext = Text(Point(760,175),"Again?")
            againtext.draw(win)

            nobox = Rectangle(Point(725,250),Point(800,300))
            nobox.setFill('white')
            nobox.draw(win)

            yestext = Text(Point(760,225),"Yes")
            yestext.draw(win)

            notext = Text(Point(760,275),"No")
            notext.draw(win)

            moneytext.undraw()
            moneytext = Text(Point(750,475),('$',money))
            moneytext.draw(win)
            
            while again == 1:
                mouse = win.getMouse()
                if mouse.getX()> 725 and mouse.getX()<800:
                    if mouse.getY()>200 and mouse.getY()<250:
                        again = 0
                        mousestart = 1
                        dealbox.undraw()
                        againbox.undraw()
                        yesbox.undraw()
                        nobox.undraw()

                        dealtext.undraw()
                        againtext.undraw()
                        yestext.undraw()
                        notext.undraw()
                        
                        skip = 1
                        images(card,x,y,win,skip)
                        cardblank.undraw()
                        cards(win,money,moneytext)
                        
                        
                if mouse.getX()> 725 and mouse.getX()<800:
                    if mouse.getY()> 250 and mouse.getY()<300:
                        win.close()
                        again = 0
        
        
            






def images(card,x,y,win,skip):
    if skip == 0:
        if card.getName() == 'Ace':
            data = '1'
             
             
            
        elif card.getName() == '2':
            data = '2'
             
            
        elif card.getName() == '3':
            data = '3'
             
            
        elif card.getName() == '4':
            data = '4'
             
            
        elif card.getName() == '5':
            data = '5'
             
            
        elif card.getName() == '6':
            data = '6'
             
             
            
        elif card.getName() == '7':
            data = '7'
             
             
            
        elif card.getName() == '8':
            data = '8'
             
             
            
        elif card.getName() == '9':
            data = '9'
             
             
            
        elif card.getName() == '10':
            data = '10'
             
             
            
        elif card.getName() == 'Jack':
            data = 'j'
             
             
            
        elif card.getName() == 'Queen':
            data = 'q'
             
             

        elif card.getName() == 'King':
            data = 'k'
    else:
        data = '0'
        
    rand = random(data,x,y,win)
    

def random(data,x,y,win):
    if data != '0':
        random = randrange(0,4)
        if random == 0:
            rand = 'h'
        elif random == 1:
            rand = 'd'
        elif random == 2:
            rand = 'c'
        else:
            rand = 's'

        rand = (rand) + (data) + ('.gif')

        cardimage = Image(Point(x,y),"cardImages\\"+rand)
        cardimage.draw(win)

        store = 1
    else:
        cardimage = 'null'
        store = 0

    clean(cardimage,win,store)
        

def clean(cardimage,win,store):
    if store == 1:
        global cardstore
        cardstore.append(cardimage)
    else:
        for cardimage in cardstore:
            cardimage = cardimage
            cardimage.undraw()
        

table()
