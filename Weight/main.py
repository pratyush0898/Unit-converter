def length_converter(value, from_unit, to_unit):
    units = {
        'meters': 1,
        'kilometers': 0.001,
        'centimeters': 100,
        'millimeters': 1000,
        'inches': 39.3701,
        'feet': 3.28084,
        'yards': 1.09361,
        'miles': 0.000621371
    }

    if from_unit not in units or to_unit not in units:
        return "Invalid unit"

    result = value * units[from_unit] / units[to_unit]
    return result


def weight_converter(value, from_unit, to_unit):
    units = {
        'grams': 1,
        'kilograms': 0.001,
        'milligrams': 1000,
        'ounces': 0.03527396,
        'pounds': 0.00220462
    }

    if from_unit not in units or to_unit not in units:
        return "Invalid unit"

    result = value * units[from_unit] / units[to_unit]
    return result


def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        return (value - 32) * 5/9
    else:
        return "Invalid conversion"

# Example usage:
weight_result = weight_converter(1000, 'grams', 'kilograms')
print(f"Weight: {1000} grams is equal to {weight_result:.4f} kilograms")