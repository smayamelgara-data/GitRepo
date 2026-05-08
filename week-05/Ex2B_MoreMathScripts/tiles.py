#You are going to tile a room whose dimensions are length by width feet. There are
# twelve tiles per box, each 1 foot by 1 foot. How many boxes of tiles do you need? You
# can only buy full boxes, not a partial box.
# You also want to buy at least 10% more tiles than you need in order to handle chips,
# breakage, and mess-ups. How many total boxes will you buy?

# Ask for room dimensions
length = float(input("What is the length of the room in feet? "))
width = float(input("What is the width of the room in feet? "))

# Calculate room area
room_area = length * width

# Add 10% extra tiles
total_tiles_needed = room_area * 1.10

# Calculate boxes needed
boxes_needed = total_tiles_needed / 12

# Round up without using math
boxes_to_buy = int(boxes_needed)

if boxes_needed > boxes_to_buy:
    boxes_to_buy = boxes_to_buy + 1

# Output
print("The room area is", room_area)
print("You need", total_tiles_needed, "tiles including extra tiles")
print("You will buy", boxes_to_buy, "boxes of tiles")

