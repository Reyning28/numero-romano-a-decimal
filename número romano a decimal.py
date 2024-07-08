"""
REYNING PERDOMO FELIZ
MATRICULA:2023-1110
"""



def roman_to_decimal(roman):
    
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    
    decimal_value = 0
    prev_value = 0
    
    
    for symbol in reversed(roman):
        current_value = roman_values[symbol]
        
        
        if current_value < prev_value:
            decimal_value -= current_value
        else:
            decimal_value += current_value
        
        prev_value = current_value
    
    return decimal_value


roman_number = "XXXIV"
decimal_number = roman_to_decimal(roman_number)
print(f"Entrada: {roman_number}\nSalida: {decimal_number}")
