raw_transactions = ["SUCCESS:100", "FAILED:50", "SUCCESS:-10",
"SUCCESS:0", "SUCCESS:250", "ERROR:200"]

# normalized transactions accepts only status: SUCCESS and get number values greater than 0 and covert it to int type
normalized_transactions = [int(value) for status, value in (transactions.split(':') for transactions in raw_transactions) if status == 'SUCCESS' and int(value) > 0]
print(f'Очищенные транзакции: {normalized_transactions}')  # [100, 250]
