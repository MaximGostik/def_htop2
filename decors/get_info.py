import psutil, datetime
from time import time
from decors import collect, show_info


@show_info.show_cpu_percent
@collect.write_info
def get_cpu_percent(): #возвращает сведения о загруженности ядер

    data = psutil.cpu_percent(interval=1, percpu=True)
    diction = {}
    for i in range(len(data)):
        diction[i] = data[i]

    return diction


@show_info.show_mem_info
@collect.write_info
def get_mem_info():#возвращает сведения об используемой оперативной памяти

    data = psutil.virtual_memory()
    name = data._fields
    diction = {}

    for i in range(len(name)):
        diction[name[i]] = data[i]

    return diction


@show_info.show_swap_memory
@collect.write_info
def get_swap_memory():

    return psutil.swap_memory()


@show_info.show_load_average
@collect.write_info
def get_load_average():#выводит сведения о средней загруженности

    return [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]


@show_info.show_up_time
@collect.write_info
def get_up_time():

    dt = datetime.timedelta(seconds=time() - psutil.boot_time())
    dt = str(dt)
    return dt


@show_info.show_count_pids
@collect.write_info
def get_count_pids():

    return psutil.pids()


@show_info.show_pids
@collect.write_info
def get_pids():
    info = []

    for i in psutil.process_iter(['pid', 'name', 'status']):
        info.append(i.info)

    return info

