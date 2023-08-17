## Property Analysis in Yogyakarta

This project focuses on the analysis of property listings in Yogyakarta. The primary dataset consists of property details such as title, location, price, bedrooms, bathrooms, features, and URL.

### Objectives:
1. **Data Cleansing**: Clean the raw data to produce a structured and usable dataset.
2. **Data Analysis**: Analyze properties based on price, location (`Kabupaten` and `Kapanewon`), and type (house, land, rent room).
3. **Data Visualization**: Visualize the distribution of properties across `Kabupaten` using a map.

### Steps:

1. **Data Loading and Cleansing**:
    - Loaded raw property data.
    - Converted all strings to lowercase.
    - Extracted and cleaned prices, removing currency symbols and converting text numbers to integers.
    - Split the location data into street, kapanewon, kabupaten, and province.
    - Removed duplicates.

2. **Data Analytics**:
    - Calculated the number of properties based on `Kabupaten` and `Kapanewon`.
    - Determined the highest and lowest-priced properties in each `Kabupaten`.
    - Tagged properties based on their type (house, land, rent room).

3. **Data Visualization**:
    - Visualized the distribution of properties across `Kabupaten` using a map with dynamic circles to represent the number of properties.
    - Clustered properties based on their count within specific regions.

### Libraries and Tools Used:
- **Python**: The primary programming language used for data manipulation and analysis.
- **Pandas**: Used for data manipulation and analysis.
- **Folium**: Used for creating interactive maps.
- **Nominatim from Geopy**: Used for geocoding locations to get their coordinates.

### Results:
- **Sleman** has the highest average property price, followed by **Gunung Kidul** and **Yogyakarta**.
- There are 737 properties tagged as "land", 668 as "house", and 28 as "rent room".

### Notes:
- Some prices, especially very low ones, seem quite unusual and might indicate potential data errors or outliers.
- The coordinates for the `Kabupaten` were manually specified due to limitations with the geocoding service.

### Future Work:
- Analyze additional features such as the size of properties (in square meters) and correlate it with prices.
- Integrate with a more robust geocoding service to automatically fetch coordinates for locations.
- Dive deeper into anomaly detection to identify and handle outliers in the dataset.