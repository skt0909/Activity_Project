from flask import Flask, render_template
import plotly.io as pio
import plotly.graph_objects as go
import numpy as np
from Activity_pstructure.src.data_loader import fetch_data_from_mongo  # Import the function here

# Initialize Flask app
app = Flask(__name__)

# Function to generate the plots
def generate_plots():
    features_columns = ['steps', 'distance', 'trackerDistance', 'loggedActivitiesDistance',
                        'veryActiveDistance', 'moderatelyActiveDistance', 'lightActiveDistance',
                        'sedentaryActiveDistance', 'veryActiveMinutes', 'fairlyActiveMinutes',
                        'lightlyActiveMinutes', 'sedentaryMinutes']

    # Fetch data from MongoDB using the imported function
    documents = fetch_data_from_mongo()

    # Extract feature data from the documents
    data = []
    for doc in documents:
        feature_row = [doc.get(col, 0) for col in features_columns]
        data.append(feature_row)

    features = np.array(data)

    # Simulating activity predictions for demonstration purposes
    activity_predictions = np.random.rand(len(features)) * 2000

    # Create activity completion plot
    target_max = 2800
    activity_completed = activity_predictions[0]
    percentage_completed = (activity_completed / target_max) * 100
    percentage_completed = min(percentage_completed, 100)

    activity_fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=percentage_completed,
        title={"text": "Activity Completion (%)"},
        gauge={
            "axis": {"range": [None, 100]},
            "bar": {"color": "#114c79"},
            "steps": [
                {"range": [0, 25], "color": "#d4f0fc"},
                {"range": [25, 50], "color": "#89d6fb"},
                {"range": [50, 75], "color": "#02a9f7"},
                {"range": [75, 100], "color": "#02577a"}
            ],
            "threshold": {"line": {"color": "black", "width": 4}, "thickness": 0.75, "value": percentage_completed}
        }
    ))
    activity_fig.update_layout(
    paper_bgcolor="#222222",  # Dark background for the whole figure
    plot_bgcolor="#121212",   # Dark background for the plot area
    font={'color': "#ffffff"},  

    )

    # Diet prediction pie chart
    diet_predictions = activity_predictions * 0.75
    diet_target = 2000
    diet_remaining = diet_target - diet_predictions[0]
    percentage_remaining = (diet_remaining / diet_target) * 100
    percentage_remaining = max(min(percentage_remaining, 100), 0)

    diet_fig = go.Figure(data=[go.Pie(
        labels=['Remaining Diet', 'Completed Diet'],
        values=[percentage_remaining, 100 - percentage_remaining],
        hole=0.3,
        title="Progress",
        marker=dict(colors=['#d4f0fc', '#02a9f7'])
    )])
    diet_fig.update_layout(
    paper_bgcolor="#222222",  # Dark background for the whole figure
    plot_bgcolor="#121212",   # Dark background for the plot area
    font={'color': "#ffffff"},
    )

    # Sleep recommendation gauge chart
    sleep_recommendation = 8 - (activity_predictions / np.max(activity_predictions)) * 4

    sleep_fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=sleep_recommendation[0],
        title={'text': "Recommended Sleep (Hours)"},
        gauge={
            'axis': {'range': [None, 8]},
            'steps': [
                {'range': [0, 4], 'color': "#d4f0fc"},
                {'range': [4, 8], 'color': "#89d6fb"}
            ],
            'bar': {'color': "#114c79"}
        }
    ))
    # Set the dark theme for the figure background
    sleep_fig.update_layout(
    paper_bgcolor="#222222",  # Dark background for the whole figure
    plot_bgcolor="#121212",   # Dark background for the plot area
    font={'color': "#ffffff"}, # White font color for readability
    )

    # Convert figures to HTML for embedding
    activity_plot_html = pio.to_html(activity_fig, full_html=False)
    diet_plot_html = pio.to_html(diet_fig, full_html=False)
    sleep_plot_html = pio.to_html(sleep_fig, full_html=False)

    return activity_plot_html, diet_plot_html, sleep_plot_html

# Route to display the plots
@app.route('/')
def index():
    activity_plot_html, diet_plot_html, sleep_plot_html = generate_plots()
    return render_template('index.html', 
                           activity_plot=activity_plot_html,
                           diet_plot=diet_plot_html,
                           sleep_plot=sleep_plot_html)

if __name__ == '__main__':
    app.run(debug=True)


"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Activity Dashboard</title>
    <style>
        body {
            background-color: black;
            color: white;
        }
        .plot-container {
            display: flex;
            justify-content: space-around;
        }
        .plot-container > div {
            width: 30%;
            height: 400px;
        }

    </style>
</head>
<body>
    <h1 style="text-align: center;">Activity Dashboard</h1>
    <div class="plot-container">
        <div>
            <h3>Activity Completion</h3>
            {{ activity_plot|safe }}
        </div>
        <div>
            <h3>Diet Progress</h3>
            {{ diet_plot|safe }}
        </div>
        <div>
            <h3>Recommended Sleep</h3>
            {{ sleep_plot|safe }}
        </div>
    </div>
</body>
</html>
"""