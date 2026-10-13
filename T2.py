# M = 
# obtener la cuota mensual de un prestamo en base al capital, tipo de interes y numbero de cuotas
#FIND CAPITAL

Initial_loan = int(input("Enter the initial loan amount in Euros: "))
#obtener tipo de interes (o dejarlo fijo en EURIBOR)

Interest = 0.025

#obtener años

Years = int(input("Enter the number of years: "))

Monthly_payment = Initial_loan * (Interest * (1 + Interest) ** (Years * 12)) / ((1 + Interest) ** (Years * 12) - 1)

Monthly_payment = round(Monthly_payment, 2)
# calculate the period which is period rate*12

#cuanto debe ganar para la casa
#resultado es un salario bruto
#maximo cuota 30% del suelto
#
print(f"The monthly payment is €{Monthly_payment}")

Salary = int(input("Enter your monthly salary in Euros: "))

if Salary < Monthly_payment * 0.3:
    print("APROBADO")
else:
    print("FAIL")


