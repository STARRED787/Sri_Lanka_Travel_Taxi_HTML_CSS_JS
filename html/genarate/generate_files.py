import os

# Updated list of locations
locations = [
    "Andiambalama", "Attanagalla", "Badalgama", "Banduragoda", "Bemmulla", "Biyagama", "Bokalagama",
    "Bollete", "Bopagama", "Buthpitiya", "Dagonna", "Danowita", "Dekatana", "Delgoda", "Dewalapola",
    "Divulapitiya", "Divuldeniya", "Dompe", "Dunagaha", "Ekala", "Gampaha", "Ganemulla", "Gonawala",
    "Heiyanthuduwa", "Henegama", "Hinatiyana Madawala", "Imbulgoda", "Ja-ela", "Kadawatha", "Kahatowita",
    "Kalagedihena", "Kaleliya", "Kaluaggala", "Kandana", "Katana", "Katunayake", "Kelaniya",
    "Kirindiwela", "Kochchikade", "Kotadeniyawa", "Kotugoda", "Loluwagoda", "Lunugama", "Makewita",
    "Makola", "Malwana", "Marandagahamula", "Minuwangoda", "Mirigama", "Mithirigala", "Muddaragama",
    "Mudungoda", "Nedungamuwa", "Negombo", "Nittambuwa", "Niwandama", "Pallewela", "Pamunugama",
    "Pasyala", "Peliyagoda", "Pethiyagoda", "Pugoda", "Radawadunna", "Radawana", "Raddolugama",
    "Ragama", "Seeduwa", "Siyambalape", "Thalahena", "Udugampola", "Urapola", "Uswetakeiyawa",
    "Veyangoda", "Walpita", "Walpola", "Wathurugama", "Wattala", "Weboda", "Weliweriya", "Weweldeniya",
    "Yakkala", "Yatiyana"
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
