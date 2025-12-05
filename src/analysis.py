import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Create dummy data (so you don't need to upload a CSV right now)
data = {
    'Date': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Sales': [150, 200, 180, 220, 300]
}
df = pd.DataFrame(data)

# 2. specific print so we can see it in the logs
print("Generating plot...")

# 3. Create the plot
plt.figure(figsize=(8, 5))
plt.bar(df['Date'], df['Sales'], color='skyblue')
plt.title('Weekly Sales Analysis')
plt.xlabel('Day')
plt.ylabel('Revenue ($)')

# 4. SAVE THE FILE (This is the critical part!)
# We save it to the current folder so the Action can find it
plt.savefig('sales_plot.png')

# 5. Verify the file exists
if os.path.exists('sales_plot.png'):
    print("SUCCESS: sales_plot.png created!")
else:
    print("ERROR: File was not created.")
