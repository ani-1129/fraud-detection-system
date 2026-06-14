-- ============================================
-- INSERT SAMPLE DATA (Optional - for testing)
-- ============================================

-- Insert sample users
INSERT INTO users (first_name, last_name, email, age, account_creation_date, city, country, risk_profile)
SELECT 
    'User' || i,
    'Name' || i,
    'user' || i || '@example.com',
    20 + (i % 50),
    DATE '2020-01-01' + (i % 1000),
    CASE (i % 5)
        WHEN 0 THEN 'Lucknow'
        WHEN 1 THEN 'Delhi'
        WHEN 2 THEN 'Mumbai'
        WHEN 3 THEN 'Bangalore'
        ELSE 'Chennai'
    END,
    'India',
    CASE (i % 10)
        WHEN 0 THEN 'high'
        WHEN 1 THEN 'medium'
        ELSE 'low'
    END
FROM GENERATE_SERIES(1, 1000) AS i;

-- Insert sample merchants
INSERT INTO merchants (merchant_name, merchant_category, country, risk_rating)
SELECT 
    'Merchant' || i,
    CASE (i % 5)
        WHEN 0 THEN 'E-commerce'
        WHEN 1 THEN 'Retail'
        WHEN 2 THEN 'Food'
        WHEN 3 THEN 'Travel'
        ELSE 'Entertainment'
    END,
    'India',
    CASE (i % 10)
        WHEN 0 THEN 'high'
        WHEN 1 THEN 'medium'
        ELSE 'low'
    END
FROM GENERATE_SERIES(1, 100) AS i;
