Select month(from_unixtime(date)) AS Birth_Month,
year(from_unixtime(date)) AS Birth_Year,
count(city) AS count,
city
from birth_report
where month(from_unixtime(date)) = '3' AND city = 'Balasore'
group by Birth_Year, Birth_Month, city;