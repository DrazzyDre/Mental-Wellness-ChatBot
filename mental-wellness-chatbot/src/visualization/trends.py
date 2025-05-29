import matplotlib.pyplot as plt
import pandas as pd

def plot_emotional_trends(data):
    """
    Plots emotional trends over time.

    Parameters:
    data (pd.DataFrame): A DataFrame containing 'date' and 'emotion' columns.

    Returns:
    None
    """
    # Ensure the 'date' column is in datetime format
    data['date'] = pd.to_datetime(data['date'])
    
    # Group by date and emotion, counting occurrences
    trend_data = data.groupby(['date', 'emotion']).size().unstack(fill_value=0)

    # Plotting
    plt.figure(figsize=(12, 6))
    for emotion in trend_data.columns:
        plt.plot(trend_data.index, trend_data[emotion], label=emotion)

    plt.title('Emotional Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Frequency')
    plt.legend(title='Emotions')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()