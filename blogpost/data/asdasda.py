import pandas as pd

# Read the TSV file
df = pd.read_csv('blogpost\data\words.tsv', sep='\t')

print("\n=== Column Summary ===")
print(f"Total columns: {len(df.columns)}")
print("Column names:", df.columns.tolist())
print("\n=== Counts (Non-empty entries) ===")
print(df.count())
    
print("\n=== Sums (Numeric columns only) ===")
# Select only numeric columns and show sums
numeric_df = df.select_dtypes(include=['number'])
if not numeric_df.empty:
    print(numeric_df.sum())
else:
    print("No numeric columns found")
# For word frequency analysis (if needed)
# print(df['column_name'].value_counts())