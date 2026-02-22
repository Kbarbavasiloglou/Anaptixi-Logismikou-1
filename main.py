# main.py
from services import DonationService, ReportService


ADMIN_CREDENTIALS = {
    "admin": "pass"
}


def print_menu():
    print("\n=== ΜΕΝΟΥ ===")
    print("1. Πραγματοποίηση δωρεάς")
    print("2. Προβολή αναφοράς δωρεών (Admin Users μόνο)")
    print("0. Έξοδος")


def handle_create_donation(donation_service):
    print("\n--- Πραγματοποίηση δωρεάς ---")

    full_name = input("Ονοματεπώνυμο: ")
    email = input("Email: ")

   
    print("\nΕπιλογές ποσού:")
    print("1. 5€")
    print("2. 10€")
    print("3. 20€")
    print("4. 50€")

    selection = input("Επιλογή (1-4): ")

    if selection == "1":
        amount = 5
    elif selection == "2":
        amount = 10
    elif selection == "3":
        amount = 20
    elif selection == "4":
        amount = 50
    else:
        Message_fail = "Αποτυχία πραγματοποίησης δωρεάς."
        print(Message_fail)
        return

    Payment_type = input("Payment_type (card/cash): ")

    date = input("Ημερομηνία (YYYY-MM-DD): ")

    confirm = input("Επιβεβαίωση δωρεάς; (y/n): ")

    if confirm != "y":
        Message_fail = "Αποτυχία πραγματοποίησης δωρεάς."
        print(Message_fail)
        return

    receipt, Message_success, Message_fail = donation_service.create_donation(
        full_name, email, amount, Payment_type, date
    )

    if Message_fail is not None:
        print(Message_fail)
        return

    print(Message_success)

    print("\n=== ΑΠΟΔΕΙΞΗ ΠΛΗΡΩΜΗΣ ===")
    print("dwrea_id:", receipt.dwrea_id)
    print("Δωρητής:", receipt.donor_name)
    print("Ποσό:", receipt.amount, "€")
    print("Ημερομηνία:", receipt.date)
    print("=========================")


def handle_admin_report(report_service):
    print("\n--- Login Διαχειριστή ---")

    username = input("Username: ")
    password = input("Password: ")

    if username not in ADMIN_CREDENTIALS or ADMIN_CREDENTIALS[username] != password:
        print("Λάθος στοιχεία.")
        return

    report = report_service.generate_report()

    if len(report) == 0:
        print("Δεν υπάρχουν δωρεές.")
        return

    print("\n--- Αναφορά Δωρεών ---")
    for entry in report:
        print(
            entry["dwrea_id"], "|",
            entry["donor_name"], "|",
            entry["amount"], "€ |",
            entry["date"], "|",
            entry["Payment_type"]
        )


def main():
    donation_service = DonationService()
    report_service = ReportService(donation_service)

    # ΔΟΚΙΜΑΣΤΙΚΑ ΔΕΔΟΜΕΝΑ
    donation_service.create_donation("Maria Papadopoulou", "maria@mail.com", 10, "card", "2025-12-01")
    donation_service.create_donation("Nikos Georgiou", "nikos@mail.com", 20, "cash", "2025-12-15")
    donation_service.create_donation("Eleni Konsta", "eleni@mail.com", 50, "card", "2026-01-12")
    donation_service.create_donation("Giorgos P.", "giorgos@mail.com", 5, "cash", "2026-02-01")

    while True:
        print_menu()
        choice = input("Επιλογή: ")

        if choice == "1":
            handle_create_donation(donation_service)
        elif choice == "2":
            handle_admin_report(report_service)
        elif choice == "0":
            print("Έξοδος!")
            break
        else:
            print("Μη έγκυρη επιλογή.")


if __name__ == "__main__":
    main()