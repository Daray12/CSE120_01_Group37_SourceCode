import math 
import cmath
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Function for the menu
def menu():
    print("Options:")
    print('1 - Add')
    print('2 - Subtract')
    print('3 - Multiply')
    print('4 - Divide')
    print('5 - Square root')
    print('6 - Logarithm')
    print('7 - Logarithm base 2')
    print('8 - Exponent')
    print('9 - Prime factors')
    print('10 - Special functions')
    print('11 - Quit')

def specialFunctionsMenu():
    print("Options:")
    print('1 - Basic derivatives')
    print('2 - Quadratic formula')
    print('3 - GCD')
    print('4 - Plot equations')
    print('5 - Geometric functions')
        
def geometric_menu():
    user_input = input('Enter your choice:\n'
                       '0 - Area, Perimeter, Volume, Surface Area\n'
                       '1 - Advance Triangle\n'
                       '2 - Unit Circle\n'
                       '3 - Plot 2D Shape\n'
                       '4 - DMS to degrees converter\n'
                       '5 - Pythagorean theorem\n'
                       ': ')
    if user_input == "0":
        result = Ask_Area_Per()
        print(result)
    elif user_input == '1':
        result = Ask_Triangle()
        print(result)
    elif user_input == '2':
        result = Ask_Unit_Circle()
        print(result)
    elif user_input == '3':
        result = Plot_2DShape()
        print(result)
    elif user_input == '4':
        result = DMF()
        print(result)
    elif user_input == '5':
        result = pythagorean_theorem()
        print(result)
        
# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

def sqrt_root():
    num = float(input("Enter number: "))
    return math.sqrt(num)

def logarithmic():
    num = float(input("Enter a number: "))
    return math.log(num)
    
def log2():
    num = float(input("Enter a number: "))
    return math.log2(num)

def exp():
    x = float(input("Enter a number: "))
    n = float(input("Enter the exponent number: "))
    return x**n
    
def fact():
    n = int(input("Enter a number: "))
    for x in range(1,n+1):
        if (n%x == 0):
            print(x, ' ')

def pythagorean_theorem():
    print("What side are you missing? (1 - Hypotenuse, 2 - Leg)")
    action = input(": ")
    if action == "1":
        adjacent = float(input("Enter the Adjacent side: "))
        opposite = float(input("Enter the Opposite side: "))
        return math.sqrt((adjacent * adjacent) + (opposite * opposite))
    elif action == "2":
        hypotenuse = float(input("Enter the Hypotenuse: "))
        leg = float(input("Enter the Leg: "))
        return math.sqrt((hypotenuse*hypotenuse) - (leg*leg)) 
    else:
        print("Invalid input. Please try again.")

def quadratic_formula():
    a = float(input("Enter the first value: "))
    b = float(input("Enter the second value: "))
    c = float(input("Enter the third value: "))
    discriminant = cmath.sqrt(b * b -4 * a * c)
    x1 = (-b + discriminant) / (2 * a)
    x2 = (-b - discriminant) / (2 * a)
    print("x is equal to", x1, "and", x2)

def gcd():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return math.gcd(num1, num2)

def bsc_derivatives():  
    function = input('Enter a function: ')
    x, a, b, c = sp.symbols('x a b c')
    expression = sp.sympify(function)
    der = int(input('How many times would you like to take the derivative? '))
    derivative = sp.diff(expression, x, der)
    return derivative

def plot_equation():
    equation = input('Enter an equation (terms of x only): ')
    x = sp.symbols('x')
    result = sp.sympify(equation)
    equation_func = sp.lambdify(x, result, 'numpy')

    x_values = np.linspace(-10, 10, 10)
    y_values = equation_func(x_values)

    plt.plot(x_values, y_values, label='Equation: ' + str(equation))
    plt.title('Equation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


def Ask_Area_Per():
    user_input = input('What is the shape? \nOr enter "0" for a list of available shapes: ')
    user_input = user_input.lower()
    if user_input == '0':
        print('Circle\n',
             'Cone\n',
             'Cube\n',
             'Octagon\n',
             'Octahedron\n',
             'Parallelgram\n',
             'Parallelepiped\n',
             'Pentagon\n',
             'Pentagonal prism\n',
             'Rectangle\n',
             'Rectangular Prism\n',
             'Rhombohedron\n',
             'Rombis\n',
             'Sphere\n',
             'Square\n',
             'Triangle\n')

#this is a list of every shape that has a function for it 

    elif user_input == 'rectangle':
        print(Rectangle())
    elif user_input == 'rectangular prism':
        print(Rectangular_Prism())
    elif user_input == 'square':
        print(Square())
    elif user_input == 'cube':
        print(Cube())
    elif user_input == 'triangle':
        print(Triangle())
    elif user_input == 'cone':
        print(Cone())
    elif user_input == 'pyramid':
        print(Pyramid())
    elif user_input == 'circle':
        print(Circle())
    elif user_input == 'sphere':
        print(Sphere())
    elif user_input == 'pentagon':
        print(Pentagon())
    elif user_input == 'pentagonal prism':
        print(Pentagonal_Prism())
    elif user_input == 'octagon':
        print("You selected Octagon")
    elif user_input == 'rhombus':
        print(Rhombus())
    elif user_input == 'rhombohedron':
        print(Rhombohedron())
    elif user_input == 'parallelogram':
        print(Parallelogram())
    else:
        print("The shape you imputed can not be calculated ")
#testing for what shape was input and if an invalid shape is input the user is told 
def Rectangle():
    length = int(input('What is the length of the rectangle side: '))
    width = int(input('what is the with of the rectangle side: '))
    perimeter = (length*2) + (width*2)
    area = length*width
    return f"The perimeter is: {perimeter}\nThe Area is: {area}"
#multiples length times with to find area, adds 2 length measurements with 2 width measurements to find the perimeter 
def Rectangular_Prism():
    length = int(input('What is the length of the rectangular prism side: '))
    width = int(input('What is the width of the rectangular prism side: '))
    depth = int(input('What is the depth of the rectangular prism: '))
    area = length * width * depth
    surface_area = (length * width) * 6
    return f"The surface area is: {surface_area}\nThe volume is: {area}"
#multiples length width and depth to find volume, multiples length by width the multiples that by 6 
def Square():
    side = int(input('what is the length of a side of the square: '))
    area = side*side
    perimeter = side*4
    return f"The perimeter is: {perimeter}\nThe Area is: {area}"
#multiplies 2 sides for the area, multiples a side by 4 for the perimeter 
def Cube():
    length = int(input('What is the length of the cube side: '))
    area = length*length*length
    surface_area = 6*length*length
    return f"The surface_area is: {surface_area}\nThe volume is: {area}"
#multplies 3 lengths to find area, multiples 6 by lengths times length
def Cone():
    height = int(input('What is the height of the cone: '))
    radious = int(input('What is the radious of the cone: '))
    slant = int(input('What is the height of the slant of the cone: '))
    area = .3333*np.pi*radious**2*height
    surface_area = np.pi*radious*slant+np.pi*radious**2
    return f"The surface_area is: {surface_area}\nThe volume is: {area}"
#multplies one third by pi by radious squared by height to find area, multiples pi, by radius by slant plus pi times radius squared 
def Pyramid():
    base = int(input('What is the base length of the pyramid: '))
    height = int(input('What is the height of the pyramid: '))
    slant = int(input('What is the height of the slant of the cone: '))
    area = .3333*base**2*height
#multplies one-third by the input base squared by height to find area,
    surface_area = .5*base*4*slant+base**2
#multiply .5 by input base by 4 by input slant pulse input base squared    
    return f"The surface_area is: {surface_area}\nThe volume is: {area}"

def Sphere():
    radius = int(input('What is the radius of the sphere: '))
    volume = (4/3)*np.pi*radius^3
# multiply four thirds by pi by radius cubed to find volume    
    surface_area = 4*np.pi*radius
#multplies 4 by pi and the radius 
    return f"The surface_area is: {surface_area}\nThe volume is: {volume}"

def Pentagonal_Prism():
    length = int(input('what is the length of the pentagonal prism base: '))
    height = int(input('What is the height of the pentagonal prism: '))
    apothem = length/(2*math.tan(math.pi/5))
#devides length by 2 times the tangent of pi over 5 
    area = (5/2)*length*height*apothem
#multplies five over two times length by height by apothem 
    surface_area = 5*length*apothem+5*length*height
    return f"The surface_area is: {surface_area}\nThe volume is: {area}"
    
def Rhombohedron ():
    lenght = int(input('what is the edge length of the rhombohedron: '))
    angle = int(input('what is the angle of the rhombohedron: '))
    angle = np.radians(angle)
#converts angle to radians 
    area = lenght**3 *(1-np.cos(angle))*math.sqrt(1+2*np.cos(angle))
# lenth cubed times 1 mins the cos of the angle times the squareroot of 3 times the cos
    surface_area = 6*lenght**2*np.sin(angle)
#6 times length squared times sin of the angle 
    return f"The surface_area is: {surface_area}\nThe volume is: {area}"
    
def Triangle():
    base1 = int(input('What is the base length: '))
    base2 = int(input('what is the leg length: '))
    hypotenuse = int(input('what is the hypotenuse length: '))
    perimeter = base1+base2+hypotenuse
#add base1 base2 and hypothenuse 
    area = base1*base2/2
#multplies base1 and base2 then devided by 2
    return f"The perimeter is: {perimeter}\nThe Area is: {area}"

def Circle():
    radious = int(input('what is the radius:  '))
    cir = 2*radious*np.pi
#two times the radius times pi 
    area = np.pi*radious**2
#pie times radius squared 
    return f"The circumference is: {cir}\nThe Area is: {area}"
   
def Pentagon():
    length = int(input('what is the length of the side: '))
    apothem = length / (2 * math.tan(math.pi / 5))
#length divided by two times the tan of pi over 5 
    perimeter = 5 * length
#multplies length by 5
    area = 0.5 * perimeter * apothem
#multplies .5 perimeter and apothem
    return f"The perimeter is: {perimeter}\nThe Area is: {area}"

def Octagon():
    length = int(input('what is the length of the side '))
    area = 2*length**2*(1+(2)**.5)
#2 times length squared times 1 puls 2 to the .5 power
    perimeter = length*6
#length times 6
    return f"The perimeter is: {perimeter}\nThe Area is: {area}"

def Rhombus():
    length1 = int(input('What is the length of the side: '))
    angle = int(input('What is the angle in degrees: '))
    angle_radians = np.radians(angle)
#converts angle to radians 
    area = (length1**2)*(np.sin(angle_radians))
#length1 squared times the sin of the angle 
    perimeter = length1*4
#length1 times 4 
    return f"The perimeter is: {perimeter}\nThe Area is: {area}"

def Parallelogram():
    length1 = int(input('What is the length of the vertical side '))
    length2 = int(input('What is the length of the horizontal side '))
    angle = int(input('What is the angle of the side '))
    angle_radians = np.radians(angle)
#converts angle to radians 
    area = length1*length2*np.sin(angle_radians)
#multplies length1 by length2 times sin of the angle 
    perimeter = 2*(length1+length2)
#length1 times lenght2 times 2
    return f"The perimeter is: {perimeter}\nThe Area is: {area}"

def DMF ():
    degree = int(input('What is your degree: '))
    min_ = int(input('What are your minutes: '))
    sec = int(input('What are your seconds: '))
    return degree+(min_/60)+(sec/3600)
    return degree+(min_/60)+(sec/3600)
    
def Ask_Triangle():
    print('Write NA to all that apply ')
    leg1 = input('What is the length of the first leg: ')
    leg2 = input('what is the length of the second leg: ')
    hypotenuse = input('What is the length of your hypotenuse: ')
    theta = input('Where is the theta: (1 - leg 1 and hypotenuse side) (2 - leg 2 and hypotenuse side)').lower()
#ask for necessary information 
    if theta == 'na':
        print(Pyagrum(leg1, leg2, hypotenuse))
#testing if there is a theta, if not the will just do Pyagrum theorem
    elif leg1 == 'na' or leg2 == 'na' or hypotenuse == 'na':
        a1, b1, c1 = Pyagrum(leg1, leg2, hypotenuse)
#send user info to pyagrum function to find missing info 
        result = Theta(a1, b1, c1, theta)
#uses pyagrum info to send to Theta function 
        print(result)
        
def Pyagrum(a,b,c):
    if a == 'na':
        b = int(b)
        c = int(c)
        a = int(math.sqrt(c**2-b**2))
        return a,b,c
    elif b == 'na':
        a = int(a)
        c = int(c)
        b = int(math.sqrt(c**2-a**2))
        return a,b,c
    elif c == 'na':
        a = int(a)
        b = int(b)
        c = int(math.sqrt(a**2+b**2))
        return a, b, c
#cast variable to integer then dose the math to find the missing side 
def Theta(a,b,c,t):
    if t == '1':
        sin_theta = f'sin theta: {a}/{c}'
        cos_theta = f'cos theta: {b}/{c}'
        tan_theta = f'tan theta: {b}/{a}'
        return '\n'.join([sin_theta, cos_theta, tan_theta])
    elif t == '2':
        sin_theta = f'sin theta: {b}/{c}'
        cos_theta = f'cos theta: {a}/{c}'
        tan_theta = f'tan theta: {a}/{b}'
        return '\n'.join([sin_theta, cos_theta, tan_theta])
#puts the variables in the correct location based on the theta 

def Ask_Unit_Circle():
    d = int(input('Enter your degree, for example: 30: '))
    theta = (input('Enter the desired trigonometric ratios (sin, cos, tan, ): '))
    a = Unit_Circle_Degree(d, theta)
    print(a)
#ask the user for info then send that info to the Unit Circle Degree Function 
def Unit_Circle_Degree (d,theta):
    unit_circle = {
    30: {'X': 'sqrt(3)/2', 'Y': '1/2'},
    45: {'X': 'sqrt(2)/2', 'Y': 'sqrt(2)/2'},
    60: {'X': '1/2', 'Y': 'sqrt(3)/2'},
    90: {'X': '0', 'Y': '1'},
    120: {'X': '-1/2', 'Y': 'sqrt(3)/2'},
    135: {'X': '-sqrt(2)/2', 'Y': 'sqrt(2)/2'},
    150: {'X': '-sqrt(3)/2', 'Y': '1/2'},
    180: {'X': '-1', 'Y': '0'},
    210: {'X': '-sqrt(3)/2', 'Y': '-1/2'},
    225: {'X': '-sqrt(2)/2', 'Y': '-sqrt(2)/2'},
    240: {'X': '-1/2', 'Y': '-sqrt(3)/2'},
    270: {'X': '0', 'Y': '-1'},
    300: {'X': '1/2', 'Y': '-sqrt(3)/2'},
    315: {'X': 'sqrt(2)/2', 'Y': '-sqrt(2)/2'},
    330: {'X': 'sqrt(3)/2', 'Y': '-1/2'},
    360: {'X': '1', 'Y': '0'}
}
#a large dictionary with the major degree's working numbers 
    if theta == 'sin':
        true_num1 = np.radians(d)        
        true_num1 = np.sin(true_num1)
        working_num1 = unit_circle[d]['Y']
        return f"The working number is: {working_num1}\nThe ture number is: {true_num1}"
#using nummpy to find the true number then indexes the appropriate degree in order to print
    elif theta == 'cos':
        true_num2 = np.radians(d)
        true_num2 = np.cos(true_num2)
        working_num2 = unit_circle[d]['X']
        return f"The working number is: {working_num2}\nThe ture number is: {true_num2}"
    elif theta == 'tan':
        true_num3 = np.radians(d)
        true_num3 = np.tan(true_num3)
        working_num3 = unit_circle[d]['Y'],'/',unit_circle[d]['X']
        return f"The working number is: {working_num3}\nThe ture number is: {true_num3}"

def Plot_2DShape():
    print('Type the coordinates of the corners of your shape one at a time, then type "stop" when done. For example: x,y')
    cords = []
    while True:
        user_input = input()
        if user_input.lower() == 'stop':
            break
#a loop that ask for corner coords 
        else:
            coordinates = user_input.split(',')  
            x_cord = int(coordinates[0].strip())  
            y_cord = int(coordinates[1].strip())  
            cords.append([x_cord, y_cord])  
#gets ride of commas and seperate x coords and y coords 
    x_coords = [point[0] for point in cords]
    y_coords = [point[1] for point in cords]

    plt.figure()
    plt.plot(x_coords + [x_coords[0]], y_coords + [y_coords[0]], marker='o')
#creat plots and plot line segments between the points 
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()
#labaling and making grid 
