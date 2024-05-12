import os
import datetime

def log(*datas):
    now = datetime.datetime.now()
    exec_time = now.strftime("%Y-%m-%d %H:%M:%S")
    filename = "run_" + now.strftime("%Y-%m-%d") + ".log"  # Format: YYYY-MM-DD
    # Open the file in append mode
    data = exec_time + " " + ' '.join(map(str, datas))
    print(data)
    # file_path = os.path.join("log", filename)
    # with open(file_path, 'a') as file:
    #     file.write(data + '\n')