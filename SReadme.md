# Non-Technical Sales Dashboard Pipeline

Automated backend pipeline to process raw Excel sheets and instantly update your visual sales dashboard.

## 🚀 Quick Setup

1. **Install Requirements:** Ensure Python 3.8+ is installed on your computer. Run the following command in your terminal:
   ```bash
   pip install pandas openpyxl
   ```

2. **Prepare Your Data:** 
   Place your weekly Excel sheet inside the `data/` folder and name it exactly `raw_sales.xlsx`. Ensure your sheet contains the core columns: `Date`, `Sales`, and `Product`.

3. **Run the Update:** 
   Double-click `run_pipeline.bat` (Windows) or execute the script in your terminal:
   ```bash
   python app.py
   ```
   The interactive visual dashboard dashboard will refresh automatically with your latest numbers.
