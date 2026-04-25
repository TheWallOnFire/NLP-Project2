import pandas as pd
import argparse
from tqdm import tqdm
from scripts.inference import IntentClassification
from sklearn.metrics import accuracy_score, classification_report

def evaluate():
    parser = argparse.ArgumentParser(description="Evaluate the fine-tuned model on the test set")
    parser.add_argument("--config", type=str, default="configs/inference.yaml", help="Path to inference config")
    parser.add_argument("--test_data", type=str, default="sample_data/test.csv", help="Path to test CSV file")
    args = parser.parse_args()

    print(f"Loading test data from {args.test_data}...")
    test_df = pd.read_csv(args.test_data)
    
    print("Initializing classifier...")
    classifier = IntentClassification(args.config)
    
    print(f"Running inference on {len(test_df)} samples...")
    predictions = []
    ground_truth = test_df["intent"].tolist()
    
    for text in tqdm(test_df["text"].tolist()):
        pred = classifier(text)
        predictions.append(pred)
        
    # Calculate accuracy
    accuracy = accuracy_score(ground_truth, predictions)
    
    print("\n" + "="*30)
    print(f"FINAL TEST ACCURACY: {accuracy:.4f}")
    print("="*30)
    
    # Optional: Detailed report
    print("\nClassification Report (Top 10 classes):")
    # We only show top 10 to keep the output readable
    report = classification_report(ground_truth, predictions, output_dict=True)
    sorted_classes = sorted(report.items(), key=lambda x: x[1]['support'] if isinstance(x[1], dict) and 'support' in x[1] else 0, reverse=True)
    
    for i, (label, metrics) in enumerate(sorted_classes):
        if i > 10: break
        if label in ['accuracy', 'macro avg', 'weighted avg']: continue
        print(f"- {label}: Precision: {metrics['precision']:.2f}, Recall: {metrics['recall']:.2f}, F1: {metrics['f1-score']:.2f}")

if __name__ == "__main__":
    evaluate()
