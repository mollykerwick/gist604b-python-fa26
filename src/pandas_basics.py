"""
Pandas Basics for GIS Data Analysis - Student Implementation

Complete the four functions in this file.
Use the notebooks to learn and test each function.

📋 FUNCTIONS TO IMPLEMENT IN THIS FILE:
=====================================
✅ Function 1: load_and_explore_gis_data()     → notebooks/01_function_...
✅ Function 2: filter_environmental_data()     → notebooks/02_function_...
✅ Function 3: calculate_station_statistics()  → notebooks/03_function_...
✅ Function 4: join_station_data()             → notebooks/04_function_...
"""

import pandas as pd
from pathlib import Path
import os


# =============================================================================
# FUNCTION 1: LOAD AND EXPLORE GIS DATA
# =============================================================================

def load_and_explore_gis_data(file_path):
    """
    Load a CSV file and display comprehensive information about the dataset.
    
    This function demonstrates the first step in any data analysis project:
    understanding your data through exploration.
    
    Args:
        file_path (str): Path to the CSV file to load
        
    Returns:
        pandas.DataFrame: The loaded dataset, or None if loading failed
    
    Example:
        >>> stations_df = load_and_explore_gis_data('data/weather_stations.csv')
        Loading data from: data/weather_stations.csv
        Dataset shape: (150, 6) - That's 150 rows and 6 columns!
        ...
    """
    print("=" * 50)
    print("LOADING AND EXPLORING GIS DATA")
    print("=" * 50)

    if not os.path.exists(file_path):
        print(f"❌ ERROR: File not found: {file_path}")
        print("Please check:")
        print("- Is the file path correct?")
        print("- Are you in the right directory?")
        print("- Does the file exist?")
        return None
    
    print(f"📁 Loading data from: {file_path}")

    try:
        df = pd.read_csv(file_path)
        print("✅ File loaded successfully!")
    except Exception as e:
        print(f"❌ ERROR loading file: {e}")
        return None
    
    print(f"\n📊 DATASET OVERVIEW")
    print(f"Dataset shape: {df.shape} - That's {df.shape[0]} rows and {df.shape[1]} columns!")
    
    print(f"Columns: {list(df.columns)}")
    
    print(f"\n👀 FIRST 5 ROWS:")
    print(df.head())
    
    print(f"\n📈 SUMMARY STATISTICS:")
    print(df.describe())
    
    print(f"\n🔍 DATA QUALITY CHECK:")
    missing = df.isnull().sum()
    if missing.sum() > 0:
        print("Missing values found:")
        print(missing[missing > 0])
    else:
        print("✅ No missing values")
    
    print(f"\n🎉 Data exploration complete! Dataset is ready for analysis.")
    
    return df

# =============================================================================
# FUNCTION 2: FILTER ENVIRONMENTAL DATA
# =============================================================================

def filter_environmental_data(df, min_temp=15, max_temp=30, quality="good"):
    """
    Filter environmental data based on temperature range and data quality.
    
    This function demonstrates how to apply multiple filtering conditions
    to clean and prepare environmental data for analysis.
    
    Args:
        df (pandas.DataFrame): Environmental data with temperature and quality columns
        min_temp (float): Minimum acceptable temperature in Celsius (default: 15)
        max_temp (float): Maximum acceptable temperature in Celsius (default: 30)
        quality (str): Required data quality level (default: "good")
        
    Returns:
        pandas.DataFrame: Filtered data meeting all specified conditions
    
    Example:
        >>> filtered_df = filter_environmental_data(readings_df, min_temp=20, max_temp=30, quality='good')
        Original data: 1000 rows
        After filtering: 247 rows (24.7% of data retained)
        Filters applied:
          - Temperature: 20.0°C to 30.0°C
          - Data quality: good
    """
    
    print("=" * 50)
    print("FILTERING ENVIRONMENTAL DATA")
    print("=" * 50)

    # Input validation
    if df is None or df.empty:
        print("❌ ERROR: Empty or None DataFrame provided")
        return pd.DataFrame()

    # Check for required columns
    required_columns = ['temperature_c', 'data_quality']
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        print(f"❌ ERROR: Missing required columns: {missing_columns}")
        print(f"📋 Available columns: {list(df.columns)}")
        return pd.DataFrame()
        
    initial_len = len(df)
    print("UNFILTERED DATAFRAME INFO")
    print("Shape of DataFrame:", df.shape)
    print("\tNumber of rows =", initial_len)

    # Temperature range filter
    mask = (df['temperature_c'] >= min_temp) & (df['temperature_c'] <= max_temp)
    filtered_df = df[mask]
    
    # Quality filter
    filtered_df = filtered_df[filtered_df['data_quality'] == quality]
    
    if not filtered_df.empty:
        print(f"\n📊 FILTERED DATA SUMMARY:")
        print(f"   Temperature range: {filtered_df['temperature_c'].min():.1f}°C to {filtered_df['temperature_c'].max():.1f}°C")
        print(f"   Average temperature: {filtered_df['temperature_c'].mean():.1f}°C")
        print(f"   Quality distribution: {dict(filtered_df['data_quality'].value_counts())}")
        print(f"\n📊 FILTERING STATISTICS:")
        new_len = len(filtered_df)
        print(f"   {new_len} rows remain after filtering")
        print(f"   {100*(new_len / float(initial_len))}% of rows remain after filtering")
        print(f"   Filter criteria used: quality ==", quality)
    else:
        print(f"\n⚠️  WARNING: No data remains after filtering!")
        print(f"   Consider relaxing your filtering criteria.")
    
    print(f"\n✅ Filtering complete! Ready for analysis.")
    
    return filtered_df


# =============================================================================
# FUNCTION 3: CALCULATE STATION STATISTICS
# =============================================================================

def calculate_station_statistics(df):
    """
    Calculate station statistics
    
    This function groups temperature readings by weather station and calculates
    summary statistics (average temperature, number of readings, etc.) for each
    station.
    
    Args:
        df (pandas.DataFrame): Environmental readings data with 'station_id', 'temperature_c' and 'humidity_percent' columns
    
    Returns:
        pandas.DataFrame: Statistics for each station with columns:
            - station_id: The weather station identifier
            - avg_temperature: Average temperature for this station
            - avg_humidity: Average humidity for this station
            - reading_count: Number of readings from this station
    
    Example:
        >>> stats_df = calculate_station_statistics(readings_df)
        Calculating statistics for 5 unique stations...
        Statistics calculated:
          - Total readings analyzed: 1000
          - Stations with data: 5
          - Average readings per station: 200.0
    """
    
    # Print header
    print("=" * 50)
    print("CALCULATING STATION STATISTICS")
    print("=" * 50)

    # Input validation
    if df is None or len(df) == 0:
        print("❌ ERROR: DataFrame is empty or None")
        return pd.DataFrame()
    
    # Check for required columns
    required_columns = ['station_id', 'temperature_c', 'humidity_percent']
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        print(f"❌ ERROR: Missing required columns: {missing_columns}")
        print(f"Available columns: {list(df.columns)}")
        return pd.DataFrame()

    n_stations = df['station_id'].nunique()
    print("Unique stations:", n_stations)
    
    df_grouped = df.groupby('station_id')
    
    # Calculate statistics
    avg_temperature = df_grouped['temperature_c'].mean().round(1)
    avg_humidity = df_grouped['humidity_percent'].mean().round(1)
    reading_count = df_grouped.size()
    
    # Create summary DataFrame
    df_summary = pd.DataFrame({
        'station_id': avg_temperature.index,
        'avg_temperature': avg_temperature.values,
        'avg_humidity': avg_humidity.values,
        'reading_count': reading_count.values
    })
    
    df_summary = df_summary.reset_index()
    
    print("\n📊 SUMMARY STATISTICS")
    print(f"\n\tTotal readings analyzed: {df_summary['reading_count'].sum()}")
    print(f"\n\tNumber of stations: {n_stations}")
    print(f"\n\tAverage readings per station: {df_summary['reading_count']}")
    
    return df_summary


# =============================================================================
# FUNCTION 4: JOIN STATION DATA
# =============================================================================

def join_station_data(stations_df, readings_df):
    """
    Join sensor readings with station metadata
    
    This function joins station information (name, location) with temperature readings.
    You'll add station details (like station name and coordinates) to each temperature reading.
    
    Args:
        stations_df (pandas.DataFrame): Station information with 'station_id', 'station_name', 
                                       'latitude', 'longitude', etc.
        readings_df (pandas.DataFrame): Temperature readings with 'station_id', 'date', 
                                       'temperature_c', etc.
    
    Returns:
        pandas.DataFrame: Combined dataset with readings AND station information
    
    Example:
        >>> joined_df = join_station_data(stations_df, readings_df)
        Joining station information with readings...
        Stations table: 5 stations
        Readings table: 1000 readings
        Joined table: 1000 rows with station details added!
    """
    
    # TODO: Print a header
    # TODO: Use print("=" * 50) and print("JOINING STATION DATA")
    
    # TODO: Print the shapes of both input DataFrames
    # TODO: Show how many stations and how many readings
    
    # TODO: Join the DataFrames using pd.merge()
    # TODO: Use the 'station_id' column as the key
    # TODO: Use how='left' to keep all readings even if station info is missing
    
    # TODO: Print the shape of the joined DataFrame
    # TODO: Verify all readings are still present
    
    # TODO: Print the new columns that were added
    # TODO: Show which columns came from the stations table
    
    # TODO: Return the joined DataFrame
    
    pass  # Remove this line when you implement the function


# =============================================================================
# HELPER FUNCTIONS (You don't need to modify these - they're provided!)
# =============================================================================

def _check_required_columns(df, required_columns, data_name="DataFrame"):
    """
    Helper function to check if required columns exist in a DataFrame.
    
    Args:
        df (pandas.DataFrame): DataFrame to check
        required_columns (list): List of required column names
        data_name (str): Name to use in error messages
    
    Returns:
        tuple: (bool, list) - (all_present, missing_columns)
    """
    if df is None or df.empty:
        return False, required_columns
    
    missing = [col for col in required_columns if col not in df.columns]
    return len(missing) == 0, missing


def _format_number(value, decimals=1):
    """
    Helper function to format numbers for display.
    
    Args:
        value: Number to format
        decimals (int): Number of decimal places
    
    Returns:
        str: Formatted number
    """
    try:
        return f"{float(value):.{decimals}f}"
    except (ValueError, TypeError):
        return str(value)
