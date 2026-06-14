"""
🚀 Hyper-Realistic Modern Fraud Detection Dashboard
AI-Powered Financial Fraud Intelligence System
15+ Interactive Visual Charts with Plotly
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.graph_objects import Scatter
from datetime import datetime, timedelta
import time


# Page configuration
st.set_page_config(
    page_title="Fraud Detection AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================
# ADVANCED CUSTOM CSS - MODERN GLOSS & GLASSMORPHISM
# ============================================
st.markdown("""
    <style>
    /* Root Variables */
    :root {
        --primary-color: #6366F1;
        --secondary-color: #8B5CF6;
        --accent-color: #EC4899;
        --danger-color: #FF4757;
        --success-color: #2ED573;
        --warning-color: #FFA502;
        --bg-dark: #0F141F;
        --bg-card: #1A2030;
        --bg-glass: rgba(26, 32, 48, 0.7);
        --border-color: #2D3748;
        --text-primary: #FFFFFF;
        --text-secondary: #A0AEC0;
    }

    /* Main Background with Gradient */
    .main {
        background: linear-gradient(135deg, #0F141F 0%, #1A2030 50%, #0F141F 100%);
        color: #FFFFFF;
        min-height: 100vh;
    }

    /* Header Styling */
    .header-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(90deg, #6366F1 0%, #EC4899 50%, #8B5CF6 100%);
        background-clip: text;
        -webkit-background-clip: text;
        color: transparent;
        text-shadow: 0 0 40px rgba(99, 102, 241, 0.3);
        margin-bottom: 0.5rem;
        animation: fadeInDown 1s ease;
    }

    .header-subtitle {
        font-size: 1.4rem;
        color: #A0AEC0;
        font-weight: 400;
        margin-bottom: 2rem;
        animation: fadeInUp 1s ease;
    }

    /* Metric Cards - Glassmorphism */
    .metric-card {
        background: linear-gradient(135deg, rgba(26, 32, 48, 0.9) 0%, rgba(45, 55, 72, 0.8) 100%);
        border: 1px solid rgba(99, 102, 241, 0.2);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3),
                    inset 0 1px 0 rgba(255, 255, 255, 0.1);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }

    .metric-card:hover {
        transform: translateY(-8px);
        border-color: rgba(99, 102, 241, 0.5);
        box-shadow: 0 12px 48px rgba(99, 102, 241, 0.2),
                    inset 0 1px 0 rgba(255, 255, 255, 0.15);
    }

    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #6366F1, #EC4899, #8B5CF6);
        opacity: 0.7;
    }

    .metric-label {
        font-size: 0.95rem;
        color: #A0AEC0;
        font-weight: 500;
        margin-bottom: 8px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 8px;
        line-height: 1;
    }

    .metric-delta {
        font-size: 0.9rem;
        font-weight: 600;
        padding: 4px 12px;
        border-radius: 8px;
        display: inline-block;
    }

    .metric-delta.positive {
        background: rgba(46, 213, 115, 0.2);
        color: #2ED573;
    }

    .metric-delta.negative {
        background: rgba(255, 71, 87, 0.2);
        color: #FF4757;
    }

    /* Section Headers */
    .section-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #FFFFFF;
        margin: 3rem 0 1.5rem 0;
        background: linear-gradient(90deg, #FFFFFF 0%, #A0AEC0 100%);
        background-clip: text;
        -webkit-background-clip: text;
        color: transparent;
    }

    .section-subheader {
        font-size: 1.1rem;
        color: #A0AEC0;
        margin-bottom: 1.5rem;
    }

    /* Chart Containers */
    .chart-container {
        background: rgba(26, 32, 48, 0.6);
        border: 1px solid rgba(99, 102, 241, 0.15);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 24px rgba(0, 0, 0, 0.2);
    }

    /* Sidebar Glass Effect */
    .sidebar {
        background: rgba(26, 32, 48, 0.95);
        border-right: 1px solid rgba(99, 102, 241, 0.2);
    }

    .sidebar-header {
        font-size: 1.6rem;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 1.5rem;
    }

    /* Table Styling */
    .dataframe {
        background: rgba(26, 32, 48, 0.8);
        border-radius: 12px;
        border: 1px solid rgba(99, 102, 241, 0.15);
    }

    /* Download Button */
    .stDownloadButton button {
        background: linear-gradient(90deg, #6366F1 0%, #EC4899 100%);
        border: none;
        border-radius: 12px;
        padding: 12px 24px;
        font-weight: 600;
        box-shadow: 0 4px 16px rgba(99, 102, 241, 0.3);
        transition: all 0.3s ease;
    }

    .stDownloadButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 24px rgba(99, 102, 241, 0.4);
    }

    /* Animations */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes pulse {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: 0.7;
        }
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #A0AEC0;
        font-size: 0.9rem;
        margin-top: 4rem;
        padding: 2rem 0;
        border-top: 1px solid rgba(99, 102, 241, 0.15);
    }
    </style>
""", unsafe_allow_html=True)


# ============================================
# DATABASE CONNECTION (Using Sample Data)
# ============================================
def get_database_connection():
    """Connect to PostgreSQL database"""
    return None


def load_fraud_data():
    """Load transaction and fraud data"""
    conn = get_database_connection()
    if conn is None:
        return load_sample_data()
    
    query = """
    SELECT 
        t.transaction_id,
        t.user_id,
        u.first_name,
        u.last_name,
        t.merchant_id,
        m.merchant_name,
        t.amount,
        t.transaction_timestamp,
        t.city,
        t.country,
        t.payment_method,
        t.transaction_type,
        fl.is_fraud,
        fl.fraud_type,
        fl.fraud_score
    FROM transactions t
    JOIN users u ON t.user_id = u.user_id
    JOIN merchants m ON t.merchant_id = m.merchant_id
    JOIN fraud_labels fl ON t.transaction_id = fl.transaction_id
    ORDER BY t.transaction_timestamp DESC
    LIMIT 10000
    """
    
    df = pd.read_sql(query, conn)
    conn.close()
    return df


def load_sample_data():
    """Load sample data for demo"""
    np.random.seed(42)
    n = 10000
    
    data = {
        'transaction_id': range(1, n+1),
        'user_id': np.random.randint(1, 1001, n),
        'first_name': ['User' + str(i) for i in np.random.randint(1, 1001, n)],
        'last_name': ['Name' + str(i) for i in np.random.randint(1, 1001, n)],
        'merchant_id': np.random.randint(1, 101, n),
        'merchant_name': ['Merchant' + str(i) for i in np.random.randint(1, 101, n)],
        'amount': np.random.normal(5000, 2000, n).clip(100, 50000),
        'transaction_timestamp': pd.date_range(end=datetime.now(), periods=n, freq='10min'),
        'city': np.random.choice(['Lucknow', 'Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad'], n),
        'country': ['India'] * n,
        'payment_method': np.random.choice(['UPI', 'Credit Card', 'Debit Card', 'Net Banking', 'Wallet'], n),
        'transaction_type': np.random.choice(['online_purchase', 'atm_withdrawal', 'bill_payment', 'money_transfer', 'merchant_payment'], n),
        'is_fraud': np.random.random(n) < 0.08,
        'fraud_type': np.random.choice(['unauthorized', 'stolen_card', 'identity_theft', 'account_takeover'], n),
        'fraud_score': np.random.random(n) * 1.0,
        'device_type': np.random.choice(['mobile', 'desktop', 'tablet'], n),
        'channel': np.random.choice(['mobile_app', 'web', 'pos', 'atm'], n)
    }
    
    df = pd.DataFrame(data)
    df['fraud_type'] = df['fraud_type'].where(df['is_fraud'], None)
    return df


# ============================================
# MAIN APP
# ============================================
def main():
    """Main Streamlit application"""
    
    # Header
    st.markdown('<h1 class="header-title">🛡️ Financial Fraud Detection AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="header-subtitle">🚀 Real-time AI-Powered Fraud Intelligence Dashboard</p>', unsafe_allow_html=True)
    
    # Load data
    df = load_fraud_data()
    
    # Sidebar filters with glass effect
    with st.sidebar:
        st.markdown('<h3 class="sidebar-header">🔍 Smart Filters</h3>', unsafe_allow_html=True)
        
        # Date range filter
        min_date = df['transaction_timestamp'].min()
        max_date = df['transaction_timestamp'].max()
        
        selected_date = st.date_input(
            "📅 Date Range",
            value=max_date,
            min_value=min_date,
            max_value=max_date
        )
        
        # Payment method filter
        payment_methods = st.multiselect(
            "💳 Payment Method",
            options=df['payment_method'].unique(),
            default=df['payment_method'].unique()
        )
        
        # City filter
        cities = st.multiselect(
            "🏙️ City",
            options=df['city'].unique(),
            default=df['city'].unique()
        )
        
        # Fraud filter
        fraud_only = st.checkbox("🚨 Show Fraud Only", value=False)
        
        # Risk level filter
        risk_level = st.selectbox(
            "⚠️ Risk Level",
            options=["All", "Low", "Medium", "High"],
            index=0
        )
    
    # Apply filters
    filtered_df = df.copy()
    filtered_df = filtered_df[filtered_df['payment_method'].isin(payment_methods)]
    filtered_df = filtered_df[filtered_df['city'].isin(cities)]
    
    if fraud_only:
        filtered_df = filtered_df[filtered_df['is_fraud'] == True]
    
    # ============================================
    # KEY METRICS - GLASSMORPHISM CARDS
    # ============================================
    st.markdown('<h2 class="section-header">📊 Real-time Intelligence Metrics</h2>', unsafe_allow_html=True)
    
    total_transactions = len(filtered_df)
    total_fraud = filtered_df['is_fraud'].sum()
    fraud_rate = (total_fraud / total_transactions * 100) if total_transactions > 0 else 0
    avg_amount = filtered_df['amount'].mean()
    total_fraud_amount = filtered_df[filtered_df['is_fraud']]['amount'].sum()
    high_risk = filtered_df[filtered_df['fraud_score'] > 0.7].shape[0]
    
    # Display metrics in glass cards
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown(f'''
            <div class="metric-card">
                <div class="metric-label">Total Transactions</div>
                <div class="metric-value">{total_transactions}</div>
                <div class="metric-delta positive">📈 Live</div>
            </div>
        ''', unsafe_allow_html=True)
    
    with col2:
        st.markdown(f'''
            <div class="metric-card">
                <div class="metric-label">Fraud Detected</div>
                <div class="metric-value">{total_fraud}</div>
                <div class="metric-delta negative">⚠️ {fraud_rate:.2f}%</div>
            </div>
        ''', unsafe_allow_html=True)
    
    with col3:
        st.markdown(f'''
            <div class="metric-card">
                <div class="metric-label">Fraud Rate</div>
                <div class="metric-value">{fraud_rate:.2f}%</div>
                <div class="metric-delta">🎯 Target</div>
            </div>
        ''', unsafe_allow_html=True)
    
    with col4:
        st.markdown(f'''
            <div class="metric-card">
                <div class="metric-label">Avg Transaction</div>
                <div class="metric-value">₹{avg_amount:.0f}</div>
                <div class="metric-delta positive">💰 Healthy</div>
            </div>
        ''', unsafe_allow_html=True)
    
    with col5:
        st.markdown(f'''
            <div class="metric-card">
                <div class="metric-label">High-Risk Alerts</div>
                <div class="metric-value">{high_risk}</div>
                <div class="metric-delta negative">🚨 Critical</div>
            </div>
        ''', unsafe_allow_html=True)
    
    st.markdown('<hr style="border: 1px solid rgba(99, 102, 241, 0.2); margin: 3rem 0;">', unsafe_allow_html=True)
    
    # ============================================
    # CHART 1: Fraud Distribution (3D Pie)
    # ============================================
    st.markdown('<h2 class="section-header">📊 Chart 1: Fraud Intelligence Distribution</h2>', unsafe_allow_html=True)
    
    fraud_counts = filtered_df['is_fraud'].value_counts()
    fraud_count = fraud_counts.get(True, 0)
    non_fraud_count = fraud_counts.get(False, 0)
    
    pie_data = pd.DataFrame({
        'Category': ['Fraud Detected', 'Legit Transactions'],
        'Count': [fraud_count, non_fraud_count]
    })
    
    fig_pie = px.pie(
        pie_data,
        values='Count',
        names='Category',
        title='Fraud vs Non-Fraud Transactions',
        color_discrete_sequence=['#FF4757', '#2ED573'],
        hole=0.4
    )
    fig_pie.update_traces(
        textposition='auto',
        textinfo='percent+label+value',
        marker=dict(line=dict(color='#000000', width=2))
    )
    fig_pie.update_layout(
        paper_bgcolor='rgba(26, 32, 48, 0.6)',
        plot_bgcolor='rgba(26, 32, 48, 0)',
        font=dict(color='#FFFFFF'),
        showlegend=True,
        legend=dict(
            bgcolor='rgba(26, 32, 48, 0.8)',
            bordercolor='rgba(99, 102, 241, 0.3)',
            borderwidth=1
        )
    )
    st.plotly_chart(fig_pie, use_container_width=True)
    
    # CHART 2: Amount by Payment Method (Animated Bar)
    st.markdown('<h2 class="section-header">📊 Chart 2: Payment Method Transaction Volume</h2>', unsafe_allow_html=True)
    
    amount_by_method = filtered_df.groupby('payment_method')['amount'].agg(['sum', 'mean', 'count']).reset_index()
    amount_by_method.columns = ['Payment Method', 'Total Amount', 'Avg Amount', 'Transaction Count']
    
    fig_bar = px.bar(
        amount_by_method,
        x='Payment Method',
        y='Total Amount',
        title='Total Transaction Volume by Payment Method',
        color='Total Amount',
        color_continuous_scale='Reds',
        hover_data=['Avg Amount', 'Transaction Count']
    )
    fig_bar.update_traces(
        text=amount_by_method['Total Amount'].apply(lambda x: f'₹{x:.0f}'),
        textposition='auto',
        marker=dict(line=dict(color='#000000', width=1.5))
    )
    fig_bar.update_layout(
        paper_bgcolor='rgba(26, 32, 48, 0.6)',
        plot_bgcolor='rgba(26, 32, 48, 0)',
        font=dict(color='#FFFFFF'),
        xaxis=dict(gridcolor='rgba(99, 102, 241, 0.2)'),
        yaxis=dict(gridcolor='rgba(99, 102, 241, 0.2)')
    )
    st.plotly_chart(fig_bar, use_container_width=True)
    
    # CHART 3: Fraud Trend (Smooth Line with Gradient)
    st.markdown('<h2 class="section-header">📊 Chart 3: Fraud Trend Analysis Over Time</h2>', unsafe_allow_html=True)
    
    filtered_df['transaction_date'] = filtered_df['transaction_timestamp'].dt.strftime('%Y-%m-%d')
    fraud_trend = filtered_df.groupby('transaction_date').agg({
        'is_fraud': 'sum',
        'amount': 'sum',
        'fraud_score': 'mean'
    }).reset_index()
    
    fig_line = px.line(
        fraud_trend,
        x='transaction_date',
        y='is_fraud',
        title='Daily Fraud Transaction Trend',
        markers=True,
        line_shape='spline'
    )
    fig_line.update_traces(
        line=dict(color='#FF4757', width=4),
        marker=dict(size=10, color='#FFFFFF', line=dict(color='#FF4757', width=2))
    )
    fig_line.update_layout(
        paper_bgcolor='rgba(26, 32, 48, 0.6)',
        plot_bgcolor='rgba(26, 32, 48, 0)',
        font=dict(color='#FFFFFF'),
        xaxis=dict(gridcolor='rgba(99, 102, 241, 0.2)'),
        yaxis=dict(gridcolor='rgba(99, 102, 241, 0.2)')
    )
    st.plotly_chart(fig_line, use_container_width=True)
    
    # CHART 4: Amount Distribution (Overlay Histogram)
    st.markdown('<h2 class="section-header">📊 Chart 4: Transaction Amount Risk Distribution</h2>', unsafe_allow_html=True)
    
    fig_hist = px.histogram(
        filtered_df,
        x='amount',
        color='is_fraud',
        title='Transaction Amount Distribution (Fraud vs Legitimate)',
        barmode='overlay',
        color_discrete_sequence=['#FF4757', '#2ED573'],
        nbins=50,
        hover_data=['amount']
    )
    fig_hist.update_traces(opacity=0.7, marker_line_color='#000000', marker_line_width=1)
    fig_hist.update_layout(
        paper_bgcolor='rgba(26, 32, 48, 0.6)',
        plot_bgcolor='rgba(26, 32, 48, 0)',
        font=dict(color='#FFFFFF'),
        xaxis=dict(gridcolor='rgba(99, 102, 241, 0.2)'),
        yaxis=dict(gridcolor='rgba(99, 102, 241, 0.2)')
    )
    st.plotly_chart(fig_hist, use_container_width=True)
    
    # CHART 5: Fraud Heatmap
    st.markdown('<h2 class="section-header">📊 Chart 5: Geographic Fraud Heatmap</h2>', unsafe_allow_html=True)
    
    fraud_by_city = filtered_df.groupby(['city', 'is_fraud']).size().reset_index(name='count')
    fraud_by_city_pivot = fraud_by_city.pivot(index='city', columns='is_fraud', values='count')
    fraud_by_city_pivot = fraud_by_city_pivot.fillna(0)
    
    fig_heatmap = px.imshow(
        fraud_by_city_pivot,
        title='Fraud Count Heatmap by City',
        text_auto=True,
        color_continuous_scale='Reds',
        aspect='auto'
    )
    fig_heatmap.update_layout(
        paper_bgcolor='rgba(26, 32, 48, 0.6)',
        plot_bgcolor='rgba(26, 32, 48, 0)',
        font=dict(color='#FFFFFF'),
        xaxis=dict(gridcolor='rgba(99, 102, 241, 0.2)'),
        yaxis=dict(gridcolor='rgba(99, 102, 241, 0.2)')
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)
    
    # CHART 6: Fraud Score Scatter
    st.markdown('<h2 class="section-header">📊 Chart 6: AI Fraud Score Analysis</h2>', unsafe_allow_html=True)
    
    fig_scatter = px.scatter(
        filtered_df.head(2000),
        x='transaction_timestamp',
        y='fraud_score',
        color='is_fraud',
        title='Fraud Score Over Time (AI Prediction)',
        size='amount',
        hover_data=['amount', 'payment_method', 'city', 'fraud_type'],
        color_discrete_sequence=['#FF4757', '#2ED573'],
        opacity=0.8
    )
    fig_scatter.update_traces(
        marker=dict(size=10, opacity=0.7, line=dict(color='#000000', width=1))
    )
    fig_scatter.update_layout(
        paper_bgcolor='rgba(26, 32, 48, 0.6)',
        plot_bgcolor='rgba(26, 32, 48, 0)',
        font=dict(color='#FFFFFF'),
        xaxis=dict(gridcolor='rgba(99, 102, 241, 0.2)'),
        yaxis=dict(gridcolor='rgba(99, 102, 241, 0.2)')
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    # CHART 7: Top 10 Fraud (Styled Table)
    st.markdown('<h2 class="section-header">📊 Chart 7: Top 10 Highest Risk Fraud Transactions</h2>', unsafe_allow_html=True)
    
    top_fraud = filtered_df[filtered_df['is_fraud'] == True].nlargest(10, 'amount')
    
    st.dataframe(
        top_fraud[['transaction_id', 'first_name', 'last_name', 'amount', 'payment_method', 'city', 'fraud_type', 'fraud_score']].
        rename(columns={
            'transaction_id': '🆔 ID',
            'first_name': 'Name',
            'last_name': '',
            'amount': '💰 Amount (₹)',
            'payment_method': '💳 Method',
            'city': '🏙️ City',
            'fraud_type': '🚨 Type',
            'fraud_score': '⚠️ Risk Score'
        }),
        use_container_width=True,
        hide_index=True
    )
    
    # CHART 8: Box Plot
    st.markdown('<h2 class="section-header">📊 Chart 8: Transaction Amount by Type (Risk Analysis)</h2>', unsafe_allow_html=True)
    
    fig_box = px.box(
        filtered_df,
        x='transaction_type',
        y='amount',
        color='is_fraud',
        title='Transaction Amount Distribution by Type',
        color_discrete_sequence=['#FF4757', '#2ED573'],
        hover_data=['amount']
    )
    fig_box.update_layout(
        paper_bgcolor='rgba(26, 32, 48, 0.6)',
        plot_bgcolor='rgba(26, 32, 48, 0)',
        font=dict(color='#FFFFFF'),
        xaxis=dict(gridcolor='rgba(99, 102, 241, 0.2)'),
        yaxis=dict(gridcolor='rgba(99, 102, 241, 0.2)')
    )
    st.plotly_chart(fig_box, use_container_width=True)
    
    # CHART 9: Area Chart
    st.markdown('<h2 class="section-header">📊 Chart 9: Transaction Velocity Trend</h2>', unsafe_allow_html=True)
    
    velocity = filtered_df.groupby('transaction_date').size().reset_index(name='count')
    
    fig_area = px.area(
        velocity,
        x='transaction_date',
        y='count',
        title='Daily Transaction Velocity',
        color='#6366F1',
        fill='tozeroy'
    )
    fig_area.update_traces(line=dict(width=4, color='#6366F1'))
    fig_area.update_layout(
        paper_bgcolor='rgba(26, 32, 48, 0.6)',
        plot_bgcolor='rgba(26, 32, 48, 0)',
        font=dict(color='#FFFFFF'),
        xaxis=dict(gridcolor='rgba(99, 102, 241, 0.2)'),
        yaxis=dict(gridcolor='rgba(99, 102, 241, 0.2)')
    )
    st.plotly_chart(fig_area, use_container_width=True)
    
    # CHART 10: Funnel
    st.markdown('<h2 class="section-header">📊 Chart 10: Fraud Breakdown by Payment Method</h2>', unsafe_allow_html=True)
    
    fraud_by_payment = filtered_df[filtered_df['is_fraud'] == True].groupby('payment_method').size().reset_index(name='count')
    fraud_by_payment = fraud_by_payment.sort_values('count', ascending=False)
    
    fig_funnel = px.funnel(
        fraud_by_payment,
        x='count',
        y='payment_method',
        title='Fraud Transactions by Payment Method',
        hover_data=['count']
    )
    fig_funnel.update_layout(
        paper_bgcolor='rgba(26, 32, 48, 0.6)',
        plot_bgcolor='rgba(26, 32, 48, 0)',
        font=dict(color='#FFFFFF')
    )
    st.plotly_chart(fig_funnel, use_container_width=True)
    
    # CHART 11: Device Pie
    st.markdown('<h2 class="section-header">📊 Chart 11: Device Type Distribution</h2>', unsafe_allow_html=True)
    
    device_dist = filtered_df['device_type'].value_counts()
    device_data = pd.DataFrame({
        'Device': device_dist.index,
        'Count': device_dist.values
    })
    
    fig_device_pie = px.pie(
        device_data,
        values='Count',
        names='Device',
        title='Device Type Usage Distribution',
        hole=0.3,
        color_discrete_sequence=['#6366F1', '#8B5CF6', '#EC4899']
    )
    fig_device_pie.update_traces(
        textposition='auto',
        textinfo='percent+label+value',
        marker=dict(line=dict(color='#000000', width=2))
    )
    fig_device_pie.update_layout(
        paper_bgcolor='rgba(26, 32, 48, 0.6)',
        plot_bgcolor='rgba(26, 32, 48, 0)',
        font=dict(color='#FFFFFF')
    )
    st.plotly_chart(fig_device_pie, use_container_width=True)
    
    # CHART 12: Channel Bar
    st.markdown('<h2 class="section-header">📊 Chart 12: Transaction Channel Analysis</h2>', unsafe_allow_html=True)
    
    channel_dist = filtered_df['channel'].value_counts()
    channel_data = pd.DataFrame({
        'Channel': channel_dist.index,
        'Count': channel_dist.values
    })
    
    fig_channel_bar = px.bar(
        channel_data,
        x='Channel',
        y='Count',
        title='Transaction Channel Distribution',
        color='Count',
        color_continuous_scale='Blues'
    )
    fig_channel_bar.update_traces(
        text=channel_data['Count'].apply(lambda x: f'{x}'),
        textposition='auto'
    )
    fig_channel_bar.update_layout(
        paper_bgcolor='rgba(26, 32, 48, 0.6)',
        plot_bgcolor='rgba(26, 32, 48, 0)',
        font=dict(color='#FFFFFF'),
        xaxis=dict(gridcolor='rgba(99, 102, 241, 0.2)'),
        yaxis=dict(gridcolor='rgba(99, 102, 241, 0.2)')
    )
    st.plotly_chart(fig_channel_bar, use_container_width=True)
    
    # CHART 13: Bubble Chart
    st.markdown('<h2 class="section-header">📊 Chart 13: City Fraud Risk Bubble Map</h2>', unsafe_allow_html=True)
    
    fraud_score_city = filtered_df[filtered_df['is_fraud'] == True].groupby('city').agg({
        'fraud_score': 'mean',
        'amount': 'sum'
    }).reset_index()
    
    fig_bubble = px.scatter(
        fraud_score_city,
        x='city',
        y='fraud_score',
        size='amount',
        title='Average Fraud Score by City (Bubble = Total Amount)',
        hover_data=['amount'],
        color='fraud_score',
        color_continuous_scale='Reds',
        opacity=0.8
    )
    fig_bubble.update_traces(
        marker=dict(line=dict(color='#000000', width=1))
    )
    fig_bubble.update_layout(
        paper_bgcolor='rgba(26, 32, 48, 0.6)',
        plot_bgcolor='rgba(26, 32, 48, 0)',
        font=dict(color='#FFFFFF'),
        xaxis=dict(gridcolor='rgba(99, 102, 241, 0.2)'),
        yaxis=dict(gridcolor='rgba(99, 102, 241, 0.2)')
    )
    st.plotly_chart(fig_bubble, use_container_width=True)
    
    # CHART 14: Crosstab
    st.markdown('<h2 class="section-header">📊 Chart 14: Transaction Type vs Fraud Matrix</h2>', unsafe_allow_html=True)
    
    crosstab = filtered_df.groupby(['transaction_type', 'is_fraud']).size().reset_index(name='count')
    crosstab_pivot = crosstab.pivot(index='transaction_type', columns='is_fraud', values='count')
    crosstab_pivot = crosstab_pivot.fillna(0)
    
    fig_crosstab = px.imshow(
        crosstab_pivot,
        title='Transaction Type vs Fraud Count Matrix',
        text_auto=True,
        color_continuous_scale='RdYlGn'
    )
    fig_crosstab.update_layout(
        paper_bgcolor='rgba(26, 32, 48, 0.6)',
        plot_bgcolor='rgba(26, 32, 48, 0)',
        font=dict(color='#FFFFFF')
    )
    st.plotly_chart(fig_crosstab, use_container_width=True)
    
    # CHART 15: Recent Alerts
    st.markdown('<h2 class="section-header">🛡️ Chart 15: Latest Fraud Alerts (Real-time)</h2>', unsafe_allow_html=True)
    
    recent_fraud = filtered_df[filtered_df['is_fraud'] == True].head(20)
    
    st.dataframe(
        recent_fraud[['transaction_id', 'transaction_timestamp', 'first_name', 'last_name', 'amount', 'payment_method', 'city', 'fraud_type', 'fraud_score']].
        rename(columns={
            'transaction_id': '🆔',
            'transaction_timestamp': '🕐 Time',
            'first_name': 'Name',
            'last_name': '',
            'amount': '💰 Amount',
            'payment_method': '💳 Method',
            'city': '🏙️',
            'fraud_type': '🚨 Type',
            'fraud_score': '⚠️ Score'
        }),
        use_container_width=True,
        hide_index=True
    )
    
    # EXPORT DATA
    st.markdown('<hr style="border: 1px solid rgba(99, 102, 241, 0.2); margin: 4rem 0;">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">💾 Export Intelligence Data</h2>', unsafe_allow_html=True)
    
    csv_data = filtered_df.to_csv(index=False)
    st.download_button(
        label="📥 Download Full Report (CSV)",
        data=csv_data,
        file_name=f"fraud_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv"
    )
    
    # Footer
    st.markdown('<hr style="border: 1px solid rgba(99, 102, 241, 0.2); margin: 4rem 0;">', unsafe_allow_html=True)
    st.markdown(f'''
        <div class="footer">
            <p>🛡️ Financial Fraud Detection AI | Powered by Streamlit + Plotly + AI</p>
            <p>🚀 Real-time Intelligence Dashboard | Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p>© 2026 Fraud Detection AI System</p>
        </div>
    ''', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
