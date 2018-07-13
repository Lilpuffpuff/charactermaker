from random import *
import turtle
#colors
tan = (250, 200, 170)
blonde = (250, 200, 17)
green = (20, 140, 70)
strawberry = (255, 60, 100)
vampirewhite = (255, 255, 255)
grey = (200, 200, 200)
pitchblack = (0, 0, 0)
blue = (100, 100, 250)
pale = (255, 242, 230)
brown = (153, 74, 0)
ginger = (255, 170, 0)
hazel = (179, 119, 0)
#traits
bodytype = ["muscular", "petite", "average", "tall", "short", "round"]
haircolor = [brown, blonde, pitchblack, ginger, strawberry, vampirewhite, grey]
hairtype = ["curly", "straight", "ringlets", "waves", "frizzy", "messy", "wild", "spikey"]
eyetype = ["narrow", "round", "bright", "dull", "ghostly", "empty", "sparkly"]
eyecolor = [brown, blue, green, hazel, grey]
skintype = [tan, brown, pale, vampirewhite, pitchblack]
action = ["sitting", "standing", "jumping", "sleeping", "hunting", "dancing", "singing", "cleaning", "running", "walking"]
emotion = ["sad", "happy", "mad", "scared", "embarressed", "flustered", "grumpy", "terrified", "devistated", "bored", "done", "gleeful", "joyus", "enraged"]
clothes = ["formal", "casual", "winter", "summer", "swimwear", "sweet", "work clothes", "farmstyle", "fairy", "goth", "steampunk", "party", "sleepwear"]

body = randint(0, len(bodytype)-1)
hairc = randint(0, len(haircolor)-1)
hairt = randint(0, len(hairtype)-1)
eyet = randint(0, len(eyetype)-1)
eyec = randint(0, len(eyecolor)-1)
skin = randint(0, len(skintype)-1)
act = randint(0, len(action)-1)
emo = randint(0, len(emotion)-1)
clo = randint(0, len(clothes)-1)

print("body type:", bodytype[body])
print("hair color:", haircolor[hairc])
print("hair type:", hairtype[hairt])
print("eye type:", eyetype[eyet])
print("eye color:", eyecolor[eyec])
print("skin color:", skintype[skin])
print("action:", action[act])
print("emotion:", emotion[emo])
print("clothes theme:", clothes[clo])

hc = haircolor[hairc]
ec = eyecolor[eyec]
sc = skintype[skin]
ht = hairtype[hairt]
#head
turtle.colormode(255)
turtle.goto(0,0)
from turtle import *
bgcolor("pink")
color(sc, sc)
begin_fill()
turtle.circle(100)
end_fill()
#eyes
turtle.goto(-50,100)
color(ec, ec)
begin_fill()
turtle.circle(10)
end_fill()
turtle.pu()
turtle.goto(50,100)
turtle.pd()
color(ec, ec)
begin_fill()
turtle.circle(10)
end_fill()
turtle.pu()
#hair
turtle.goto(-100, 150)
turtle.pd()
color(hc,hc)
begin_fill()
if ht == "wild":
    turtle.forward(205)
    turtle.circle(50, 180)
    turtle.forward(20)
    turtle.right(180)
    turtle.circle(-50, 180)
    turtle.right(90)
    turtle.circle(90, 180)
else:
    done()
end_fill()

hideturtle()
done()
