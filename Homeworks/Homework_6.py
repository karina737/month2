		
class Distance:
    conversion_dict = {
    "см": 0.01,   
    "м": 1,       
    "км": 1000,   
}
    def convert(self):
     return self.value * Distance.conversion_dict.get(self.unit, 1)
	
    def __init__(self, value, unit):
        if unit not in Distance.conversion_dict:
         raise ValueError("Неподдерживаемая единица измерения")
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"
    
    @staticmethod
    def from_meters(meters, unit):
        return meters / Distance.conversion_dict[unit]

    def __add__(self, other):
        if not isinstance(other, Distance):
            raise TypeError("Складывать можно только Distance")

        total_m = self.convert() + other.convert()
        result_value = Distance.from_meters(total_m, self.unit)
        return Distance(result_value, self.unit)

    def __sub__(self, other):
        if not isinstance(other, Distance):
            raise TypeError("Вычитать можно только Distance")

        diff_m = self.convert() - other.convert()

        if diff_m < 0:
            raise ValueError("Результат не может быть отрицательным")

        result_value = Distance.from_meters(diff_m, self.unit)
        return Distance(result_value, self.unit)
    
    def __eq__(self, other):
       if self.value == other.value:
            return True
       return False

       


distans_1 = Distance(100, "м")
print(distans_1)
distans_2 = Distance(1, "м")
print(distans_2 + distans_1)
print(distans_1 - distans_2)
print(distans_2 == distans_1)



