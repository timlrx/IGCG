import os
import json
import pandas as pd

log_folder = './Our_GCG_target_len_20/gcss/20240805-150141/log'
output_csv = 'top_results.csv'

# Create a list to store all the results
all_results = []

# Iterate through all files in the log folder
for filename in os.listdir(log_folder):
    if filename.endswith('.json'):
        file_path = os.path.join(log_folder, filename)
        
        # Extract the question number from the filename (e.g., result_40.json -> 40)
        index = int(filename.split('_')[1].split('.')[0])
        
        # Open and read the JSON file
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # Sort data by loss (ascending) and get the top 5 entries
        sorted_data = sorted(data, key=lambda x: float(x['loss']))
        top_5_results = sorted_data[:5]
        
        # Extract the necessary fields and add them to the results list
        for entry in top_5_results:
            result = {
                'index': index,
                'loss': float(entry['loss']),
                'user_prompt': entry['user_prompt'],
                'adv_suffix': entry['adv_suffix'],
                'gen_str': entry['gen_str']
            }
            all_results.append(result)

# Convert the results to a DataFrame
df = pd.DataFrame(all_results)

# Define the output CSV file path
output_csv = os.path.join(log_folder, 'top_igcg_results.csv')

# Write the results to the CSV file
df.to_csv(output_csv, index=False)

print(f"Top results saved to {output_csv}")
