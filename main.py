import subprocess
import time
start_time = time.time()
# Запрос названия видео у пользователя
# Видео должно находится в той-же папке что и скрипт
video_name = input("Введите название видео: ")
hours = input("Введите желаемое кол-во часов: ")
# Получение длительности видео
command_duration = ['ffprobe', '-i', video_name, '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=%s' % ("p=0")]
result_duration = subprocess.check_output(command_duration)
duration = float(result_duration)

hours_in_seconds = int(hours) * 3600
multiplier = int((hours_in_seconds / duration) - 1)
# Создание 10-часовой версии видео
command = ['ffmpeg', '-stream_loop', str(multiplier), '-i', video_name, '-c', 'copy', f'{hours}_hour_' + video_name]

# Запуск команды
result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

sec_time = int(time.time() - start_time)

time_units = {"ч": 3600, "мин": 60, "сек": 1}

for unit, value in time_units.items():
    if sec_time >= value:
        time = round(sec_time / value, 1)
        print(f"--- Генерация видео заняла: {time} {unit}{'s' if time > 1 else ''} ---")
        break
