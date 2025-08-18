# Beast battle game setup with color-coded types

print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")

# Initialize player attributes
player = {
    "name": None,
    "type": None,
    "special move": None,
    "starting HP": None,
    "starting MP": None
}

# Ask the user to input each attribute
for name, value in player.items():
    player[name] = input(f"Input your beast's {name} > ").strip().title()

# Set terminal text color based on beast type
if player["type"] == "Earth":
    print("\033[32m", end="")  # Green
elif player["type"] == "Air":
    print("\033[37m", end="")  # White
elif player["type"] == "Fire":
    print("\033[31m", end="")  # Red
elif player["type"] == "Water":
    print("\033[34m", end="")  # Blue
else:
    print("\033[33m", end="")  # Yellow for unknown type

# Display the formatted player info
for name, value in player.items():
    print(f" {name: <15}: {value}")