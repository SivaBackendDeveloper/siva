def drinks():#define the drinks
    menu={
         "1":"coke-------30 rs",
         "2":"thumpsup---30 rs",
         "3":"sprite-----30 rs",
         "4":"pepsi------30 rs"
         }
    for k,v in menu.items():
        print(k,v)
    n=int(input("what do you want ="))
    total=0
    while n in range(1,5):
        if n==1:
            print("you are choosen coke")
            q=int(input("how many quantity you want ="))
            cost=q*30
            break
        elif n==2:
            print("you are choosen thumpsup")
            q=int(input("how many quantity you want ="))
            cost=q*30
            break
        elif n==3:
            print("you are choosen sprite")
            q=int(input("how many quantity you want ="))
            cost=q*30
            break
        elif n==4:
            print("you are choosen pepsi")
            q=int(input("how many quantity you want ="))
            cost=q*30
            break

    total=total+cost
    return(total)



def roties():#define the roties
    menu={
         "1":"pulka-------------15 rs",
         "2":"thandhuri roti----20 rs",
         "3":"butternon roti----20 rs",
         "4":"kadak roti--------20 rs",
         "5":"chapati-----------15 rs"
         }
    for k,v in menu.items():
        print(k,v)
    n=int(input("what do you want ="))
    total=0
    while n!=0:
        if n==1:
            print("you are choosen pulka")
            q=int(input("how many quantity you want ="))
            cost=q*15
            break
        elif n==2:
            print("you are choosen thandhuri roti")
            q=int(input("how many quantity you want ="))
            cost=q*20
            break
        elif n==3:
            print("you are choosen bitternon roti")
            q=int(input("how many quantity you want ="))
            cost=q*20
            break
        elif n==4:
            print("you are choosen kadak roti")
            q=int(input("how many quantity you want ="))
            cost=q*20
            break
        elif n==5:
            print("you are choosen chapati")
            q=int(input("how many quantity you want ="))
            cost=q*15
            break
    total=total+cost
    return(total)
            
    

def curries(): #define the curries
    menu={
         "1":"chicken --------150 rs",
         "2":"c.boonless------180 rs",
         "3":"mutton----------200 rs",
         "4":"egg-------------120 rs",
         "5":"dhal------------100 rs",
         "6":"panner----------160 rs",
         "7":"kaaju masala----160 rs"
         }
    for k,v in menu.items():
        print(k,v)
    n=int(input("what do you want ="))
    total=0
    while n!=0:
        if n==1:
            print("you are choosen  chicken curry")
            q=int(input("how many quantity you want ="))
            cost=q*150
            break
        elif n==2:
            print("you are choosen  chicken boonless curry")
            q=int(input("how many quantity you want ="))
            cost=q*180
            break
        elif n==3:
            print("you are choosen  mutton curry")
            q=int(input("how many quantity you want ="))
            cost=q*200
            break
        elif n==4:
            print("you are choosen  egg curry")
            q=int(input("how many quantity you want ="))
            cost=q*120
            break
        elif n==5:
            print("you are choosen  dhal curry")
            q=int(input("how many quantity you want ="))
            cost=q*100
            break
        elif n==6:
            print("you are choosen  panner curry")
            q=int(input("how many quantity you want ="))
            cost=q*160
            break
        elif n==7:
            print("you are choosen  kaaju masala curry")
            q=int(input("how many quantity you want ="))
            cost=q*160
            break
    total=total+cost
    return(total)
            
    

def soups():#define the soups
    menu={
         "1":"chicken ----150",
         "2":"mutton------150",
         "3":"tomato------90",
         "4":"onion-------50"
         }
    for k,v in menu.items():
        print(k,v)
    n=int(input("what do you want ="))
    total=0
    while n!=0:
        if n==1:
            print("you are choosen  chicken soup")
            q=int(input("how many quantity you want ="))
            cost=q*150
            break
        elif n==2:
            print("you are choosen  mutton soup")
            q=int(input("how many quantity you want ="))
            cost=q*150
            
            break
        elif n==3:
            print("you are choosen  tomato soup")
            q=int(input("how many quantity you want ="))
            cost=q*90
            
            break
        elif n==4:
            print("you are choosen  onion soup")
            q=int(input("how many quantity you want ="))
            cost=q*50
            
            break
    total=total+cost
    return(total)

def starts():#define the starts 
    menu={
        "1":"chilli chicken-----120 rs",
        "2":"wings(1 pice)------40 rs",
        "3":"joints(1 pice)-----40 rs",
        "4":"lolipops(1 pice)---30 rs",
        "5":"lever fry (plate)--120 rs"
        }
    for k,v in menu.items():
        print(k,v)
    n=int(input("what do you want ="))
    total=0
    while n!=0:
        if n==1:
            print("you are choosen chilli chicken")
            q=int(input("how many quantity you want ="))
            cost=q*120
            
            break
        elif n==2:
            print("you are choosen wings fry")
            q=int(input("how many quantity you want ="))
            cost=q*40
            
            break
        elif n==3:
            print("you are choosen joints")
            q=int(input("how many quantity you want ="))
            cost=q*40
            
            break
        elif n==4:
            print("you are choosen chicken lolipops")
            q=int(input("how many quantity you want ="))
            cost=q*30
            
            break
        elif n==5:
            print("you are choosen chilli lever fry")
            q=int(input("how many quantity you want ="))
            cost=q*120
            
            break
        
    total=total+cost
    return(total)
            
def biryanies():#define the biryanies data
    menu={
        "1":"chicken dhum--------160 rs",
        "2":"chicken fry---------180 rs",
        "3":"chicken boonless----180 rs",
        "4":"chicken joint-------180 rs",
        "5":"chicken wings-------200 rs",
        "6":"mutto dhum----------200 rs",
        "7":"mutton boonless-----240 rs",
        "8":"motton keema--------250 rs"
        }
    for k,v in menu.items():
        print(k,v)
    n=int(input("what do you want ="))
    total=0
    while n!=0:
        if n==1:
            print("you are choosen chicken dhum biryani")
            q=int(input("how many quantity you want ="))
            cost=q*160
            
            break
        elif n==2:
            print("you are choosen chicken fry biryani")
            q=int(input("how many quantity you want ="))
            cost=q*180
            
            break
        elif n==3:
            print("you are choosen chicken boonless biryani")
            q=int(input("how many quantity you want ="))
            cost=q*180
            
            break
        elif n==4:
            print("you are choosen chicken joint biryani")
            q=int(input("how many quantity you want ="))
            cost=q*180
           
            break
        elif n==5:
            print("you are choosen chicken wings biryani")
            q=int(input("how many quantity you want ="))
            cost=q*200
            
            break
        elif n==6:
            print("you are choosen mutton dhum biryani")
            q=int(input("how many quantity you want ="))
            cost=q*200
            
            break
        elif n==7:
            print("you are choosen mutton boonless biryani")
            q=int(input("how many quantity you want ="))
            cost=q*240
            
            break
        elif n==8:
            print("you are choosen mutton keema biryani")
            q=int(input("how many quantity you want ="))
            cost=q*250
            
            break
        
    total=total+cost
    return(total)
    

                
total_bill=0            
def main_menu():#define the main menu
    print("------------------")
    print("---family dhaba---")
    print("==================")
   
    print("----MENU-----")
    print("-----------------")
    menu={
             "1":"strats",
             "2":"biryanies",
             "3":"soups",
             "4":"curries",
             "5":"roties",
             "6":"drinks",
             "0":"exit"
              }
    for k,v in menu.items():
        print(k,v)
    n=int(input("enter your option ="))
    global total_bill
    while n!=0:
        if n==1:
            total_bill=total_bill+starts()#accessing the starts data
            break
        elif n==2:
            total_bill=total_bill+biryanies() #accessing the biryanies data
            break
        elif n==3:
            total_bill=total_bill+soups()#accessing the soups data
            break
        elif n==4:
            total_bill=total_bill+curries()#accessing the curries data
            break
        elif n==5:
            total_bill=total_bill+roties()#accessing the roties data
            break
        elif n==6:
            total_bill=total_bill+drinks()#accessing the drinks data
            break
        elif n==0:
            break
    print("do u wanna continue")
    ch=input("enter y/n ( press 's' exit) =")
   
    '''
    press y it will goes to main menu
    press n it will goes to calculating total bill
    press s to exit
    '''
        
    if ch=='y':
               main_menu()# accessing the main menu
    elif ch=='n':
        while ch=='n':
            
            print("=========================")
            print("                           ")
            print("you are total bill =",total_bill," rs")
            print("=========================") 
            print("thank you for ordered")
            print("**************************")
            print("     visit again ")
            print("   have a great day")
            print("---------------------------")
            from datetime import datetime
            today=datetime.today()
            print("      ",today)
            break
    else :
        while ch=='s':# complete exit
            break
   
    
    
    
main_menu() #accessing the menu data     
        
