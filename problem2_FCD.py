#Ron Swanson in Management can be reached at 555-1234.
#Leslie Knope in Middle Management can be reached at 555-4321.
#Andy Dwyer in Shoe Shining can be reached at 555-1122.
#April Ludgate in Administration can be reached at 555-3345.


employees = [
{
 "name": "Ron Swanson",
 "age": 55,
 "department": "Management",
 "phone": "555-1234",
 "salary": "10000"
},
{
 "name": "Leslie Knope",
 "age": 45,
 "department": "Middle Management",
 "phone": "555-4321",
 "salary": "20000"
},
{
 "name": "Andy Dwyer",
 "age": 35,
 "department": "Shoe Shining",
 "phone": "555-1122",
 "salary": "5000"
},
{
 "name": "April Ludgate",
 "age": 25,
 "department": "Administration",
 "phone": "555-3345",
 "salary": "5000"
}
]
for employee in employees:
  print(f"{employee['name']} in {employee['department']} can be reached at {employee['phone']}.")
