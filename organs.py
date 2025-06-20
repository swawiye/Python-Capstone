import re  # regex module
from datetime import datetime # importing the datetime class
import sqlite3

# === DATABASE SETUP ===
# Connect to SQLite and create a database file if it doesn't exist
conn = sqlite3.connect('Organs.db')
c = conn.cursor()

# Create Donors table
c.execute('''
    CREATE TABLE IF NOT EXISTS Donors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        nation TEXT,
        dob TEXT,
        age INTEGER,
        state TEXT,
        hospital TEXT,
        donation_date TEXT,
        surgery_time TEXT,
        organ TEXT,
        organization TEXT
    )
''')

# Create Recipients table
c.execute('''
    CREATE TABLE IF NOT EXISTS Recipients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        nation TEXT,
        dob TEXT,
        hospital TEXT,
        donor_id TEXT,
        reception_date TEXT,
        surgery_time TEXT,
        organ TEXT,
        organization TEXT
    )
''')

# Create Transplants table
c.execute('''
    CREATE TABLE IF NOT EXISTS Transplants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        recipient_id INTEGER,
        donor_id INTEGER,
        organ TEXT,
        hospital TEXT,
        date TEXT,
        time TEXT,
        organization TEXT,
        FOREIGN KEY (recipient_id) REFERENCES Recipients(id),
        FOREIGN KEY (donor_id) REFERENCES Donors(id)
    )
''')


print("==== ORGAN DONATION SYSTEM ====")
print("Welcome to the organ donation system.")

# === VALIDATION FUNCTIONS ===

def validate_date(prompt):
    while True:
        date_input = input(prompt).strip()
        try:
            datetime.strptime(date_input, "%d/%m/%Y")
            return date_input
        except ValueError:
            print("Invalid date format. Please use DD/MM/YYYY.")

def validate_time(prompt):
    while True:
        time_input = input(prompt).strip()
        if re.match(r"^(?:[01]\d|2[0-3]):[0-5]\d$", time_input):
            return time_input
        else:
            print("Invalid time format. Please use HH:MM (24-hour format).")

def validate_state(prompt):
    while True:
        state_input = input(prompt).strip().lower()
        if state_input in ['alive', 'dead']:
            return state_input
        else:
            print("Invalid state. Please enter 'alive' or 'dead'.")

DONATEABLE_ORGANS = [
    "heart", "lungs", "liver", "kidneys", "pancreas", "intestines", 
    "corneas", "skin", "bone marrow", "tendons", "veins", "heart valves"
]
def validate_organ(prompt):
    while True:
        organ_input = input(prompt).strip().lower()
        if organ_input in DONATEABLE_ORGANS:
            return organ_input
        else:
            print("Invalid organ. Please enter a valid donateable organ:")
            print(", ".join(DONATEABLE_ORGANS))

# === MAIN MENU ===
while True:
    print("\nWhat services are you seeking?")
    print("1. Register as an organ donor")
    print("2. Register as an organ recipient")
    print("3. Exit the system")
    print("4. Manage records (view, update, delete)")
    position = input("Select your position (1, 2, 3 or 4): ").strip()

    if position == '1':
        # === ORGAN DONOR SECTION ===
        print("\nEnter your details:")
        full_name = input("1. Full Name (e.g., Maria Talasow Carter): ")
        nation = input("2. Nation where donor is currently residing: ")
        dob_str = validate_date("3. D.O.B (DD/MM/YYYY): ")

        # Age validation
        dob = datetime.strptime(dob_str, "%d/%m/%Y")
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        if age < 18:
            print("Sorry, donors must be at least 18 years old.")
            continue

        state = validate_state("4. State (e.g., dead or alive): ")
        hospital = input("5. Hospital (e.g., Aga Khan): ")
        donation_date = validate_date("6. Date of donation (DD/MM/YYYY): ")
        surgery_time = validate_time("7. Time the surgery was completed (HH:MM): ")
        organ = validate_organ("8. Which organ is being donated? ")
        org = input("9. Donation Organization: ")

        # INSERT DONOR DATA INTO DATABASE
        c.execute('''
            INSERT INTO Donors (
                full_name, nation, dob, age, state, hospital, 
                donation_date, surgery_time, organ, organization
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (full_name, nation, dob_str, age, state, hospital, donation_date, surgery_time, organ, org))
        conn.commit()  # Save changes to the database

        print("\n✅ Donor information saved successfully.")

        # Display data for confirmation
        print("\nPlease confirm if the donor's information is correct:")
        print(f"Full Name: {full_name}")
        print(f"Nation of Residence: {nation}")
        print(f"D.O.B: {dob_str} (Age: {age})")
        print(f"State: {state}")
        print(f"Hospital: {hospital}")
        print(f"Donation Date: {donation_date}")
        print(f"Surgery Time: {surgery_time}")
        print(f"Organ: {organ}")
        print(f"Donation Organization: {org}")
        break

    elif position == '2':
        # === ORGAN RECIPIENT SECTION ===
        print("\nEnter your details:")
        full_name = input("1. Full Name (e.g., Maria Talasow Carter): ")
        nation = input("2. Nation where recipient is currently residing: ")
        dob = validate_date("3. D.O.B (DD/MM/YYYY): ")
        hospital = input("4. Hospital (e.g., Aga Khan): ")
        donor_id = input("5. Donor ID: ")
        reception_date = validate_date("6. Date of reception (DD/MM/YYYY): ")
        surgery_time = validate_time("7. Time the surgery is set to begin (HH:MM): ")
        organ = validate_organ("8. Which organ is being received? ")
        org = input("9. Donation Organization: ")

        # === VALIDATION: Verify donor ID exists and organ matches ===
        c.execute("SELECT organ, donation_date, surgery_time FROM Donors WHERE id = ?", (donor_id,))
        donor_data = c.fetchone()

        if not donor_data:
            print("❌ Donor ID not found. Please check the ID.")
            continue

        donor_organ, donor_date_str, donor_time_str = donor_data

        if donor_organ.lower() != organ.lower():
            print(f"❌ Organ mismatch! Donor is donating '{donor_organ}', but recipient requested '{organ}'.")
            continue

        # === VALIDATION: Check surgery is within 24 hours ===
        donor_datetime = datetime.strptime(donor_date_str + ' ' + donor_time_str, "%d/%m/%Y %H:%M")
        recipient_datetime = datetime.strptime(reception_date + ' ' + surgery_time, "%d/%m/%Y %H:%M")

        time_diff = recipient_datetime - donor_datetime
        if not (0 <= time_diff.total_seconds() <= 86400):  # 24 hours = 86400 seconds
            print("❌ Surgery must occur within 24 hours of the donor's operation.")
            print(f"⏱ Time difference is {time_diff}.")
            continue

        # INSERT RECIPIENT DATA INTO DATABASE
        c.execute('''
            INSERT INTO Recipients (
                full_name, nation, dob, hospital, donor_id, 
                reception_date, surgery_time, organ, organization
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (full_name, nation, dob, hospital, donor_id, reception_date, surgery_time, organ, org))
        conn.commit()

        # Get the ID of the newly inserted recipient
        recipient_id = c.lastrowid

        # Insert transplant record
        try:
            c.execute('''
                INSERT INTO Transplants (
                    recipient_id, donor_id, organ, hospital, date, time, organization
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (recipient_id, donor_id, organ, hospital, reception_date, surgery_time, org))
            conn.commit()
            print("✅ Transplant record created successfully.")
        except Exception as e:
            print(f"⚠️ Could not create transplant record: {e}")

        # === VALIDATION: Check if organizations match ===
        c.execute("SELECT organization FROM Donors WHERE id = ?", (donor_id,))
        donor_org = c.fetchone()[0]

        if donor_org.strip().lower() != org.strip().lower():
            print(f"❌ Donation organization mismatch!")
            print(f"Donor is registered under '{donor_org}', but recipient entered '{org}'.")
            continue


        print("\n✅ Recipient information saved successfully.")

        # Display data for confirmation
        print("\nPlease confirm if the recipient's information is correct:")
        print(f"Full Name: {full_name}")
        print(f"Nation of Residence: {nation}")
        print(f"D.O.B: {dob}")
        print(f"Hospital: {hospital}")
        print(f"Donor ID: {donor_id}")
        print(f"Reception Date: {reception_date}")
        print(f"Surgery Time: {surgery_time}")
        print(f"Organ: {organ}")
        print(f"Donation Organization: {org}")
        break

    elif position == '3':
        print("\nThank you for using the Organ Donation System. Goodbye!")
        conn.close()  # Close the database connection before exiting
        exit()  # Exit the program cleanly

    elif position == '4':
        print("\n=== MANAGE RECORDS ===")
        table = input("Which table would you like to manage? (Donors / Recipients / Transplants): ").strip().lower()

        if table not in ['donors', 'recipients', 'transplants']:
            print("Invalid table selection.")
            continue

        print("\n1. View records")
        print("2. Modify a record")
        print("3. Delete a record")
        action = input("Select an action (1-3): ").strip()

        if action == '1':
            # View records
            c.execute(f"SELECT * FROM {table.capitalize()}")
            records = c.fetchall()
            if records:
                for row in records:
                    print(row)
            else:
                print(f"No records found in {table}.")

        elif action == '2':
            record_id = input("Enter the ID of the record you want to modify: ")
            column = input("Which column do you want to modify? ").strip()
            new_value = input("Enter the new value: ")

            # Update record
            try:
                c.execute(f"UPDATE {table.capitalize()} SET {column} = ? WHERE id = ?", (new_value, record_id))
                conn.commit()
                print(f"Record {record_id} updated successfully.")
            except sqlite3.OperationalError as e:
                print(f"Error: {e}")

        elif action == '3':
            record_id = input("Enter the ID of the record you want to delete: ")

            confirm = input(f"Are you sure you want to delete record {record_id} from {table}? (yes/no): ").strip().lower()
            if confirm == 'yes':
                c.execute(f"DELETE FROM {table.capitalize()} WHERE id = ?", (record_id,))
                conn.commit()
                print(f"Record {record_id} deleted successfully.")
            else:
                print("Deletion cancelled.")

        else:
            print("Invalid action. Returning to main menu.")

    else:
        print("Invalid option. Please select either '1', '2', or '3'.")

# Close database connection
conn.close()
