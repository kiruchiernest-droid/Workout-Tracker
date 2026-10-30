import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

OUTPUT_CHART = "data/loan_amount_distribution.png"


def run_triple_s_analysis():
    """Generates 150 loan records, flags IQR outliers, computes correlation,

    and saves an executive dashboard histogram chart.
    """
    os.makedirs("data", exist_ok=True)

    # 1. Generate 150 Fictional Microfinance Loan Records
    np.random.seed(101)
    loan_ids = [f"MBSA-{i:03d}" for i in range(1, 151)]

    # Mix standard community micro-loans with a few large commercial accounts
    amount_kes = np.random.lognormal(mean=10.8, sigma=0.5, size=150) * 2.5
    amount_kes = np.round(amount_kes, -2)  # Clean rounding to nearest hundred

    # Generate timeline metrics for days to first repayment
    days_to_repayment = np.random.randint(14, 45, size=150)

    # Ensure slight realistic inverse correlation structure for testing
    days_to_repayment = np.clip(
        days_to_repayment - (amount_kes / 12000).astype(int), 7, 60
    )

    df = pd.DataFrame(
        {
            "loan_id": loan_ids,
            "amount_kes": amount_kes,
            "days_to_first_repayment": days_to_repayment,
            "county": ["Mombasa"] * 150,
        }
    )

    # 2. Run Comprehensive Statistical Profile
    stats = df["amount_kes"].describe()

    print("\n" + "=" * 50)
    print("      TRIPLE S MICROFINANCE - STATISTICAL PROFILE")
    print("=" * 50)
    print(f"Typical Loan Amount (Mean)   : KES {stats['mean']:,.2f}")
    print(f"Typical Loan Amount (Median) : KES {stats['50%']:,.2f}")
    print(f"Standard Deviation           : KES {stats['std']:,.2f}")
    print(f"25th Percentile (Q1)         : KES {stats['25%']:,.2f}")
    print(f"75th Percentile (Q3)         : KES {stats['75%']:,.2f}")
    print("-" * 50)

    # 3. Structural Outlier Detection via Interquartile Range (IQR) Method
    q1 = stats["25%"]
    q3 = stats["75%"]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outliers = df[
        (df["amount_kes"] < lower_bound) | (df["amount_kes"] > upper_bound)
    ]
    outlier_ids = outliers["loan_id"].tolist()

    print(f"Detected Outliers (Total: {len(outlier_ids)})")
    print(f"Flagged Loan IDs: {outlier_ids if outlier_ids else 'None'}")
    print("-" * 50)

    # 4. Correlation Calculation & Narrative Assessment
    correlation = df["amount_kes"].corr(df["days_to_first_repayment"])
    print(f"Statistical Correlation Coefficient: {correlation:.4f}")

    # Plain sentence interpretation translation for Board Members
    if abs(correlation) < 0.1:
        narrative = "There is no meaningful relationship between the size of a loan and how quickly the first payment is made."
    elif correlation < 0:
        narrative = "Larger loans marginally tend to see their first payment arrive slightly sooner than smaller loans."
    else:
        narrative = "Larger loans tend to take a longer time to receive their initial repayment compared to smaller accounts."

    print(f"\nBoard Summary Statement:\n\"{narrative}\"")
    print("=" * 50 + "\n")

    # 5. Build Executive Distribution Chart
    plt.figure(figsize=(10, 6))
    plt.hist(
        df["amount_kes"],
        bins=20,
        color="#2ecc71",
        edgecolor="#27ae60",
        alpha=0.8,
    )

    plt.title(
        "Mombasa Portfolio Distribution: Breakdown of Disbursed Loan Values",
        fontsize=13,
        fontweight="bold",
        pad=15,
    )
    plt.xlabel("Disbursed Loan Volume (KES)", fontsize=11)
    plt.ylabel("Number of Open Accounts", fontsize=11)
    plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    plt.grid(axis="y", linestyle="--", alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUTPUT_CHART, dpi=300)
    plt.close()


if __name__ == "__main__":
    run_triple_s_analysis()
