from pydantic import BaseModel
from typing import Optional


class CustomerDataRaw(BaseModel):
    monthly_ir: float
    married: int
    active_member: int
    last_transaction_month: int
    
    age: int
    balance: float
    credit_sco: int
    engagement_score: int
    tenure_ye: int
    nums_card: int
    nums_service: int
    
    gender: str
    occupation: str
    customer_segment: str
    loyalty_level: str
    digital_behavior: str
    
    created_date: str
    last_active_date: str