"""
Phase 1: 
Create a class that would represent pc parts. It should contain basic methods to retreive items name, price, colour (if applicable).
PC part list can be found here: https://pcpartpicker.com/list/
The every separate part should have at least 3-4 methods to gather this part specific data (example: CPU - brand , speed, power usuage etc.)
At this stage, dictionary data structures can work as Database. OOP abstraction, inheritance and encapsulation must be presented in a code base. 
Unit tests must be written for the methods.

"""


class ComputerPart():
    def __init__(self, name, brand, price) -> None:
        self.name = name
        self.brand = brand
        self.price = price

    def get_product_name(self):
        return self.name
    
    def get_product_brand(self):
        return self.brand
    
    def get_product_price(self):
        return self.price
    

class Cpu(ComputerPart):

    def __init__(self, name, brand, price, core_count, performance_core_clock, integrated_gpu) -> None:
        super().__init__(name, brand, price)
        self.core_count = core_count
        self.performance_core_clock = performance_core_clock
        self.integrated_gpu = integrated_gpu


    def get_cpu_core_count(self):
        return self.core_count
    
    def get_cpu_performance_core_clock_speed(self):
        return self.performance_core_clock

    def get_cpu_integrated_gpu_info(self):
        return self.integrated_gpu
    
    
class Gpu(ComputerPart):
    def __init__(self, name, brand, price, chipset, memory, core_clock) -> None:
        super().__init__(name, brand, price)
        self.chipset = chipset
        self.memory = memory
        self.core_clock = core_clock

    def get_gpu_chipset(self):
        return self.chipset
    
    def get_gpu_memory(self):
        return self.memory

    def get_gpu_core_clock(self):
        return self.core_clock



cpu_part = {'name': 'CPU', 
        'brand': 'INTEL',
        'price': '1500', 
        'core_count': '16', 
        'performance_core_clock': '3.4 GHz', 
        'integrated_gpu': 'Intel UHD Graphics 770'
        }

gpu_part = {
        'name': 'GPU',
        'brand': 'MSI',
        'price': '3000',
        'chipset': 'GeForce RTX 3060',
        'memory' : '12GB',
        'core_clock': '1320 MHz'
}

cpu1 = Cpu(name=cpu_part['name'], 
          brand=cpu_part['brand'], 
          price=cpu_part['price'], 
          core_count=cpu_part['core_count'],
          performance_core_clock=cpu_part['performance_core_clock'],
          integrated_gpu=cpu_part['integrated_gpu']
          )

gpu1 = Gpu(name=gpu_part['name'], 
          brand=gpu_part['brand'], 
          price=gpu_part['price'], 
          chipset=gpu_part['chipset'],
          memory=gpu_part['memory'],
          core_clock=gpu_part['core_clock']
        )

print(cpu1.get_product_brand())
print(cpu1.get_cpu_integrated_gpu_info())
print('###########')
print(gpu1.get_gpu_chipset())
print(gpu1.get_gpu_memory())





