# reconciliation_logic.py

import pandas as pd
import numpy as np
import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# ---
# NOTE TO REVIEWER:
# This script contains the core logic for an automated bank reconciliation pipeline.
# The original script ran in a Databricks environment and pulled data from internal
# databases and Google Sheets. All sensitive paths, table names, and credential
# information have been replaced with generic placeholders for this public portfolio.
# ---


def connect_to_gspread():
    """
    Establishes a connection to the Google Sheets API.
    In a real environment, the credentials file would be securely managed.
    """
    try:
        scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive"]
        # SANITIZED: Replaced specific file path with a generic placeholder.
        creds_path = 'path/to/your/google_credentials.json'
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
        gc = gspread.authorize(creds)
        return gc
    except Exception as e:
        print(f"Error connecting to Google Sheets: {e}")
        return None

def fetch_bank_statements_from_gsheet(gc):
    """
    Fetches and cleans bank statement data from different tabs in a Google Sheet.
    """
    try:
        # SANITIZED: Replaced specific Google Sheet name with a generic placeholder.
        gsheet = gc.open('[Placeholder] Bank Transaction History')

        # Fetch and clean BDO statements
        bdo_ws = gsheet.worksheet('BDO')
        bdo_df = pd.DataFrame(bdo_ws.get_all_values())
        bdo_df = clean_bank_dataframe(bdo_df, header_row=5)

        # Fetch and clean BPI statements
        bpi_ws = gsheet.worksheet('BPI')
        bpi_df = pd.DataFrame(bpi_ws.get_all_values())
        bpi_df = clean_bank_dataframe(bpi_df, header_row=5)

        # Fetch and clean Unionbank statements
        ub_ws = gsheet.worksheet('UB')
        ub_df = pd.DataFrame(ub_ws.get_all_values())
        ub_df = clean_bank_dataframe(ub_df, header_row=4)

        # Fetch and clean Netbank statements
        netbank_ws = gsheet.worksheet('Netbank')
        netbank_df = pd.DataFrame(netbank_ws.get_all_values())
        netbank_df = clean_bank_dataframe(netbank_df, header_row=4)

        return {
            'BDO': bdo_df,
            'BPI': bpi_df,
            'Unionbank': ub_df,
            'Netbank': netbank_df
        }
    except Exception as e:
        print(f"Error fetching bank statements: {e}")
        return None

def clean_bank_dataframe(df, header_row):
    """
    A helper function to apply initial cleaning steps to raw dataframes from Google Sheets.
    """
    df = df.drop(df.columns[0], axis=1)
    df = df.drop(index=range(0, header_row))
    df = df.reset_index(drop=True)
    df = df.set_axis(df.iloc[0], axis='columns').iloc[1:].reset_index(drop=True)
    return df

def fetch_loan_tapes_from_databricks():
    """
    Fetches loan tape data. In the original environment, this was a Spark SQL query.
    For this portfolio version, we simulate this by loading a sample CSV.
    """
    # SANITIZED: Replaced Spark SQL query with a local CSV load for demonstration.
    # Original query: spark.sql('select * from [DATABASE].[TABLE_NAME]').toPandas()
    try:
        # In a real portfolio, you would provide a sample, anonymized CSV here.
        loan_tapes_df = pd.read_csv('sample_data/anonymized_loan_tapes.csv')
        
        # Data processing steps from the original notebook
        loan_tapes_df['yr-mon'] = pd.to_datetime(loan_tapes_df['actual_company_payment_date']).dt.strftime('%Y-%m')
        loan_tapes_df = loan_tapes_df[loan_tapes_df['yr-mon'] > '2023-06']
        return loan_tapes_df
    except FileNotFoundError:
        print("Error: 'sample_data/anonymized_loan_tapes.csv' not found. Please create a sample CSV for this script to run.")
        return None

def perform_reconciliation(loan_tapes, bank_statements_map, year, month):
    """
    Core reconciliation logic to compare loan tapes against bank statements for a given month and year.
    """
    # This function would contain the detailed logic from your 'aggregate_function'.
    # It would iterate through each bank, filter the data for the specified year/month,
    # sum the credit amounts, compare against the loan tape totals, and calculate the variance.

    print(f"--- Reconciliation for {year}-{month:02d} ---")
    
    # Placeholder for the detailed reconciliation logic.
    # This is where you would implement the main loop from your notebook.
    # The logic would:
    # 1. Map bank names to their respective dataframes and column names.
    # 2. Clean and format the 'Credit' columns to be numeric.
    # 3. Filter both bank statements and loan tapes for the target month and year.
    # 4. Sum the totals for each source.
    # 5. Calculate the variance and variance percentage.
    # 6. Return a summary DataFrame.

    # Example of what the final output DataFrame would look like:
    summary_data = {
        'year': [year] * 4,
        'month': [month] * 4,
        'bank': ['Unionbank', 'BDO', 'BPI', 'Netbank'],
        'bank_statement_total': [np.random.randint(10e6, 20e6) for _ in range(4)], # Using random data for demo
        'loan_tape_total': [np.random.randint(10e6, 20e6) for _ in range(4)],
    }
    summary_df = pd.DataFrame(summary_data)
    summary_df['variance'] = summary_df['loan_tape_total'] - summary_df['bank_statement_total']
    summary_df['variance_percent'] = (summary_df['variance'] / summary_df['bank_statement_total']) * 100
    
    return summary_df


if __name__ == '__main__':
    # --- Main execution block ---
    
    # 1. Connect to Google Sheets
    gspread_client = connect_to_gspread()
    
    if gspread_client:
        # 2. Fetch and clean bank statements
        bank_statements = fetch_bank_statements_from_gsheet(gspread_client)

        # 3. Fetch loan tapes
        loan_tapes = fetch_loan_tapes_from_databricks()
        
        if bank_statements is not None and loan_tapes is not None:
            # 4. Run reconciliation for a specific month
            # (In a real pipeline, this would loop through a date range)
            target_year = 2024
            target_month = 10
            
            final_report = perform_reconciliation(loan_tapes, bank_statements, target_year, target_month)
            
            print("\nReconciliation Summary Report:")
            print(final_report)
