# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("First line of text\n")
        file.write("Second line: 42\n")
        file.write("Third line: Hello, world!\n")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("File creation process completed.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Fourth line: Appended text\n")
        file.write("Fifth line: 12345\n")
        file.write("Sixth line of appended text\n")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("Appending process completed.")
    