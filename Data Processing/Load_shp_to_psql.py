import geopandas as gpd
from sqlalchemy import create_engine

# Database connection parameters
db_username = 'postgres'
db_password = ''
db_host = 'localhost'
db_port = '5432'
db_name = 'Vessel and Ocean data'

# Create a connection string
connection_string = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(connection_string)

# List of shapefiles and their target table names
shapefiles = [
    (rf'D:\Datasets\Illegal Fishing\Original Data\ne_110m_ocean\ne_110m_ocean.shp', 'ocean_boundaries'),
    (rf'D:\Datasets\Illegal Fishing\Processed Data\Filtered MPA data\filtered_points.shp', 'multipoint_mpa'),
    (rf'D:\Datasets\Illegal Fishing\Processed Data\Filtered MPA data\filtered_polygons.shp', 'polygon_mpa')
]

# Function to load shapefile into PostgreSQL with chunking
def load_shapefile_chunked(shapefile_path, table_name, chunk_size=1000):
    # Read the shapefile using GeoPandas
    gdf = gpd.read_file(shapefile_path)
    
    # Ensure the CRS is set to EPSG:4326
    gdf = gdf.to_crs(epsg=4326)
    
    # Initialize the table in PostgreSQL by writing the first chunk
    gdf.iloc[:chunk_size].to_postgis(table_name, engine, if_exists='replace')
    
    # Append the remaining chunks
    for start in range(chunk_size, len(gdf), chunk_size):
        end = start + chunk_size
        gdf.iloc[start:end].to_postgis(table_name, engine, if_exists='append')

# Load each shapefile with chunking
for shapefile_path, table_name in shapefiles:
    load_shapefile_chunked(shapefile_path, table_name)

print("Shapefiles loaded successfully.")

