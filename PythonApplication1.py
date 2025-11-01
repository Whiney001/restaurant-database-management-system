

import sqlite3

#  Function to Add a Restaurant
def add_restaurant(name, longitude, latitude, address, postcode, cuisine):
    conn = sqlite3.connect("restaurantList.db")
    cursor = conn.cursor()

    cursor.execute(f"""
        INSERT INTO Restaurants (Name, Long, Lat, Address, Postcode, Cuisine)
        VALUES (?, ?, ?, ?, ?, ?);
    """, (name, longitude, latitude, address, postcode, cuisine))

    conn.commit()
    conn.close()
    print(f" Added restaurant: {name}")

#  Function to Add a Menu Item
def add_menu_item(restaurant_id, dish_name, price, dietary_info):
    conn = sqlite3.connect("restaurantList.db")
    cursor = conn.cursor()

    cursor.execute(f"""
        INSERT INTO Menus (RestaurantID, DishName, Price, DietaryInfo)
        VALUES (?, ?, ?, ?);
    """, (restaurant_id, dish_name, price, dietary_info))

    conn.commit()
    conn.close()
    print(f" Added menu item: {dish_name}")

#  Function to Add a Review
def add_review(restaurant_id, rating, comment):
    conn = sqlite3.connect("restaurantList.db")
    cursor = conn.cursor()

    if 1 <= rating <= 5:
        cursor.execute(f"""
            INSERT INTO Reviews (RestaurantID, Rating, Comment)
            VALUES (?, ?, ?);
        """, (restaurant_id, rating, comment))

        conn.commit()
        conn.close()
        print(f" Added review for Restaurant ID {restaurant_id}")
    else:
        print(" Invalid rating! Must be between 1 and 5.")

# Function to Add Dietary Information
def add_dietary_info(menu_id, dietary_type):
    conn = sqlite3.connect("restaurantList.db")
    cursor = conn.cursor()

    cursor.execute(f"""
        INSERT INTO Dietary_Info (MenuID, Type)
        VALUES (?, ?);
    """, (menu_id, dietary_type))

    conn.commit()
    conn.close()
    print(f" Added dietary info '{dietary_type}' to Menu ID {menu_id}")
    import sqlite3

# Connect to the database (Creates it if it doesn't exist)
conn = sqlite3.connect("restaurantList.db")
cursor = conn.cursor()

#  Drop tables if they already exist (optional, for fresh starts)
cursor.execute("DROP TABLE IF EXISTS Restaurants;")
cursor.execute("DROP TABLE IF EXISTS  Menus;")
cursor.execute("DROP TABLE IF EXISTS Reviews;")
cursor.execute("DROP TABLE IF EXISTS Dietary_Info;")

# Create Restaurants Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Restaurants (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Long REAL NOT NULL,
        Lat REAL NOT NULL,
        Address TEXT,
        Postcode TEXT,
        Cuisine TEXT
    );
""")

#  Create Menus Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Menus (
        MenuID INTEGER PRIMARY KEY AUTOINCREMENT,
        RestaurantID INTEGER,
        DishName TEXT NOT NULL,
        Price REAL,
        DietaryInfo TEXT,
        FOREIGN KEY (RestaurantID) REFERENCES Restaurants(ID)
    );
""")

#  Create Reviews Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Reviews (
        ReviewID INTEGER PRIMARY KEY AUTOINCREMENT,
        RestaurantID INTEGER,
        Rating INTEGER CHECK (Rating >= 1 AND Rating <= 5),
        Comment TEXT,
        FOREIGN KEY (RestaurantID) REFERENCES Restaurants(ID)
    );
""")

# Create Dietary_Info Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Dietary_Info (
        DietaryID INTEGER PRIMARY KEY AUTOINCREMENT,
        MenuID INTEGER,
        Type TEXT NOT NULL,  -- Vegan, Vegetarian, Gluten-Free, etc.
        FOREIGN KEY (MenuID) REFERENCES Menus(MenuID)
    );
""")

#  Commit and close the connection
conn.commit()
conn.close()

print( "Database setup complete!")