# shipping cost calculator

## input package weight and shipping rate
weight= float (input (''enter the package weight in kilograms: ''))
rate=float (input(''Enter shipping rate per kilogram: ''))

## Calculate shipping cost
shipping_cost=weight * rate

display the result 
print (f''shipping cost :{shipping_cost} USD'')
