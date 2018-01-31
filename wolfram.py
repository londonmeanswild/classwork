#!/usr/bin/env python3
# (c) 2017 Landon A Marchant
""" Imports random, randint, PIL image, imageDraw.
  Usese these to create an image using wolfram's rule 110 automata.
"""
from random import randint
from PIL import Image, ImageDraw
def main():

# some colors
  WHITE = (255, 255, 255)
  RED = (255, 0, 0)
  GREEN = (0, 255, 0)
  BLUE = (0, 0, 255)

  OUTPUT_FILE ='wolfram_none_occupied.png'

  def image(width, height):
    """Create a width x height RGB PIL image, initially all white."""
    return Image.new("RGB", (width, height), WHITE)

  def draw_point(image, x_cord, y_cord, color):
    """Draw a color (RGB) pixel at x,y in image."""
    ImageDraw.Draw(image).point((x_cord, y_cord), color)

  def save_image(image, filename):
    """Write image to a PNG file."""
    image.save(filename, "PNG")

  def rule(left, center, right, rule_n=110):
    """Implement wolfram's rule n.
      Args:
        rule_n: Implements rule n
      """
    row = (4 if left else 0) + (2 if center else 0) + (1 if right else 0) 
    return 0 != (rule_n & ((1) << row)) 

  def occupied(hood, occupied_house):
    """True if n is valid and h[n] is True.
       Args:
       house: house from Wolfram's rule n. was h.
       occupied_house: occupied house in neighborhood. Changed from n.
    """
    return hood[occupied_house] if 0 <= occupied_house < len(hood) else False

  WIDTH = 100
# An alternating neighborhood
  #hood = range(WIDTH * [True]
  # hood = (WIDTH//2)*[True,False]  # 

  # hood = [True for _ in range(100)] # initially all populated 
  # hood = [False for _ in range(40)] + [randint(0, 1) == 1 for _ in range(20)] + [False for _ in range(40)] # the neighborhood is randomly populated in the middle 20. wolfram_rand20
  hood = [False for _ in range(40)] + [False for _ in range(20)] + [False for _ in range(40)] # the neighborhood is empty wolfram_EMPTY
  img = image(WIDTH, WIDTH)

  for row in range(WIDTH):  # one per year
    for col in range(WIDTH):  # one each house
      draw_point(img, col, row, (BLUE if hood[col] else WHITE))
    hood = [rule(occupied(hood, col -1), occupied(hood, col), occupied(hood, col +1)) for col in range(0, len(hood))]
  img.save(OUTPUT_FILE)
main()
