import csv

rows = []

with open('nyc_311_requests.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)
        
open_count = 0

for row in rows:
    if row['resolution_status'] == 'Open':
        open_count += 1

complaint_counts = {}

for row in rows:
    complaint = row['complaint_type']
    if complaint in complaint_counts:
        complaint_counts[complaint] += 1
    else:
        complaint_counts[complaint] = 1

most_common = max(complaint_counts, key=complaint_counts.get)

borough_counts = {}

for row in rows:
    borough = row['borough']
    if borough in borough_counts:
        borough_counts[borough] += 1
    else:
        borough_counts[borough] = 1

open_by_borough = {}

for row in rows:
    if row['resolution_status'] == 'Open':
        borough = row['borough']
        if borough in open_by_borough:
            open_by_borough[borough] += 1
        else:
            open_by_borough[borough] = 1

most_open_borough = max(open_by_borough, key=open_by_borough.get)

closed_by_borough = {}

for row in rows:
    if row['resolution_status'] == 'Closed':
        borough = row['borough']
        if borough in closed_by_borough:
            closed_by_borough[borough] += 1
        else:
            closed_by_borough[borough] = 1

sorted_boroughs = sorted(borough_counts, key=lambda b: (-borough_counts[b], b))
top_3 = sorted_boroughs[:3]

sorted_complaints = sorted(complaint_counts, key=complaint_counts.get, reverse=True)

with open('output.txt', 'w') as f:
    f.write(f"Open requests: {open_count}\n")
    f.write("\n")
    f.write(f"Most common complaint type: {most_common} ({complaint_counts[most_common]} requests)\n")
    f.write("\n")
    f.write("Requests per borough:\n")
    for borough in sorted(borough_counts):
        f.write(f"- {borough}: {borough_counts[borough]}\n")
    f.write("\n")
    f.write("Requests by complaint type:\n")
    
    for complaint in sorted_complaints:
        f.write(f"- {complaint}: {complaint_counts[complaint]}\n")
    f.write("\n")
    f.write(f"Borough with most open requests: {most_open_borough} ({open_by_borough[most_open_borough]} open)\n")
    f.write("\n")
    f.write("Closure rate by borough:\n")
    for borough in sorted(borough_counts):
        rate = closed_by_borough[borough] / borough_counts[borough] * 100
        f.write(f"- {borough}: {rate:.1f}%\n")
    f.write("\n")
    f.write("Top 3 boroughs by total requests:\n")
    for i, borough in enumerate(top_3):
        f.write(f"{i + 1}. {borough} ({borough_counts[borough]} requests)\n")
print("Output saved to output.txt")