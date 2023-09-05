
import pandas as pd
import subprocess
import time,uuid
import os,re
from datetime import datetime
from tqdm import tqdm,trange
timeOut=60#seconds

df = pd.read_csv('list.csv')

today = datetime.today().strftime('%Y-%m-%d')
dir_name = os.path.join(".", today)

os.makedirs(dir_name, exist_ok=True)
counter = 0
total_files = df['A'].tolist()

for index, prompt in tqdm(enumerate(total_files), total=len(total_files)):
    prompt = re.sub(r'^\d+\.\s*', '', prompt)

    prompt = re.sub(r'[<>:"/\\|?*]', ' ', prompt).strip()
    command = f'python -m BingImageCreator -U your_Bing_U_Cookie  --prompt "{prompt}" --output-dir {dir_name}'
    subprocess.run(command, shell=True, check=True)
  
    try:
        with open('counter.txt', 'r') as counter_file:
            counter1 = int(counter_file.read())
    except (FileNotFoundError, ValueError):
        counter1 = 0  
    tqdm.write(f"The total prompts in the CSV is \033[92m{len(total_files)}\033[0m while the TOTAL number of generated photos is \033[92m{4+counter1*4}\033[0m (\033[92m{counter1+1}\033[0m requests towards Bing)")
    for i in range(4):
        for ext in ['jpeg', 'jpg']: 
            old_file = os.path.join(dir_name, f'{i}.{ext}')
            if os.path.isfile(old_file):
                unique_id = str(uuid.uuid4()) 
                new_filename = f"{counter} {prompt.replace(' ', '_')}_{counter}"
                if len(new_filename) + len(unique_id) + len(ext) + 2 > 240:
                    new_filename = new_filename[:(240 - len(unique_id) - len(ext) - 2)]
                new_filename += f"_{unique_id}.{ext}"
                new_file = os.path.join(dir_name, new_filename)
                os.rename(old_file, new_file)

    counter += 1

    with open('counter.txt', 'w') as counter_file:
        counter_file.write(str(counter))
        counter1 += 1
        if counter % 20 == 0:
            tqdm.write(f"Time out \033[92m{timeOut}\033[0m  seconds")
            for i in trange(timeOut):
                time.sleep(1)
        else:    
            time.sleep(1.5)
            

print("Finished")


