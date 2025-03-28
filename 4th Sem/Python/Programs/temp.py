import matplotlib.pyplot as plt

# Data
languages = ['JavaScript', 'HTML/CSS', 'Python', 'SQL', 'TypeScript', 
             'Bash/Shell', 'Java', 'C#', 'C++', 'C']
percentages = [63.61, 52.97, 49.28, 48.66, 38.87, 32.37, 30.55, 27.62, 22.42, 19.34]

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

# Horizontal bar chart
bars = ax.barh(languages, percentages, color='#fc6255')

# Add text annotations to the bars
for bar in bars:
    width = bar.get_width()
    ax.text(width - 5, bar.get_y() + bar.get_height() / 2, 
            f'{width:.2f}%', ha='center', va='center', color='white', fontsize=10)

# Invert y-axis to have the highest values at the top
ax.invert_yaxis()

# Remove spines for a cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Remove x and y ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

# Add title
ax.set_title('Most Popular Programming Languages in 2023', fontsize=15)

# Customize background color
fig.patch.set_facecolor('#283b42')
ax.set_facecolor('#283b42')

# Customize tick labels color
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

# Show the plot
plt.show()
