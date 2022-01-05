def copy_file_content(source, destination):
    with open(source, 'r') as file_source:
        file_content = file_source.read()
        with open(destination, 'w') as file_destination:
            file_destination.write(file_content)
            print("Operation done.")


copy_file_content(r"C:\Users\omerz\Desktop\New folder (2)\aviv.txt", r"C:\Users\omerz\Desktop\New folder (2)\gilad.txt")


