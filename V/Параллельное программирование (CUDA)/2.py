# 2. С использованием инструментария CUDA напишите программу, выводящую в терминал (или в графическое окно, по желанию) 
# список основных возможностей установленных в системе GPU.

from numba import cuda

gpu_count = cuda.gpus.lst
device = cuda.get_current_device()
handle = cuda.current_context()

# # print(device.__dict__)

print(f"id: {device.id}")
print(f"Главных CUDA процессоров(версия): {device.COMPUTE_CAPABILITY_MAJOR}")
print(f"Память доступная: {cuda.cudadrv.driver.Context(device,handle).get_memory_info().free}")
print(f"Память всего: {cuda.cudadrv.driver.Context(device,handle).get_memory_info().total}")
print(f"Вспомогательных CUDA процессоров(версия): {device.COMPUTE_CAPABILITY_MINOR}")
print(f"Версия CUDA: {device.compute_capability}")
print(f"Имя: {device.name}")
# print(f"UUID: {device.uuid}")
print(f"Количество мультипроцессоров: {device.MULTIPROCESSOR_COUNT}")

print(f"Частота тактов процессора: {device.CLOCK_RATE/1000000} ГГц")
# print(f"Максимальный размер блоков: {device.MAX_BLOCK_DIM_X}x{device.MAX_BLOCK_DIM_Y}x{device.MAX_BLOCK_DIM_Z}")
# print(f"Максимальный размер сетки: {device.MAX_GRID_DIM_X}*{device.MAX_GRID_DIM_Y}x{device.MAX_GRID_DIM_Z}")
print(f"Максимальное количество потоков на блок: {device.MAX_THREADS_PER_BLOCK}")
print(f"PCI-шина: {device.PCI_BUS_ID}, Устройство: {device.PCI_DEVICE_ID}")

# _______________________________________________________________________________
# import pycuda.driver as cuda
# import pycuda.autoinit

# #https://documen.tician.de/pycuda/driver.html
# device = cuda.Device(0)
# print(f"Устройство {0}: {device.name()}")
# print(f"Общая память: {device.total_memory() / (1024**3)} ГБ")
# print(f"Количество мультипроцессоров: {device.get_attribute(cuda.device_attribute.MULTIPROCESSOR_COUNT)}")
# print(f"Частота тактов процессора: {cuda.device_attribute.CLOCK_RATE} ГГц")

# print(f"""Максимальный размер блоков: {device.get_attribute(cuda.device_attribute.MAX_BLOCK_DIM_X)} x
#       {device.get_attribute(cuda.device_attribute.MAX_BLOCK_DIM_Y)} x
#       {device.get_attribute(cuda.device_attribute.MAX_BLOCK_DIM_Z)}""")
# print(f"""Максимальный размер сетки: {device.get_attribute(cuda.device_attribute.MAX_GRID_DIM_X)} x
#       {device.get_attribute(cuda.device_attribute.MAX_GRID_DIM_Y)} x
#       {device.get_attribute(cuda.device_attribute.MAX_GRID_DIM_Z)}""")
# print(f"""Максимальное количество потоков на блок: {device.get_attribute(cuda.device_attribute.MAX_THREADS_PER_BLOCK)}""")
# print(f"""Версия CUDA: {device.get_attribute(cuda.device_attribute.COMPUTE_CAPABILITY_MAJOR)}.
#       {device.get_attribute(cuda.device_attribute.COMPUTE_CAPABILITY_MINOR)}""")