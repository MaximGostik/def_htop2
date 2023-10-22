import json

def write_info(func):

    diction = {"get_cpu_percent":"CPU-Info.json", 
               "get_mem_info":"mem-info.json", 
               "get_load_average":"load-average-info.json",
               "get_swap_memory":"swap-ifo.json", 
               "get_up_time":"getup-info.json", 
               "get_count_pids":"pids-count-info.json",
               "get_pids":"pids-info.json"}
    
    file_name = diction[func.__name__]

    def worker():
        res = func()
        with open(file_name, "w") as file:
            file.write(json.dumps(res, indent=4))
        return res

    return worker
