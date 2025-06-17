print("==== ORGAN DONATION SYSTEM ====")
print("Welcome to the organ donation system.")

print("\nAre you an organ donor or an organ recepient?")
print("1. Organ donor")
print("2. Organ recepient")
position = input("Select a your position: ").strip()

while True:
    if position == '1':
        # Organ Donors
        print("\nEnter your details")
        input("1. Full Name(ex: Maria Talasow Carter): ")
        input("2. Nation where donor is currently residing: ")
        input("3. D.O.B(DD/MM/YYYY): ")
        input("4. State(ex: either dead or alive): ")
        input("5. Hospital(ex: Aga Khan): ")
        input("6. Date of donation(DD/MM/YYYY): ")
        input("7. Time the surgery was completed: ")
        input("8. Donation Organisation: ")
        break
    elif position == '2': 
        # Organ Recepients
        print("\nEnter your details")
        input("1. Full Name(ex: Maria Talasow Carter): ")
        input("2. Nation where recepient is currently residing: ")
        input("3. D.O.B(DD/MM/YYYY): ")
        input("4. Hospital(ex: Aga Khan): ")
        input("5. Donor ID: ")
        input("6. Date of reception(DD/MM/YYYY): ")
        input("7. Time the surgery is set to begin: ")
        input("8. Donation Organisation: ")
        break
    else:
        print("Select a valid option")
        break

