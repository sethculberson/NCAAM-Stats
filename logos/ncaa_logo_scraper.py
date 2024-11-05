import pandas as pd
import os


df = pd.read_csv("team_ids.csv")

def rename_file(old_name, new_name):
  """Renames a file from old_name to new_name."""

  try:
    os.rename(f"{old_name}", f"{new_name}")
    print(f"File '{old_name}' renamed to '{new_name}'")
  except FileNotFoundError:
    print(f"Error: File '{old_name}' not found.")
  except OSError as e:
    print(f"Error renaming file: {e}")

for index, row in df.iterrows():
  team = row["team"]
  id = row["team.id"]
  rename_file(f"{id}.png",f"{team}.png")