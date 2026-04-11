import pandas as pd
import json

# Load mappings
with open("artifacts/segment_mapping.json") as f:
    segment_map = json.load(f)

with open("artifacts/loyalty_mapping.json") as f:
    loyalty_map = json.load(f)

with open("artifacts/woe_mappings.json") as f:
    woe_map = json.load(f)


def preprocess(data: dict):
    df = pd.DataFrame([data])

    # Dates
    df['created_date'] = pd.to_datetime(df['created_date'])
    df['last_active_date'] = pd.to_datetime(df['last_active_date'])
    today = pd.Timestamp.today()

    df['customer_age'] = df['age']
    df['recency'] = (today - df['last_active_date']).dt.days

    # Financial
    df['balance_per_tenure'] = df['balance'] / (df['tenure_ye'] + 1)
    df['credit_intensity_proxy'] = df['credit_sco'] / (df['balance'] + 1)
    df['interest_burden_proxy'] = df['monthly_ir'] * df['nums_card']

    # Behavioral
    df['total_products'] = df['nums_card'] + df['nums_service']
    df['engagement_per_product'] = df['engagement_score'] / (df['total_products'] + 1)

    # Activity
    df['is_dormant'] = (df['recency'] > 90).astype(int)
    df['is_low_activity'] = (df['engagement_score'] < 50).astype(int)

    # Encoding
    df['gender_male'] = (df['gender'] == 'Male').astype(int)
    df['digital_behavior_offline'] = (df['digital_behavior'] == 'Offline').astype(int)

    # Occupation encoding
    occupations = [
        "business_salesperson", "engineer_it_specialist", "general_laborer",
        "housewife_student", "manager_leader",
        "office_worker_civil_servant", "retired",
        "small_business_owner", "teacher_lecturer"
    ]

    for occ in occupations:
        df[f'occupation_{occ}'] = (df['occupation'].str.lower().str.replace("/", "_").str.replace(" ", "_") == occ).astype(int)

    # Target encoding
    df['customer_segment_target_encoded'] = df['customer_segment'].map(segment_map).fillna(0)
    df['loyalty_level_target_encoded'] = df['loyalty_level'].map(loyalty_map).fillna(0)

    # WoE
    df['age_woe'] = df['age'].map(woe_map['age']).fillna(0)
    df['balance_woe'] = df['balance'].map(woe_map['balance']).fillna(0)
    df['credit_sco_woe'] = df['credit_sco'].map(woe_map['credit_sco']).fillna(0)

    final_features = [...]  # same as training
    return df[final_features]