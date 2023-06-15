list_data = [
    {
        "type": "Curb Weight",
        "unit": "lbs",
        "value": 3985
    },
    {
        "type": "Standard Towing",
        "unit": "lbs",
        "value": 5000
    },
    {
        "type": "Standard GVWR",
        "unit": "lbs",
        "value": 5050
    }
]

result_text = ""
for key, dict_data in enumerate(list_data):
    for key in dict_data:
        result_text += f"{key}: {dict_data[key]}|"
print(result_text)
