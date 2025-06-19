import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib
import os

print("📥 Loading data...")

# Load your university dataset
if not os.path.exists("data/universities.csv"):
    print("❌ ERROR: universities.csv not found in data/ folder!")
    exit()

df = pd.read_csv("data/universities.csv")

# Encode categorical columns
le_field = LabelEncoder()
le_country = LabelEncoder()
le_university = LabelEncoder()

df['Field_encoded'] = le_field.fit_transform(df['Field'])
df['Country_encoded'] = le_country.fit_transform(df['Country'])
df['University_encoded'] = le_university.fit_transform(df['University'])

# Features and target
X = df[['Field_encoded', 'Min GPA', 'IELTS', 'Country_encoded']]
y = df['University_encoded']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
print("🤖 Training model...")
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Create model folder if not exists
if not os.path.exists("ml_model"):
    os.makedirs("ml_model")

# Save model and encoders
print("💾 Saving model and encoders...")
joblib.dump(model, "ml_model/model.pkl")
joblib.dump(le_field, "ml_model/le_field.pkl")
joblib.dump(le_country, "ml_model/le_country.pkl")
joblib.dump(le_university, "ml_model/le_university.pkl")

print("✅ Training complete. Model saved in 'ml_model/' folder.")
