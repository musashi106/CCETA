import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv("D:\IP PROJECT\Carbon capture Technology\carbon_capture_data.csv")

print("Welcome to the Carbon Capture Efficiency Analyzer!")

# Dictionary to match user input to column names
metrics = {
    '1': 'CO2_Captured (tons/year)',
    '2': 'Energy_Used (kWh/ton)',
    '3': 'Cost_Per_Ton (USD)'
}

# Loop to keep the program running
while True:
    print("\nSelect the data you want to analyze:")
    print("1. CO₂ Captured (tons/year)")
    print("2. Energy Used (kWh/ton)")
    print("3. Cost per Tonne (USD)")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '4':
        print("Goodbye!")
        break

    if choice not in metrics:
        print("Invalid choice. Try again.")
        continue

    metric = metrics[choice]

    print("\nChoose a type of graph to display:")
    print("1. Bar Chart")
    print("2. Horizontal Bar Chart")
    print("3. Pie Chart")
    print("4. Line Chart")
    print("5. Scatter Plot")
    chart_choice = input("Enter your choice (1-5): ")

    # Sort data for better visuals
    chart_data = data.sort_values(by=metric, ascending=False)

    plt.figure(figsize=(10, 6))
    title = f"{metric} by Technology"

    if chart_choice == '1':
        plt.bar(chart_data['Technology'], chart_data[metric], color='skyblue')
        plt.xlabel("Technology")
        plt.ylabel(metric)
        plt.xticks(rotation=45, ha='right', fontsize=9)

    elif chart_choice == '2':
        plt.barh(chart_data['Technology'], chart_data[metric], color='lightgreen')
        plt.xlabel(metric)
        plt.ylabel("Technology")
        plt.gca().invert_yaxis()

    elif chart_choice == '3':
        plt.figure(figsize=(8, 8))
        plt.pie(chart_data[metric], labels=chart_data['Technology'], autopct='%1.1f%%', startangle=140, textprops={'fontsize': 9})
        title = f"{metric} Distribution"

    elif chart_choice == '4':
        plt.plot(chart_data['Technology'], chart_data[metric], marker='o', color='orange')
        plt.xlabel("Technology")
        plt.ylabel(metric)
        plt.xticks(rotation=45, ha='right', fontsize=9)

    elif chart_choice == '5':
        plt.scatter(chart_data['Technology'], chart_data[metric], color='purple', marker='D')
        plt.xlabel("Technology")
        plt.ylabel(metric)
        plt.xticks(rotation=45, ha='right', fontsize=9)

    else:
        print("Invalid graph option. Returning to main menu.")
        continue

    plt.title(title)
    plt.tight_layout()
    plt.grid(False)
    plt.show()
