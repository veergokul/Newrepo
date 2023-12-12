# Open a file for writing
with open('sample.txt', 'w') as file:
    # Write content to the file
    file.write('Hello, this is a sample file created with Python!\n')
    file.write('You can add more content here.')

print("File 'sample.txt' has been created.")
