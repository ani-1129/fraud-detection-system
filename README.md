# 🛡️ Financial Fraud Detection AI

> 🚀 **AI-Powered Financial Fraud Intelligence System** with 15+ Interactive Visual Charts using Plotly & Streamlit

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-orange.svg)
![Plotly](https://img.shields.io/badge/Plotly-5.23+-cyan.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Demo](https://img.shields.io/badge/Demo-Available-blue.svg)

---

## 🎯 **Live Demo**

### **🚀 Try the Dashboard Online:**
[![Open in Streamlit](https://img.shields.io/badge/Open-in-Streamlit-blue.svg)](https://fraud-detection-system-by-aniket-singh.streamlit.app/)

**🔗 Demo Link:** https://fraud-detection-system-by-aniket-singh.streamlit.app/

> Click the link above to access the live dashboard with real-time fraud intelligence!

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Visualization Charts](#visualization-charts)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Demo](#demo)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🎯 Project Overview

**Financial Fraud Detection AI** is a hyper-realistic modern dashboard that provides real-time AI-powered fraud intelligence. The system uses advanced analytics and machine learning to detect fraudulent transactions, visualize patterns, and alert security teams about high-risk activities.

### Key Goals:
- Detect fraudulent transactions in real-time
- Visualize fraud patterns across multiple dimensions
- Provide actionable intelligence for security teams
- Enable data export for further analysis

---

## ✨ Features

### 🎨 **Modern UI with Glassmorphism**
- Hyper-realistic gloss & glassmorphism design
- Gradient backgrounds with custom CSS
- Responsive metric cards with hover effects
- Smooth animations and transitions

### 📊 **15 Interactive Charts**
- Real-time fraud intelligence metrics
- Multiple visualization types (Pie, Bar, Line, Heatmap, etc.)
- Interactive Plotly charts with hover data
- Custom color schemes and styling

### 🔍 **Smart Filters**
- Payment method filtering
- City-based filtering
- Fraud-only toggle
- Date range selection
- Risk level filtering

### 💾 **Data Export**
- Download full reports as CSV
- Real-time data timestamping
- Custom file naming

---

## 📈 Visualization Charts

| Chart # | Title | Type | Description |
|---------|-------|------|-------------|
| 1 | Fraud Intelligence Distribution | Pie Chart | Fraud vs Non-Fraud transactions |
| 2 | Payment Method Transaction Volume | Bar Chart | Total volume by payment method |
| 3 | Fraud Trend Analysis Over Time | Line Chart | Daily fraud transaction trend |
| 4 | Transaction Amount Risk Distribution | Histogram | Fraud vs legitimate amount distribution |
| 5 | Geographic Fraud Heatmap | Heatmap | Fraud count by city |
| 6 | AI Fraud Score Analysis | Scatter Plot | Fraud score over time |
| 7 | Top 10 Highest Risk Fraud | Data Table | Top fraud transactions by amount |
| 8 | Transaction Amount by Type | Box Plot | Amount distribution by transaction type |
| 9 | Transaction Velocity Trend | Area Chart | Daily transaction velocity |
| 10 | Fraud Breakdown by Payment Method | Funnel Chart | Fraud transactions by payment method |
| 11 | Device Type Distribution | Pie Chart | Device usage distribution |
| 12 | Transaction Channel Analysis | Bar Chart | Channel distribution |
| 13 | City Fraud Risk Bubble Map | Bubble Chart | Average fraud score by city |
| 14 | Transaction Type vs Fraud Matrix | Crosstab Heatmap | Transaction type vs fraud count |
| 15 | Latest Fraud Alerts | Data Table | Real-time fraud alerts |

---

## 🛠️ Tech Stack

### **Frontend**
- ![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-orange.svg) - Web application framework
- ![Plotly](https://img.shields.io/badge/Plotly-5.23+-cyan.svg) - Interactive visualizations
- ![CSS3](https://img.shields.io/badge/CSS3-Glassmorphism-purple.svg) - Custom styling

### **Backend**
- ![Python](https://img.shields.io/badge/Python-3.10+-blue.svg) - Programming language
- ![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg) - Data manipulation
- ![NumPy](https://img.shields.io/badge/NumPy-1.24+-yellow.svg) - Numerical computing

### **Database** (Optional)
- PostgreSQL - Transaction database
- Sample data generator for demo

---

## 📦 Installation

### **Requirements**
- Python 3.10 or higher
- pip (Python package manager)
- 4GB RAM minimum
- 2GB disk space

### **Step 1: Clone Repository**
```bash
cd C:\Users\Aniket Singh\OneDrive\Desktop\fraud-detection-system
```

### **Step 2: Create Virtual Environment**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac
```

### **Step 3: Install Dependencies**
```bash
pip install streamlit==1.28.0
pip install pandas==2.0.0
pip install numpy==1.24.0
pip install plotly==5.23.0
pip install matplotlib==3.7.0
```

### **Step 4: Install All Packages**
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### **Alternative: Try the Demo First**
👉 **No installation needed!** Access the live dashboard at:
[https://fraud-detection-system-by-aniket-singh.streamlit.app/](https://fraud-detection-system-by-aniket-singh.streamlit.app/)

### **Run the Dashboard Locally**
```bash
streamlit run dashboard/app.py
```

### **Access the Application**
- Open browser: `http://localhost:8501`
- Dashboard will load automatically

### **Using Filters**
1. **Payment Method**: Select from multiselect (UPI, Credit Card, Debit Card, etc.)
2. **City**: Choose cities from multiselect
3. **Fraud Only**: Toggle checkbox to show only fraudulent transactions
4. **Date Range**: Select date range from date input
5. **Risk Level**: Choose from dropdown (All, Low, Medium, High)

### **Export Data**
1. Click "📥 Download Full Report (CSV)" button
2. File will be saved with timestamp: `fraud_data_YYYYMMDD_HHMMSS.csv`

---

## 📁 Project Structure
