def GeneEncrypt(data):
    """
    데이터를 이진수로 변환하고, 다시 이진수를 염기로 변환하는 함수입니다.
    
    Args:
        data (any): 변환할 데이터입니다. 어떤 형식이든 8bit 이하의 이진수로 변환할 수 있다면 가능합니다.
        
    Returns:
        res (str): 변환된 데이터입니다. A, T, G, C 네 가지의 염기가 연속되어 있는 형태로 이루어집니다.
    """
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
    """
    염기로 변환된 데이터를 압축하여 더 짧게 만드는 코드입니다. Decode 전 이를 한번 거쳐야 가능합니다. 만약 이 결과를 저장하고 싶지 않다면 GeneDecode(Compress(data))로 이용할 수 있습니다.
    
    Args:
        data (str): 변환할 데이터입니다. A, T, G, C 네 가지의 염기와 각각의 염기로 이루어집니다. 예시는 다음과 같습니다 -> AAATTGCAAAAAAA
        
    Returns:
        res (str): 변환된 데이터입니다. A, T, G, C 네 가지의 염기와 각각의 염기가 연속된 개수로 이루어집니다. 예시는 다음과 같습니다 -> A3T2GCA7
    """
    
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
    """
    염기 텍스트를 다시 데이터로 변환합니다.
    
    Args:
        data (any): 변환할 데이터입니다. A, T, G, C 네 가지의 염기와 각각의 염기가 연속된 개수로 이루어집니다. 예시는 다음과 같습니다 -> A3T2GCA7
        
    Returns:
        string (any): 변환된 데이터입니다. 원래 데이터의 내용을 가지고 있습니다.
    """
    
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