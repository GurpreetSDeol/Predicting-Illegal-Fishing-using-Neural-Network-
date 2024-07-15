DROP TABLE IF EXISTS ship_data,ocean_boundaries, multipoint_mpa, polygon_mpa;
CREATE TABLE IF NOT EXISTS ship_data (
    mmsi FLOAT,
    timestamp TIMESTAMPTZ,
    distance_from_shore DOUBLE PRECISION,
    distance_from_port DOUBLE PRECISION,
    speed DOUBLE PRECISION,
    course DOUBLE PRECISION,
    lat DOUBLE PRECISION,
    lon DOUBLE PRECISION,
    is_fishing FLOAT,
    source TEXT,
    shiptype TEXT,
    geometry GEOMETRY(Point, 4326)
);

TRUNCATE ship_data;

COPY ship_data(mmsi, timestamp, distance_from_shore, distance_from_port, speed, course, lat, lon, is_fishing, source, shiptype)
FROM 'D:\Datasets\Illegal Fishing\Processed Data\Complete_ship_data.csv' DELIMITER ',' CSV HEADER;
UPDATE ship_data SET geometry = ST_SetSRID(ST_MakePoint(lon, lat), 4326);


CREATE TABLE ocean_boundaries (id SERIAL PRIMARY KEY, geom GEOMETRY(Polygon, 4326));
CREATE TABLE multipoint_mpa (id SERIAL PRIMARY KEY, geom GEOMETRY(MultiPoint, 4326));
CREATE TABLE polygon_mpa (id SERIAL PRIMARY KEY, geom GEOMETRY(Polygon, 4326));

