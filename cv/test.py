

import pandas as pd

# Convert the data to pandas DataFrames
user_df = pd.DataFrame(user_data)
purchase_df = pd.DataFrame(purchase_data)
country_df = pd.DataFrame(country_data)
media_source_df = pd.DataFrame(media_source_data)
session_df = pd.DataFrame(session_data)

# Calculations
number_of_sessions = session_df['session_id'].nunique()
count_users_with_sessions = session_df['user_id'].nunique()
count_of_purchases = purchase_df['purchase_id'].nunique()
total_purchase_revenue = purchase_df['purchase_revenue'].sum()
revenue_per_purchase = total_purchase_revenue / count_of_purchases
purchasing_users = purchase_df['user_id'].nunique()
revenue_per_purchasing_user = total_purchase_revenue / purchasing_users
sessions_with_purchases = purchase_df['purchase_session_id'].nunique()
count_of_new_users = user_df['user_id'].nunique()

# Results
print("Number of sessions:", number_of_sessions)
print("Count of users with sessions:", count_users_with_sessions)
print("Count of purchases:", count_of_purchases)
print("Total purchase revenue:", total_purchase_revenue)
print("Revenue per purchase:", revenue_per_purchase)
print("Revenue per purchasing user:", revenue_per_purchasing_user)
print("Count of sessions with purchases:", sessions_with_purchases)
print("Total count of new users:", count_of_new_users)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Bar plot for purchase revenue by country
merged_df = pd.merge(purchase_df, user_df, on="user_id")
merged_df = pd.merge(merged_df, country_df, left_on="user_country_id", right_on="Country_id")
country_revenues = merged_df.groupby("country_name")["purchase_revenue"].sum()

plt.figure(figsize=(12, 6))
sns.barplot(x=country_revenues.index, y=country_revenues.values)
plt.title("Total Purchase Revenue by Country")
plt.ylabel("Total Revenue")
plt.xlabel("Country")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Histogram for distribution of purchase revenues
plt.figure(figsize=(12, 6))
sns.histplot(purchase_df['purchase_revenue'], bins=50, kde=True)
plt.title("Distribution of Purchase Revenues")
plt.xlabel("Purchase Revenue")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# 3. Line chart for number of purchases over time
purchase_df['purchase_datetime'] = pd.to_datetime(purchase_df['purchase_datetime'])
purchases_over_time = purchase_df.groupby(purchase_df['purchase_datetime'].dt.date).size()

plt.figure(figsize=(12, 6))
sns.lineplot(x=purchases_over_time.index, y=purchases_over_time.values)
plt.title("Number of Purchases Over Time")
plt.ylabel("Number of Purchases")
plt.xlabel("Date")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 4. Scatterplot for session counts vs. purchase counts for each user
session_counts = session_df.groupby("user_id").size()
purchase_counts = purchase_df.groupby("user_id").size()

# Merge both series into a DataFrame for visualization
scatter_data = pd.merge(session_counts, purchase_counts, on="user_id", how="outer").fillna(0)
scatter_data.columns = ['session_count', 'purchase_count']

plt.figure(figsize=(12, 6))
sns.scatterplot(data=scatter_data, x='session_count', y='purchase_count')
plt.title("Session Counts vs. Purchase Counts for Users")
plt.xlabel("Number of Sessions")
plt.ylabel("Number of Purchases")
plt.tight_layout()
plt.show()

# 5. Box plot for distribution of purchase revenues by country
plt.figure(figsize=(12, 6))
sns.boxplot(data=merged_df, x="country_name", y="purchase_revenue")
plt.title("Distribution of Purchase Revenues by Country")
plt.xlabel("Country")
plt.ylabel("Purchase Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


