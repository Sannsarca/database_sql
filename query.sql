--For several countries outputs its points for 2019 year

SELECT country_name,year_data,points 
FROM country 
LEFT JOIN years ON country.country_id=years.country_id 
LEFT JOIN information ON years.year_id=information.Year_country_id 
WHERE (year_data=2019);

--Outputs list of regions with number of countries located there 

SELECT country_region,COUNT( country_region)
FROM country
GROUP BY country_region;

--Output countries points and plase depending on year

SELECT country.country_name,years.year_data,information.points,information.place FROM country
LEFT JOIN years ON country.country_id=years.country_id 
LEFT JOIN information ON years.year_id=information.year_country_id  
WHERE (information.year_country_id=years.year_id AND years.country_id=country.country_id AND country.country_name='Ukraine') ORDER BY year_data;