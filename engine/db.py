import sqlite3

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

# Create tables
query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

# --- Insert common applications into the sys_command table ---
# Note: You may need to change the paths below to match your system.
app_data = [
    ('vscode', 'C:\\Users\\priti\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Code.exe'),
    ('calculator', 'C:\\Windows\\System32\\calc.exe'),
    ('paint', 'C:\\Users\\priti\\AppData\\Local\\Microsoft\\WindowsApps\\mspaint.exe'),
    ('notepad', 'C:\\Windows\\System32\\notepad.exe'),
    ('microsoft edge', 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'),
    ('command prompt', 'C:\\Windows\\System32\\cmd.exe'),
    ('file explorer', 'C:\\Windows\\explorer.exe'),
    ('control panel', 'C:\\Windows\\System32\\control.exe'),
    ('task manager', 'C:\\Windows\\System32\\Taskmgr.exe'),
    ('word', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE'),
    ('excel', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE'),
    ('powerpoint', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE'),
    ('anydesk', 'C:\\Program Files (x86)\\AnyDesk\\AnyDesk.exe'),
    ('chrome', 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
]
cursor.executemany('INSERT OR IGNORE INTO sys_command (name, path) VALUES (?, ?)', app_data)

# --- Insert popular websites and apps with URI schemes into the web_command table ---
web_data = [
    ('youtube', 'https://www.youtube.com/'),
    ('web whatsapp', 'https://web.whatsapp.com/'),
    ('geeks for geeks', 'https://www.geeksforgeeks.org/'),
    ('wikipedia', 'https://www.wikipedia.org/'),
    ('camera', 'microsoft.windows.camera:')
]
cursor.executemany('INSERT OR IGNORE INTO web_command (name, url) VALUES (?, ?)', web_data)

con.commit()
con.close()

print("Database populated successfully.")