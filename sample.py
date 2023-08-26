# GLOBAL VARIABLES

const UPDATE_RATE = 100

# image
avatar:byte[30*30] = [
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,175,175,175,0,0,0,175,175,175,175,175,175,175,175,175,175,175,175,0,0,0,0,0,0,0,0,0,
0,0,0,175,175,175,0,0,0,175,175,175,175,175,175,175,175,175,175,175,175,0,0,0,0,0,0,0,0,0,
0,0,0,175,175,175,0,0,0,175,175,175,175,175,175,175,175,175,175,175,175,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,175,175,175,31,31,31,31,31,31,31,31,31,31,31,31,175,175,175,0,0,0,0,0,0,
0,0,0,0,0,0,175,175,175,31,31,31,31,31,31,31,31,31,31,31,31,175,175,175,0,0,0,0,0,0,
0,0,0,0,0,0,175,175,175,31,31,31,31,31,31,31,31,31,31,31,31,175,175,175,0,0,0,0,0,0,
0,0,0,175,175,175,31,31,31,31,31,31,1,1,1,31,31,31,1,1,1,31,31,31,0,0,0,0,0,0,
0,0,0,175,175,175,31,31,31,31,31,31,1,1,1,31,31,31,1,1,1,31,31,31,0,0,0,0,0,0,
0,0,0,175,175,175,31,31,31,31,31,31,1,1,1,31,31,31,1,1,1,31,31,31,0,0,0,0,0,0,
0,0,0,0,0,0,31,31,31,31,31,31,18,18,18,31,31,31,18,18,18,31,31,31,0,0,0,0,0,0,
0,0,0,0,0,0,31,31,31,31,31,31,18,18,18,31,31,31,18,18,18,31,31,31,0,0,0,0,0,0,
0,0,0,0,0,0,31,31,31,31,31,31,18,18,18,31,31,31,18,18,18,31,31,31,0,0,0,0,0,0,
0,0,0,0,0,0,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,0,0,0,0,0,0,
0,0,0,0,0,0,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,0,0,0,0,0,0,
0,0,0,0,0,0,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,31,31,31,31,31,31,1,1,1,31,31,31,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,31,31,31,31,31,31,1,1,1,31,31,31,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,31,31,31,31,31,31,1,1,1,31,31,31,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,98,98,98,98,98,98,98,98,98,98,98,98,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,98,98,98,98,98,98,98,98,98,98,98,98,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,98,98,98,98,98,98,98,98,98,98,98,98,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,0,0,0,0,0,0,
0,0,0,0,0,0,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,0,0,0,0,0,0,
0,0,0,0,0,0,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,0,0,0,0,0,0,
0,0,0,0,0,0,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,0,0,0,0,0,0,
0,0,0,0,0,0,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,0,0,0,0,0,0,
0,0,0,0,0,0,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,0,0,0,0,0,0
]

# image
glasses:byte[24*24] = [
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,
0,0,0,0,0,0,1,3,3,3,1,0,0,1,3,3,3,1,0,0,0,0,0,0,
0,0,0,0,0,0,1,3,3,3,1,0,0,1,3,3,3,1,0,0,0,0,0,0,
0,0,1,1,1,1,1,3,3,3,1,1,1,1,3,3,3,1,1,1,0,0,0,0,
0,0,1,0,0,0,1,3,3,3,1,0,0,1,3,3,3,1,0,0,0,0,0,0,
0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
]

# image
headlight:byte[24*24] = [
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,147,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,147,0,0,0,0,147,0,0,0,0,147,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,147,0,0,0,147,0,0,0,147,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,147,0,0,147,0,0,147,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,147,0,147,0,147,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,147,147,147,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,147,147,147,147,147,147,147,147,147,147,147,147,147,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,147,147,147,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,147,0,147,0,147,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,147,0,0,147,0,0,147,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,147,0,0,0,147,0,0,0,147,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,147,0,0,0,0,147,0,0,0,0,147,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,147,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
]

# image
sweat:byte[8*8] = [
0,0,0,184,0,0,0,0,
0,0,0,184,0,0,0,0,
0,0,184,184,184,0,0,0,
0,184,184,184,184,184,0,0,
0,184,184,184,184,184,0,0,
0,0,184,184,184,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0
]

# image
vomit:byte[24*24] = [
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,181,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,181,127,181,181,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,181,181,181,181,181,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,181,127,181,149,181,96,181,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,181,181,181,181,181,181,181,181,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,181,149,181,96,181,149,181,181,181,181,0,0,0,0,0,0,
0,0,0,0,0,0,0,181,181,181,181,181,181,181,181,214,181,181,0,0,0,0,0,0,
0,0,0,0,0,0,181,181,181,181,214,181,149,181,127,181,181,181,181,0,0,0,0,0,
0,0,0,0,0,181,181,181,149,181,181,181,181,181,181,181,149,181,181,181,0,0,0,0,
0,0,0,0,0,181,96,181,181,181,0,0,181,0,0,0,181,181,0,181,0,0,0,0,
0,0,0,0,0,181,181,0,181,127,181,0,0,181,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
]

class Sickness:

    sicknessDurationMilliseconds:int
    currentAcceleration:float
    lastAccelerationVector:vector3D
    accelerationHistory:float[10]
    index:int
    updateCounter:int
    alreadySick:bool

    def init():
        sicknessDurationMilliseconds = 5000

    def record():
        currentAccelerationVector = getAcceleration()
        accelerationHistory[index % 10] = lastAccelerationVector.distance(currentAccelerationVector)
        lastAccelerationVector = currentAccelerationVector
        index = (index + 1) % 10

    def isSick()->bool:
        updateCounter++
        sum:float = 0
        for histItem in accelerationHistory:
            sum = sum + histItem
        
        
        sick:bool = sum > 20
        if sick:
            if alreadySick == false:
                print("SICKNESS STARTED")
                updateCounter = 0
                alreadySick = true
                return true
            else:
                print("STILL SICK")
                return true;
        else:
            if alreadySick:
                print("SICKNESS HEALING")

                if UPDATE_RATE * updateCounter > sicknessDurationMilliseconds:
                    alreadySick = false
                    return false;
                else:
                    return true   

            
        return false


class Person:

    sickness:Sickness

    def init():
        sickness.init();

    def drawHeadlights():
        push()
        translate(125, 40)
        scale(3)
        drawSprite(0,0,24,24,headlight)
        pop()
    
    def drawSunglasses():
        push()
        translate(120, 80)
        scale(4)
        drawSprite(1,0,24,24,glasses)
        pop()

    def drawVomit():
        push()
        translate(122, 82)
        scale(4.1)
        drawSprite(2,11,24,24,vomit)
        pop()

    def drawSweating():
        # drop 1
        push()
        translate(100, 55)
        scale(2)
        drawSprite(0,0,8,8,sweat)
        pop()

        # drop 2
        push()
        translate(150, 70)
        scale(2)
        drawSprite(0,0,8,8,sweat)
        pop()

        # drop 3
        push()
        translate(105, 90)
        scale(2)
        drawSprite(0,0,8,8,sweat)
        pop()

        push()
        fill(255,0,0)
        noStroke()
        drawRectangle(120,95,7,12)
        pop()
    

    def draw():
        push()
        translate(120,80)
        scale(4)
        drawSprite(0,0,30,30,avatar)
        pop()

        if getAmbientLux() <= 20:
            drawHeadlights()
        elif getAmbientLux() > 25000:
            drawSunglasses()

        if sickness.isSick():
            drawVomit()

        sickness.record()

        if getTemperature() > 26:
            drawSweating()        

class Text:
    def draw(): 
        push()
        translate(20,140)
        textFont(FONT_ROBOTO_32)
        noStroke()
        tx = "We miss you!"
        stroke(255,255,255)
        drawTextCentered(100,20,tx)
        pop()
    
class Countdown:
    def draw():
        push()
        translate(120,200)
        if isConnected():
            textFont(FONT_ROBOTO_16)
            returnDate:dateTime
            returnDate.setDate(3,6,2024)

            nowDate:dateTime
            nowDate.now()

            seconds = returnDate.getEpoch() - nowDate.getEpoch()
            diffDays = (seconds / 60 / 60 / 24) + 1
            
            drawTextCentered(0,0,"See you in " + diffDays + " days")
        else: 
            drawTextCentered(0,0,"See you in June 2024")
        pop()


person:Person
text:Text
countdown:Countdown

person.init()

def onDraw():

    background(0,0,0)
    person.draw()
    text.draw()
    countdown.draw()

    update()
    delay(UPDATE_RATE)


    if getButton():
        if returnToMenu():
            return