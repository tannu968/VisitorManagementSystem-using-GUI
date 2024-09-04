

from firebase_admin import credentials, db, initialize_app
import tkinter as tk
from datetime import datetime
from dateutil import parser as date_parser
from PIL import ImageTk, Image
import base64
from io import BytesIO

cred = credentials.Certificate("C:/Users/Dell/Downloads/tannu-f8ba9-firebase-adminsdk-30n5u-322cb4d9a1.json")
initialize_app(cred, {'databaseURL': 'https://tannu-f8ba9-default-rtdb.firebaseio.com/'})

def display_all_visitors_gui(root, from_date=None, to_date=None, mobile_number=None):
    try:
        from_date_obj = date_parser.parse(from_date).date() if from_date else None
        to_date_obj = date_parser.parse(to_date).date() if to_date else None
    except Exception as e:
        print("Error parsing date:", e)
        return

    all_visitors_window = tk.Toplevel(root)
    all_visitors_window.title("All Visitors")
    all_visitors_window.geometry("800x600")
    all_visitors_window.configure(bg="#6F4E37")  # Set the background color to #6F4E37

    all_visitors_window.attributes('-alpha', 0)  # Start with transparency
    for i in range(1, 101):
        all_visitors_window.attributes('-alpha', i / 100)  # Gradually increase transparency
        all_visitors_window.update_idletasks()
        all_visitors_window.after(5)  # Adjust animation speed

    all_visitors_frame = tk.Frame(all_visitors_window)
    all_visitors_frame.pack(fill='both', expand=True)

    scrollbar = tk.Scrollbar(all_visitors_frame)
    scrollbar.pack(side="right", fill="y")

    canvas = tk.Canvas(all_visitors_frame, yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar.config(command=canvas.yview)

    inner_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    ref = db.reference('/visitors')
    visitors = ref.get()

    if visitors:
        for i, (visitor_id, visitor_data) in enumerate(visitors.items()):
            timestamp = visitor_data.get('timestamp', 'Unknown')
            visitor_date = date_parser.parse(timestamp).date()  

            if from_date_obj and to_date_obj:
                if not (from_date_obj <= visitor_date <= to_date_obj):
                    continue

            name = visitor_data.get('name', 'Unknown')
            mobile = visitor_data.get('mobile_number', 'Unknown')
            photo_data = visitor_data.get('photo', None)  

            if mobile_number and mobile_number != mobile:
                continue

            bg_color = "#FFFFFF" if i % 2 == 0 else "#6F4E37"

            row_frame = tk.Frame(inner_frame, bg=bg_color)
            row_frame.pack(fill='x', padx=10, pady=5)  

            if photo_data:
                photo_bytes = base64.b64decode(photo_data)
                photo_image = Image.open(BytesIO(photo_bytes))
                photo_image = photo_image.resize((100, 100), Image.BILINEAR)
                photo_image = ImageTk.PhotoImage(photo_image)
                visitor_photo_label = tk.Label(row_frame, image=photo_image)
                visitor_photo_label.image = photo_image
                visitor_photo_label.pack(side='left', padx=(0, 10)) 

            name_label = tk.Label(row_frame, text=f"Name: {name}", font=("Helvetica", 30))
            name_label.pack(side='left')
            if bg_color == "#6F4E37":
                name_label.configure(bg=bg_color, fg="white")
            else:
                name_label.configure(bg=bg_color, fg="black")

            mobile_label = tk.Label(row_frame, text=f"Mobile: {mobile_number}", font=("Helvetica", 30))
            mobile_label.pack(side='left', padx=(10, 0))
            if bg_color == "#6F4E37":
                mobile_label.configure(bg=bg_color, fg="white")
            else:
                mobile_label.configure(bg=bg_color, fg="black")

            timestamp_label = tk.Label(row_frame, text=f"Timestamp: {timestamp}", font=("Helvetica", 30))
            timestamp_label.pack(side='left', padx=(10, 0))
            if bg_color == "#6F4E37":
                timestamp_label.configure(bg=bg_color, fg="white")
            else:
                timestamp_label.configure(bg=bg_color, fg="black")

    else:
        print("No visitors found!")

    inner_frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

from PIL import Image, ImageTk


def create_gui():
    root = tk.Tk()
    root.title("Visitor Details Search")
    root.geometry("800x600")
    root.configure(bg="#6F4E37")  

    logo_image = Image.open("C:/Users/Dell/Downloads/WhatsApp Image 2024-03-28 at 4.11.51 PM.jpeg")
    logo_image = logo_image.resize((80, 80))  
    logo_photo = ImageTk.PhotoImage(logo_image)

    logo_label = tk.Label(root, image=logo_photo, bg="#6F4E37")
    logo_label.image = logo_photo
    logo_label.pack(side="left", padx=10, pady=10, anchor="nw")  

    heading_label = tk.Label(root, text="Shaswat Restaurant", bg="#6F4E37", fg="white", font=("Helvetica", 50, "bold"))
    heading_label.pack(pady=20)  

    from_date_label = tk.Label(root, text="From Date (YYYY-MM-DD):", bg="#6F4E37", fg="white", font=("Helvetica", 16))
    from_date_label.pack()

    entry_from_date = tk.Entry(root, width=50)
    entry_from_date.pack()

    to_date_label = tk.Label(root, text="To Date (YYYY-MM-DD):", bg="#6F4E37", fg="white", font=("Helvetica", 16))
    to_date_label.pack()

    entry_to_date = tk.Entry(root, width=50)
    entry_to_date.pack()

    mobile_number_label = tk.Label(root, text="Mobile Number:", bg="#6F4E37", fg="white", font=("Helvetica", 16))
    mobile_number_label.pack()

    entry_mobile_number = tk.Entry(root, width=50)
    entry_mobile_number.pack()

    search_button = tk.Button(root, text="Search", command=lambda: search_by_date_range(root, entry_from_date, entry_to_date, entry_mobile_number), font=("Helvetica", 16))
    search_button.pack()

    display_button = tk.Button(root, text="Display All Visitors", command=lambda: display_all_visitors_gui(root), font=("Helvetica", 16))
    display_button.pack()

    root.mainloop()


def search_by_date_range(root, from_date_entry, to_date_entry, mobile_number_entry):
    from_date = from_date_entry.get()
    to_date = to_date_entry.get()
    mobile_number = mobile_number_entry.get()
    display_all_visitors_gui(root, from_date, to_date, mobile_number)

create_gui()






