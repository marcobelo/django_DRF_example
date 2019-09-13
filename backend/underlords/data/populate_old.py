import sqlite3
import csv

conn = sqlite3.connect("underlords.db")
c = conn.cursor()

heroes_insert = """
    INSERT INTO heroes(
        name, brazilian_name, class
    ) VALUES(?,?,?)
"""
alliances_insert = """
    INSERT INTO alliances(
        name
    ) VALUES(?)
"""
heroes_alliances_insert = """
    INSERT INTO heroes_alliances(
        heroes_id, alliances_id
    ) VALUES(?,?)
"""
alliances_effects_insert = """
    INSERT INTO alliances_effects(
        alliances_id, quantity, effect
    ) VALUES(?,?,?)
"""

with open("data/heroes.csv", "r") as file:
    csv_reader = csv.reader(file, delimiter="|")
    for row in csv_reader:
        data = (row[0], row[1], row[2])
        print(data)
        c.execute(heroes_insert, data)

with open("data/alliances.csv", "r") as file:
    csv_reader = csv.reader(file, delimiter="|")
    for row in csv_reader:
        data = (row[0],)
        print(data)
        c.execute(alliances_insert, data)

with open("data/heroes_alliances.csv", "r") as file:
    csv_reader = csv.reader(file, delimiter="|")
    for row in csv_reader:
        hero, alliance = row
        c.execute("SELECT id FROM heroes WHERE name = ?", (hero,))
        heroes_id = c.fetchone()[0]
        c.execute("SELECT id FROM alliances WHERE name = ?", (alliance,))
        alliances_id = c.fetchone()[0]
        data = (heroes_id, alliances_id)
        c.execute(heroes_alliances_insert, data)

with open("data/alliances_effects.csv", "r") as file:
    csv_reader = csv.reader(file, delimiter="|")
    for row in csv_reader:
        alliance, quantity, effect = row
        c.execute("SELECT id FROM alliances WHERE name = ?", (alliance,))
        alliances_id = c.fetchone()[0]
        data = (alliances_id, quantity, effect)
        c.execute(alliances_effects_insert, data)


conn.commit()
conn.close()
