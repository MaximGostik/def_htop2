def show_cpu_percent(func): #выводит сведения о загруженности ядер

    info = func()

    for i in range(len(info)):
        counter = info[i] // 5
        print(i, '[' + '|' * round(counter) + '.' * (20 - round(counter)), info[i], '%]', end = '\n')


def show_mem_info(func):#выводит сведения об используемой оперативной памяти

    data = func()

    counters = int(data['percent']) // 5
    mem_used = round(data['used'] / 1024**3, 2)
    mem_total = round(data['total'] / 1024**3, 2)
    print('\nMem[' + '|' * counters + '.' * (20 - counters), mem_used, '/', mem_total, 'Gb]')


def show_load_average(func):#выводит сведения о средней загруженности

    data = func()
    print('Load average:', *data)


def show_swap_memory(func):

    info = func()

    total = info[0] // 1024 ** 2
    used = info[1] // 1024 ** 2
    print('Swp[' + '|' * round(used / total / 20) + '.' * (20 - round(used / total / 20)), used, 'Мб /', total, 'Мб]')


def show_up_time(func):

    data = func()
    print('Uptime:', data)


def show_count_pids(func):
    
    data = func()
    print('Tasks:', len(data), '\n')


def show_pids(func):

    data = func()
    format_pid = "{pid:<7} {name:<28} {status:<20}"
    print("{:<7} {:<28} {:<20}".format("PID", "Name", "Status"))
    for p in data:
        print(format_pid.format(**p))


