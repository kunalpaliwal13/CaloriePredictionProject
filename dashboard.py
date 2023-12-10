import plotly
import plotly.graph_objs as go
import plotly.offline as opy
import sqlite3
import plotly.express as px
import json
import pandas as pd


def fetch_data(userid):
    conn = sqlite3.connect('Calorie.db')
    cursor = conn.cursor()


    # Example query: Retrieve total quantity sold for each product
    query = "SELECT exercise_name, duration, date, calories, bpm FROM exercise WHERE userid = ?"
    cursor.execute(query, (userid,))
    data = cursor.fetchall()

    uquery = "SELECT exercise_name, duration, date, calories, bpm FROM exercise WHERE userid = ?"
    cursor.execute(query, (userid,))
    data_with_bpm = cursor.fetchall()


    # Example query: Retrieve total quantity sold over time
    time_query = "SELECT date, calories FROM exercise WHERE userid = ?"
    cursor.execute(time_query, (userid,))
    time_data = cursor.fetchall()

    calories_query = "SELECT exercise_name, calories FROM exercise WHERE userid = ?"
    cursor.execute(calories_query, (userid,))
    calories_data = cursor.fetchall()

    heart_query = "SELECT bpm, calories FROM exercise WHERE userid = ?"
    cursor.execute(heart_query, (userid,))
    heart_data = cursor.fetchall()

    import pandas as pd
    df = pd.read_csv("calorie_prediction_db")
    correlation_matrix = df.corr()

    cursor.close()
    conn.close()

    return data, time_data, calories_data, heart_data, correlation_matrix, data_with_bpm


"""
def create_bar_chart(data):
    exercise, duration = zip(*data)

    trace = go.Bar(x=exercise, y=duration)
    layout = go.Layout(title='Exercise vs duration', xaxis=dict(title='Exercise'), yaxis=dict(title='Duration'))
    fig = go.Figure(data=[trace], layout=layout)

    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


def create_line_chart(time_data):
    date, calories = zip(*time_data)

    trace = go.Scatter(x=date, y=calories, mode='lines+markers', marker=dict(size=10), line=dict(width=2))
    layout = go.Layout(title='Total Calories Over Time', xaxis=dict(title='Date'), yaxis=dict(title='Total Calories'))
    fig = go.Figure(data=[trace], layout=layout)

    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

def create_pie_chart(data, title):
    exercise_names, calories = zip(*data)

    trace = go.Pie(labels=exercise_names, values=calories)
    layout = go.Layout(title=title)
    fig = go.Figure(data=[trace], layout=layout)

    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

def create_heart_rate_scatter_plot(data):
    bpm, calories = zip(*data)

    trace = go.Scatter(x=bpm, y=calories, mode='markers', marker=dict(size=12))
    layout = go.Layout(title='Heart Rate vs. Calories Burned', xaxis=dict(title='Heart Rate (BPM)'), yaxis=dict(title='Calories Burned'))
    fig = go.Figure(data=[trace], layout=layout)

    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
"""


def create_bar_chart(data):
    exercise, duration, date, calories, bpm = zip(*data)

    # Convert 'duration' to numeric
    duration = pd.to_numeric(duration, errors='coerce')

    trace = go.Bar(x=exercise, y=duration)
    layout = go.Layout(title='Exercise vs duration', xaxis=dict(
        title='Exercise'), yaxis=dict(title='Duration'))
    fig = go.Figure(data=[trace], layout=layout)

    return opy.plot(fig, auto_open=False, output_type='div')



def create_line_chart(time_data):
    date, calories = zip(*time_data)

    calories = pd.to_numeric(calories, errors='coerce')

    trace = go.Scatter(x=date, y=calories, mode='lines+markers',
                       marker=dict(size=10), line=dict(width=2))
    layout = go.Layout(title='Total Calories Over Time', xaxis=dict(
        title='Date'), yaxis=dict(title='Total Calories'))
    fig = go.Figure(data=[trace], layout=layout)

    return opy.plot(fig, auto_open=False, output_type='div')


def create_pie_chart(data, title):
    exercise_names, calories = zip(*data)

    trace = go.Pie(labels=exercise_names, values=calories)
    layout = go.Layout(title=title)
    fig = go.Figure(data=[trace], layout=layout)

    return opy.plot(fig, auto_open=False, output_type='div')


def create_heart_rate_scatter_plot(data):
    bpm, calories = zip(*data)

    bpm = pd.to_numeric(bpm, errors='coerce')
    calories = pd.to_numeric(calories, errors='coerce')

    trace = go.Scatter(x=bpm, y=calories, mode='markers', marker=dict(size=12))
    layout = go.Layout(title='Heart Rate vs. Calories Burned', xaxis=dict(
        title='Heart Rate (BPM)'), yaxis=dict(title='Calories Burned'))
    fig = go.Figure(data=[trace], layout=layout)

    return opy.plot(fig, auto_open=False, output_type='div')



def create_heatmap(correlation_matrix):
    # Customize the color scale (you can choose any color scale from Plotly)
    color_scale = 'Mint'

    fig = px.imshow(correlation_matrix, labels=dict(color="Correlation"), 
                    x=correlation_matrix.columns, y=correlation_matrix.columns,
                    color_continuous_scale=color_scale)

    fig.update_layout(title="Variable Correlation Heatmap")
    return opy.plot(fig, auto_open=False, output_type='div')

def create_exercise_vs_calories_chart(data):
    # Assuming data is a list of tuples where each tuple contains exercise_name and calories
    exercise, duration, date, calories, bpm = zip(*data)

    # Convert 'calories' to numeric
    calories = pd.to_numeric(calories, errors='coerce')

    trace = go.Bar(x=exercise, y=calories)
    layout = go.Layout(title='Exercise vs Calories Burned', xaxis=dict(title='Exercise'), yaxis=dict(title='Calories Burned'))
    fig = go.Figure(data=[trace], layout=layout)

    return opy.plot(fig, auto_open=False, output_type='div')
    

def create_violin_plot(data):
    exercise, duration, date, calories, bpm = zip(*data)

    # Convert 'duration' and 'bpm' to numeric
    duration = pd.to_numeric(duration, errors='coerce')
    bpm = pd.to_numeric(bpm, errors='coerce')

    fig = px.violin(y=duration, x=bpm, box=True, points="all",
                    labels={'y': 'Exercise Duration', 'x': 'Heart Rate (BPM)'})

    fig.update_layout(title='Exercise Duration vs. Heart Rate')
    return opy.plot(fig, auto_open=False, output_type='div')

def create_temperature_vs_exercise_plot(data):
    exercise, duration, date, calories, bpm = zip(*data)

    combined_data = list(zip(exercise, bpm))
    sorted_data = sorted(combined_data, key=lambda x: x[0])
    sorted_exercise, sorted_bpm = zip(*sorted_data)

    # Convert 'sorted_bpm' to numeric
    sorted_bpm = pd.to_numeric(sorted_bpm, errors='coerce')

    trace = go.Scatter(x=sorted_exercise, y=sorted_bpm, mode='markers', marker=dict(size=12))
    layout = go.Layout(title='Body Temperature vs Exercise', xaxis=dict(
        title='Exercise'), yaxis=dict(title='Body Temperature'))
    fig = go.Figure(data=[trace], layout=layout)

    return opy.plot(fig, auto_open=False, output_type='div')


def heart_rate_over_time(data):
    exercise, duration, date, calories, bpm = zip(*data)

    # Convert 'calories' to numeric
    calories = pd.to_numeric(calories, errors='coerce')

    trace = go.Scatter(x=date, y=bpm, mode='lines+markers',
                       marker=dict(size=10), line=dict(width=2))
    layout = go.Layout(title='Heart Rate Over Time', xaxis=dict(
        title='Date'), yaxis=dict(title='Heart Rate (BPM)'))
    fig = go.Figure(data=[trace], layout=layout)

    return opy.plot(fig, auto_open=False, output_type='div')


def heart_rate_track(data):
    exercise, duration, date, calories, bpm = zip(*data)

    # Define heart rate zones and their corresponding BPM ranges
    heart_rate_zones = {'Low': (0, 100), 'Moderate': (100, 150), 'High': (150, float('inf'))}

    # Calculate the distribution of heart rate zones
    zone_distribution = {'Low': 0, 'Moderate': 0, 'High': 0}

    for bpm_value in bpm:
        bpm_float = float(bpm_value)
        for zone, (lower, upper) in heart_rate_zones.items():
            if lower <= bpm_float < upper:
                zone_distribution[zone] += 1
                break

    # Create a pie chart
    labels = list(zone_distribution.keys())
    values = list(zone_distribution.values())

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

    # Update layout
    fig.update_layout(
        title='Heart Rate Zone Distribution',
        showlegend=True
    )

    div = opy.plot(fig, auto_open=False, output_type='div')
    return div