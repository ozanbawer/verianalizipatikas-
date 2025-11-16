# Ödev 1 


def flatten_list(nested_list):

    flat_list = []
    
    for element in nested_list:
        
        if isinstance(element, list):
            flat_list.extend(flatten_list(element))
        else:
            flat_list.append(element)
    return flat_list


input_list_1 = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output_1 = flatten_list(input_list_1)

print(f"Girdi (Flatten): {input_list_1}")
print(f"Çıktı (Flatten): {output_1}")

# Ödev 1 

