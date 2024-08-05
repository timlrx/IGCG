import pandas as pd
import json

# Define the input CSV file, output JSON file, and the original config file
input_csv = './Our_GCG_target_len_20/gcss/20240805-150141/log/top_igcg_results.csv'
output_json = 'behaviours_gcss_config_init_continued3.json'
original_config_file = 'behaviours_gcss_config_init.json'

# Read the CSV file
df = pd.read_csv(input_csv)

# Read the original config file
with open(original_config_file, 'r') as f:
    original_config = json.load(f)

# Create a mapping from 'id' to 'target' using the original config
id_to_target = {entry['id']: entry['target'] for entry in original_config}

# Group by 'index' and select the row with the minimum 'loss' for each group
df_lowest_loss = df.loc[df.groupby('index')['loss'].idxmin()]

# Initialize an empty list to store the configuration data
config_data = []

# Iterate through the rows of the filtered DataFrame
for i, row in df_lowest_loss.iterrows():
    # Create a dictionary for each entry
    entry = {
        "id": int(row['index']),
        "behaviour": row['user_prompt'],
        "target": id_to_target.get(int(row['index']), ""),  # Get the target from the original config
        "adv_init_suffix": row['adv_suffix'],
        "step": 128,
        "batch_size": 128,
        "top_k": 256
    }
    # Append the entry to the config_data list
    config_data.append(entry)

# Write the list of dictionaries to the JSON file
with open(output_json, 'w') as f:
    json.dump(config_data, f, indent=4)

print(f"Configuration data with lowest loss saved to {output_json}")
