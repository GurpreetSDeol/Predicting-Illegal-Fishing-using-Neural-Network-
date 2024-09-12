-- Add the 'illegal' column to the ship_data table
ALTER TABLE ship_data ADD COLUMN illegal TEXT;

-- Update 'illegal' column to 'yes' if conditions are met
UPDATE ship_data
SET illegal = 'yes'
WHERE is_fishing > 0
AND EXISTS (
    SELECT 1
    FROM multipoint_mpa
    WHERE ST_Intersects(ship_data.geometry, multipoint_mpa.geom)
    AND EXTRACT(YEAR FROM ship_data.timestamp) >= multipoint_mpa.status_yr
);

UPDATE ship_data
SET illegal = 'yes'
WHERE is_fishing > 0
AND EXISTS (
    SELECT 1
    FROM polygon_mpa
    WHERE ST_Intersects(ship_data.geometry, polygon_mpa.geom)
    AND EXTRACT(YEAR FROM ship_data.timestamp) >= polygon_mpa.status_yr
);

-- Update 'illegal' column to 'maybe' for rows where is_fishing = 0 and intersection is present
UPDATE ship_data
SET illegal = 'maybe'
WHERE is_fishing = 0
AND illegal IS NULL
AND EXISTS (
    SELECT 1
    FROM multipoint_mpa
    WHERE ST_Intersects(ship_data.geometry, multipoint_mpa.geom)
    AND EXTRACT(YEAR FROM ship_data.timestamp) >= multipoint_mpa.status_yr
);

UPDATE ship_data
SET illegal = 'maybe'
WHERE is_fishing = 0
AND illegal IS NULL
AND EXISTS (
    SELECT 1
    FROM polygon_mpa
    WHERE ST_Intersects(ship_data.geometry, polygon_mpa.geom)
    AND EXTRACT(YEAR FROM ship_data.timestamp) >= polygon_mpa.status_yr
);

-- Set 'illegal' to 'no' where it is NULL
UPDATE ship_data
SET illegal = 'no'
WHERE illegal IS NULL;

-- Export the updated table to a CSV file
COPY ship_data TO 'D:\Datasets\Illegal Fishing\Processed Data\filtered_ship_data.csv' DELIMITER ',' CSV HEADER;

-- Check the counts of illegal, maybe, and legal fishing activities
SELECT illegal, COUNT(*) AS count
FROM ship_data
GROUP BY illegal
ORDER BY illegal;
