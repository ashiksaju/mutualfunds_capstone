# Data Dictionary

## 01_fund_master.csv

| Column            | Data Type | Description                   |
| ----------------- | --------- | ----------------------------- |
| amfi_code         | Integer   | Unique AMFI scheme identifier |
| fund_house        | Text      | Mutual fund company           |
| scheme_name       | Text      | Scheme name                   |
| category          | Text      | Fund category                 |
| sub_category      | Text      | Fund sub-category             |
| plan              | Text      | Regular or Direct             |
| launch_date       | Date      | Scheme launch date            |
| benchmark         | Text      | Benchmark index               |
| expense_ratio_pct | Decimal   | Expense ratio percentage      |
| risk_category     | Text      | Risk classification           |

---

## 02_nav_history.csv

| Column    | Data Type | Description     |
| --------- | --------- | --------------- |
| amfi_code | Integer   | Fund identifier |
| date      | Date      | NAV date        |
| nav       | Decimal   | Net Asset Value |

---

## 03_aum_by_fund_house.csv

| Column         | Data Type | Description       |
| -------------- | --------- | ----------------- |
| date           | Date      | Reporting date    |
| fund_house     | Text      | Fund house        |
| aum_lakh_crore | Decimal   | AUM in lakh crore |
| aum_crore      | Decimal   | AUM in crore      |
| num_schemes    | Integer   | Number of schemes |

---

## 08_investor_transactions.csv

| Column           | Data Type | Description              |
| ---------------- | --------- | ------------------------ |
| investor_id      | Text      | Investor ID              |
| transaction_date | Date      | Transaction date         |
| amfi_code        | Integer   | Fund code                |
| transaction_type | Text      | SIP, Lumpsum, Redemption |
| amount_inr       | Decimal   | Transaction amount       |
| state            | Text      | Investor state           |
| city             | Text      | Investor city            |
| kyc_status       | Text      | Verification status      |

---

## 07_scheme_performance.csv

| Column            | Data Type | Description             |
| ----------------- | --------- | ----------------------- |
| amfi_code         | Integer   | Scheme identifier       |
| return_1yr_pct    | Decimal   | One year return         |
| return_3yr_pct    | Decimal   | Three year return       |
| return_5yr_pct    | Decimal   | Five year return        |
| expense_ratio_pct | Decimal   | Expense ratio           |
| aum_crore         | Decimal   | Assets under management |
| risk_grade        | Text      | Risk level              |
