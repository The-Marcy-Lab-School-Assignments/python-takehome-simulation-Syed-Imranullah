# NYC 311 Service Requests Analysis

## How to Run

1. Make sure you have Python 3 installed.
2. Navigate to this folder in your terminal.
3. Run the script:

```
python3 analysis.py
```

The results will be saved to `output.txt`. You'll also see a confirmation message in the terminal once it's done.

## What This Script Does

I pulled a sample of 100 NYC 311 service requests and wrote a script to dig into the data. It figures out how many requests are still open, what people are complaining about the most, and how each borough stacks up in terms of volume and how quickly they close out requests.

Here's a quick summary of what it found:
- **17 open requests** out of 100
- **Noise - Residential** was the most common complaint (30 requests)
- **Brooklyn** had the most open requests (5), but **Queens** had the best closure rate at 90%

## Dependencies

Just Python's built-in `csv` module — no installs needed.

## Notes

The dataset is a small sample (100 rows), so the numbers aren't meant to be statistically significant — this was more about practicing working with CSV data and writing loops to aggregate things manually without using any external libraries.
