def money(hours, ot_hours):
	normal_hourly = 28.85
	overtime_hourly = normal_hourly + normal_hourly/2
	normal_hours = hours
	overtime_hours = ot_hours
	wr_benefits = 200
	taxes = .1839
	fica_tax = .0765
	tips = input("How much did you make in tips? ")
	normal_pay = normal_hours * normal_hourly
	normal_taxed = (normal_pay * taxes)
	normal_fica = (normal_pay * fica_tax)
	total_tax = normal_taxed + normal_fica
	normal_total = (normal_pay - total_tax) - wr_benefits
	normal_total_clean = float(round(normal_total, 3))
	overtime_pay = overtime_hours * overtime_hourly
	overtime_total = overtime_pay
	total_pay = normal_total + overtime_total
	return normal_total_clean, overtime_total
print(money(, 0))
