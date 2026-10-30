# Nakuru Co-op Regional Summary Generator

A streamlined pandas automation utility that cross-references daily delivery data matrices against dynamic payout rate parameters to build localized monthly performance reports.

## 📥 Required Input Files

The data engine safely imports and references two localized CSV templates stored within a `data/` subdirectory structure:

1. **`data/daily_milk_collection.csv`**
   * Tracks rolling volume receipts across individual drops.
   * *Expected Fields:* `farmer_name`, `date`, `litres`

2. **`data/farmer_details.csv`**
   * Contains localized structural categorization frameworks and specific currency conversions.
   * *Expected Fields:* `farmer_name`, `zone`, `payment_rate`

## 🚀 Execution Guide

1. Make sure your local Python environment has the `pandas` analytical package installed:
   ```bash
   pip install pandas
   ```
2. Place the processor file into your active directory alongside your files, and execute:
   ```bash
   python zone_processor.py
   ```

## 📊 Sample Visual Report Layout
```text
==============================================================================
 NAKURU DAIRY CO-OPERATIVE - MONTHLY ZONE PERFORMANCE REPORT
==============================================================================
  Zone  Total Litres This Month  Total Payout (KES)       Top Farmer (Volume)
Bahati                   2335.5          120,440.00      James Mwangi (890.0L)
  Molo                   2081.0          118,542.00     Faith Kiprop (640.0L)
 Njoro                   1961.0          104,742.50     Mary Wangari (620.0L)
==============================================================================
```
