User Manual for GPS Converter

https://github.com/bneild/SDEV140GIDGUI.git

Introduction
This user manual provides instructions on how to use the GPS Converter, a Python program that converts CSV files containing GPS data into KML files suitable for use with mapping applications.

Installation
Ensure you have Python 3 and the following libraries installed: tkinter, filedialog, pandas, simplekml.
Place the main.py file and any required additional files in the same directory.

Getting Started
Launch the program by running main.py in your terminal.
The main window will open with a welcome message and a "Start" button.

Converting CSV to KML
Click the "Start" button.
A file browser window will appear. Select the CSV file containing your GPS data.
Click "Open" to load the data.
The program will validate the data, checking for required columns (Latitude and Longitude) and empty values.
If validation is successful, you will see a message confirming data extraction.
Click the "Close" button on the file browser window.
A file browser window will reappear for saving the KML file. Choose a location and filename.
Click "Save" to export the data as a KML file.
A message will confirm successful export.

Additional Features
The program includes a confirmation dialog when closing the application.
The code offers basic data validation to ensure correct column names and format.

Error Handling
The program displays error messages if problems occur during data extraction or export.
These messages typically indicate missing or invalid data in the CSV file.

 Further Notes
The current version of the program only supports exporting points from the CSV file.
You can customize the code to add additional features or adjust functionality as needed.

Contact
For any questions or feedback, please contact Ben Neild at bneild@ivytech.edu


Documentation of Source Code

Module 1: User Interface and Initialization
class GPSConverter:
    # This class defines the main application logic and manages the user interface.
    def __init__(self):
        # Initialize the main window and title.
        self.window = tk.Tk()
        self.window.title("GPS Converter")
        # Create a StringVar to store the selected file path.
        self.file_path = tk.StringVar()
        # Call the method to create UI elements.
        self.create_widgets()
    def create_widgets(self):
        # This method creates and arranges the GUI components.

Module 2: File Selection
    def select_file(self):
        # This method opens a file browser window and handles file selection.
        filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        # Set the file path and call data extraction if selected.
        if filepath:
            self.file_path.set(filepath)
            self.extract_data()
        else:
            # Display message if no file is selected.

Module 3: Data Extraction and Validation
    def extract_data(self):
        # This method reads the CSV file and performs basic data validation.
        try:
            df = pd.read_csv(self.file_path.get())
            # Check for required columns and raise error if missing.
            if not ('Latitude' in df.columns and 'Longitude' in df.columns):
                raise ValueError(...)
            # Check for empty values in required columns.
            if df['Latitude'].isnull().any() or df['Longitude'].isnull().any():
                raise ValueError(...)
            # Display success message and call export method.
        except Exception as e:
            # Display error message with exception details.


Module 4: Kml Export and Closing
    def export_to_kml(self):
        # This method converts the data into a KML file and saves it.
        try:
            # Initialize Kml object and read data again.
            kml = simplekml.Kml()
            df = pd.read_csv(self.file_path.get())
            # Iterate through rows and create KML points with name and description.
            ...
            # Open file browser for saving and handle save process.
            ...
        except Exception as e:
            # Display error message with exception details.
            ...

    def start(self):
        # This method starts
