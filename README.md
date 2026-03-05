# PC Components Price Dashboard — Bangladesh


> A data analytics project that scrapes, cleans, and visualizes PC component pricing data from [Techland BD](https://www.techlandbd.com) using **Selenium** and **Tableau**.

---

##  Problem Statement

PC component prices in Bangladesh vary wildly across brands and categories, and it's hard to know which components offer the best deals or which brands dominate the market. I wanted to build a data pipeline that scrapes live product data and answers questions like:

-  Which brands offer the highest discount ratios?
-  Is the processor market a monopoly?
-  How does price relate to discount amount across components?

---

## Findings and Observations from the Dashboard (https://public.tableau.com/shared/8QZ7JT6ND?:display_count=n&:origin=viz_share_link)

1. The processor market is effectively a duopoly — only 2 brands (Intel & AMD) dominate, compared to 89 brands in the SSD market.
2. **Graphics Cards** have the highest average price (~৳93,000) and also the highest average discount (~৳7,800).
3. **SSDs** have the most product variety with 789 products and 89 distinct brands.
4. Higher priced products do not always get bigger discounts — most discounts are concentrated in the lower price range.
5. Motherboards have the second highest product count but low brand variety, suggesting a few brands dominate that market too.

---

## Dashboards

### Dashboard 1 — Market Overview
| Chart | Type |
|---|---|
| Product Distribution by Component | Bar Chart |
| Average Price by Component | Bar Chart |
| Brand Availability by Component | Packed Bubble Chart |
| Discount Comparison Across Components | Bar Chart |

### Dashboard 2 — Price & Discount Analysis
| Chart | Type |
|---|---|
| Price vs Discount Analysis by Component | Scatter Plot |
| Brands with Highest Discount Ratio | Horizontal Bar Chart |
| Brand-wise Average Product Price | Bar Chart |

---


## Build From Sources

### 1. Clone the repo
```bash
git clone https://github.com/Yeash1213/PC-Components-Price-Dashboard.git
```

### 2. Intialize and activate virtual environment
```bash
python -m venv .venv
source ./.venv/bin/activate

```

### 3. Run the scrapers
```bash
ram_scraping.py
gpu_scraping.py
ssd_scraping.py
motherboard_scraping.py
processor_scraping.py
```
> Each scraper saves a CSV file — e.g. `ram_details2.csv`, `gpu_details2.csv`, etc.

### 4. Clean the data
Open and run `clean_data.ipynb` in Jupyter Notebook.

This produces `pc_products.csv` with:
- All 5 component CSV files merged into one
- Rows with null values in Current Price and Old Price columns are removed
- Price columns converted to proper numeric format
- Rows with misinterpreted values cleaned out

### 5. Build the dashboard using the prepared data.



## Tech Stack

| Tool | Purpose |
|---|---|
| `Python` | Core programming language |
| `Selenium` | Web scraping |
| `pandas` | Data cleaning and processing |
| `Tableau Public` | Data visualization and dashboard |
| `Jupyter Notebook` | Data cleaning workflow |

---

## Requirements

```
selenium
pandas
```

Install all dependencies:
```bash
pip install -r requirements.txt
```

---
