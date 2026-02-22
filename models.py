# models.py


class Donor:
    def __init__(self, full_name, email):
        self.full_name = full_name
        self.email = email


class Donation:
    def __init__(self, dwrea_id, donor, amount, date, Payment_type):
        self.dwrea_id = dwrea_id
        self.donor = donor
        self.amount = amount
        self.date = date
        self.Payment_type = Payment_type


class PaymentReceipt:
    def __init__(self, dwrea_id, donor_name, amount, date):
        self.dwrea_id = dwrea_id
        self.donor_name = donor_name
        self.amount = amount
        self.date = date