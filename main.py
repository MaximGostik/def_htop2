from decors import get_info as gi


def main():
    return gi.get_cpu_percent, gi.get_mem_info, gi.get_swap_memory, \
           gi.get_load_average, gi.get_up_time, gi.get_count_pids, gi.get_pids

if __name__ == '__main__':
    main()
