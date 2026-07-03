import pandas as pd

results_path = r"runs/detect/train-8/results.csv"

df = pd.read_csv(results_path)

last_row = df.iloc[-1]

precision = last_row['metrics/precision(B)']
recall = last_row['metrics/recall(B)']
map50 = last_row['metrics/mAP50(B)']
map5095 = last_row['metrics/mAP50-95(B)']

accuracy = (precision + recall) / 2

print("\nFINAL MODEL RESULTS\n")

print(f"Detection Accuracy : {accuracy*100:.2f}%")
print(f"Precision          : {precision*100:.2f}%")
print(f"Recall             : {recall*100:.2f}%")
print(f"mAP@50             : {map50*100:.2f}%")
print(f"mAP@50-95          : {map5095*100:.2f}%")

