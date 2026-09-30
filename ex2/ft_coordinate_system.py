import math


def get_player_pos():
    while True:
        coordinates = input(
                "Enter new coordinates as "
                "floats in format 'z,y,z': "
                )
        values = coordinates.split(",")
        if len(values) != 3:
            print("Invalid syntax")
            continue
        try:
            x = float(values[0])
            y = float(values[1])
            z = float(values[2])

            return (x, y, z)

        except ValueError as error:
            for value in values:
                try:
                    float(value)
                except ValueError:
                    print(f"Error on parameter {value}: {error}")
                    break


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")

    first = get_player_pos()
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")

    distance = math.sqrt((first[0] ** 2) + (first[1] ** 2) + (first[2] ** 2))
    print(f"Distance to center: {distance:.4f}\n")

    print("Get a second set of coordinates")
    second = get_player_pos()
    distance = math.sqrt(
            ((second[0] - first[0]) ** 2)
            + ((second[1] - first[1]) ** 2)
            + ((second[2] - first[2]) ** 2)
            )
    print(f"Distance between the 2 sets of coordinates: {distance:.4f}")
