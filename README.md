#### AI5063 Cyber Security and AI
# AI-Enhanced Retail Cybersecurity Threat Detection System
---

This guide explains how to set up, run, and use the system. It includes steps to process POS logs, visualize them on the dashboard, and authenticate users using JWT.

---

## **1. Setting Up the System**

### **Step 1: Clone the Repository**

```bash
git clone <repository-url>
cd project
```

### **Step 2: Backend Setup**

1. **Install dependencies**:

   ```bash
   cd backend
   pip install fastapi uvicorn sqlite3 scikit-learn pydantic python-jose tensorflow
   ```

2. **Start the FastAPI server**:

   ```bash
   uvicorn app.main:app --reload
   ```

   The backend will be available at `http://localhost:8000`.

### **Step 3: Frontend Setup**

1. **Install frontend dependencies**:

   ```bash
   cd frontend
   npm install
   ```

2. **Start the React application**:

   ```bash
   npm run dev
   ```

   The frontend will be available at `http://localhost:3000`.

---

## **2. Logging In to the Dashboard**

1. Open the dashboard in your browser (`http://localhost:3000`).
2. Click on the **Login** button and enter your credentials:

   - **Username**: `admin`
   - **Password**: `password`

3. Upon successful login, the dashboard will display real-time monitoring and data visualization.

---

## **3. Uploading POS Logs to the System**

1. **Format the POS logs** in the following structure:

| Date       | Transaction ID                       | Amount | Customer ID | Balance | Reference ID                         | Payment Method | Status |
| ---------- | ------------------------------------ | ------ | ----------- | ------- | ------------------------------------ | -------------- | ------ |
| 2024-08-30 | f6435144-3e1e-49b6-b597-2b71219ae9eb | 12.39  | C789        | 10.88   | 826db77d-cf66-4f71-8538-89fc3b102411 | cash           | 0      |
| 2024-07-25 | fec5a710-9723-4773-bc4e-f7cab0bebd4e | 11.66  | C789        | 19.5    | 19f8a5d1-b1ad-4338-b727-2586437a5265 | credit_card    | 0      |
| 2024-03-01 | da705f4b-b05c-4bd0-bbed-2c1e21d3cd40 | 10.39  | C789        | 27.03   | 79ad373a-3641-411e-93bd-e9f5a1bd84a6 | credit_card    | 0      |

## **4. Viewing Logs in the Dashboard**

1. Navigate to the **Dashboard** tab.
2. The uploaded POS logs will appear in the visualization panels, alongside any flagged anomalies.

---

## **5. Real-Time Monitoring**

1. Navigate to the **Network Monitor** tab.
2. View live network traffic data, including:
   - Source and Destination IPs
   - Bytes transferred
   - Threat category
3. The table updates every second with new data streamed from the backend.

---

## **5. Real-Time Monitoring**

1. Navigate to the **Network Monitor** tab.
2. View live network traffic data, including:
   - Source and Destination IPs
   - Bytes transferred
   - Threat category
3. The table updates every second with new data streamed from the backend.

---

## **5. ML Model for Network Analysis**

1. Navigate to the **UNSW-NB15_Preprocessing.ipynb** and **Threat_Classification.ipynb**.

---

## **6. Logging Out**

1. To log out, simply close the browser tab or clear the JWT token from the browser’s storage.

---
