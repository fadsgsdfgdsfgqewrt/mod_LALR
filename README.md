# Latitude and Longitude Recognition Module

English | [简体中文](./README_zh.md)

This project uses the **GADM (Geographical Administrative Boundaries Database)** to identify the country or region based on latitude and longitude coordinates. The GADM database defines 400,276 administrative areas.

## GADM Database

- **Current Version**: 4.1
- **Number of Administrative Regions**: 400,276
- **Download URL**: [https://geodata.ucdavis.edu/gadm/gadm4.1/gadm_410-gpkg.zip](https://geodata.ucdavis.edu/gadm/gadm4.1/gadm_410-gpkg.zip)

---

## How to Use

### 1. Download Database

Ensure that the GADM database has been downloaded and decompressed to the project root directory<br>
https://geodata.ucdavis.edu/gadm/gadm4.1/gadm_410-gpkg.zip

### 2. Install Dependencies

Ensure the following Python packages are installed:

```bash
pip install geopandas shapely pandas
```

### 3. Run the Script

To process the input Excel file, run the following command:

```bash
python process_excel.py <input_excel_file>
```

Where `<input_excel_file>` is the path to your Excel file containing the latitude and longitude columns (`high_conf_lat` and `high_conf_lon`). The program will output a new Excel file with an additional column indicating the identified region.

---


