import geopandas as gpd
from shapely.geometry import Point
import pandas as pd
import argparse

# Create command line argument parser
parser = argparse.ArgumentParser(description='Process an Excel file and determine the region of the given latitude and longitude')
parser.add_argument('input_excel', help='Path to the input Excel file')

# Parse command line arguments
args = parser.parse_args()

# Load GADM GeoPackage data
gadm_data = gpd.read_file("gadm_410.gpkg", layer="gadm_410")

# Optional: Simplify geometry data to improve performance
gadm_data['geometry'] = gadm_data['geometry'].simplify(tolerance=0.01)

# Create spatial index
spatial_index = gadm_data.sindex

# Read the provided Excel file
df = pd.read_excel(args.input_excel)

# Function to determine the region for a given latitude and longitude
def get_region(lat, lon):
    point = Point(lon, lat)
    
    # Use spatial index to quickly find candidate polygons
    possible_matches_index = list(spatial_index.intersection(point.bounds))
    possible_matches = gadm_data.iloc[possible_matches_index]
    
    # Precisely check if the point is within a polygon
    for _, region in possible_matches.iterrows():
        if point.within(region['geometry']):
            return region['NAME_0']  # Return region name
    return None  # Return None if no region is found

# Process each row and determine the region for `high_conf_lat` and `high_conf_lon`
df['Identified regions'] = df.apply(lambda row: get_region(row['high_conf_lat'], row['high_conf_lon']), axis=1)

# Write the result to a new Excel file
output_excel_file = f"output/{args.input_excel.split('/')[-1].split('.')[0]}-with-region.xlsx"
df.to_excel(output_excel_file, index=False)

print(f"Data has been processed and saved to {output_excel_file}")
