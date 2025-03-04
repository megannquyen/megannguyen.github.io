#========================================================================================================
# MEGAN NGUYEN PROJECT 1
#========================================================================================================

from datetime import datetime

while True:  # big loop
    # timestamps
    now = datetime.now()  # Get the current time
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")  # Format as YYYY-MM-DD HH:MM:SS
    print("\nTimestamp:", current_time)

    # 2. pass type 
    while True: #smaller loop
        print("\nWhat type of park pass would you like to purchase today?".title())
        print("\nSilver Pass: $625/person (Must be a resident of Southern California)".title())
        print("Gold Pass: $995/person".title())
        print("Platinum Pass: $1399/person".title())

        passType = input("\nEnter desired pass type. (Silver, Gold, or Platinum): ").strip().lower()

        if passType not in ['silver', 'gold', 'platinum']:
            print("Invalid selection. Please enter Silver, Gold, or Platinum.")
            continue

        if passType == "silver":
            price = 625
            resident = input("\nYou chose the Silver pass. Are you a resident of Southern California? (yes/no) ").strip().lower()

            if resident != "yes":
                print("Sorry! The Silver pass is only for Southern California Residents.")
                continue  # go back to pass type selection
            
        elif passType == "gold":
            price = 995
            print("Each Gold Pass Costs $995")
            
        elif passType == "platinum":
            price = 1399
            print("Each Platinum Pass Costs $1399")
        
        break  # break out of the pass select loop 

    # qty of passes
    while True: #sml loop
        try:
            numPasses = int(input(f"How many {passType} Passes do you want? "))
            if numPasses < 1:
                print("Please enter a positive number of passes.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    print(f"You got it. You would like {numPasses} {passType} pass(es).")

    subtotal_passes = numPasses * price

    # parking pass
    while True: #small loop
        parking_passes = 0  # default to 0 

        need_parking = input("\nWill you need an annual parking pass? (yes/no): ").strip().lower()
        if need_parking == "yes":
            try:
                parking_passes = int(input("How many parking passes will you need? "))
                if parking_passes < 0:
                    print("Please enter a valid number of parking passes.")
                    continue
                print(f"You got it. You would like {parking_passes} Annual Parking Pass(es).")
                break
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
        elif need_parking == "no":
            print("You got it. You would not like to purchase any Annual Parking Pass(es).")
            break
        else:
            print("Invalid selection. Please input 'yes' or 'no'.")

    parking_price = 135
    subtotal_parking = parking_price * parking_passes

    # subtotal w/o Club 33
    subtotal = subtotal_passes + subtotal_parking
    print(f"\n{passType} passes (${price:.2f} ea) x {numPasses} = ${subtotal_passes:.2f}".title())
    print(f"Parking passes (${parking_price:.2f} ea) x {parking_passes} = ${subtotal_parking:.2f}".title())
    print(f"Subtotal = ${subtotal:.2f}".title())

    # club 33 
    while True: #smal loop
        club33 = input("\nAre you a member of Club 33? (yes/no) ").strip().lower()
        if club33 in ["yes", "no"]:
            break
        print("Invalid input. Please enter 'yes' or 'no'.")

    club33disc = subtotal * 0.1 if club33 == "yes" else 0
    club33subtotal = subtotal - club33disc

    # receipt printing
    print("\n------ RECEIPT ------")
    print(f"{passType} passes (${price:.2f} ea) x {numPasses} = ${subtotal_passes:.2f}".title())
    print(f"Parking passes (${parking_price:.2f} ea) x {parking_passes} = ${subtotal_parking:.2f}".title())
    print(f"Subtotal: ${subtotal:.2f}".title())
  
    if club33 == "yes":
            print(f"Club 33 discount (10%): -${club33disc:.2f}".title())
            print(f"Discounted Subtotal: ${club33subtotal:.2f}".title())

    # taxes
    tax_rate = 0.0975
    tax_due = club33subtotal * tax_rate
    print(f"Tax (9.75%): ${tax_due:.2f}".title())

    # grand total
    grandtotal = club33subtotal + tax_due
    print(f"\nGrand Total: ${grandtotal:.2f}".title())
    print("-------------------")

    # continu or Quit
    while True: #small loop
        continue_transaction = input("\nWould you like to process another reservation or quit? (yes/quit): ").strip().lower()
        if continue_transaction in ["yes", "quit"]:
            break
        print("Invalid input. Please enter 'yes' or 'quit'.")

    if continue_transaction == "quit":
        print("Thank you for using the Disney Pass Purchase System. Goodbye!")
        break  # exit big loop
