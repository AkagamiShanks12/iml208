import os
from tkinter import Label, messagebox, ttk
import tkinter
from PIL import Image, ImageTk  # Make sure to install Pillow: pip install Pillow

def register():
    username = entry_username.get()
    email = entry_email.get()

    if username and email:
        messagebox.showinfo("Registration Successful", f"Welcome to the One Piece fan club!, {username}!")
        # You can add additional logic here, like saving the registration data to a file or a database.
    else:
        messagebox.showwarning("Registration Error", "Please fill in all the fields.")

def add_favorite():
    selected_character = variable.get()
    if selected_character:
        listbox_favorites.insert(tkinter.END, selected_character)

def delete_favorite():
    selected_index = listbox_favorites.curselection()
    if selected_index:
        listbox_favorites.delete(selected_index)

def delete_data():
    entry_username.delete(0, tkinter.END)
    entry_email.delete(0, tkinter.END)
    variable.set("")  # Clear the selected favorite character
    listbox_favorites.delete(0, tkinter.END)  # Clear the list of favorite characters



def clear_fields():
    entry_username.delete(0, tkinter.END)
    entry_email.delete(0, tkinter.END)
    variable.set("")  # Clear the selected favorite character
    listbox_favorites.delete(0, tkinter.END)  # Clear the list of favorite characters

def save_data():
    username = entry_username.get()
    email = entry_email.get()
    favorite_character = variable.get()

    if username and email and favorite_character:
        if favorite_character in registered_data:
            registered_data[favorite_character]['username'] = username
            registered_data[favorite_character]['email'] = email
        else:
            registered_data[favorite_character] = {'username': username, 'email': email}

        messagebox.showinfo("Data Saved", "Your data has been updated.")
        clear_fields()
    else:
        messagebox.showwarning("Save Error", "Please fill in all the fields and select a favorite character.")

def load_character_images(folder_path):
    character_images = {}
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, file_name)
            character_name = os.path.splitext(file_name)[0]  # Extracting character name without extension
            character_images[character_name] = ImageTk.PhotoImage(Image.open(image_path).resize((50, 50), Image.ANTIALIAS))
    return character_images

def read_file():
    try:
        with open('file.txt', 'r', encoding='utf-8') as file:
            content = file.read()
        button_read.delete(1.0, tkinter.END)  # Clear existing content
        button_read.insert(tkinter.END, content)  # Insert new content
    except FileNotFoundError:
        messagebox.showerror("File Not Found", "The file does not exist.")
    except UnicodeDecodeError as e:
        messagebox.showerror("Unicode Error", f"Error decoding file: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def update():
    selected_index = listbox_favorites.curselection()
    if selected_index:
        selected_username = listbox_favorites.get(selected_index)
        user_data = registered_data.get(selected_username, {})
        
        # Assuming you have entry widgets for username, email, and favorite character
        updated_username = entry_username.get()
        updated_email = entry_email.get()
        updated_favorite_character = variable.get()

        if updated_username and updated_email and updated_favorite_character:
            # Update user data
            user_data['email'] = updated_email
            user_data['favorite_character'] = updated_favorite_character

            # Update the listbox display
            listbox_favorites.delete(selected_index)
            listbox_favorites.insert(tkinter.END, updated_username)

            messagebox.showinfo("Update Successful", f"User information updated for {updated_username}.")
            clear_fields()
        else:
            messagebox.showwarning("Update Error", "Please fill in all the fields.")
    else:
        messagebox.showwarning("No User Selected", "Please select a user to update.")


def display_user_data(event):
    selected_index = listbox_records.curselection()
    if selected_index:
        selected_username = listbox_records.get(selected_index)
        user_data = registered_data.get(selected_username, {})
        
        # Display user information in the text widget
        text_widget.delete(1.0, tkinter.END)
        text_widget.insert(tkinter.END, f"Username: {selected_username}\n")
        text_widget.insert(tkinter.END, f"Email: {user_data.get('email', '')}\n")
        text_widget.insert(tkinter.END, f"Favorite Character: {user_data.get('favorite_character', '')}")

root = tkinter.Tk()
root.title("One PieceFan Club Registration")

# Set the window size and position
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


# Set the background color for the main window
root.configure(bg="yellow")  # Replace with your desired color

# Customize the title font and color
root.option_add('*TFrame*background', '#800080')  # Set background color for the frame
root.option_add('*TLabel*background', '#808000')  # Set background color for labels

# Create and pack widgets
label_title = tkinter.Label(root, text="One Piece Fan Club Registration", font=("Helvetica", 28, "bold"), foreground="#800000")
label_title.pack(pady=10)

label_username = tkinter.Label(root, text="Username:")
label_username.pack(pady=5)
entry_username = tkinter.Entry(root)
entry_username.pack(pady=5)

label_email = tkinter.Label(root, text="Email:")
label_email.pack(pady=5)
entry_email = tkinter.Entry(root)
entry_email.pack(pady=5)

label_favorite_character = tkinter.Label(root, text="Favorite Character:")
label_favorite_character.pack(pady=5)

# Options for the dropdown menu
character = ["LUFFY", "ZORO", "SANJI", "JINBEI", "FRANKY", "BROOK"]
variable = tkinter.StringVar(root)
variable.set("")  # default value

# Dropdown menu
character_menu = tkinter.OptionMenu(root, variable, *character)
character_menu.pack(pady=5)

# Listbox to display selected favorite characters
listbox_favorites = tkinter.Listbox(root, selectmode=tkinter.MULTIPLE)
listbox_favorites.pack(pady=5)

# Buttons
button_add_favorite = tkinter.Button(root, text="Add Favorite", command=add_favorite)
button_add_favorite.pack(pady=5)

button_delete_favorite = tkinter.Button(root, text="Delete Favorite", command=delete_favorite)
button_delete_favorite.pack(pady=5)

button_register = tkinter.Button(root, text="Register", command=register)
button_register.pack(pady=5)

button_read = tkinter.Button(root, text="Read", command=display_user_data)
button_read.pack(pady=5)

# Create an "Update" button
update_button = tkinter.Button( text="Update", command=update)
update_button.pack(pady=5)

button_delete = tkinter.Button(root, text="Delete", command=delete_data)
button_delete.pack(pady=10)

text_widget = tkinter.Text(root, wrap=tkinter.WORD, height=10, width=50)
text_widget.pack(pady=10)


# Record listbox to display registered usernames
listbox_records = tkinter.Listbox(root)
listbox_records.pack(pady=5)
listbox_records.bind("<ButtonRelease-1>")  # Bind the click event to display user information


# Placeholder for registered data
registered_data = {}

# Run the application
root.mainloop()