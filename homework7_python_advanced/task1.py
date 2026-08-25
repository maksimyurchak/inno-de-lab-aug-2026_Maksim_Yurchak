# Initial user input
raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "

# split the string to separate elements by ";"
split_user_record = raw_user_record.split(';')

# remove excess spaces from both sides
split_user_record = [element.strip(' ') for element in split_user_record]

# Add prefix to the user id
split_user_record[0] = 'UID-' + split_user_record[0]

# Change user name symbol _ into space(' ') and make it in title format
split_user_record[1] = split_user_record[1].replace('_', ' ')
split_user_record[1] = split_user_record[1].title()

# Change user city string into uppercase
split_user_record[2] = split_user_record[2].upper()

# Change user status string into lowercase
split_user_record[3] = split_user_record[3].lower()

#make it one string separated by ' | ' 
normalized_user_record = ' | '.join(split_user_record)
print(normalized_user_record)  # UID-10827 | Alexander Vladimirov | MINSK | active
