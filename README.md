# GIST 604B – Python for GIS

Repository for working with tabular, vector, and raster GIS data using Python.

## Repository Structure

    .
    ├── README.md
    ├── .devcontainer
    │   ├── devcontainer.json
    │   ├── Dockerfile
    ├── data/
    │   ├── neighborhood_samples.geojson
    │   ├── temperature_readings.csv
    │   └── weather_stations.csv
    ├── notebooks/
    │   ├── pandas/
    │   ├── geopandas/
    │   └── rasterio/
    ├── src/
    │   ├── pandas_basics.py
    │   ├── geopandas_basics.py
    │   └── download_real_data.py
    ├── tests/
    │   ├── test_pandas_basics.py
    │   └── test_geopandas_basics.py
    ├── pyproject.toml
    └── uv.lock

## Notes

- Notebooks are for exploration and learning.
- Final implementations are in `src/`.
- Tests validate pandas and GeoPandas functionality.
- Rasterio work is completed entirely in the notebook.


## Key Takeaways

Learned how to utilize Python libraries Pandas, GeoPandas, and Rasterio for geospatial analysis.

### Pandas

- Loaded, explored, and filtered geographic data
- Calculated data quality statistics like data retention
- Joined DataFrames using `pd.merge`
- Performed comprehensive error handling

### GeoPandas

- Explored myriad functions for `gpd.GeoDataFrame`
- Downloaded, explored, and transformed geographic data
- Projected data for geometry analysis
- Determined spatial relationships and performed spatial joins
- Created maps and graphs

### Rasterio

- Performed remote sensing analysis on infrared data for vegetation quality
- Calculated and visualized NDVI for different regions
- Identified and isolated areas of greatest concern