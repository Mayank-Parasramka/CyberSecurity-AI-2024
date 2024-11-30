from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from database import Base
from datetime import datetime

import pandas as pd
from sklearn.ensemble import IsolationForest
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("pos_logs.csv")
# Convert timestamp to numeric format
# data['timestamp_numeric'] = pd.to_datetime(data['timestamp']).dt.hour  # Convert to Unix timestamp
columns = data.columns
features = data[columns[:-1]]
features = features.drop(columns=['timestamp','transaction_id','user_id', 'payment_method'])

# Initialize LabelEncoder
label_encoders = {}

# Map categorical columns to numeric values
for column in ['item_code']:  # List of categorical columns
    le = LabelEncoder()
    features[column] = le.fit_transform(features[column])
    label_encoders[column] = le  

# Train Isolation Forest
iso_forest = IsolationForest(n_estimators=100,
                            contamination=0.1,
                            max_samples=256,
                             bootstrap=True,
                            random_state=42)

iso_forest.fit(features)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class POSLog(Base):
    __tablename__ = "pos_logs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    transaction_id = Column(String, unique=True, index=True)
    duration_time = Column(Float)
    item_code = Column(String)
    amount = Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"))
    payment_method = Column(String)
    is_anomalous = Column(Boolean, default=False)

    __table_args__ = {"extend_existing": True}
