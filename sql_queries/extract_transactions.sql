-- ===================================================================================
-- SQL Query to Extract Loan Tape Data for Bank Reconciliation
--
-- Author: Keith [Your Last Name]
-- Purpose: This script extracts and aggregates loan payment data from our core
--          payments table. It prepares the "loan tape" side of the reconciliation
--          by calculating the total payment amount for each bank on a given day.
-- Note:    All database, schema, and table names have been sanitized for this
--          public portfolio.
-- ===================================================================================

-- Use a Common Table Expression (CTE) to select and filter the initial raw data.
-- This makes the query more readable and modular.
WITH raw_payments AS (
    SELECT
        company_payment_bank,
        actual_company_payment_date,
        payment_amount
    FROM
        -- SANITIZED: Replaced the specific production table name with a generic one.
        [PROD_DATABASE].[LOAN_PAYMENTS]
    WHERE
        -- Filter for relevant payment dates to keep the dataset manageable.
        -- In a production run, this date range would be parameterized.
        actual_company_payment_date >= '2023-07-01'
        AND payment_status = 'COMPLETED' -- Ensure we only pull successful payments
),

-- A second CTE to aggregate the data.
-- This separates the filtering logic from the aggregation logic.
aggregated_payments AS (
    SELECT
        -- Standardize bank names for consistent grouping.
        CASE
            WHEN company_payment_bank = 'Bank 1.' THEN 'Bank 1'
            WHEN company_payment_bank = 'Bank 2,' THEN 'Bank 2'
            WHEN company_payment_bank = 'Bank 3,' THEN 'Bank 3'
            WHEN company_payment_bank = 'Bank 4!' THEN 'Bank 4'
            ELSE 'Other'
        END AS bank_name,
        CAST(actual_company_payment_date AS DATE) AS payment_date,
        SUM(CAST(payment_amount AS DECIMAL(18, 2))) AS loan_tape_total
    FROM
        raw_payments
    GROUP BY
        bank_name,
        payment_date
)

-- Final SELECT statement to output the clean, aggregated data.
-- This is the data that would be ingested by the Python script for reconciliation.
SELECT
    payment_date,
    bank_name,
    loan_tape_total
FROM
    aggregated_payments
ORDER BY
    payment_date DESC,
    bank_name;
