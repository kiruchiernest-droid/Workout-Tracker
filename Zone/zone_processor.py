import os
import pandas as pd

# Define data structures directly for easy replication/mocking
COLLECTIONS_FILE = "data/daily_milk_collection.csv"
FARMERS_FILE = "data/farmer_details.csv"


def generate_mock_data():
    """Generates the local mock CSV data files for testing if they do not exist."""
    os.makedirs("data", exist_ok=True)

    # 12 Realistic Farmers across 3 distinct Nakuru Zones
    farmers_data = {
        "farmer_name": [
            "John Kamau",
            "Mary Wangari",
            "David Koech",
            "Grace Cherono",
            "Peter Njoroge",
            "Alice Chebet",
            "James Mwangi",
            "Esther Wanjiku",
            "Samuel Rotich",
            "Faith Kiprop",
            "Paul Otieno",
            "Mercy Atieno",
        ],
        "zone": [
            "Njoro",
            "Njoro",
            "Njoro",
            "Njoro",
            "Bahati",
            "Bahati",
            "Bahati",
            "Bahati",
            "Molo",
            "Molo",
            "Molo",
            "Molo",
        ],
        "payment_rate": [
            52.0,
            52.0,
            55.0,
            55.0,
            50.0,
            50.0,
            53.0,
            53.0,
            58.0,
            58.0,
            56.0,
            56.0,
        ],
    }

    # Cumulative monthly totals representing daily collection entries
    collections_data = {
        "farmer_name": [
            "John Kamau",
            "Mary Wangari",
            "David Koech",
            "Grace Cherono",
            "Peter Njoroge",
            "Alice Chebet",
            "James Mwangi",
            "Esther Wanjiku",
            "Samuel Rotich",
            "Faith Kiprop",
            "Paul Otieno",
            "Mercy Atieno",
        ],
        "date": ["2026-10-30"] * 12,
        "litres": [
            450.5,
            620.0,
            310.0,
            580.5,
            710.0,
            420.5,
            890.0,
            315.0,
            510.5,
            640.0,
            430.0,
            500.5,
        ],
    }

    pd.DataFrame(farmers_data).to_csv(FARMERS_FILE, index=False)
    pd.DataFrame(collections_data).to_csv(COLLECTIONS_FILE, index=False)


def process_zone_summary():
    """Merges collection profiles, computes payouts, aggregates by zone,

    and extracts the top performing producer per sector.
    """
    if not os.path.exists(COLLECTIONS_FILE) or not os.path.exists(FARMERS_FILE):
        generate_mock_data()

    # Load Source Datasets
    df_collections = pd.read_csv(COLLECTIONS_FILE)
    df_farmers = pd.read_csv(FARMERS_FILE)

    # 1. Merge datasets securely on common structural identity keys
    df_merged = pd.merge(df_collections, df_farmers, on="farmer_name")

    # 2. Derive individual farmer dynamic transactional revenue payout lines
    df_merged["total_payout"] = df_merged["litres"] * df_merged["payment_rate"]

    # 3. Compute structural groupings at Zone levels
    zone_groups = df_merged.groupby("zone")
    zone_summary = zone_groups.agg(
        total_litres=("litres", "sum"), total_payout=("total_payout", "sum")
    ).reset_index()

    # 4. Extract Top performing producer per operational grid node
    # Sort descending by litres, group by zone, and grab the first row
    top_farmers = (
        df_merged.sort_values(by="litres", ascending=False)
        .groupby("zone")
        .first()
        .reset_index()
    )
    top_farmers["top_farmer"] = (
        top_farmers["farmer_name"]
        + " ("
        + top_farmers["litres"].astype(str)
        + "L)"
    )

    # 5. Compile into final delivery summary table frame matrix layout
    final_summary = pd.merge(
        zone_summary, top_farmers[["zone", "top_farmer"]], on="zone"
    )

    # Clean Up Formatting layouts for pristine screenshots
    final_summary.columns = [
        "Zone",
        "Total Litres This Month",
        "Total Payout (KES)",
        "Top Farmer (Volume)",
    ]

    print("\n" + "=" * 78)
    print(" NAKURU DAIRY CO-OPERATIVE - MONTHLY ZONE PERFORMANCE REPORT")
    print("=" * 78)
    print(
        final_summary.to_string(
            index=False, formatters={"Total Payout (KES)": "{:,.2f}".format}
        )
    )
    print("=" * 78 + "\n")


if __name__ == "__main__":
    process_zone_summary()
