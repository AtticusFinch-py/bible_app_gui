from tkinter import Tk, Label, Entry, Button, Text, font, Scrollbar, END
from bible_functions import retrieve_verses

def search_verse():
    search_query = verse_entry.get()
    verses, cross_references = retrieve_verses(search_query)

    # Format verses with bullet points and line breaks for easier reading
    formatted_verses = '\n'.join([f"{verse.split(':')[0]}:\n{' '.join(verse.split(':')[1:])}" for verse in verses])

    # If there are cross references, format them too
    if cross_references:
        formatted_cross_references = '\n'.join([f"{ref.split(':')[0]}:\n{' '.join(ref.split(':')[1:])}" for ref in cross_references])
        formatted_verses += "\n\nCross-References:\n" + formatted_cross_references

    # Use the insert method to add text to the Text widget
    verse_text.delete(1.0, END)  # Clear the existing text first
    verse_text.insert(END, formatted_verses)

# Create the main window
window = Tk()
window.title("Bible App")

# Create the UI components
verse_label = Label(window, text="Enter Verse:")
verse_entry = Entry(window)
search_button = Button(window, text="Search", command=search_verse)

# Set the font size for the verse text
verse_font = font.Font(size=14)  # Adjust the size value as needed

# Use a Text widget for displaying the verse text
verse_text = Text(window, font=verse_font, width=100, height=40, wrap="word")
scrollbar = Scrollbar(window, command=verse_text.yview)
verse_text['yscrollcommand'] = scrollbar.set

# Arrange the components using grid layout
verse_label.grid(row=0, column=0, padx=10, pady=10)
verse_entry.grid(row=0, column=1, padx=10, pady=10)
search_button.grid(row=0, column=2, padx=10, pady=10)
verse_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
scrollbar.grid(row=1, column=3, sticky='ns')

# Start the main event loop
window.mainloop()



