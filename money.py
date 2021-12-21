def money(hours, ot_hours):
	hourly = int(input("How much do you make an hour? "))
	ot_hourly = hourly + (hourly/2)
	benefits = int(input("How much do you pay in benefits? "))
	taxes = .1839
	fica_tax = .0765
	pay = hours * normal_hourly
	taxed = (pay * taxes)
	fica = (pay * fica_tax)
	total_tax = taxed + fica
	total = (pay - total_tax) - benefits
	total_clean = float(round(total, 3))
	overtime_pay = ot_hours * ot_hourly
	overtime_total = overtime_pay
	total_pay = total + overtime_total
	return normal_total_clean, overtime_total
print(money(0, 0))
