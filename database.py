import sqlite3

# create a connection to the database
conn = sqlite3.connect('app_instances.db')

# create a cursor object
cursor = conn.cursor()

# create the Devices table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Devices (
        device_id INTEGER PRIMARY KEY,
        device_name TEXT
    )
''')

# create the Applications table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Applications (
        app_id INTEGER PRIMARY KEY,
        app_name TEXT
    )
''')

# create the AppInstances table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS AppInstances (
        instance_id INTEGER PRIMARY KEY,
        device_id INTEGER,
        app_id INTEGER,
        start_time DATETIME,
        end_time DATETIME,
        duration_secs INTEGER,
        FOREIGN KEY (device_id) REFERENCES Devices(device_id),
        FOREIGN KEY (app_id) REFERENCES Applications(app_id)
    )
''')

# commit the changes and close the connection
conn.commit()
conn.close()
