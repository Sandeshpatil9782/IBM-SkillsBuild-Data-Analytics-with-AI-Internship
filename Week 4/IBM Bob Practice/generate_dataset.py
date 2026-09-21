import csv
import random
from datetime import date, timedelta

random.seed(42)

# ── Reference data ────────────────────────────────────────────────────────────
CITIES = [
    "Mumbai", "Delhi", "Bangalore", "Chennai", "Hyderabad",
    "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Surat"
]

FIRST_NAMES = [
    "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Reyansh",
    "Ayaan", "Krishna", "Ishaan", "Ananya", "Aadhya", "Diya", "Pihu",
    "Saanvi", "Priya", "Riya", "Kavya", "Pooja", "Neha", "Rahul",
    "Rohit", "Amit", "Suresh", "Vikram", "Sneha", "Meera", "Anjali",
    "Kiran", "Deepak", "Rajesh", "Sunita", "Geeta", "Lakshmi", "Nisha"
]

LAST_NAMES = [
    "Sharma", "Verma", "Singh", "Patel", "Kumar", "Gupta", "Joshi",
    "Rao", "Nair", "Mehta", "Shah", "Yadav", "Mishra", "Tiwari",
    "Chaudhary", "Pandey", "Srivastava", "Agarwal", "Bose", "Reddy"
]

GENDER_FIRST = {
    "Male":   ["Aarav","Vivaan","Aditya","Vihaan","Arjun","Sai","Reyansh",
               "Ayaan","Krishna","Ishaan","Rahul","Rohit","Amit","Suresh",
               "Vikram","Deepak","Rajesh"],
    "Female": ["Ananya","Aadhya","Diya","Pihu","Saanvi","Priya","Riya",
               "Kavya","Pooja","Neha","Sneha","Meera","Anjali","Kiran",
               "Sunita","Geeta","Lakshmi","Nisha"]
}

CATEGORIES = {
    "Electronics":    [("Smartphone", 18000, 45000),
                       ("Laptop",     45000, 95000),
                       ("Tablet",     15000, 40000),
                       ("Earphones",   1500,  5000),
                       ("Smartwatch",  5000, 20000)],
    "Clothing":       [("Men's T-Shirt",  400,  1200),
                       ("Women's Kurti",  600,  2000),
                       ("Jeans",          800,  2500),
                       ("Saree",         1200,  6000),
                       ("Jacket",        1500,  5000)],
    "Groceries":      [("Rice (5 kg)",    250,   500),
                       ("Cooking Oil",    200,   450),
                       ("Flour (10 kg)",  350,   600),
                       ("Sugar (5 kg)",   150,   280),
                       ("Pulses (1 kg)",   80,   180)],
    "Home & Kitchen": [("Pressure Cooker", 800,  2500),
                       ("Mixer Grinder",  1500,  4000),
                       ("Bedsheet Set",    600,  2000),
                       ("Curtains",        400,  1500),
                       ("Water Bottle",    150,   600)],
    "Sports":         [("Cricket Bat",   1200,  4000),
                       ("Football",       500,  1800),
                       ("Yoga Mat",       400,  1200),
                       ("Dumbbells",      800,  3000),
                       ("Badminton Set",  600,  2000)],
    "Beauty":         [("Face Cream",     150,   800),
                       ("Shampoo",        200,   700),
                       ("Perfume",        500,  3000),
                       ("Lipstick",       200,  1000),
                       ("Sunscreen",      250,   900)],
    "Books":          [("Fiction Novel",  200,   600),
                       ("Self-Help Book", 250,   700),
                       ("Textbook",       400,  1200),
                       ("Children Book",  150,   400),
                       ("Comic Book",     100,   350)],
    "Toys":           [("Board Game",     600,  2000),
                       ("Action Figure",  300,  1200),
                       ("Puzzle Set",     400,  1500),
                       ("Remote Car",     800,  3000),
                       ("Doll",           350,  1200)],
}

PAYMENT_METHODS = ["Credit Card", "Debit Card", "UPI", "Cash", "Net Banking", "Wallet"]

# ── Date range: 2024-01-01 to 2024-12-31 ─────────────────────────────────────
START_DATE = date(2024, 1, 1)
END_DATE   = date(2024, 12, 31)
DATE_RANGE = (END_DATE - START_DATE).days

# ── Build rows ────────────────────────────────────────────────────────────────
rows = []
used_txn_ids = set()
used_cust_ids = set()

# Pre-generate 500 unique transaction IDs
txn_id_pool = random.sample(range(10001, 20000), 500)

# Pre-generate a pool of customer IDs (repeat customers allowed)
cust_id_pool = [f"CUST{random.randint(1001, 1200):04d}" for _ in range(500)]

for i in range(500):
    txn_id   = f"TXN{txn_id_pool[i]}"
    txn_date = START_DATE + timedelta(days=random.randint(0, DATE_RANGE))
    cust_id  = cust_id_pool[i]

    gender     = random.choice(["Male", "Female"])
    first_name = random.choice(GENDER_FIRST[gender])
    last_name  = random.choice(LAST_NAMES)
    cust_name  = f"{first_name} {last_name}"
    age        = random.randint(18, 65)
    city       = random.choice(CITIES)

    category   = random.choice(list(CATEGORIES.keys()))
    prod_name, price_lo, price_hi = random.choice(CATEGORIES[category])
    quantity   = random.randint(1, 10)
    unit_price = round(random.uniform(price_lo, price_hi), 2)
    discount_pct = round(random.uniform(0, 30), 2)
    payment    = random.choice(PAYMENT_METHODS)

    gross_sales    = round(quantity * unit_price, 2)
    discount_amt   = round(gross_sales * discount_pct / 100, 2)
    net_sales      = round(gross_sales - discount_amt, 2)

    rows.append([
        txn_id, txn_date.strftime("%Y-%m-%d"), cust_id, cust_name,
        gender, age, city, category, prod_name, quantity, unit_price,
        discount_pct, payment, gross_sales, discount_amt, net_sales
    ])

# ── Write CSV ─────────────────────────────────────────────────────────────────
HEADER = [
    "Transaction_ID", "Transaction_Date", "Customer_ID", "Customer_Name",
    "Gender", "Age", "City", "Product_Category", "Product",
    "Quantity", "Unit_Price", "Discount_Percentage", "Payment_Method",
    "Gross_Sales", "Discount_Amount", "Net_Sales"
]

with open("data/raw/sales_500.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(HEADER)
    writer.writerows(rows)

print(f"Dataset written: {len(rows)} rows, {len(HEADER)} columns")
