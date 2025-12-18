import csv
import random

# Original sample data
data = [
    ['product_title', 'price_usd', 'seller_name', 'seller_location', 'stock_level', 'image_url', 'review_score', 'shipping_origin', 'sales_rank', 'grey_risk_flag'],
    ['iPhone 15 Pro Max 256GB', '899', 'TechHubStore', 'USA', 'Low (5 left)', 'https://ex.com/img1.jpg', '4.2', 'China', '1200', 'High'],
    ['Sony WH-1000XM5', '250', 'GlobalDeals', 'India', 'High', 'https://ex.com/img2.jpg', '3.8', 'UAE', '450', 'Medium'],
    ['Rolex Submariner', '7500', 'LuxuryHub', 'Turkey', 'Out of Stock', 'https://ex.com/img3.jpg', '1.5', 'Turkey', '89', 'High'],
]

# Add simulated government aggregate rows (from Census E-STATS/DataWeb style)
gov_data = [
    ['US E-comm Q2 2025 Total', '304200000000', 'US Census Bureau', 'USA', 'N/A', 'N/A', 'N/A', 'Domestic+Import', '1', 'Low'],
    ['Retail Total Q2 2025', '1865400000000', 'US Census Bureau', 'USA', 'N/A', 'N/A', 'N/A', 'USA', '1', 'Low'],
    ['Electronics Imports 2025', '15000000000', 'USITC DataWeb', 'Global', 'High', 'N/A', 'N/A', 'China+Others', '50', 'Medium'],
]

data.extend(gov_data)

# Generate 500+ synthetic rows for scale (ethics-compliant)
for i in range(500):
    data.append([
        f'Electronics Product {i+1}',
        f'{random.randint(50, 5000)}',
        f'GovVerifiedSeller{i}',
        random.choice(['USA', 'EU', 'Asia']),
        random.choice(['High', 'Low', 'Out of Stock']),
        'https://ex.com/img.jpg',
        f'{random.uniform(1.0, 5.0):.1f}',
        random.choice(['USA', 'China', 'India']),
        str(random.randint(10, 10000)),
        random.choice(['Low', 'Medium', 'High'])
    ])

# Write CSV
with open('grey_market_data_enhanced.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)

print(f"Enhanced CSV saved! Total rows: {len(data)} (incl. {len(gov_data)} gov aggregates)")


