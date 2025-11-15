import psutil
import time
import os

# Получаем текущий процесс
process = psutil.Process(os.getpid())


def bytes_to_mb(b):
    return b / (1024 * 1024)


def monitor_memory():
    memory_history = []
    max_memory = 0
    start_time = time.time()

    print("Мониторинг памяти... (Ctrl+C для остановки)\n")

    # Создаём "нагрузку" — растущий список
    big_list = []

    try:
        while True:
            # Текущее потребление памяти (RSS — resident set size)
            current_mem = process.memory_info().rss
            current_mem_mb = bytes_to_mb(current_mem)

            # Обновляем максимум
            if current_mem_mb > max_memory:
                max_memory = current_mem_mb

            # Сохраняем для расчёта скорости
            memory_history.append((time.time(), current_mem_mb))

            # Удаляем старые записи (>10 сек назад)
            now = time.time()
            memory_history = [(t, m) for t, m in memory_history if now - t <= 10]

            # Считаем среднюю скорость роста (МБ/с) за последние 10 сек
            if len(memory_history) > 1:
                first_time, first_mem = memory_history[0]
                last_time, last_mem = memory_history[-1]
                delta_mem = last_mem - first_mem
                delta_time = last_time - first_time
                avg_growth = delta_mem / delta_time if delta_time > 0 else 0
            else:
                avg_growth = 0.0

            # Вывод
            print(f"\rТекущая память: {current_mem_mb:.2f} МБ | "
                  f"Максимум: {max_memory:.2f} МБ | "
                  f"Скорость роста: {avg_growth:.2f} МБ/с", end='', flush=True)

            # Проверка превышения лимита (1 ГБ = 1024 МБ)
            if current_mem_mb > 1024:
                print("\n⚠️  ВНИМАНИЕ: Потребление памяти превысило 1 ГБ!")
                # Можно добавить break, если нужно остановить
                # break

            # Нагрузка: добавляем данные в список
            big_list.append("X" * 100000)  # ~100 КБ на итерацию

            time.sleep(1)

    except KeyboardInterrupt:
        print("\n\n✅ Мониторинг остановлен.")
        print(f"Максимальное потребление памяти: {max_memory:.2f} МБ")


if __name__ == "__main__":
    monitor_memory()