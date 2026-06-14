-- ============================================
-- FINANCIAL FRAUD DETECTION DATABASE SCHEMA
-- ============================================

-- Create database
CREATE DATABASE fraud_detection;

-- Connect to database
-- \c fraud_detection

-- ============================================
-- 1. USERS TABLE
-- ============================================
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INTEGER,
    account_creation_date DATE NOT NULL,
    phone_number VARCHAR(20),
    address VARCHAR(200),
    city VARCHAR(50),
    country VARCHAR(50) DEFAULT 'India',
    risk_profile VARCHAR(20) DEFAULT 'low',
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- 2. MERCHANTS TABLE
-- ============================================
CREATE TABLE merchants (
    merchant_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    merchant_name VARCHAR(100) NOT NULL,
    merchant_category VARCHAR(50),
    country VARCHAR(50) DEFAULT 'India',
    risk_rating VARCHAR(20) DEFAULT 'low',
    contact_email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- 3. TRANSACTIONS TABLE
-- ============================================
CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    merchant_id INTEGER NOT NULL REFERENCES merchants(merchant_id),
    amount DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'INR',
    transaction_type VARCHAR(30),
    transaction_timestamp TIMESTAMP NOT NULL,
    device_id VARCHAR(50),
    device_type VARCHAR(30),
    ip_address VARCHAR(50),
    location_latitude DECIMAL(10, 6),
    location_longitude DECIMAL(10, 6),
    city VARCHAR(50),
    country VARCHAR(50),
    channel VARCHAR(30),
    payment_method VARCHAR(30),
    status VARCHAR(20) DEFAULT 'completed',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- 4. FRAUD_LABELS TABLE
-- ============================================
CREATE TABLE fraud_labels (
    label_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    transaction_id INTEGER NOT NULL REFERENCES transactions(transaction_id),
    is_fraud BOOLEAN NOT NULL,
    fraud_type VARCHAR(50),
    fraud_score DECIMAL(5, 4),
    investigation_status VARCHAR(30) DEFAULT 'pending',
    investigated_by VARCHAR(50),
    investigation_date TIMESTAMP,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- 5. USER_BEHAVIOR_PROFILE TABLE (for ML features)
-- ============================================
CREATE TABLE user_behavior_profile (
    profile_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    avg_transaction_amount DECIMAL(10, 2),
    median_transaction_amount DECIMAL(10, 2),
    total_transactions INTEGER,
    total_amount_spent DECIMAL(12, 2),
    avg_transactions_per_day DECIMAL(5, 2),
    max_transaction_amount DECIMAL(10, 2),
    min_transaction_amount DECIMAL(10, 2),
    std_transaction_amount DECIMAL(10, 2),
    unique_merchants INTEGER,
    unique_devices INTEGER,
    unique_locations INTEGER,
    last_transaction_date TIMESTAMP,
    days_since_last_transaction INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- 6. INDEXES FOR PERFORMANCE
-- ============================================
CREATE INDEX idx_transactions_user_id ON transactions(user_id);
CREATE INDEX idx_transactions_merchant_id ON transactions(merchant_id);
CREATE INDEX idx_transactions_timestamp ON transactions(transaction_timestamp);
CREATE INDEX idx_transactions_amount ON transactions(amount);
CREATE INDEX idx_transactions_is_fraud ON fraud_labels(is_fraud);
CREATE INDEX idx_users_risk_profile ON users(risk_profile);
CREATE INDEX idx_merchants_risk_rating ON merchants(risk_rating);

-- ============================================
-- 7. VIEWS FOR ANALYTICS
-- ============================================
CREATE VIEW v_fraud_transactions AS
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
    fl.fraud_type,
    fl.fraud_score
FROM transactions t
JOIN users u ON t.user_id = u.user_id
JOIN merchants m ON t.merchant_id = m.merchant_id
JOIN fraud_labels fl ON t.transaction_id = fl.transaction_id
WHERE fl.is_fraud = TRUE;

CREATE VIEW v_transaction_stats AS
SELECT 
    DATE_TRUNC('day', transaction_timestamp) AS transaction_date,
    COUNT(*) AS total_transactions,
    SUM(amount) AS total_amount,
    AVG(amount) AS avg_amount,
    COUNT(CASE WHEN fl.is_fraud = TRUE THEN 1 END) AS fraud_count,
    COUNT(CASE WHEN fl.is_fraud = TRUE THEN 1 END) * 100.0 / COUNT(*) AS fraud_rate
FROM transactions t
LEFT JOIN fraud_labels fl ON t.transaction_id = fl.transaction_id
GROUP BY DATE_TRUNC('day', transaction_timestamp)
ORDER BY transaction_date;

-- ============================================
-- 8. COMMENTS
-- ============================================
COMMENT ON TABLE users IS 'Customer information and risk profiles';
COMMENT ON TABLE merchants IS 'Merchant information and risk ratings';
COMMENT ON TABLE transactions IS 'All financial transactions with metadata';
COMMENT ON TABLE fraud_labels IS 'Fraud classification and investigation data';
COMMENT ON TABLE user_behavior_profile IS 'Aggregated user behavior for ML features';
