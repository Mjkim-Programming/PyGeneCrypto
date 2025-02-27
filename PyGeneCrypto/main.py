def GeneEncrypt(data):
    # Change Data To Binary
    bin = list(''.join(format(ord(char), '08b') for char in data))
    
    for i in range(0, int(bin.__len__())):
        bin[i] = int(bin[i])
    
    res = ""
    
    # Change Binary To Gene Code
    for i in range(0, int(bin.__len__()), 2):
        chunk = bin[i:i+2]
        match chunk:
            case [0, 0]:
                res = res + "A"
            case [0, 1]:
                res = res + "G"
            case [1, 0]:
                res = res + "C"
            case [1, 1]:
                res = res + "T"
    
    return res

def Compress(res):
    # Compression
    res = list(res)
    result = ""
    i = 0
    j = 0
    
    while i < len(res):
        j = i
        count = 0
        
        while j < len(res) and res[j] == res[i]:
            count += 1
            j += 1
        
        if count == 1:
            result = result + f"{res[i]}"
        else :
            result = result + f"{res[i]}{count}"
            
        i += count
    
    return result

def GeneDecode(data):
    data = list(data)
    
    i = 0
    j = 0
    
    res = ""
    result = []
    
    while(i < len(data)):
        code = data[i]
        
        try:
            count = int(data[i+1])
            i += 2
        except:
            count = 1
            i += 1
        
        res += code * count
    
    for i in range(0, len(res)):
        match res[i]:
            case "A":
                result.append(0)
                result.append(0)
            case "G":
                result.append(0)
                result.append(1)
            case "C":
                result.append(1)
                result.append(0)
            case "T":
                result.append(1)
                result.append(1)

    string = "".join(
        chr(int("".join(map(str, result[i:i+8])), 2))
        for i  in range(0, len(result), 8)
    )
    
    return string