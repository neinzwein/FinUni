# Создайте класс Length (Длина), имеющий атрибуты: value (значение), unit (единица измерения).
# При изменении единицы измерения значение должно соответственно меняться.
# Например, при переходе от сантиметров к метрам значение должно уменьшаться в 100 раз.
# Допустимые значения атрибуты unit: ‘см’, ‘м’, ‘км’.
# Организуйте эту проверку. Продемонстрируйте работу с классом.

class Length(object):

    possible_units = ['см','м','км']

    def __init__(self,value:int,unit:str) -> None:
        
        self.value = value
        self.unit = unit

        self.verificate_unit(unit)

    @classmethod
    def verificate_unit(cls,unit:str):
        if unit not in cls.possible_units:
            raise ValueError(f"Неправильная единица измерения - {unit}")
        
    def change_between_units(self,unit:str):
        c_idx = self.possible_units.index(self.unit)
        n_idx = self.possible_units.index(unit)
        
        if n_idx-c_idx>0:
            self.value /=10 ** ((n_idx-c_idx) * 2)
        else:
            self.value *=10 ** (-1*(n_idx-c_idx) * 2)

    @property
    def change_value(self)->int:
        return self.value
    
    @change_value.setter
    def change_value(self,value:int)->None:
        self.value = value

    @property
    def change_unit(self)->str:
        return self.unit
    
    @change_unit.setter
    def change_unit(self,unit:str)->None:

        self.verificate_unit(unit)
        self.change_between_units(unit)

        self.unit = unit
    

if __name__ == "__main__":
     
    l=Length(1000,'м')
    print(l.value,l.unit)

    l.change_unit='см'
    print(l.value,l.unit)

    l.change_unit='км'
    print(l.value,l.unit)
