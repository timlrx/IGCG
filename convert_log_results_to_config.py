import pandas as pd
import json

# Define the input CSV file and output JSON file
input_csv = './Our_GCG_target_len_20/gcss/20240804-211531/log/top_igcg_results.csv'
output_json = 'behaviours_gcss_config_init_continued.json'

# Read the CSV file
df = pd.read_csv(input_csv)

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
        "target": row['gen_str'],
        "adv_init_suffix": row['adv_suffix'],
        "step": 256,
        "batch_size": 128,
        "top_k": 256
    }
    # Append the entry to the config_data list
    config_data.append(entry)

# Write the list of dictionaries to the JSON file
with open(output_json, 'w') as f:
    json.dump(config_data, f, indent=4)

print(f"Configuration data with lowest loss saved to {output_json}")