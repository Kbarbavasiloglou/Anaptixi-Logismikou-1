# services.py
from models import Donor, Donation, PaymentReceipt


class DonationService:
    def __init__(self):
        self.donations = []
        self.next_dwrea_id = 100

    def create_donation(self, full_name, email, amount, Payment_type, date):
        Message_success = "Επιτυχής πραγματοποίηση δωρεάς."
        Message_fail = "Αποτυχία πραγματοποίησης δωρεάς."

        if full_name == "" or email == "" or Payment_type== "" or date== "" :
            return None, None,None, None, Message_fail

        donor = Donor(full_name, email)

        dwrea_id = self.next_dwrea_id
        self.next_dwrea_id += 1

        donation = Donation(dwrea_id, donor, amount, date, Payment_type)
        self.donations.append(donation)

        receipt = PaymentReceipt(dwrea_id, donor.full_name, amount, date)

        return receipt, Message_success, None

    def get_all_donations(self):
        return self.donations


class ReportService:
    def __init__(self, donation_service):
        self.donation_service = donation_service

    def generate_report(self):
        report = []
        for donation in self.donation_service.get_all_donations():
            report.append({
                "dwrea_id": donation.dwrea_id,
                "donor_name": donation.donor.full_name,
                "amount": donation.amount,
                "date": donation.date,
                "Payment_type": donation.Payment_type
            })
        return report