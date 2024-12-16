import threading
import time
import os


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='UTF-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i}')
            time.sleep(0.1)
    print(f'Завершилась запись в файл: {file_name}')


main_th_start = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
main_th_end = time.time()
print(f'Длительность выполнения без многопоточности: {main_th_end - main_th_start}')


thread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
multi_th_start = time.time()
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
multi_th_end = time.time()
print(f'Длительность выполнения с многопоточностью: {multi_th_end - multi_th_start}')

# Удаляем ненужное
os.remove('example1.txt')
os.remove('example2.txt')
os.remove('example3.txt')
os.remove('example4.txt')
os.remove('example5.txt')
os.remove('example6.txt')
os.remove('example7.txt')
os.remove('example8.txt')