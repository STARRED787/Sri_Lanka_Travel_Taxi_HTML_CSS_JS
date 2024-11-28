import os
import glob

# New list of locations (updated with the new locations)
locations = [
    "Alawwa", 
    "Ambanpola", 
    "Awulegama", 
    "Balalla", 
    "Bingiriya", 
    "Bopitiya", 
    "Boyagane", 
    "Dambadeniya", 
    "Daraluwa", 
    "Deegalla", 
    "Diddeniya", 
    "Dodangaslanda", 
    "Doratiyawa", 
    "Dummalasuriya", 
    "Ehetuwewa", 
    "Galgamuwa", 
    "Giriulla", 
    "Gokarella", 
    "Halmillawewa", 
    "Hettipola", 
    "Ibbagamuwa", 
    "Kadigawa", 
    "Kalugamuwa", 
    "Katupota", 
    "Kekunagolla", 
    "Kirimetiyawa", 
    "Kobeigane", 
    "Konwewa", 
    "Kosgolla", 
    "Kotawehera", 
    "Kuliyapitiya", 
    "Kumbukgete", 
    "Kumbukwewa", 
    "Kurunegala", 
    "Maeliya", 
    "Maho", 
    "Makulewa", 
    "Makulpotha", 
    "Maspotha", 
    "Mawathagama", 
    "Meegalewa", 
    "Melsiripura", 
    "Metiyagane", 
    "Minuwangete", 
    "Moragollagama", 
    "Nagollagama", 
    "Nakkawatta", 
    "Narammala", 
    "Nelliya", 
    "Nikadalupotha", 
    "Nikaweratiya", 
    "Padeniya", 
    "Pannala", 
    "Pilessa", 
    "Polgahawela", 
    "Polpitigama", 
    "Pothuhera", 
    "Ridigama", 
    "Siyambalangamuwa", 
    "Thalakolawewa", 
    "Torayaya", 
    "Uhumiya", 
    "Wadakada", 
    "Wariyapola", 
    "Wellawa", 
    "Weuda"
]

# Directory to save files
output_dir = "taxi_services"

# Remove all existing files in the directory
if os.path.exists(output_dir):
    files = glob.glob(os.path.join(output_dir, "*.html"))
    for file in files:
        os.remove(file)

# Ensure the directory exists
os.makedirs(output_dir, exist_ok=True)

# Generate files for the new locations
for location in locations:
    # Create a valid filename
    filename = f"{location.replace(' ', '_').lower()}.html"
    filepath = os.path.join(output_dir, filename)
    
    # Write basic HTML content to the file
    with open(filepath, "w") as f:
        f.write(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{location} Taxi | Cab Service | 0777756352</title>
        </head>
        <body>
            <h1>Welcome to {location} Taxi Service</h1>
            <p>For reliable and efficient taxi services in {location}, call us now at <strong>0777756352</strong>.</p>
        </body>
        </html>
        """)

print(f"HTML files for the new locations have been successfully created in the '{output_dir}' folder.")
