
def sub_level(key, memCon):
    result = []
    for data in memCon:	
        if key == data[0]:
            result.append(data[1])
    return result

def maxGenePhone(arri, memCon):
    levels = {}
    for data in memCon:
        if data in memCon:
            levels.update({data[0] : sub_level(data[0], memCon)})
    total = [arri[0]]
    for root, childerns in levels.items():
        childer_sum = 0
        for childs in childerns:
            childer_sum = childer_sum + arri[childs]
        total.append(childer_sum)
    return max(total)

def main():
	# Hardcoded input for arri
    arri = [15, 10, 25, 30, 16, 9, 5, 3, 15, 1, 8, 11, 13]
    
    # Hardcoded input for memCon
    memCon = [
        [0, 1],
        [0, 2],
        [0, 3],
        [1, 4],
        [1, 5],
        [2, 6],
        [2, 7],
        [3, 8],
        [3, 9],
        [4, 10],
        [5, 11],
        [6, 12]
    ]
    
    result = maxGenePhone(arri, memCon)
    print(result)

if __name__ == "__main__":
	main()