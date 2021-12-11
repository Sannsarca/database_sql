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
print("\nFirst query:- ", PointsIn2019)

cursor.execute(query_2)
AmountCont = cursor.fetchall()
print("\nSecond query:- ", AmountCont)

cursor.execute(query_3)
StatForYears = cursor.fetchall()
print("\nThird query:- ", StatForYears)

with connection:
    cur = connection.cursor()
    cur.execute(query_1)
    country_name = []
    points = []

    for row in cur:
        country_name.append(row[0])
        points.append(row[2])


    x_range = range(len(country_name))

    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1,3)
    bar = bar_ax.bar(x_range, points)
    bar_ax.set_title('Countries and its points in 2019')
    bar_ax.set_xlabel('Countries')
    bar_ax.set_ylabel('Points')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(country_name)


    cur.execute(query_2)
    country_region = []
    count = []

    for row in cur:
        country_region.append(row[0])
        count.append(row[1])

    pie_ax.pie(count, labels=country_region, autopct='%1.1f%%')
    pie_ax.set_title('Part of each region')



    cur.execute(query_3)
    country_name = []
    year = []
    points = []

    for row in cur:
        country_name.append(row[0])
        year.append(row[1])
        points.append(row[2])

    graph_ax.plot(year, points, marker='o')

    graph_ax.set_xlabel('Year')
    graph_ax.set_ylabel('Points')
    graph_ax.set_title('For each year each points')

    for year, points in zip(year, points):
        graph_ax.annotate(year, xy=(year, points), xytext=(7, 2), textcoords='offset points')

    mng = plt.get_current_fig_manager()
    mng.resize(1400, 600)

    plt.show()