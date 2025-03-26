Task 1: Read a File and Handle Errors
firstly create a sample.txt file 
open file in read mode using try and except method 
print the data of the file using for loop 
Handle the case where the file does not exist by printing 'Error: The file 'sample.txt' does not exist'
Handle any other unexpected errors and print(f"An unexpected error occurred: {e}"


Task 2: Write and Append Data to a File
Take user input and write it to a file
open file 'output.txt' in write mode using try and except method 
write user input in the file and change the line using file.write(user_input + "\n")
reopen the file 'output.txt' in append mode 
Append additional data to the same file using  file.write(additional_data + "\n")
Read and display the final content of the file by opening it in read mode
also handle exception if occurred
