from dice import Die
import argparse

def main():
    parser = argparse.ArgumentParser(description="Set properties of Die from the command line.")
    parser.add_argument('--dice_roll', type=str, required=True)

    args = parser.parse_args()

    properties = {}
    for pair in args.dice_roll.split(','):
        key, value = pair.split(':')
        properties[key] = value

    die = Die(number=int(properties['number']), sides=int(properties['sides']), value=int(properties['value']))
    die.display()

if __name__ == "__main__":
    main()
