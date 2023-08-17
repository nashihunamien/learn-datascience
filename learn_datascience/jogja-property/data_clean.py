import pandas as pd

def clean_data(input_file, output_file):
    print("Converting to lowercase...")
    # Load the CSV file into a DataFrame
    df_dirty = pd.read_csv(input_file)

    # Convert all string columns to lowercase
    df_dirty['Title'] = df_dirty['Title'].str.lower()
    df_dirty['Location'] = df_dirty['Location'].str.lower()
    df_dirty['Features'] = df_dirty['Features'].str.lower()
    df_dirty['URL'] = df_dirty['URL'].str.lower()

    print("Removing and adjusting quotes...")
    # Remove any existing quotes from string columns
    def remove_quotes(s):
        return s.strip('"')

    df_dirty['Title'] = df_dirty['Title'].apply(remove_quotes)
    df_dirty['Location'] = df_dirty['Location'].apply(remove_quotes)
    df_dirty['URL'] = df_dirty['URL'].apply(remove_quotes)

    print("Extracting and cleaning prices...")
    # Clean the "Price" column
    def convert_price(price):
        # Remove the "Rp" prefix
        price = price.replace("Rp", "").strip()
        
        # Convert values with "jt" to millions, "M" to billions, and "rb" to thousands
        if "jt" in price:
            price = price.replace("jt", "").replace(",", ".").strip()
            price = float(price) * 1e6
        elif "M" in price:
            price = price.replace("M", "").replace(",", ".").strip()
            price = float(price) * 1e9
        elif "rb" in price:
            price = price.replace("rb", "").replace(",", ".").strip()
            price = float(price) * 1e3
        return int(price)

    df_dirty['Price'] = df_dirty['Price'].apply(convert_price)

    print("Cleaning URLs...")
    # Clean the "URL" column by removing any repeated base URLs
    df_dirty['URL'] = df_dirty['URL'].str.replace("https://www.rumah.comhttps://www.rumah.com", "https://www.rumah.com")

    print("Saving cleaned data...")
    # Save the cleansed data to the output file
    df_dirty.to_csv(output_file, index=False, quoting=1)

    print("Done!")

clean_data('data_dirty.csv', 'data_cleaned.csv')
