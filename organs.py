print("==== ORGAN DONATION SYSTEM ====")
print("Welcome to the organ donation system.")

while True:
    print("\nAre you an organ donor or an organ recipient?")
    print("1. Organ donor")
    print("2. Organ recipient")
    position = input("Select a your position (1 or 2): ").strip()

    if position == '1':
        # Organ Donors
        print("\nEnter your details")
        full_name = input("1. Full Name(ex: Maria Talasow Carter): ")
        nation = input("2. Nation where donor is currently residing: ")
        dob = input("3. D.O.B(DD/MM/YYYY): ")
        state= input("4. State(ex: either dead or alive): ")
        hospital = input("5. Hospital(ex: Aga Khan): ")
        donation_date = input("6. Date of donation(DD/MM/YYYY): ")
        surgery_time = input("7. Time the surgery was completed: ")
        org = input("8. Donation Organisation: ")

        print("\nThank you! The donor information has been recorded.")
        break
    elif position == '2': 
        # Organ Recepients
        print("\nEnter your details")
        full_name = input("1. Full Name(ex: Maria Talasow Carter): ")
        nation = input("2. Nation where recipient is currently residing: ")
        dob = input("3. D.O.B(DD/MM/YYYY): ")
        hospital = input("4. Hospital(ex: Aga Khan): ")
        donor_id = input("5. Donor ID: ")
        reception_date = input("6. Date of reception(DD/MM/YYYY): ")
        surgery_time = input("7. Time the surgery is set to begin: ")
        org = input("8. Donation Organisation: ")

        print("\nThank you! The recepient information has been recorded.")
        break
    else:
        print("Invalid option, select either '1' or '2'.")
        break

