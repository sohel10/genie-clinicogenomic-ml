import pandas as pd
from pathlib import Path

RAW_DATA = Path("data/raw/TCGA_LUAD_clinical_genomic.xlsx")
OUTPUT_DATA = Path("data/processed/clinical_genomic_clean.csv")

def main():
    df = pd.read_excel(RAW_DATA)

    # Basic sanity checks
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    # Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("/", "_")
    )

    # Encode survival outcome
    df["event"] = df["survival"].map({
        "DECEASED": 1,
        "LIVING": 0
    })

    # Save clean file
    OUTPUT_DATA.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_DATA, index=False)

    print("Saved:", OUTPUT_DATA)

if __name__ == "__main__":
    main()
