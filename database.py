import sqlite3


conn = sqlite3.connect('braiding_services.db')
cur = conn.cursor()


cur.execute('''
CREATE TABLE IF NOT EXISTS Services (
    style_name TEXT,
    duration_hours REAL,
    price REAL,
    skill_level TEXT
)
''')
conn.commit()


def add_service():
    style = input("Enter style name: ")
    duration = float(input("Enter duration (hours): "))
    price = float(input("Enter price ($): "))
    skill = input("Enter skill level (Beginner / Intermediate / Advanced): ")

    cur.execute('INSERT INTO Services VALUES (?, ?, ?, ?)', (style, duration, price, skill))
    conn.commit()
    print(f"\n✅ {style} added successfully!\n")

def view_services():
    print("\n📋 All Services:")
    for row in cur.execute('SELECT * FROM Services'):
        print(f"- {row[0]} | {row[1]} hrs | ${row[2]} | {row[3]}")
    print()

def search_by_price():
    max_price = float(input("Show services cheaper than: $"))
    print(f"\n💅🏽 Services under ${max_price}:")
    for row in cur.execute('SELECT * FROM Services WHERE price <= ?', (max_price,)):
        print(f"- {row[0]} | ${row[2]} | {row[3]}")
    print()

def search_by_skill():
    level = input("Enter skill level (Beginner / Intermediate / Advanced): ")
    print(f"\n🎓 {level} Level Styles:")
    for row in cur.execute('SELECT * FROM Services WHERE skill_level = ?', (level,)):
        print(f"- {row[0]} | ${row[2]} | {row[1]} hrs")
    print()


while True:
    print("💇🏽‍♀️ BRAIDING SERVICES MENU 💇🏽‍♀️")
    print("1. Add a new service")
    print("2. View all services")
    print("3. Search by price")
    print("4. Search by skill level")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_service()
    elif choice == "2":
        view_services()
    elif choice == "3":
        search_by_price()
    elif choice == "4":
        search_by_skill()
    elif choice == "5":
        print("\n👋🏽 Goodbye!")
        break
    else:
        print("\n❌ Invalid choice, try again.\n")

conn.close()
