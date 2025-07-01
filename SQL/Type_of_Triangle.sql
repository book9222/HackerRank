select
case 
when a+b<=c or a+c<=b or b+c<=a then 'Not A Triangle' 
when a=b and a=c and b=c then 'Equilateral'
when a=b or a=c or b=c then 'Isosceles' /*some input have two same side but not triangle e.g. 20 20 40*/
else 'Scalene'
end
from TRIANGLES 
