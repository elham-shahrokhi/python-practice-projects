print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")

player = {"name":None, "type":None, "special move": None, "starting HP":None, "starting MP": None}

for name,value in player.items():
    player[name] =  input(f"Input your beast's {name} >").strip().title()

if player["type"]=="Earth":
  print("\033[32m", end="")
elif player["type"]=="Air":
  print("\033[37m", end="")
elif player["type"]=="Fire":
  print("\033[31m", end="")
elif player["type"]=="Water":
  print("\033[34m", end="")
else:
  print("\033[33m", end="")

for name, value in player.items():
    print(f" {name: <15}: {value}")