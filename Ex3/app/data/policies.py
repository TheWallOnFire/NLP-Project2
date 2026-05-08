# Banking Policy Database
# This module contains policy snippets and guidelines for various banking intents

BANKING_POLICIES = {
    "card_lost": {
        "snippet": "If you have lost your card, please freeze it immediately in the mobile app or call 1-800-BLOCK-NOW. We will issue a replacement within 3-5 business days. A replacement fee may apply.",
        "source": "General Terms & Conditions - Security Section"
    },
    "card_not_received": {
        "snippet": "If you haven't received your new card within 10 business days, please verify your mailing address in the app settings and request a re-shipment. We will track the previous shipment and disable the old card for safety.",
        "source": "Card Delivery Policy"
    },
    "balance_inquiry": {
        "snippet": "You can check your balance via the mobile app, online banking, or by texting BALANCE to 12345. ATM balance checks are free at our bank's machines. For detailed statements, please use online banking.",
        "source": "Help Center - Account Management"
    },
    "transfer_failure": {
        "snippet": "Transfers may fail due to insufficient funds, incorrect recipient details, daily limits, or technical issues. Please check your transaction history for the specific error code. Most failed transfers are automatically reversed within 24 hours.",
        "source": "Payment Guidelines"
    },
    "international_transfer": {
        "snippet": "For international transfers, you need the recipient's SWIFT/BIC code and IBAN. Fees vary by destination and amount. Processing typically takes 1-3 business days. Use the 'International' tab in the transfer section.",
        "source": "Global Banking Guide"
    },
    "blocked_account": {
        "snippet": "Accounts are blocked after three incorrect PIN attempts or for suspicious activity. To unblock, please visit a branch with valid ID or call our security team at 1-800-SECURITY. Online unblocking is available for PIN-related issues.",
        "source": "Security Policy"
    },
    "atm_swallowed_card": {
        "snippet": "If an ATM has swallowed your card, please report it immediately via the app or call 1-800-ATM-HELP. If the ATM is at a branch, visit the staff. We will issue a new card within 3 business days.",
        "source": "ATM Usage Policy"
    },
    "refund_request": {
        "snippet": "For unauthorized transactions or disputes, please submit a refund request through the mobile app or call 1-800-DISPUTE. Investigation typically takes 5-7 business days. Provisional credit may be available for eligible cases.",
        "source": "Dispute Resolution Policy"
    },
    "direct_debit_payment_not_recognized": {
        "snippet": "If you don't recognize a direct debit, you can cancel it up to the day before it's due. For past payments, use the 'Dispute' button in the transaction details. We can process a refund under the Direct Debit Guarantee.",
        "source": "Payment Protections"
    },
    "loan_inquiry": {
        "snippet": "For loan applications, please visit our Loans section in the mobile app or schedule an appointment with a loan officer. We offer personal loans, mortgages, and business financing with competitive rates. Pre-approval is available online.",
        "source": "Lending Services"
    },
    "transaction_history": {
        "snippet": "You can view up to 90 days of transaction history in the mobile app. For older statements, please use online banking or request PDF statements. Transaction details include merchant info, amount, and reference numbers.",
        "source": "Account Services"
    },
    "change_pin": {
        "snippet": "You can change your PIN at any of our bank's ATMs by selecting 'PIN Services' -> 'Change PIN'. For your security, avoid simple combinations like 1234 or your birth date.",
        "source": "Security Settings"
    },
    "general": {
        "snippet": "For general inquiries, please contact our support team at support@ourbank.com, call 1-800-BANK-HELP, or use the live chat feature in our app. Our support hours are Monday-Friday 8AM-8PM, Saturday 9AM-5PM.",
        "source": "Customer Support Overview"
    }
}
