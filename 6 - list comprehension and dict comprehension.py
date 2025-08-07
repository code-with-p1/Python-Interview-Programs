result = [i for i in range(0, 11)]
print(result)

dict_result = {str(i):i*i for i in range(0, 11) if i % 2 == 0 }
print(dict_result)