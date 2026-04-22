import os
import argparse
from datasets import load_dataset
import pandas as pd

# Hardcoded intent names for BANKING77 dataset (77 intents)
# This ensures robustness when loading via mteb/banking77 which lacks metadata
BANKING77_INTENTS = [
    "activate_my_card", "age_limit", "apple_pay_or_google_pay", "atm_support", 
    "automatic_top_up", "balance_not_updated_after_bank_transfer", 
    "balance_not_updated_after_cheque_or_cash_deposit", "beneficiary_not_allowed", 
    "cancel_transfer", "card_about_to_expire", "card_acceptance", "card_arrival", 
    "card_delivery_estimate", "card_linking", "card_not_working", 
    "card_payment_fee_charged", "card_payment_not_recognised", 
    "card_payment_wrong_exchange_rate", "card_swallowed", "cash_withdrawal_charge", 
    "cash_withdrawal_not_recognised", "change_pin", "compromised_card", 
    "contactless_not_working", "country_support", "declined_card_payment", 
    "declined_cash_withdrawal", "declined_transfer", 
    "direct_debit_payment_not_recognised", "disposable_card_limits", 
    "edit_personal_details", "exchange_charge", "exchange_rate", 
    "exchange_via_app", "extra_charge_on_statement", "failed_transfer", 
    "fiat_currency_support", "get_disposable_virtual_card", "get_physical_card", 
    "getting_spare_card", "getting_virtual_card", "lost_or_stolen_card", 
    "lost_or_stolen_phone", "order_physical_card", "passcode_forgotten", 
    "pending_card_payment", "pending_cash_withdrawal", "pending_top_up", 
    "pending_transfer", "pin_blocked", "receiving_money", "refund_not_showing_up", 
    "request_refund", "reverted_card_payment?", "supported_cards_and_currencies", 
    "terminate_account", "top_up_by_bank_transfer_charge", "top_up_by_card_charge", 
    "top_up_by_cash_or_cheque", "top_up_failed", "top_up_limits", 
    "top_up_reverted", "topping_up_by_card", "transaction_charged_twice", 
    "transfer_fee_charged", "transfer_into_account", 
    "transfer_not_received_by_recipient", "transfer_timing", 
    "unable_to_verify_identity", "verify_my_identity", "verify_source_of_funds", 
    "verify_top_up", "virtual_card_not_working", "visa_or_mastercard", 
    "why_verify_identity", "wrong_amount_of_cash_received", 
    "wrong_exchange_rate_for_cash_withdrawal"
]

def main():
    parser = argparse.ArgumentParser(description="Preprocess BANKING77 data for Intent Detection")
    parser.add_argument("--train_size", type=int, default=1000, help="Number of training samples to use")
    parser.add_argument("--test_size", type=int, default=200, help="Number of test samples to use")
    parser.add_argument("--output_dir", type=str, default="sample_data", help="Directory to save processed data")
    args = parser.parse_args()
    
    print(f"Downloading/Loading BANKING77 dataset (via mteb/banking77)...")
    try:
        dataset = load_dataset("mteb/banking77")
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return
    
    # Preprocess splits
    def process_split(split_name, size):
        df = dataset[split_name].to_pandas()
        if size < len(df):
            df = df.sample(n=size, random_state=42)
        
        # Map integer labels to string intent names for LLM fine-tuning using hardcoded list
        df["intent"] = df["label"].apply(lambda x: BANKING77_INTENTS[x])
        return df[["text", "intent"]]

    print("Sampling and mapping labels...")
    train_df = process_split("train", args.train_size)
    test_df = process_split("test", args.test_size)
    
    os.makedirs(args.output_dir, exist_ok=True)
    
    train_path = os.path.join(args.output_dir, "train.csv")
    test_path = os.path.join(args.output_dir, "test.csv")
    
    train_df.to_csv(train_path, index=False)
    test_df.to_csv(test_path, index=False)
    
    print(f"Successfully processed data!")
    print(f"- Training set: {len(train_df)} samples -> {train_path}")
    print(f"- Test set: {len(test_df)} samples -> {test_path}")
    print("\nPre-processing completed successfully.")

if __name__ == "__main__":
    main()
