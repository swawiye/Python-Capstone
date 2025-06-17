print("==== ORGAN DONATION SYSTEM ====")
print("Welcome to the organ donation system.")

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
        dob = input("3. D.O.B (DD/MM/YYYY): ")
        state = input("4. State (e.g., dead or alive): ")
        hospital = input("5. Hospital (e.g., Aga Khan): ")
        donation_date = input("6. Date of donation (DD/MM/YYYY): ")
        surgery_time = input("7. Time the surgery was completed: ")
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
        print("Donation Organization: " + org)
        break

    elif position == '2':
        # Organ Recipients
        print("\nEnter your details:")
        full_name = input("1. Full Name (e.g., Maria Talasow Carter): ")
        nation = input("2. Nation where recipient is currently residing: ")
        dob = input("3. D.O.B (DD/MM/YYYY): ")
        hospital = input("4. Hospital (e.g., Aga Khan): ")
        donor_id = input("5. Donor ID: ")
        reception_date = input("6. Date of reception (DD/MM/YYYY): ")
        surgery_time = input("7. Time the surgery is set to begin: ")
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
        print("Donation Organization: " + org)
        break

    else:
        print("Invalid option. Please select either '1' or '2'.\n")
