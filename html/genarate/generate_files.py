import os

# Updated list of locations
locations = [
    "Angunakolawewa", "Badalkumbura", "Balaharuwa", "Bibile", "Buddama", "Buttala", "Dambagalla",
    "Dombagahawela", "Ethimale", "Ethiliwewa", "Galabedda", "Hambegamuwa", "Hulandawa", "Katharagama",
    "Kiribbanwewa", "Medagama", "Monaragala", "Nilgala", "Okkampitiya", "Randeniya", "Sella Katharagama",
    "Sewanagala", "Siyambalanduwa", "Thanamalwila", "Pelwatta", "Handapanagala", "Wellawaya"
]

# Directory to save files
output_dir = "taxi_services"

# Ensure the directory exists
os.makedirs(output_dir, exist_ok=True)

# Generate files
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

print(f"HTML files have been successfully created in the '{output_dir}' folder.")
