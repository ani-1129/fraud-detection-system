"""
DateTime Utilities for Time Range Filtering and Calculations
"""
from datetime import datetime, timedelta
import pandas as pd

def get_date_range(start_date=None, end_date=None, days=30):
    """
    Get date range for filtering
    
    Args:
        start_date: Start date (datetime)
        end_date: End date (datetime)
        days: Number of days if start_date not provided
    
    Returns:
        tuple: (start_date, end_date)
    """
    if end_date is None:
        end_date = datetime.now()
    
    if start_date is None:
        start_date = end_date - timedelta(days=days)
    
    return start_date, end_date

def calculate_time_since(timestamp):
    """
    Calculate time since a given timestamp
    
    Args:
        timestamp: datetime object
    
    Returns:
        timedelta: Time difference
    """
    return datetime.now() - timestamp

def format_timestamp(timestamp, format_str="%Y-%m-%d %H:%M:%S"):
    """
    Format timestamp to string
    
    Args:
        timestamp: datetime object
        format_str: Format string
    
    Returns:
        str: Formatted timestamp
    """
    return timestamp.strftime(format_str)

def extract_date_features(timestamp):
    """
    Extract date features from timestamp
    
    Args:
        timestamp: datetime object
    
    Returns:
        dict: Date features
    """
    return {
        'year': timestamp.year,
        'month': timestamp.month,
        'day': timestamp.day,
        'hour': timestamp.hour,
        'minute': timestamp.minute,
        'day_of_week': timestamp.weekday(),
        'is_weekend': timestamp.weekday() >= 5,
        'is_month_start': timestamp.day == 1,
        'is_month_end': timestamp.day == 28
    }

def group_by_time_period(timestamps, period='day'):
    """
    Group timestamps by time period
    
    Args:
        timestamps: List of datetime objects
        period: 'day', 'hour', 'week', 'month'
    
    Returns:
        dict: Grouped timestamps
    """
    grouped = {}
    
    for ts in timestamps:
        if period == 'day':
            key = ts.strftime('%Y-%m-%d')
        elif period == 'hour':
            key = ts.strftime('%Y-%m-%d %H')
        elif period == 'week':
            key = ts.strftime('%Y-%W')
        elif period == 'month':
            key = ts.strftime('%Y-%m')
        else:
            key = ts.strftime('%Y-%m-%d')
        
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(ts)
    
    return grouped
