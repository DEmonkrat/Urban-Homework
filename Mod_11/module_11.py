import time, multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if line:
                all_data.append(line)
            else:
                break


if __name__ == '__main__':
    files_names = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
    time_start = time.time()
    # list(map(read_info, files_names))   # Время 7.5-7.8
    with multiprocessing.Pool() as m_pool:  # Время ~2.7
        m_pool.map(read_info, files_names)
    print(time.time() - time_start)
# Разница по времени в 3 раза !!!