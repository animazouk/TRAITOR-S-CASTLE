import random
import time

def generate_enemy_position():
  return random.randint(1, 9)

def display_row(enemy_position):
  row = ""
  for i in range(1, 10):
    if i == enemy_position:
      row += "O"
    else:
      row += "."
  return row

def get_user_input(timeout=1):  # Optional timeout parameter for limited input time
  start_time = time.time()
  while True:
    if time.time() - start_time > timeout:
      return "MISSED"
    try:
      user_input = int(input("Enter a number between 1 and 9 (or 'q' to quit): "))
      if 1 <= user_input <= 9:
        return user_input
      else:
        print("Invalid input. Please enter a number between 1 and 9.")
    except ValueError:
      if input("Quit? (y/n): ").lower() == 'y':
        quit()
      else:
        print("Invalid input.""\n"" Please enter a number between 1 and 9.")

def main():
  score = 0
  for _ in range(10):
    enemy_position = generate_enemy_position()
    row = display_row(enemy_position)
    print(row)
    user_input = get_user_input()  # You can optionally add a timeout here
    if user_input == "MISSED":
      print("MISSED!")
    elif user_input == enemy_position:
      print("GOOD SHOT!")
      score += 1
    else:
      print("Invalid input.""\n"" Please enter a number between 1 and 9.")
  print(f"YOU HIT {score} OUT OF 10")

if __name__ == "__main__":
  main()
