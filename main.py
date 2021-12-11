import psycopg2
import matplotlib.pyplot as plt

username = 'Danylevych93'
password = 'qwerty228'
database = 'postgres'
host = 'localhost'
port = 5555

query_1 = '''
SELECT country_name,year_data,points 
FROM country 
LEFT JOIN years ON country.country_id=years.country_id 
LEFT JOIN information ON years.year_id=information.Year_country_id 
WHERE (year_data=2019);
'''

query_2 = '''
SELECT country_region,COUNT( country_region)
FROM country
GROUP BY country_region;
'''

query_3 = '''
SELECT country.country_name,years.year_data,information.points,information.place FROM country
LEFT JOIN years ON country.country_id=years.country_id 
LEFT JOIN information ON years.year_id=information.year_country_id  
WHERE (information.year_country_id=years.year_id AND years.country_id=country.country_id AND country.country_name='Ukraine') ORDER BY year_data;
'''
connection = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

cursor = connection.cursor()
cursor.execute(query_1)
PointsIn2019 = cursor.fetchall()
print("First query:- ", PointsIn2019)

cursor.execute(query_2)
AmountCont = cursor.fetchall()
print("Second query:- ", AmountCont)

cursor.execute(query_3)
StatForYears = cursor.fetchall()
print("Third query:- ", StatForYears)