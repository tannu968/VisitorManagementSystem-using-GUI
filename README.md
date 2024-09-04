# Shaswat Restaurant Visitor Management System

This is a GUI-based application built with Python's Tkinter library for managing visitor details at Shaswat Restaurant. The application integrates with Firebase to store and retrieve visitor data, including their name, mobile number, and timestamp of their visit. The application allows searching and filtering of visitor data based on date range and mobile number.

## Features

- **Display All Visitors:** View a list of all visitors, with their name, mobile number, and timestamp of the visit.
- **Search by Date Range and Mobile Number:** Filter visitors based on a specific date range or mobile number.
- **Dynamic GUI:** The interface dynamically updates and displays visitor information along with their photos (if available).
- **Firebase Integration:** The visitor data is fetched from and stored in a Firebase Realtime Database.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Firebase Admin SDK
- Tkinter
- Pillow (Python Imaging Library)
- `dateutil` library

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/ShaswatRestaurantVisitor.git
   cd ShaswatRestaurantVisitor

Install the required Python packages:

pip install firebase-admin
pip install python-dateutil
pip install Pillow


Set up Firebase:

Create a Firebase project and download the serviceAccountKey.json file.
Replace the tannu-f8ba9-firebase-adminsdk-30n5u-322cb4d9a1.json in the code with the path to your own Firebase Admin SDK JSON file.
Update the Firebase Realtime Database URL in the code.



**Steps to upload this to GitHub:**

1. Copy the above content into a file named `README.md`.
2. In your repository directory, create a new file and paste the content.
3. Commit the file to your repository using Git commands or GitHub Desktop.
4. Push the changes to GitHub.

This `README.md` file provides an overview of your project, installation steps, usage instructions, and other relevant information.
