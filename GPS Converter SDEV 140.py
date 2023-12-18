import tkinter as tk
from tkinter import filedialog
import pandas as pd
import simplekml

class GPSConverter:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("GPS Converter")
        self.file_path = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Module 1: User welcome box with start button
        welcome_label = tk.Label(self.window, text="Welcome to GPS Converter!")
        welcome_label.pack(pady=10)

        start_button = tk.Button(self.window, text="Start", command=self.select_file)
        start_button.pack(pady=5)

    def select_file(self):
        # Module 2: File browse window to choose the CSV file
        filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if filepath:
            self.file_path.set(filepath)
            self.extract_data()
        else:
            self.file_path.set("")
            self.display_message("No file selected.")

    def extract_data(self):
        # Module 3: Extract GPS data from the CSV file
        try:
            df = pd.read_csv(self.file_path.get())
            # Validate for required columns
            if not ('Latitude' in df.columns and 'Longitude' in df.columns):
                raise ValueError("Required columns 'Latitude' and 'Longitude' not found in CSV file.")
            # Check for empty values
            if df['Latitude'].isnull().any() or df['Longitude'].isnull().any():
                raise ValueError("Empty values found in 'Latitude' or 'Longitude' columns.")
            self.display_message("Data extracted successfully!")
            self.export_to_kml()
        except Exception as e:
            self.display_message(f"Failed to extract data.\nError: {str(e)}")

    def export_to_kml(self):
        # Module 4: Export data as points
        try:
            kml = simplekml.Kml()

            df = pd.read_csv(self.file_path.get())

            for _, row in df.iterrows():
                longitude = row['Longitude']
                latitude = row['Latitude']
                name = row['Name']
                description = row['Description']

                kml.newpoint(name=name, description=description, coords=[(longitude, latitude)])

            output_file = filedialog.asksaveasfilename(filetypes=[("KML Files", "*.kml")])
            if output_file:
                kml.save(output_file)
                self.display_message("Data exported successfully!")
            else:
                self.display_message("Export cancelled.")

        except Exception as e:
            self.display_message(f"Failed to export data.\nError: {str(e)}")

    def display_message(self, message):
        message_label = tk.Label(self.window, text=message)
        message_label.pack(pady=5)

    def start(self):
        self.window.mainloop()

if __name__ == "__main__":
    converter = GPSConverter()
    converter.start()

def confirm_close():
 
    #Shows a confirmation dialog to close the program.
   
    confirm_box = tk.messagebox.askquestion(
        title="Close GPS Converter?",
        message="Are you sure you want to close the program?",
        icon="question"
    )
    if confirm_box == "yes":
        self.window.destroy()
    else:
        return
    close_button = tk.Button(self.window, text="Close Program", command=confirm_close)
close_button.pack(pady=10)
# Remember to close the pandas dataframe after use
df.close()
