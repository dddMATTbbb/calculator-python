#if the acitve is set to 1 the loop runs if you set it on 0 the loop stops so to the whole program
active = 1
#ads x and y toghter
def plus(x, y):
    return(x + y)
#subtract y from x
def min(x, y):
    return(x - y)
#times x and y
def time(x, y):
        return(x * y)
#divide x and y
def div(x, y):
        return(x / y)
#calculate the circumference from a circle, straal is the variable for the radius from the circle, and dia for if were using the radius or
#diameter
def omtrek_circel(straal, dia = True):
        if dia == True:
                return(3.1415926535 * straal)
        elif dia == False:
                return(2 * 3.1415926535 * straal)
        else:
                print("there is a error occur")
                exit()

while active == 1:
        print("\n","*****CALCULATOR*****")
        print("1 = +")
        print("2 = -")
        print("3 = *")
        print("4 = /")
        print("5 = caculate circumference from circle")
        print("exit = exit")
        print("********************")

        choice = input("enter your choise: ")

        if choice == "1":
                Xp = float(input("first diged: "))
                Yp = float(input("second diged: "))
                answerp = plus(Xp, Yp)
                print(Xp, "+", Yp, "= ", answerp)
        elif choice == "2":
                Xm = float(input("first diged: "))
                Ym = float(input("second diged: "))
                answerm = min(Xm, Ym)
                print(Xm, "+", Ym, "= ", answerm)
        elif choice == "3":
                Xt = float(input("first diged: "))
                Yt = float(input("second diged: "))
                answert = time(Xt, Yt)
                print(Xt, "*", Yt, "= ", answert)
        elif choice == "4":
                Xd = float(input("first diged: "))
                Yd = float(input("second diged: "))
                answerd = div(Xd, Yd)
                print(Xd, "/", Yd, "= ", answerd)
        elif choice == "5":
                dia = input("are we using the diameter or radius. bye diamter write: 'True' bye radius write: 'False: '")
                if dia == "True":
                        dia = float(input("write the diameter of the circle: "))
                        answerdia = omtrek_circel(dia, True)
                        print("the circumference of the circle= ", answerdia)
                elif dia == "False":
                        rad = float(input("write the radius of the circle: "))
                        answerrad = omtrek_circel(rad, False)
                        print("the circumference of the circle= ", answerrad)
        elif choice == "exit":
                active = 0
        else:
                print("invalid number")