import sqlite3

conn = sqlite3.connect("underlords.db")
c = conn.cursor()

heroes_table = """
    CREATE TABLE heroes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        class INTEGER NOT NULL,
        name STRING, 
        brazilian_name STRING
    )
"""
alliances_table = """
    CREATE TABLE alliances(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name STRING NOT NULL
    )
"""
heroes_alliances_table = """
    CREATE TABLE heroes_alliances(
        heroes_id INTEGER NOT NULL,
        alliances_id INTEGER NOT NULL,
        PRIMARY KEY (heroes_id, alliances_id),
        FOREIGN KEY (heroes_id) REFERENCES heroes(id),
        FOREIGN KEY (alliances_id) REFERENCES alliances(id)
    )
"""
alliances_effects_table = """
    CREATE TABLE alliances_effects(
        alliances_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        effect STRING NOT NULL,
        PRIMARY KEY (alliances_id, quantity),
        FOREIGN KEY (alliances_id) REFERENCES alliances(id)
    )
"""
queries = [
    heroes_table,
    alliances_table,
    heroes_alliances_table,
    alliances_effects_table,
]
for query in queries:
    c.execute(query)

conn.commit()
conn.close()
