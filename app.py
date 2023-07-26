
from task_01 import Cpu, Gpu
from my_dict_db import cpu_list, gpu_list

def initialize_cpu() -> list:
    list_of_cpu_objects = []
    for cpu_part in cpu_list:
        cpu = Cpu(id=cpu_part['id'],
                    name=cpu_part['name'], 
                    brand=cpu_part['brand'], 
                    price=cpu_part['price'], 
                    core_count=cpu_part['core_count'],
                    performance_core_clock=cpu_part['performance_core_clock'],
                    integrated_gpu=cpu_part['integrated_gpu']
                )
        list_of_cpu_objects.append(cpu)
    
    return list_of_cpu_objects

def initialize_gpu() -> list:
    list_of_gpu_objects = []
    for gpu_part in gpu_list:
        gpu = Gpu(id=gpu_part['id'],
                    name=gpu_part['name'], 
                    brand=gpu_part['brand'], 
                    price=gpu_part['price'], 
                    chipset=gpu_part['chipset'],
                    memory=gpu_part['memory'],
                    core_clock=gpu_part['core_clock']
                )
        list_of_gpu_objects.append(gpu)
    return list_of_gpu_objects

all_cpu = initialize_cpu()
all_gpu = initialize_gpu()

while True:

    choice = input("1 - print_all_cpu\n2 - print_all_gpu\n3 - sorted CPU by AMD\n4 - update gpu price\n5 - Show only some cpu brand\n0 - exit\n")

    match choice:
        case '1':
            print("#####################=- CPU list -=#####################")
            for cpu in initialize_cpu():
                print(cpu)
            print("#####################=- END -=#####################")
            
        case '2': 
            print("#####################=- GPU list -=#####################")
            for gpu in initialize_gpu():
                print(gpu)
            print("#####################=- END -=#####################")

        case '3':
            print("#####################=- sorted CPU by AMD -=#####################")
            amd_cpu_list = [cpu_object for cpu_object in all_cpu if cpu_object.brand == 'AMD']
            for amd_cpu in amd_cpu_list:
                print(amd_cpu)
            print("#####################=- END -=#####################")

        case '4':
            print("#####################=- update gpu price -=#####################")
            for gpu_part in enumerate(all_cpu):
                print(f'No. {gpu_part[0]}, {gpu_part[1]}')
            while True:
                try:
                    chanege_price = input('Please enter no. gpu to change price: ')
                    all_cpu[int(chanege_price)].update_price()
                    print(f'Price are updated: {all_cpu[int(chanege_price)]}')
                    break
                except IndexError:
                    print('Index not exist')
                except ValueError:
                    print('Input must be integer')
            print("#####################=- END -=#####################")

        case '5':
            print("#####################=- Show only some cpu brand -=#####################")
            # all_cpu = initialize_cpu()
            while True:
                try:
                    choice_brand = input('Please enter cpu brand intel or amd: ').upper()
                    cpu_list_by_brand = [cpu_object for cpu_object in all_cpu if cpu_object.brand == choice_brand]
                    if not cpu_list_by_brand:
                        print('Sorry cpu brand not exist!!!')
                        continue
                    break
                except Exception as e:
                    print({e})
            for cpu in cpu_list_by_brand:
                print(cpu)
            print("#####################=- END -=#####################")
        
        
        case '0':
            print("Goodbye")
            break

        case other:
            print("Wrong command!!!")