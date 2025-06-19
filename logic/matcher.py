# logic/matcher.py

def preprocess_input(gpa, ielts, major, country):
    # Basic encoding logic – match with training encoding
    field_map = {
        'Computer Science': 0,
        'Engineering': 1,
        'Data Science': 2,
        'Business': 3,
        # Add more as needed
    }

    country_map = {
        'USA': 0,
        'Canada': 1,
        'Switzerland': 2,
        'Australia': 3,
        'UK': 4,
        # Add more as needed
    }

    field_encoded = field_map.get(major, -1)
    country_encoded = country_map.get(country, -1)

    return [gpa, ielts, field_encoded, country_encoded]
