-- 1. Top 5 Fund Houses by AUM

SELECT fund_house, aum_crore
FROM aum_by_fund_house
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per Month

SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

-- 3. Total SIP Amount by Year

SELECT
strftime('%Y', transaction_date) AS year,
SUM(amount_inr) AS total_sip
FROM fact_transactions
WHERE transaction_type = 'Sip'
GROUP BY year;

-- 4. Transactions by State

SELECT
state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Funds with Expense Ratio Below 1%

SELECT
scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Top 10 Funds by 5 Year Return

SELECT
scheme_name,
return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- 7. Average Transaction Amount by State

SELECT
state,
AVG(amount_inr) AS avg_amount
FROM fact_transactions
GROUP BY state;

-- 8. Count of Transactions by Type

SELECT
transaction_type,
COUNT(*) AS total
FROM fact_transactions
GROUP BY transaction_type;

-- 9. Average Expense Ratio by Category

SELECT
category,
AVG(expense_ratio_pct) AS avg_expense_ratio
FROM fact_performance
GROUP BY category;

-- 10. Top Funds by AUM

SELECT
scheme_name,
aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 10;
