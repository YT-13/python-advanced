"""Complete the task from the classword to manage the "team"
Add a new function: `player_update` which updates the player by its number
Update the `player_add` function so for now the application validate
if the user with the same number already exists in a team"""

# CRUD (Create Read Update Delete) operations

# Database representation
team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 31, "number": 12},
]


# Application source code
def repr_players(players: list[dict]):
    for player in players:
        print(
            f"\t[Player {player['number']}]: {player['name']},{player['age']}"
        )


def player_add(name: str, age: int, number: int) -> dict:
    player: dict = {
        "name": name,
        "age": age,
        "number": number,
    }
    team.append(player)

    return player


def player_delete(number: int) -> None:
    for player in team:
        if player["number"] == number:
            del player


def main():
    operations = ("add", "del", "repr", "update", "exit")

    while True:
        operation = input(
            "Please enter the operation (add, del, repr, update, exit): "
        )
        if operation not in operations:
            print(f"Operation: '{operation}' is not available\n")
            continue

        if operation == "exit":
            print("Bye")
            break
        elif operation == "repr":
            repr_players(team)
        elif operation == "add":
            user_data = input(
                "Enter new player information[name,age,number]: "
            )
            # Input: 'Clark,19,22'
            user_items: list[str] = user_data.split(",")
            # Result: ['Clark', '19', '22']
            name, age, number = user_items
            try:
                if any(player["number"] == int(number) for player in team):
                    print(
                        "The player with this number already exists in team \U0001F937"
                    )
                else:
                    player_add(name=name, age=int(age), number=int(number))
            except ValueError:
                print("Age and number of player must be integers\n\n")
                continue

        elif operation == "update":
            number_input = int(
                input(
                    "Enter the number of the player whose data you want to update: "
                )
            )
            try:
                player = next(i for i in team if i["number"] == number_input)
            except StopIteration:
                print("Not found player in the team \U0001F641")
            else:
                new_user_data = input(
                    "Enter new information for this player [name, age, number]: "
                )
                name, age, number = new_user_data.split(",")
                player["name"] = name
                player["age"] = int(age)
                player["number"] = int(number)
                print("Information updated \U0001F44D")
        else:
            raise NotImplementedError


if __name__ == "__main__":
    main()
