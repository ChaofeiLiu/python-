#dayupq2.py
dayfactor =0.005
dayup =pow(1+dayfactor,365)
daydown =pow(1-dayfactor,365)
print("向上的力量:{:.2f},向下的力量:{:.2f}".format(dayup,daydown))
