# Automated Bank Reconciliation Dashboard

## 🎯 Project Overview

This project was developed to solve a critical operational bottleneck for the finance team at Advance Tech Lending Inc. The team was spending over **20 hours of manual effort each month** reconciling thousands of transactions between raw bank statements and our internal records. This manual process, performed in spreadsheets, was not only time-consuming but also prone to human error, posing a risk to financial accuracy.

The goal was to engineer a fully automated, reliable, and scalable solution that would eliminate this manual workload and provide the team with immediate, actionable insights.

---

## 💡 Solution

I designed and built an end-to-end ETL (Extract, Transform, Load) pipeline and an automated dashboard to solve this problem. The solution automates the entire reconciliation lifecycle:

1.  **Extract:** The pipeline begins by using SQL queries to automatically extract raw transaction data from our production databases.
2.  **Transform:** A Python script, running in a Databricks environment, then ingests and cleans the raw data. It performs the complex reconciliation logic, programmatically matching records and isolating any discrepancies or variances.
3.  **Load:** The final, processed insights are loaded into a user-friendly Tableau dashboard. This dashboard provides a clear, at-a-glance view of the reconciliation status and highlights the specific transactions that require manual investigation.

---

## 📊 Dashboard Showcase

The final dashboard provides a multi-layered view for the finance team, from a high-level summary down to the individual transaction details.

**1. High-Level Monthly Overview:** The main view tracks the total variance across all banks, allowing for a quick health check.
![Dashboard Overview](./dashboard-overview.png)

**2. Detailed Variance Analysis:** Users can then drill down into specific variances to understand the scale of the discrepancy for each bank.
![Variance Details](./variance-details.png)

**3. Transaction-Level Data:** Finally, a table view allows analysts to see the specific, individual transactions that have been flagged, making manual investigation fast and efficient.
![Data Table View](./data-table-view.png)

---

## ✨ Key Features & My Role

As the sole data scientist on this project, I was responsible for the entire development lifecycle. My key contributions include:

* **End-to-End ETL Pipeline Development:** Architected and built the full data pipeline from scratch.
* **Complex Transformation Logic:** Wrote the core Python and SQL scripts to handle the complex business rules for transaction matching and variance identification.
* **Automation & Scheduling:** Set up the pipeline to run on an automated schedule in Databricks, ensuring the finance team always has up-to-date information.
* **Stakeholder Collaboration:** Worked closely with the finance team to gather requirements, provide progress updates, and ensure the final dashboard met their exact needs.

---

## 🛠️ Tech Stack

* **Data Extraction & Querying:** `SQL`
* **Data Processing & Transformation:** `Python`, `Pandas`, `Databricks`
* **Data Visualization & Dashboarding:** `Tableau`
* **Version Control:** `Git`, `GitHub`

---

## 🚀 Quantified Impact & Results

This project transformed the finance team's workflow and delivered significant, measurable value:

* **✅ 90% Reduction in Manual Effort:** Reduced the monthly reconciliation time from **20 hours to under 2 hours**.
* **✅ 200+ Analyst Hours Saved Annually:** Freed up the finance team to focus on high-value strategic analysis instead of tedious data entry.
* **✅ Improved Financial Accuracy:** The tool's precision was proven immediately. In its first three months, it pinpointed **12 previously undetected discrepancies**, leading to the direct recovery of funds.

---

## 📂 Repository Structure

```
├── python_scripts/
│   └── reconciliation_logic.py
├── sql_queries/
│   └── extract_transactions.sql
└── README.md
```
