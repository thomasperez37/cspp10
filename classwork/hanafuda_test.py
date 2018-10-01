#http://hanafudahawaii.com/ginstructions.html
import random
class Card(object):
    def __init__(self,month,row,yaku1,yaku2,value):
        self.month = month
        self.row = row
        self.yaku1 = yaku1
        self.yaku2 = yaku2
        self.value = value
    def __str__(self):
        if self.row == '4th' and self.month == 'November':
            return "Card: The 4th card of November(the lightning card) which is worth 0 points. Yaku Slot 1: Empty. Yaku Slot 2: Empty."
        return "Card: The {} card of {} which is worth {} points. Yaku Slot 1: {}. Yaku Slot 2: {}.".format(self.row,self.month,self.value,self.yaku1,self.yaku2)
class Deck(object):
    def __init__(self):
        months = ['January','February','March','April','May','June','July','August','September','October','November','December']
        rows = ['1st','2nd','3rd','4th']
        yaku_letters = ["Empty","'i'","'ro'","'ha'","'ni'","'ho'","'he'","'to'","'chi'"]
        point_values = [0,5,10,20]
        self.cards = []
        for month in months:
            for row in rows:
                if row == '4th' or row == '3rd' and month != 'November':
                    c = Card(month,row,yaku_letters[0],yaku_letters[0],point_values[0])
                    self.cards.append(c)
                elif (row == '2nd' or row == '3rd') and month == 'November':
                    c = Card(month,row,yaku_letters[0],yaku_letters[0],point_values[1])
                    self.cards.append(c)
                elif month == 'November' and row == '1st' or month == 'December' and row == '2nd':
                    c = Card(month,row,yaku_letters[0],yaku_letters[0],point_values[2])
                    self.cards.append(c)
                elif month == 'December':
                    c = Card(month,row,yaku_letters[0],yaku_letters[0],point_values[3])
                elif month == 'January' and row == '1st':
                    c = Card(month,row,yaku_letters[0],yaku_letters[2],point_values[3])
                    self.cards.append(c)
                elif month == 'February' and row == '1st' or row == '2nd' and (month == 'January' or month == 'March'):
                    c = Card(month,row,yaku_letters[0],yaku_letters[3],point_values[2])
                    self.cards.append(c)
                elif month == 'February':
                    c = Card(month,row,yaku_letters[0],yaku_letters[2],point_values[1])
                    self.cards.append(c)
                elif month == 'March':
                    c = Card(month,row,yaku_letters[2],yaku_letters[1],point_values[3])
                    self.cards.append(c)
                elif row == '1st' and (month == 'April' or month == 'May' or month == 'July'):
                    c = Card(month,row,yaku_letters[0],yaku_letters[6],point_values[2])
                    self.cards.append(c)
                elif row == '2nd' and (month == 'April' or month == 'May'):
                    c = Card(month,row,yaku_letters[0],yaku_letters[7],point_values[1])
                    self.cards.append(c)
                elif row == '1st' and (month == 'June' or month == 'September' or month == 'October'):
                    c = Card(month,row,yaku_letters[0],yaku_letters[4],point_values[2])
                    self.cards.append(c)
                elif month == 'June':
                    c = Card(month,row,yaku_letters[0],yaku_letters[5],point_values[1])
                    self.cards.append(c)
                elif month == 'July':
                    c = Card(month,row,yaku_letters[8],yaku_letters[7],point_values[1])
                    self.cards.append(c)
                elif month == 'August' and row == '1st':
                    c = Card(month,row,yaku_letters[0],yaku_letters[1],point_values[3])
                    self.cards.append(c)
                elif month == 'August':
                    c = Card(month,row,yaku_letters[0],yaku_letters[8],point_values[1])
                    self.cards.append(c)
                elif month == 'September':
                    c = Card(month,row,yaku_letters[5],yaku_letters[1],point_values[1])
                    self.cards.append(c)
                elif month == 'October':
                    c = Card(month,row,yaku_letters[8],yaku_letters[5],point_values[1])
                    self.cards.append(c)