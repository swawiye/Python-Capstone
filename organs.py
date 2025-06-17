import re # regex module
from datetime import datetime # importing the datetime class

print("==== ORGAN DONATION SYSTEM ====")
print("Welcome to the organ donation system.")

# Date validation
def validate_date(prompt):
    while True:
        date_input = input(prompt).strip() # user input
        try:
            datetime.strptime(date_input, "%d/%m/%Y") #regex for date format
            return date_input
        except ValueError:
            print("Invalid date format. Please use DD/MM/YYY.")

# Time validation
def validate_time(prompt):
    while True:
        time_input = input(prompt).strip() 
        if re.match(r"^(?:[01]\d|2[0-3]):[0-5]\d$", time_input):
            return time_input
        else:
            print("Invalid time format. Please use HH:MM (24-hour format).")

# State validation
def validate_state(prompt):
    while True:
        state_input = input(prompt).strip().lower()
        if state_input in ['alive', 'dead']:
            return state_input
        else:
            print("Invalid state. Please enter 'alive' or 'dead'.")

while True:
    print("\nAre you an organ donor or an organ recipient?")
    print("1. Organ donor")
    print("2. Organ recipient")
    position = input("Select your position (1 or 2): ").strip()

    if position == '1':
        # Organ Donors
        print("\nEnter your details:")
        full_name = input("1. Full Name (e.g., Maria Talasow Carter): ")
        nation = input("2. Nation where donor is currently residing: ")
        dob = validate_date("3. D.O.B (DD/MM/YYYY): ")

        # Age validation
        today = datetime.today()
        age = (today - dob).days // 365
        if age < 18:
            print("Sorry, donors must be at least 18 years old.")
            continue # loop back to the main menu

        state = validate_state("4. State (e.g., dead or alive): ")
        hospital = input("5. Hospital (e.g., Aga Khan): ")
        donation_date = validate_date("6. Date of donation (DD/MM/YYYY): ")
        surgery_time = validate_time("7. Time the surgery was completed(HH:MM - 24-hour format): ")
        org = input("8. Donation Organization: ")

        print("\nThank you! The donor information has been recorded.")

        # Display data
        print("\nPlease confirm if the donor's information is correct:")
        print("Full Name: " + full_name)
        print("Nation of Residence: " + nation)
        print("D.O.B: " + dob)
        print("State: " + state)
        print("Hospital: " + hospital)
        print("Donation Date: " + donation_date)
        print("Time Surgery Was Completed: " + surgery_time)
        print("Donation Organization: " + org + "\n")
        break

    elif position == '2':
        # Organ Recipients
        print("\nEnter your details:")
        full_name = input("1. Full Name (e.g., Maria Talasow Carter): ")
        nation = input("2. Nation where recipient is currently residing: ")
        dob = validate_date("3. D.O.B (DD/MM/YYYY): ")
        hospital = input("4. Hospital (e.g., Aga Khan): ")
        donor_id = input("5. Donor ID: ")
        reception_date = validate_date("6. Date of reception (DD/MM/YYYY): ")
        surgery_time = validate_time("7. Time the surgery is set to begin (HH:MM - 24-hour format): ")
        org = input("8. Donation Organization: ")

        print("\nThank you! The recipient information has been recorded.")

        # Display data
        print("\nPlease confirm if the recipient's information is correct:")
        print("Full Name: " + full_name)
        print("Nation of Residence: " + nation)
        print("D.O.B: " + dob)
        print("Hospital: " + hospital)
        print("Donor ID: " + donor_id)
        print("Reception Date: " + reception_date)
        print("Time Surgery Is Set to Begin: " + surgery_time)
        print("Donation Organization: " + org + "\n")
        break

    else:
        print("Invalid option. Please select either '1' or '2'.\n")
