import sys, math, time
import turtle, random

collections = {
  "moniamonds" : [[2, 2, 2]],
  "diamonds" : [[1, 2, 1, 2]],
  "triamonds" : [[0, 2, 1, 1, 2]],
  "tetriamonds" : [[0, 1, 2, 0, 1, 2], [-1, 2, 1, 1, 1, 2], [0, 2, 0, 2, 0, 2]],
  "pentiamonds" :[[0, 0, 2, 1, 0, 1, 2], [-1, 2, 0, 2, 0, 1, 2], [-2, 2, 1, 1, 1, 1, 2], [-1, 1, 2, 0, 1, 1, 2]],
  "hexiamonds" : [[-1, 1, 2, -1, 2, 0, 1, 2], [-1, 0, 2, 1, 0, 1, 1, 2], [-1, 1, 2, 0, 0, 2, 0, 2], [-1, 2, -1, 2, 1, 0, 1, 2], [-1, 1, 2, 0, 1, 0, 2, 1], [-2, 2, 1, 0, 2, 0, 1, 2], [0, 0, 1, 2, 0, 0, 1, 2], [-2, 2, 0, 2, 0, 1, 1, 2], [1, 1, 1, 1, 1, 1], [-2, 1, 2, 0, 1, 1, 1, 2], [-1, 1, 1, 2, -1, 1, 1, 2], [-1, 2, 0, 2, -1, 2, 0, 2]],
  "heptiamonds" : [[-1, 0, 2, 0, 2, -1, 1, 1, 2], [-2, 1, 2, 0, 1, 0, 2, 0, 2], [-2, 2, 0, 2, -1, 2, 0, 1, 2], [-2, 1, 2, 0, 0, 2, 0, 1, 2], [-1, 1, 0, 2, 1, -1, 1, 1, 2], [-2, 2, -1, 2, 1, 0, 1, 1, 2], [-1, 1, 2, -1, 2, 0, 0, 2, 1], [-1, 0, 2, 1, 0, 0, 2, 0, 2], [0, 2, 0, 1, 1, 1, 1], [0, 0, 0, 2, 1, 0, 0, 1, 2], [-2, 2, 0, 1, 2, -1, 1, 1, 2], [-2, 2, 1, -1, 2, 1, 0, 1, 2], [-2, 1, 1, 2, -1, 1, 1, 1, 2], [-2, 0, 2, 1, 0, 1, 1, 1, 2], [-1, 1, 2, 0, 0, 1, 2, -1, 2], [-2, 1, 2, 0, 1, 1, 0, 2, 1], [-1, 1, 2, -1, 1, 2, -1, 1, 2], [-1, 0, 2, 1, 0, 1, 0, 2, 1], [-1, 1, 2, -1, 2, -1, 2, 0, 2], [-2, 2, 0, 2, 0, 0, 2, 0, 2], [-1, 0, 1, 2, 0, 0, 1, 1, 2], [-1, -1, 2, 1, 1, 0, 1, 1, 2], [-2, 1, 2, -1, 2, 0, 1, 1, 2], [-1, 0, 2, 1, -1, 2, 0, 1, 2]],
  "octiamonds" : [[-2, 2, -1, 2, 1, 0, 0, 2, 0, 2], [-2, 1, 1, 2, -1, 0, 2, 0, 1, 2], [-2, 1, 2, -1, 2, -1, 2, 0, 1, 2], [-2, 0, 2, 0, 2, -1, 1, 1, 1, 2], [-2, 1, 2, 0, 0, 2, -1, 2, 0, 2], [-2, 1, 2, -1, 2, 0, 1, 0, 2, 1], [-2, 0, 2, 1, 0, 0, 2, 0, 1, 2], [-2, 1, 2, 0, 0, 2, 0, 0, 2, 1], [-2, 1, 1, 2, -1, 1, 1, 0, 2, 1], [-1, 0, 0, 2, 1, 0, 0, 1, 1, 2], [-1, 0, 2, 0, 2, -1, 0, 2, 0, 2], [-2, 0, 2, 1, -1, 2, 0, 1, 1, 2], [-1, 0, 1, 2, 0, -1, 2, 0, 1, 2], [0, 2, 0, 1, 0, 2, 0, 1], [-2, 1, 1, 1, 2, -2, 1, 1, 1, 2], [-1, 0, 2, 1, -1, 1, 2, -1, 1, 2], [-1, 1, -1, 2, 1, 1, -1, 1, 1, 2], [0, 2, -1, 2, 0, 1, 1, 1], [0, 2, 0, 0, 2, 0, 1, 1], [-2, 1, 2, 0, 1, -1, 2, 1, 0, 2], [-2, 1, 2, -1, 1, 2, -1, 1, 1, 2], [-2, 1, 1, 2, -2, 2, 0, 1, 1, 2], [-2, 2, 0, 2, -1, 2, -1, 2, 0, 2], [-2, 2, 1, -1, 1, 2, 0, 0, 1, 2], [-2, 2, -1, 1, 2, 0, 0, 1, 1, 2], [-1, -1, 1, 2, 0, 1, 0, 1, 1, 2], [-2, -1, 2, 1, 1, 0, 1, 1, 1, 2], [-2, 1, 2, 0, 0, 1, 2, -1, 1, 2], [-2, 1, 2, 0, -1, 2, 1, 0, 1, 2], [-2, 2, -2, 2, 1, 1, 0, 1, 1, 2], [-2, 0, 2, 1, 0, 1, 1, 0, 2, 1], [-2, 2, 0, 2, -2, 2, 1, 0, 1, 2], [-2, 1, 1, 2, -1, 1, 0, 2, 0, 2], [-1, -1, 2, 1, 0, 2, -1, 1, 1, 2], [-1, 0, 2, 1, -1, 2, -1, 2, 0, 2], [-2, 2, 0, 1, 2, -1, 0, 2, 0, 2], [-1, 1, 0, 2, 1, -1, 1, 0, 2, 1], [-1, 1, 2, -1, 2, -1, 2, -1, 2, 1], [-2, 1, 2, -1, 2, 0, 0, 2, 0, 2], [-1, 0, 2, 1, 0, 0, 2, -1, 2, 1], [-1, 0, 1, 2, 0, 0, 0, 2, 0, 2], [-2, 2, 0, 1, 2, -2, 2, 0, 1, 2], [-1, 0, 2, 1, -1, 2, 0, 0, 2, 1], [-2, 1, 2, 0, 1, 0, 1, 2, -1, 2], [-1, 0, 2, 1, 0, 1, 0, 1, 2, 0], [-1, 0, 2, -1, 2, 1, -1, 1, 1, 2], [-1, -1, 2, 0, 2, 0, 0, 1, 1, 2], [-1, 0, 2, 1, 0, 0, 1, 2, -1, 2], [-1, 1, 2, -1, 2, -1, 1, 2, -1, 2], [-2, 2, 0, 0, 2, 1, -1, 1, 1, 2], [-1, 0, 2, 1, 0, 1, -1, 2, 1, 1], [-1, 0, 1, 2, 0, 0, 1, 0, 2, 1], [-1, 0, 1, 2, -1, 2, -1, 1, 1, 2], [-2, 0, 1, 2, 0, 0, 1, 1, 1, 2], [-2, 0, 2, 1, 0, 1, 0, 2, 0, 2], [-2, 2, -1, 2, 1, -1, 2, 0, 1, 2], [-1, 0, 1, 1, 2, -1, 0, 1, 1, 2], [0, 0, 0, 1, 2, 0, 0, 0, 1, 2], [-1, 1, 2, 0, 0, 0, 2, 1, -1, 2], [-2, 2, -1, 2, 0, 2, -1, 1, 1, 2], [-2, 2, 0, 2, -1, 1, 2, -1, 1, 2], [-2, 2, 1, -1, 2, 0, 2, -1, 1, 2], [-2, 1, 0, 2, 1, -1, 1, 1, 1, 2], [-2, 1, 2, -2, 2, 1, 0, 1, 1, 2], [-1, 0, 2, 0, 2, -1, 1, 0, 2, 1], [-1, 2, 1, 0, 1, 1, 1, 1]]
}

def decimal_to_hex_string(dec):
  return hex(dec).split('x')[-1].zfill(2)

def randomColor():
  red = random.randint(0,255)
  green = random.randint(0,255)
  blue = random.randint(0,255)
  return "#" + decimal_to_hex_string(red) + decimal_to_hex_string(green) + decimal_to_hex_string(blue)

def render(shape, my_turtle, start, flag, screen):
  my_turtle.pu()
  my_turtle.goto(start)
  my_turtle.pd()

  for angle in shape:
    my_turtle.forward(11)
    my_turtle.left(angle * 60.0)

home = [300, 250]
window = turtle.Screen()
window.bgcolor("#eebeca")
winka = turtle.Turtle()
winka.speed(10)

j = 250
k = 200
index = 1
for shape in collections[sys.argv[1]]:
  render(shape, winka, [j,k], index, window)
  j -= 60
  if index % 11 == 0:
    j = 250
    k -= 55
  index += 1

winka.pu()
winka.speed(1)
winka.goto(home)
window.exitonclick()