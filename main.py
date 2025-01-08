import geopandas as gpd
from shapely.geometry import Point

# Load GADM GeoPackage data
gadm_data = gpd.read_file("gadm_410.gpkg", layer="gadm_410")

# Optional: Simplify geometry data to improve performance
gadm_data['geometry'] = gadm_data['geometry'].simplify(tolerance=0.01)

# Create spatial index
spatial_index = gadm_data.sindex

lat = 39.9042
lon = 116.4074

point = Point(lat, lon)    # China, Beijing

# Use spatial index to quickly find candidate polygons
possible_matches_index = list(spatial_index.intersection(point.bounds))
possible_matches = gadm_data.iloc[possible_matches_index]

# Precisely check if the point is within a polygon
found = False
for _, region in possible_matches.iterrows():
    if point.within(region['geometry']):
        print(f"Point ({lat}, {lon}) is within the region: {region['NAME_0']}")
        found = True
        break
if not found:
    print(f"Point ({lat}, {lon}) does not correspond to any region")
