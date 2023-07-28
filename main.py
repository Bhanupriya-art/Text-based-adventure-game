import time

# Define the rooms and their descriptions
rooms = {
    'start': "You are standing in a dimly lit room. There are two doors in front of you.",
    'left_door': "You entered a room with a spooky atmosphere.",
    'right_door': "You find yourself in a room filled with treasure!",
    'trap_room': "Oh no! You've entered a trap room. Spikes start descending from the ceiling.",
    'monster_room': "You hear a growl and see a ferocious monster blocking your path.",
    'escape_room': "Congratulations! You've found the secret escape room with a way out."
}

# Define the connections between rooms
room_connections = {
    'start': ('left_door', 'right_door'),
    'left_door': ('trap_room', 'monster_room'),
    'right_door': ('monster_room', 'escape_room'),
    'trap_room': ('start',),
    'monster_room': ('start', 'left_door', 'right_door'),
    'escape_room': ()
}

# Define actions and their consequences
actions = {
    'look_around': "You look around the room and see: ",
    'take_treasure': "You take some treasure. Good job!",
    'fight_monster': "You bravely fight the monster but lose some health.",
    'run_away': "You run away from the monster and go back to the start room.",
    'try_again': "You should try again."
}

# Player attributes
player_health = 100
player_inventory = []

# Helper function to print text with a delay for a better user experience
def print_with_delay(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Function to handle the player's action
def handle_action(action, current_room):
    global player_health

    if action == 'look_around':
        print_with_delay(rooms[current_room])
    elif action == 'take_treasure':
        player_inventory.append('treasure')
        print_with_delay(actions[action])
    elif action == 'fight_monster':
        player_health -= 20
        print_with_delay(actions[action])
        print_with_delay(f"Your health: {player_health}")
    elif action == 'run_away':
        print_with_delay(actions[action])
        current_room = 'start'
    else:
        print_with_delay(actions['try_again'])
    
    return current_room

# Main game loop
def game_loop():
    current_room = 'start'

    print_with_delay("Welcome to the Text-Based Adventure Game!")
    print_with_delay("You find yourself in a dimly lit room. Your adventure begins...\n")

    while True:
        print_with_delay("What would you like to do?")
        print_with_delay("1. Look around")
        print_with_delay("2. Take the treasure")
        print_with_delay("3. Fight the monster")
        print_with_delay("4. Run away")

        choice = input("Enter the number of your choice (1/2/3/4): ")

        if choice == '1':
            handle_action('look_around', current_room)
        elif choice == '2':
            if current_room == 'right_door':
                handle_action('take_treasure', current_room)
            else:
                print_with_delay("There's no treasure here.")
        elif choice == '3':
            if current_room == 'monster_room':
                handle_action('fight_monster', current_room)
            else:
                print_with_delay("There's no monster here.")
        elif choice == '4':
            if current_room in ('left_door', 'right_door', 'monster_room'):
                current_room = handle_action('run_away', current_room)
            else:
                print_with_delay("You can't run away from here.")
        else:
            print_with_delay("Invalid choice. Please choose a valid option.")

        if player_health <= 0:
            print_with_delay("Game Over! Your health reached 0.")
            break

        if current_room == 'escape_room':
            print_with_delay("Congratulations! You've escaped with the treasure!")
            break

# Start the game
if __name__ == "__main__":
    game_loop()
