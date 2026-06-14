"""
Mock Data Generator for Fraud Detection System
Using Faker and Random for realistic transaction data
"""
import random
from datetime import datetime, timedelta
from faker import Faker
import pandas as pd
import numpy as np

# Initialize Faker
fake = Faker('en_IN')  # Indian locale

# Configuration
NUM_USERS = 1000
NUM_MERCHANTS = 100
NUM_TRANSACTIONS = 10000
FRAUD_RATE = 0.08  # 8% fraud rate

# Transaction types
TRANSACTION_TYPES = ['online_purchase', 'atm Withdrawal', 'bill_payment', 'money_transfer', 'merchant_payment']
PAYMENT_METHODS = ['UPI', 'Credit Card', 'Debit Card', 'Net Banking', 'Wallet']
CHANNELS = ['mobile_app', 'web', 'pos', 'atm']
DEVICE_TYPES = ['mobile', 'desktop', 'tablet']
CITIES = ['Lucknow', 'Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata', ' Hyderabad']
CATEGORIES = ['E-commerce', 'Retail', 'Food', 'Travel', 'Entertainment', 'Healthcare']

def generate_users(num_users=NUM_USERS):
    """Generate mock user data"""
    users = []
    
    for i in range(num_users):
        user = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'age': random.randint(18, 70),
            'account_creation_date': fake.date_between(start_date='-5y', end_date='-1d'),
            'phone_number': fake.phone_number(),
            'address': fake.address(),
            'city': random.choice(CITIES),
            'country': 'India',
            'risk_profile': random.choice(['low', 'low', 'low', 'medium', 'high']),
            'is_active': random.choice([True, True, True, False])
        }
        users.append(user)
    
    return users

def generate_merchants(num_merchants=NUM_MERCHANTS):
    """Generate mock merchant data"""
    merchants = []
    
    for i in range(num_merchants):
        merchant = {
            'merchant_name': f"{fake.company()} Store",
            'merchant_category': random.choice(CATEGORIES),
            'country': 'India',
            'risk_rating': random.choice(['low', 'low', 'medium', 'high']),
            'contact_email': fake.email()
        }
        merchants.append(merchant)
    
    return merchants

def generate_transactions(num_users=NUM_USERS, num_merchants=NUM_MERCHANTS, num_transactions=NUM_TRANSACTIONS):
    """Generate mock transaction data with fraud labels"""
    transactions = []
    fraud_labels = []
    
    # Generate user IDs and merchant IDs
    user_ids = list(range(1, num_users + 1))
    merchant_ids = list(range(1, num_merchants + 1))
    
    # Base transaction amount distribution
    base_amounts = np.random.normal(5000, 2000, num_transactions)
    
    for i in range(num_transactions):
        user_id = random.choice(user_ids)
        merchant_id = random.choice(merchant_ids)
        
        # Generate timestamp (last 1 year)
        timestamp = fake.date_time_between(start_date='-1y', end_date='now')
        
        # Generate amount (some fraud transactions have unusually high amounts)
        is_fraud = random.random() < FRAUD_RATE
        if is_fraud:
            amount = max(100, base_amounts[i] * random.uniform(2, 10))  # Fraud: 2-10x higher
            fraud_type = random.choice(['unauthorized', 'stolen_card', 'identity_theft', 'account_takeover'])
        else:
            amount = max(10, base_amounts[i])
            fraud_type = None
        
        # Generate device and location
        if is_fraud and random.random() < 0.7:
            # Fraud: often different location
            city = random.choice(CITIES)
            device_type = random.choice(DEVICE_TYPES)
        else:
            # Normal: user's regular location
            city = random.choice(CITIES)
            device_type = random.choice(DEVICE_TYPES)
        
        transaction = {
            'user_id': user_id,
            'merchant_id': merchant_id,
            'amount': round(amount, 2),
            'currency': 'INR',
            'transaction_type': random.choice(TRANSACTION_TYPES),
            'transaction_timestamp': timestamp,
            'device_id': f"DEV{random.randint(1000, 9999)}",
            'device_type': device_type,
            'ip_address': fake.ipv4(),
            'location_latitude': random.uniform(20.0, 30.0),
            'location_longitude': random.uniform(70.0, 80.0),
            'city': city,
            'country': 'India',
            'channel': random.choice(CHANNELS),
            'payment_method': random.choice(PAYMENT_METHODS),
            'status': random.choice(['completed', 'completed', 'completed', 'pending'])
        }
        transactions.append(transaction)
        
        # Fraud label
        fraud_label = {
            'transaction_id': i + 1,
            'is_fraud': is_fraud,
            'fraud_type': fraud_type,
            'fraud_score': round(random.uniform(0.8, 1.0), 4) if is_fraud else round(random.uniform(0.0, 0.3), 4),
            'investigation_status': random.choice(['pending', 'investigated', 'closed']),
            'notes': f"Transaction flagged for review" if is_fraud else None
        }
        fraud_labels.append(fraud_label)
    
    return transactions, fraud_labels

def generate_user_behavior_profiles(transactions):
    """Generate aggregated user behavior profiles from transactions"""
    df = pd.DataFrame(transactions)
    
    profiles = []
    for user_id in df['user_id'].unique():
        user_tx = df[df['user_id'] == user_id]
        
        profile = {
            'user_id': user_id,
            'avg_transaction_amount': user_tx['amount'].mean(),
            'median_transaction_amount': user_tx['amount'].median(),
            'total_transactions': len(user_tx),
            'total_amount_spent': user_tx['amount'].sum(),
            'avg_transactions_per_day': len(user_tx) / 365,
            'max_transaction_amount': user_tx['amount'].max(),
            'min_transaction_amount': user_tx['amount'].min(),
            'std_transaction_amount': user_tx['amount'].std(),
            'unique_merchants': len(user_tx['merchant_id'].unique()),
            'unique_devices': len(user_tx['device_id'].unique()),
            'unique_locations': len(user_tx['city'].unique()),
            'last_transaction_date': user_tx['transaction_timestamp'].max(),
            'days_since_last_transaction': (datetime.now() - user_tx['transaction_timestamp'].max()).days
        }
        profiles.append(profile)
    
    return profiles

def save_to_csv(users, merchants, transactions, fraud_labels, profiles):
    """Save all data to CSV files"""
    pd.DataFrame(users).to_csv('users.csv', index=False)
    pd.DataFrame(merchants).to_csv('merchants.csv', index=False)
    pd.DataFrame(transactions).to_csv('transactions.csv', index=False)
    pd.DataFrame(fraud_labels).to_csv('fraud_labels.csv', index=False)
    pd.DataFrame(profiles).to_csv('user_behavior_profiles.csv', index=False)
    
    print("✓ Data saved to CSV files:")
    print("  - users.csv")
    print("  - merchants.csv")
    print("  - transactions.csv")
    print("  - fraud_labels.csv")
    print("  - user_behavior_profiles.csv")

def main():
    """Main function to generate all mock data"""
    print("🚀 Generating Mock Data for Fraud Detection System...")
    print(f"  Users: {NUM_USERS}")
    print(f"  Merchants: {NUM_MERCHANTS}")
    print(f"  Transactions: {NUM_TRANSACTIONS}")
    print(f"  Fraud Rate: {FRAUD_RATE*100}%")
    print()
    
    # Generate data
    users = generate_users()
    print(f"✓ Generated {len(users)} users")
    
    merchants = generate_merchants()
    print(f"✓ Generated {len(merchants)} merchants")
    
    transactions, fraud_labels = generate_transactions()
    print(f"✓ Generated {len(transactions)} transactions")
    print(f"  Fraud transactions: {sum(1 for f in fraud_labels if f['is_fraud'])}")
    
    profiles = generate_user_behavior_profiles(transactions)
    print(f"✓ Generated {len(profiles)} user behavior profiles")
    
    # Save to CSV
    save_to_csv(users, merchants, transactions, fraud_labels, profiles)
    
    print()
    print("✓ Mock data generation complete!")

if __name__ == "__main__":
    main()
