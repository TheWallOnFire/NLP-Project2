# NLP-Project2

This project is a template for NLP model training and inference.

## 1. Setup Environment

It is recommended to use a virtual environment to manage dependencies.

### Using `venv`
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 2. Download Data

Place your training and testing data in the `sample_data/` directory. 
- `train.csv`: Training dataset.
- `test.csv`: Testing/Validation dataset.

If you have external links to download datasets, update this section with the relevant `wget` or `curl` commands.

## 3. Preprocess Data

To preprocess your data before training, you can use the `scripts/preprocess_data.py` script:

```bash
python scripts/preprocess_data.py --input sample_data/train.csv --output sample_data/train_processed.csv
```

## 4. Train the Model

You can train the model using the provided shell script or by running the training script directly.

### Using Shell Script
```bash
bash train.sh
```

### Direct Command
```bash
python scripts/train.py --config configs/train.yaml
```

Configuration for training can be modified in `configs/train.yaml`.

## 5. Run Inference

To run inference on the test data:

### Using Shell Script
```bash
bash inference.sh
```

### Direct Command
```bash
python scripts/inference.py --config configs/inference.yaml
```

Inference settings can be adjusted in `configs/inference.yaml`.

## Project Structure
```
|-- scripts/
|   |-- train.py          # Training logic
|   |-- inference.py      # Inference/Prediction logic
|   |-- preprocess_data.py # Data cleaning and preparation
|
|-- configs/
|   |-- train.yaml        # Training hyperparameters and paths
|   |-- inference.yaml    # Inference settings
|
|-- sample_data/
|   |-- train.csv         # Sample training data
|   |-- test.csv          # Sample test data
|
|-- train.sh              # Bash script to trigger training
|-- inference.sh          # Bash script to trigger inference
|-- requirements.txt      # List of dependencies
|-- README.md             # Project documentation
```
