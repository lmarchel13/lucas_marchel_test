def compare(version1, version2):
    if ',' in version1 or ',' in version2: 
        raise Exception('Invalid input. Use dot instead comma separator.')
    
    # Edge cases
    if len(version2) == 0 and len(version1) > 0: 
        return 1
    if len(version1) == 0 and len(version2) > 0: 
        return -1
    if len(version1) == 0 and len(version2) == 0:
        return 0
    
    v1 = version1.split('.')
    v2 = version2.split('.')   

    # Compare with array size is equal
    # If not, create new indexes to make equal

    if len(v1) < max(len(v1), len(v2)):
        v1 = v1 + ['0'] * (len(v2) - len(v1))        
    elif len(v2) < max(len(v1), len(v2)):
        v2 = v2 + ['0'] * (len(v1) - len(v2))        

    # Start comparision
    # Return 1 if version1 is bigger than version2
    # Return -1 if version2 is bigger than version1
    # Return 0 if both are equal    
    
    for i in range (0, len(v1)):
        if int(v1[i]) > int(v2[i]):
            # print('Version {} is greater than version {}'.format(version1,version2))            
            return 1
        elif int(v1[i]) < int(v2[i]):
            # print('Version {} is greater than version {}'.format(version2,version1))
            return -1
    
    # print('Both versions are equal')
    return 0


compare("1.2","1.1")

