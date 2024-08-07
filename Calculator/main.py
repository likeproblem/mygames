import pygame
import math
pygame.init()

def isInside(bl, tr, p) :
   if (p[0] > bl[0] and p[0] < tr[0] and p[1] > bl[1] and p[1] < tr[1]) :
      return True
   else :
      return False

def ifOper(string):
    return string == "+" or string == "-" or string == "÷" or string == "*" or string == "(" or string == "/"

def numberCook(var, aboutToFrac=False):
    if type(var[-1]) is list:
        return var
    for i in range(len(var) - 1, -2, -1):
        if ifOper(var[i]) or i == -1:
            combine = var[i + 1:len(var)]
            del var[i + 1:len(var)]
            if fractionMode:
                convert_func = int
            else:
                convert_func = float
            var.append(convert_func("".join(combine)))
            if var[i] == "/":
                apend = Fraction(var[i-1], var[i+1])
                print(var[i-1])
                del var[i-1:i+1]
                var.append(apend)
                del var[i - 1]
            elif fractionMode and not aboutToFrac:
                var.append(Fraction(var.pop(), 1))
            break
    return var

def solve(var):
    i = 0
    while i < len(var):
        if type(var[i]) is list:
            result = solve(var[i])
            del var[i]
            var.insert(i, result[0])
        i += 1
    i = 0
    while i < len(var):
        if var[i] == "÷" or var[i] == "*":
            if var[i] == "÷":
                result = var[i - 1] / var[i + 1]
            if var[i] == "*":
                result = var[i - 1] * var[i + 1]
            del var[i - 1:i + 2]
            var.insert(i - 1, result)
            i -= 1
        i += 1
    i = 0
    while i < len(var):
        if var[i] == "+" or var[i] == "-":
            if var[i] == "+":
                result = var[i - 1] + var[i + 1]
            if var[i] == "-":
                result = var[i - 1] - var[i + 1]
            del var[i - 1:i + 2]
            var.insert(i - 1, result)
            i -= 1
        i += 1
    return var

def stringify(var):
    eq = ""
    for i in var:
        eq+=str(i)
    return eq

class Button(pygame.sprite.Sprite):
    def __init__(self, image, pressimage, x, y, col1, col2, tag, toogle=False):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.col1 = list(col1)
        self.col1 = (self.x - self.col1[0], self.y - self.col1[1])
        self.col2 = list(col2)
        self.col2 = (self.x + self.col2[0], self.y + self.col2[1])
        self.tag = tag
        self.pressed = False
        self.since = False
        self.toogleMode = toogle
        self.toogle = False
        self.pressimage = pressimage
        self.originalimage = image
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))

    def gotPressed(self):
        if self.pressed and not self.since:
            self.since = True
            self.toogle = not self.toogle
            return True
        elif not self.pressed and self.since:
            self.since = False
        return False

    def update(self):
        if isInside(self.col1, self.col2, pygame.mouse.get_pos()) and pygame.mouse.get_pressed(3)[0]:
            self.pressed = True
        else:
            self.pressed = False
        if self.toogleMode:
            if self.toogle:
                self.image = self.pressimage
            else:
                self.image = self.originalimage
        else:
            if self.pressed:
                self.image = self.pressimage
            else:
                self.image = self.originalimage
        self.rect.center = (self.x, self.y)
        self.rect = self.image.get_rect(center=self.rect.center)

class Fraction:
    def __init__(self, up, down):
        self.up = int(up)
        self.down = int(down)
        self.simplify()
    def __repr__(self):
        return f"{self.up}/{self.down}"
    def __add__(self, other):
        newlcm = math.lcm(self.down, other.down)
        selfup = int(self.up * (newlcm / self.down))
        otherup = int(other.up * (newlcm / other.down))
        selfup += otherup
        newfraction = Fraction(selfup, newlcm)
        newfraction.simplify()
        return newfraction
    def __sub__(self, other):
        newlcm = math.lcm(self.down, other.down)
        selfup = int(self.up * (newlcm / self.down))
        otherup = int(other.up * (newlcm / other.down))
        selfup -= otherup
        newfraction = Fraction(selfup, newlcm)
        newfraction.simplify()
        return newfraction
    def __mul__(self, other):
        selfup = self.up * other.up
        selfdown = self.down * other.down
        newfraction = Fraction(selfup, selfdown)
        newfraction.simplify()
        return newfraction
    def __truediv__(self, other):
        selfup = self.up * other.down
        selfdown = self.down * other.up
        newfraction = Fraction(selfup, selfdown)
        newfraction.simplify()
        return newfraction
    def __pow__(self, other):
        powup = self.up
        powdown = self.down
        for i in range(other+1):
            powup *= self.up
            powdown *= self.down
        newfraction = Fraction(powup, powdown)
        newfraction.simplify()
        return newfraction
    def __int__(self):
        return Fraction(self.up, self.down)

    def simplify(self):
        gcd = math.gcd(self.up, self.down)
        self.up = int(self.up / gcd)
        self.down = int(self.down / gcd)

screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Calculator')
screen.fill('orange')

zeroImage = pygame.image.load("0.png")
oneImage = pygame.image.load("1.png")
twoImage = pygame.image.load("2.png")
threeImage = pygame.image.load("3.png")
fourImage = pygame.image.load("4.png")
fiveImage = pygame.image.load("5.png")
sixImage = pygame.image.load("6.png")
sevenImage = pygame.image.load("7.png")
eightImage = pygame.image.load("8.png")
nineImage = pygame.image.load("9.png")
plusImage = pygame.image.load("plus.png")
minusImage = pygame.image.load("minus.png")
multiplyImage = pygame.image.load("multiply.png")
divideImage = pygame.image.load("divide.png")
equalsImage = pygame.image.load("equals.png")
sqrtImage = pygame.image.load("sqrt.png")
rightBracketImage = pygame.image.load("rightBracket.png")
leftBracketImage = pygame.image.load("leftBracket.png")
squareImage = pygame.image.load("square.png")
fracImage = pygame.image.load("frac.png")
fracPressedImage = pygame.image.load("fracPressed.png")
fractionImage = pygame.image.load("fraction.png")
resetImage = pygame.image.load("reset.png")
pressedImage = pygame.Surface((70,40))
pressedImage.fill("green")
font = pygame.font.SysFont('timesnewroman',  32)

col = (35,20)
groupy = pygame.sprite.Group(Button(oneImage, pressedImage, 100, 200, col, col, "1"),
                             Button(twoImage, pressedImage, 200, 200, col, col, "2"),
                             Button(threeImage, pressedImage, 300, 200, col, col, "3"),
                             Button(fourImage, pressedImage, 100, 250, col, col, "4"),
                             Button(fiveImage, pressedImage, 200, 250, col, col, "5"),
                             Button(sixImage, pressedImage, 300, 250, col, col, "6"),
                             Button(sevenImage, pressedImage, 100, 300, col, col, "7"),
                             Button(eightImage, pressedImage, 200, 300, col, col, "8"),
                             Button(nineImage, pressedImage, 300, 300, col, col, "9"),
                             Button(zeroImage, pressedImage, 200, 350, col, col, "0"),
                             Button(plusImage, pressedImage, 100, 400, col, col, "+"),
                             Button(minusImage, pressedImage, 200, 400, col, col, "-"),
                             Button(multiplyImage, pressedImage, 100, 450, col, col, "*"),
                             Button(divideImage, pressedImage, 200, 450, col, col, "÷"),
                             Button(sqrtImage, pressedImage, 300, 450, col, col, "sqrt"),
                             Button(leftBracketImage, pressedImage, 100, 500, col, col, "("),
                             Button(rightBracketImage, pressedImage, 200, 500, col, col, ")"),
                             Button(squareImage, pressedImage, 300, 500, col, col, "square"),
                             Button(fractionImage, pressedImage, 300, 400, col, col, "/"),
                             Button(fracImage, fracPressedImage, 350, 25, col, col, "frac", True),
                             Button(resetImage, pressedImage, 50, 25, col, col, "reset"),
                             Button(equalsImage, pressedImage, 200, 550, col, col, "="))

eq = []
running = True

fractionMode = False
while running:
    screen.fill('orange')
    pygame.draw.rect(screen, "gray", ((50, 50), (300, 100)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    groupy.draw(screen)
    groupy.update()
    text = font.render(stringify(eq), True, "red")
    textRect = text.get_rect()
    textRect.center = (200, 100)
    screen.blit(text, textRect)
    for i in groupy.sprites():
        if i.gotPressed():
            if len(eq) != 0 and eq[0] == "=":
                eq = []
            if i.tag == "=":
                eq = numberCook(eq)
                print(eq)
                print(solve(eq))
                eq.insert(0, i.tag)
            if i.tag == "reset":
                eq = []
            elif i.tag == "sqrt":
                if not fractionMode:
                    eq = numberCook(eq)
                    eq.append(str(math.sqrt(eq.pop())))
            elif i.tag == "square":
                if not fractionMode:
                    eq = numberCook(eq)
                    eq.append(str(eq.pop()**2))
            elif i.tag == ")":
                eq = numberCook(eq)
                for i in range(len(eq) - 1, -2, -1):
                    if eq[i] == "(" or i == -1:
                        combine = eq[i + 1:len(eq)]
                        del eq[i:len(eq)]
                        eq.append(combine)
                        break
            elif i.tag == "(":
                if len(eq) > 1:
                    if type(eq[-1]) is list or eq[-1].replace(".", "").isnumeric():
                        eq = numberCook(eq)
                        eq.append("*")
                eq.append(i.tag)
            elif i.tag == "frac":
                fractionMode = not fractionMode
            elif i.tag == "/":
                if fractionMode:
                    eq = numberCook(eq, True)
                    eq.append(i.tag)
            elif ifOper(i.tag):
                eq = numberCook(eq)
                eq.append(i.tag)
            else:
                eq.append(i.tag)
            print(eq)

    pygame.display.flip()
    pygame.display.update()
