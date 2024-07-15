ALTER TABLE filtered_ship_data ADD COLUMN illegal TEXT;

UPDATE filtered_ship_data
SET illegal = 'yes'
WHERE is_fishing > 0
AND EXISTS (
    SELECT 1
    FROM multipoint_mpa
    WHERE ST_Intersects(filtered_ship_data.geometry, multipoint_mpa.geometry)
    AND EXTRACT(YEAR FROM filtered_ship_data.timestamp) >= multipoint_mpa."STATUS_YR"
);


UPDATE filtered_ship_data
SET illegal = 'yes'
WHERE is_fishing > 0
AND EXISTS (
    SELECT 1
    FROM polygon_mpa
    WHERE ST_Intersects(filtered_ship_data.geometry, polygon_mpa.geometry)
    AND EXTRACT(YEAR FROM filtered_ship_data.timestamp) >= polygon_mpa."STATUS_YR"
);

UPDATE filtered_ship_data
SET illegal = 'no'
WHERE illegal IS NULL;

COPY filtered_ship_data TO 'D:\Datasets\Illegal Fishing\Processed Data\filtered_ship_data.csv' DELIMITER ',' CSV HEADER;


SELECT is_fishing, COUNT(*) AS count
FROM filtered_ship_data
GROUP BY is_fishing
ORDER BY is_fishing;
