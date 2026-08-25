raw_transactions = ["SUCCESS:100", "FAILED:50", "SUCCESS:-10",
"SUCCESS:0", "SUCCESS:250", "ERROR:200"]

# normalized transactions accepts only status: SUCCESS and get number values greater than 0 and covert it to int type
normalized_transactions = [int(value[1]) for value in [value.split(':') for value in raw_transactions] if value[0] == 'SUCCESS' and int(value[1]) > 0]
print(normalized_transactions)  # [100, 250]

