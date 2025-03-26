#
try:
    # Open the file in read mode
    with open("sample.txt", "r") as file:
        # Read and print its content line by line
        for line in file:
            print(line.strip())
except FileNotFoundError:
    # Handle the case where the file does not exist
    print("Error: The file 'sample.txt' does not exist.")
except Exception as e:
    # Handle any other unexpected errors
    print(f"An unexpected error occurred: {e}")

# f=open('sample.txt','r')
# f.readlines()