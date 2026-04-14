import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, "artifacts", "segment_mapping.json")) as f:
    segment_map = json.load(f)
with open(os.path.join(BASE_DIR, "artifacts", "loyalty_mapping.json")) as f:
    loyalty_map = json.load(f)

def preprocess(data: dict):
    df = pd.DataFrame([data])

    # Dates
    df['created_date'] = pd.to_datetime(df['created_date'])
    df['last_active_date'] = pd.to_datetime(df['last_active_date'])
    today = pd.Timestamp.today()

    # Age
    df['customer_age'] = df['age']

    # Recency
    df['recency'] = (today - df['last_active_date']).dt.days

    # Financial features
    df['balance_per_tenure'] = df['balance'] / (df['tenure_ye'] + 1)
    df['credit_intensity_proxy'] = df['credit_sco'] / (df['balance'] + 1)
    df['interest_burden_proxy'] = df['monthly_ir'] * df['nums_card']

    # Behavioral features
    df['total_products'] = df['nums_card'] + df['nums_service']
    df['engagement_per_product'] = df['engagement_score'] / (df['total_products'] + 1)

    # Activity flags
    df['is_dormant'] = (df['recency'] > 90).astype(int)
    df['is_low_activity'] = (df['engagement_score'] < 50).astype(int)

    # Gender encoding
    df['gender_male'] = (df['gender'] == 'Male').astype(int)

    # Digital behavior encoding
    df['digital_behavior_offline'] = (df['digital_behavior'] == 'Offline').astype(int)

    # Occupation encoding - must match training exactly
    occupations = [
        "Business_Salesperson",
        "Engineer_IT Specialist",
        "General Laborer",
        "Housewife_Student",
        "Manager_Leader",
        "Office Worker_Civil Servant",
        "Retired",
        "Small Business Owner",
        "Teacher_Lecturer"
    ]
    for occ in occupations:
        df[f'occupation_{occ}'] = (df['occupation'] == occ).astype(int)

    # Target encoding
    df['customer_segment_target_encoded'] = df['customer_segment'].map(segment_map).fillna(0)
    df['loyalty_level_target_encoded'] = df['loyalty_level'].map(loyalty_map).fillna(0)

    # Final feature list - exact order from training
    final_features = [
        'monthly_ir',
        'married',
        'active_member',
        'last_transaction_month',
        'customer_age',
        'recency',
        'balance_per_tenure',
        'credit_intensity_proxy',
        'interest_burden_proxy',
        'total_products',
        'engagement_per_product',
        'is_dormant',
        'is_low_activity',
        'customer_segment_target_encoded',
        'loyalty_level_target_encoded',
        'gender_male',
        'occupation_Business_Salesperson',
        'occupation_Engineer_IT Specialist',
        'occupation_General Laborer',
        'occupation_Housewife_Student',
        'occupation_Manager_Leader',
        'occupation_Office Worker_Civil Servant',
        'occupation_Retired',
        'occupation_Small Business Owner',
        'occupation_Teacher_Lecturer',
        'digital_behavior_offline'
    ]

    return df[final_features]