# Import the required modules
import sqlite3

# Connect to the SQLite database file named "books.db"
connect = sqlite3.connect("books.db")

# Create a cursor object to execute SQL queries
cursor = connect.cursor()

# Create the 'books' table if it does not exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        rating FLOAT,
        genre TEXT,
        summary TEXT
    )
""")

# Create the 'reviews' table if it does not exist, with a foreign key reference to the 'books' table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER,
        user TEXT,
        rating FLOAT,
        review_text TEXT,
        FOREIGN KEY (book_id) REFERENCES books(id)
    )
""")

# Data for books to be inserted into the 'books' table
books_data = [
    ("Ephemeral Echoes", "Luna Mirage", 4.5, "Fantasy", "Luna Mirage crafts a mesmerizing fantasy where a reluctant hero must wield the power of forgotten realms to thwart an ancient darkness, blending magic and adventure seamlessly."),
    ("Quantum Whispers", "Orion Nexus", 4.5, "Science Fiction", "Orion Nexus explores the blurred lines between reality and imagination as a group of scientists unravels the secrets of quantum mechanics, leading to a world shaped by the power of the mind."),
    ("City of Secrets", "Lucinda Shadows", 4.8, "Mystery Thriller", "Lucinda Shadows weaves a gripping mystery as a detective races against time to decipher cryptic messages throughout a sprawling metropolis, revealing shocking truths that reshape the city."),
    ("Threads of Time", "Jasper Kaleidos", 4.6, "Historical Fiction", "Jasper Kaleidos creates a rich tapestry of interconnected lives across epochs, exploring the profound impact of seemingly unrelated choices and the threads of fate that bind them."),
    ("Stardust Serenade", "Nova Celestia", 4.9, "Romance Fantasy", "Nova Celestia's celestial love story follows two souls across dimensions, overcoming cosmic challenges in a realm where starlight weaves destinies, offering a tale of transcendent love."),
    ("Whispers in the Void", "Orion Eclipse", 4.7, "Space Opera", "Orion Eclipse crafts an epic space opera, where a reluctant hero navigates interstellar politics, ancient prophecies, and cosmic anomalies to save the galaxy from impending doom."),
    ("Specters of Solitude", "Astrid Solstice", 4.4, "Paranormal Mystery", "Astrid Solstice unravels a chilling paranormal mystery, as a detective confronts spectral apparitions tied to a forgotten tragedy, leading to a revelation that blurs the line between the living and the dead."),
    ("Labyrinth of Illusions", "Mirage Phantasia", 4.6, "Psychological Thriller", "Mirage Phantasia delves into the complexities of the human mind, crafting a psychological thriller where characters navigate a labyrinth of illusions, facing their deepest fears and desires."),
    ("Chronicles of Celestial Beasts", "Drakon Skysong", 4.8, "Mythical Adventure", "Drakon Skysong's mythical adventure unfolds as a group of heroes embarks on a quest to restore balance to a world inhabited by celestial beasts, blending awe-inspiring landscapes with epic battles."),
    ("Eternal Enigma", "Serenity Cipher", 4.7, "Mystery Fantasy", "Serenity Cipher's mystery fantasy unveils a world where enigmatic puzzles hold the key to unraveling an ancient secret, challenging characters to decipher the clues before time runs out."),
    ("Crimson Horizon", "Scarlet Horizon", 4.5, "Historical Fantasy", "Scarlet Horizon's historical fantasy paints a vivid picture of an alternate past, where empires clash, and characters navigate a world of political intrigue, magic, and war on the crimson horizon."),
    ("Whispers Among Shadows", "Silhouette Muse", 4.6, "Suspenseful Romance", "Silhouette Muse crafts a suspenseful romance where secrets and shadows intertwine, unraveling a love story filled with passion, danger, and unexpected twists."),
    ("Symbiosis", "Nexus Harmonia", 4.9, "Biotechnological Thriller", "Nexus Harmonia's biotechnological thriller explores a future where humans and machines form an intricate symbiotic relationship, blurring the lines between man and technology in a gripping narrative."),
    ("Lost in Luminescence", "Aurora Lumina", 4.8, "Urban Fantasy", "Aurora Lumina's urban fantasy unfolds in a world where hidden realms coexist with the mundane, as characters discover their extraordinary abilities and confront dark forces lurking in the city's shadows."),
    ("Rogue Constellations", "Orion Rogue", 4.7, "Sci-Fi Adventure", "Orion Rogue's sci-fi adventure follows a crew of intergalactic rogues navigating uncharted space, encountering rogue constellations, and unraveling the mysteries of the cosmos in a thrilling space odyssey."),
]

# Insert  data into the 'books' table
for book in books_data:
    try:
        cursor.execute('''
        INSERT INTO books (title, author, rating, genre, summary)
        VALUES (?, ?, ?, ?, ?)
    ''', book)
    except sqlite3.Error as error:
        print(f"Error inserting data: {error}")

# Data for reviews to be inserted into the 'reviews' table
reviews_data = [
    (1, "user1", 4.5, "Ephemeral Echoes is a captivating fantasy with intricate world-building. The characters are well-developed, and the plot keeps you hooked from start to finish."),
    (2, "user2", 4.5, "Quantum Whispers is a mind-bending science fiction adventure. The quantum concepts are explored in a way that adds depth to the storyline."),
    (3, "user3", 4.8, "City of Secrets is a gripping mystery thriller. The detective's race against time and the cryptic messages create an engaging and suspenseful read."),
    (4, "user4", 4.6, "Threads of Time is a well-crafted historical fiction novel. The interconnected lives across epochs provide a fascinating perspective on the impact of choices."),
    (5, "user5", 4.9, "Stardust Serenade is a beautiful romance fantasy. The celestial elements add a magical touch to the love story, making it an enchanting read."),
    (6, "user6", 4.7, "Lone Wolf is an intriguing biography that provides deep insights into the life of the protagonist. The narrative is well-paced, keeping the reader engaged throughout."),
    (7, "user7", 4.4, "Lost in Luminescence offers a unique take on urban fantasy. The hidden realms coexisting with the mundane create a dynamic setting for the characters' extraordinary abilities."),
    (8, "user8", 4.6, "Chronicles of Celestial Beasts takes readers on a mythical adventure filled with awe-inspiring landscapes and epic battles. The celestial beasts add a mystical element to the narrative."),
    (9, "user9", 4.8, "Crimson Horizon paints a vivid picture of an alternate historical fantasy world. The clash of empires, magic, and war on the crimson horizon creates a compelling storyline."),
    (10, "user10", 4.7, "Whispers Among Shadows is a suspenseful romance where secrets and shadows intertwine. The unexpected twists add an extra layer of excitement to the love story."),
    (11, "user11", 4.5, "Symbiosis explores a future where humans and machines form an intricate symbiotic relationship. The blurred lines between man and technology create a gripping biotechnological thriller."),
    (12, "user12", 4.6, "Rogue Constellations follows a crew of intergalactic rogues navigating uncharted space. The encounters with rogue constellations and unraveling cosmic mysteries make it a thrilling space odyssey."),
    (13, "user13", 4.9, "Eternal Enigma presents a mystery fantasy world where enigmatic puzzles hold the key to unraveling an ancient secret. The challenge to decipher the clues adds an exciting element to the narrative."),
    (14, "user14", 4.8, "Specters of Solitude unravels a chilling paranormal mystery, as a detective confronts spectral apparitions tied to a forgotten tragedy. The revelation blurs the line between the living and the dead."),
    (15, "user15", 4.7, "Labyrinth of Illusions delves into the complexities of the human mind, crafting a psychological thriller where characters navigate a labyrinth of illusions, facing their deepest fears and desires."),
    
]

# Insert sample data into reviews table
for review in reviews_data:
    cursor.execute("""
        INSERT INTO reviews (book_id, user, rating, review_text)
        VALUES (?, ?, ?, ?)
    """, review)

# Commit changes to the database
connect.commit()

# Close the cursor and the connection to the database
cursor.close()
connect.close()
