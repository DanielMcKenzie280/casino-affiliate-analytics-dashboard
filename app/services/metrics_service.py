from app.utils import safe_divide

def calculate_roi(revenue, cost):
    return safe_divide(revenue - cost, cost)

def calculate_ltv(avg_deposit, deposits_per_user):
    return avg_deposit * deposits_per_user

def calculate_conversion(clicks, signups):
    return safe_divide(signups, clicks)
