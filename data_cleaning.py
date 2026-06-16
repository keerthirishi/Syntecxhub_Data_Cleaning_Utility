import pandas as pd
df = pd.read_csv("sample_data.csv")
log = []
df.columns = df.columns.str.lower().str.replace(" ", "_")
log.append("Column names standardized.")
missing_before = df.isnull().sum().sum()
df["age"] = df["age"].fillna(df["age"].mean())
df["join_date"] = df["join_date"].fillna("2024-01-01")

log.append(f"Missing values handled: {missing_before}")
duplicates = df.duplicated().sum()
df = df.drop_duplicates()

log.append(f"Duplicates removed: {duplicates}")
df["join_date"] = pd.to_datetime(df["join_date"], errors="coerce")

log.append("Date column converted to datetime format.")
df.to_csv("cleaned_data.csv", index=False)
with open("cleaning_log.txt", "w") as file:
    for item in log:
        file.write(item + "\n")

print("Data cleaned successfully!")
print("cleaned_data.csv created")
print("cleaning_log.txt created")