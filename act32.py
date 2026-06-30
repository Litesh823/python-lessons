import getpass

while True:
    # 1. Collect inputs INSIDE the loop so they can be re-prompted if validation fails
    name = input("Enter name : ").strip()
    email = input("Enter email : ").strip()
    password = getpass.getpass("Enter password : ")
    confirm_pass = getpass.getpass("Enter password again : ")

    # 2. Validation Checks (Using 'continue' to restart the loop on failure)
    if len(name) < 6:
        print("❌ Name should be at least 6 characters long.\n")
        continue 
        
    # Fixed: Changed 'and' to 'or'. If EITHER is missing, it's invalid.
    elif '@' not in email or '.' not in email: 
        print("❌ Invalid Email...\n")
        continue
        
    elif len(password) < 8:
        print("❌ Password length must be at least 8 chars long.\n")
        continue
        
    elif password != confirm_pass:
        print("❌ Passwords do not match. Please try again...\n")
        continue
        
    # 3. Success Block (Only runs if all the 'if/elif' checks pass)
    print("\n✅ User created successfully...") 
    print(f"Name  : {name}")
    print(f"Email : {email}\n")
    
    # Fixed: Added the actual input() function here
    choice = input("Do you want to add another user? (y/n): ").strip().lower()
    if choice in ['yes', 'y']:
        print("\n--- Registering Next User ---")
        continue  # Loops back to the top for a fresh start
    else:
        print("Goodbye!")
        break  # Exits the loop and ends the program

