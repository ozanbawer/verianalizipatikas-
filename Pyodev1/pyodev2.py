# Ödev 2 


def reverse_nested_list(nested_list):
    
    reversed_list = nested_list[::-1]
    
    for i, element in enumerate(reversed_list):
        if isinstance(element, list):
            reversed_list[i] = reverse_nested_list(element)
    return reversed_list


input_list_2 = [[1, 2], [3, 4], [5, 6, 7]]
output_2 = reverse_nested_list(input_list_2)

print(f"\nGirdi (Reverse): {input_list_2}")
print(f"Çıktı (Reverse): {output_2}")

