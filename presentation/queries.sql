-- Trend Over Time
SELECT 
    year,
    AVG(maternal_mortality) AS avg_mmr,
    AVG(health_expenditure) AS avg_health_exp,
    AVG(gdp_per_capita) AS avg_gdp
FROM fact_health_metrics
GROUP BY year
ORDER BY year;

-- Country Comparison
SELECT 
    country,
    AVG(maternal_mortality) AS avg_mmr
FROM fact_health_metrics
GROUP BY country
ORDER BY avg_mmr DESC;

-- Data Validation Checks
SELECT COUNT(*) 
FROM fact_health_metrics
WHERE maternal_mortality IS NULL;

SELECT country_code, year, COUNT(*)
FROM fact_health_metrics
GROUP BY country_code, year
HAVING COUNT(*) > 1;
