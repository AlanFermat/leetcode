def balance(lines):
    """
        Input: lines - an array of strings, representing the commands from API or BAL
        Return: res - an array of integers representing dollars for corresponding accounts
    """
    res = []
    def calculate(num):
        fee = num * 0.029 + 30
        return num * 1.0 - fee
    account_data = {}
    for line in lines:
        if line[0] == "A":
            temp = line[5:].split("&")
            amount = int(temp[0].split("=")[1])
            merchant = temp[1].split("=")[1]
            driver_money = []
            drivers = []
            if len(temp) > 2:
                idx = 2
                while idx < len(temp):
                    drivers.append(temp[idx].split("=")[1])
                    if idx + 1 == len(temp):
                        drivers.pop()
                        break
                    driver_money += [int(temp[idx+1].split("=")[1])]
                    idx += 2
            remain = round(calculate(amount))
            if drivers:
                for i, driver in enumerate(drivers):
                    account_data[driver] = driver_money[i]
            account_data[merchant] = account_data.get(merchant,0) + int(remain - sum(driver_money))
        if line[0] == "B":
            li = line[5:].split("=")
            id_num = li[1]
            res.append(account_data.get(id_num,0))
    return res

			
			


			
lines = ["API: amount=1000&merchant=123456789","API: amount=1000&merchant=123456789&destination[account]=111111&destination[amount]=877&destination[account]=114411&destination[amount]=7",\
"API: amount=800&merchant=123456789&destination[account]=112211&destination[amount]=622",\
"BAL: merchant=123456789",\
"BAL: merchant=112211"]

print balance(lines)

