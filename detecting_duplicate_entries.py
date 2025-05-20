import pandas as pd
from fuzzywuzzy import fuzz

def get_customer_data():
    """
    Collects customer data from user input.
    Returns a DataFrame with Name and Email columns.
    """
    records = []
    print("Enter customer records (type 'done' to finish):")
    while True:
        name = input("Enter name: ")
        if name.lower() == 'done':
            break
        email = input("Enter email: ")
        if email.lower() == 'done':
            break
        records.append({'Name': name.strip(), 'Email': email.strip()})
    return pd.DataFrame(records)

def find_duplicates(df, threshold=90):
    """
    Compares each pair of records using fuzzy matching.
    Returns a list of duplicate pairs.
    """
    duplicates = []
    for i in range(len(df)):
        for j in range(i + 1, len(df)):
            name_score = fuzz.token_sort_ratio(df.loc[i, 'Name'], df.loc[j, 'Name'])
            email_score = fuzz.token_sort_ratio(df.loc[i, 'Email'], df.loc[j, 'Email'])

            if name_score >= threshold or email_score >= threshold:
                duplicates.append({
                    'Index1': i, 'Index2': j,
                    'Name1': df.loc[i, 'Name'],
                    'Name2': df.loc[j, 'Name'],
                    'Email1': df.loc[i, 'Email'],
                    'Email2': df.loc[j, 'Email'],
                    'Name_Similarity': name_score,
                    'Email_Similarity': email_score
                })
    return duplicates

def print_duplicates(duplicates):
    """
    Prints duplicate records in a readable format.
    """
    if not duplicates:
        print("\n✅ No duplicates found.")
        return
    print("\n🔍 Possible duplicate entries found:\n")
    for dup in duplicates:
        print(f"[{dup['Index1']}] {dup['Name1']} - {dup['Email1']}")
        print(f"[{dup['Index2']}] {dup['Name2']} - {dup['Email2']}")
        print(f"🔁 Name Similarity: {dup['Name_Similarity']} | Email Similarity: {dup['Email_Similarity']}\n")

def main():
    df = get_customer_data()
    if df.empty:
        print("No data provided. Exiting.")
        return

    try:
        threshold = int(input("Enter similarity threshold (e.g., 85-100): "))
    except ValueError:
        print("Invalid threshold. Using default of 90.")
        threshold = 90

    duplicates = find_duplicates(df, threshold=threshold)
    print_duplicates(duplicates)

if __name__ == "__main__":
    main()
