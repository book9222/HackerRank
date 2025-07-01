select *,
case 
when a=b and b=c and a=b then 'Equilateral' 
when a=b or b=c or a=c then 'Isosceles'
when a+b<=c or b+c<=a or a+c<=b then 'Not A Triangle'
else 'Scalene'
end
from TRIANGLES 