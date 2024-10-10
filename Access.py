import subprocess

def run_file(filename):
    try:
        subprocess.run(['python', f'{filename}.py'])
    except FileNotFoundError:
        print(f"Error: '{filename}.py' not found.")

def main():
    print("Choose a file to run:")
    print("1. bandgapFINAL")
    print("2. Deborglie")
    print("3. dielectricFINAL")
    print("4. HallEffectFINAL")
    print("5. malus")
    print("6. photocellFINAL")

    choice = input("Enter the number corresponding to the file you want to run: ")

    files = {
        '1': 'C:/Users/hpp/Desktop/Goding/Python/1st Year Project/bandgapFINAL',
        '2': 'Deborglie',
        '3': 'dielectricFINAL',
        '4': 'HallEffectFINAL',
        '5': 'malus',
        '6': 'photocellFINAL'
    }

    if choice in files:
        run_file(files[choice])
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
