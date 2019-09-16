import sqlite3
import csv

conn = sqlite3.connect("../../db.sqlite3")
c = conn.cursor()

heroes_insert = """
    INSERT INTO underlords_heroes(
        name, brazilian_name, tier
    ) VALUES(?,?,?)
"""
alliances_insert = """
    INSERT INTO underlords_alliances(
        name
    ) VALUES(?)
"""
heroes_alliances_insert = """
    INSERT INTO underlords_heroes_alliances(
        heroes_id, alliances_id
    ) VALUES(?,?)
"""
alliances_effects_insert = """
    INSERT INTO underlords_allianceseffects(
        alliance_id, quantity, effect
    ) VALUES(?,?,?)
"""

with open("csvs/heroes.csv", "r") as file:
    csv_reader = csv.reader(file, delimiter="|")
    for row in csv_reader:
        data = (row[0], row[1], row[2])
        print(data)
        c.execute(heroes_insert, data)

with open("csvs/alliances.csv", "r") as file:
    csv_reader = csv.reader(file, delimiter="|")
    for row in csv_reader:
        data = (row[0],)
        print(data)
        c.execute(alliances_insert, data)

with open("csvs/heroes_alliances.csv", "r") as file:
    csv_reader = csv.reader(file, delimiter="|")
    for row in csv_reader:
        hero, alliance = row
        c.execute("SELECT id FROM underlords_heroes WHERE name = ?", (hero,))
        heroes_id = c.fetchone()[0]
        c.execute("SELECT id FROM underlords_alliances WHERE name = ?", (alliance,))
        alliances_id = c.fetchone()[0]
        data = (heroes_id, alliances_id)
        c.execute(heroes_alliances_insert, data)

with open("csvs/alliances_effects.csv", "r") as file:
    csv_reader = csv.reader(file, delimiter="|")
    for row in csv_reader:
        alliance, quantity, effect = row
        c.execute("SELECT id FROM underlords_alliances WHERE name = ?", (alliance,))
        alliances_id = c.fetchone()[0]
        data = (alliances_id, quantity, effect)
        c.execute(alliances_effects_insert, data)


conn.commit()
conn.close()
