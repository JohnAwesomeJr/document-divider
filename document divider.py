import tkinter as tk
from tkinter import filedialog

def select_file():
    file_path = filedialog.askopenfilename(title="Select a text document")
    if file_path:
        file_path_var.set(file_path)
        file_button.configure(text="✅ File Selected", state="disabled")

def select_output_directory():
    output_directory = filedialog.askdirectory(title="Select the output directory")
    if output_directory:
        output_directory_var.set(output_directory)
        output_button.configure(text="✅ Output Directory Selected", state="disabled")

def process_document():
    file_path = file_path_var.get()
    output_directory = output_directory_var.get()

    if file_path and output_directory:
        with open(file_path, 'r') as file:
            content = file.read()

        divided_documents = [content[i:i+char_limit] for i in range(0, len(content), char_limit)]

        for i, document in enumerate(divided_documents):
            file_name = f"document_{i+1}.txt"
            file_path = f"{output_directory}/{file_name}"
            with open(file_path, 'w') as file:
                file.write(document)

        message_label.configure(text="Document divided and saved successfully!", fg="black")
    else:
        message_label.configure(text="Please select the file and output directory!", fg="red")

root = tk.Tk()
root.title("Document Divider")
root.geometry("300x300")  # Set window size to 800x600
root.resizable(False, False)  # Make the window non-resizable

# Program Description Label
description_label = tk.Label(root, text="This program allows you to divide a\n"
                                        "text document into multiple smaller documents\n"
                                        "with a maximum length of 10,000 charicters")
description_label.pack(pady=10)

char_limit = 10000

file_path_var = tk.StringVar()
output_directory_var = tk.StringVar()

file_button = tk.Button(root, text="Select File", command=select_file)
file_button.pack(pady=10)

output_button = tk.Button(root, text="Select Output Directory", command=select_output_directory)
output_button.pack(pady=10)

process_button = tk.Button(root, text="Process Document", command=process_document)
process_button.pack(pady=10)

message_label = tk.Label(root, text="")
message_label.pack()

root.mainloop()
