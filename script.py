import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Load and preprocess data
def load_data():
    # Simulate Current Quiz Data
    current_quiz_data = {
        'Question ID': [1, 2, 3, 4, 5],
        'Topic': ['Algebra', 'Geometry', 'Biology', 'Chemistry', 'Physics'],
        'Difficulty': ['Easy', 'Medium', 'Hard', 'Medium', 'Hard'],
        'Response': ['Correct', 'Incorrect', 'Correct', 'Incorrect', 'Correct']
    }

    # Simulate Historical Quiz Data
    historical_quiz_data = [
        {'Quiz ID': 1, 'Scores': 75, 'Responses': {1: 'Correct', 2: 'Incorrect', 3: 'Correct', 4: 'Correct', 5: 'Incorrect'}},
        {'Quiz ID': 2, 'Scores': 65, 'Responses': {1: 'Incorrect', 2: 'Correct', 3: 'Incorrect', 4: 'Correct', 5: 'Correct'}},
        {'Quiz ID': 3, 'Scores': 80, 'Responses': {1: 'Correct', 2: 'Correct', 3: 'Correct', 4: 'Incorrect', 5: 'Incorrect'}},
        {'Quiz ID': 4, 'Scores': 70, 'Responses': {1: 'Correct', 2: 'Correct', 3: 'Incorrect', 4: 'Incorrect', 5: 'Correct'}},
        {'Quiz ID': 5, 'Scores': 85, 'Responses': {1: 'Correct', 2: 'Correct', 3: 'Correct', 4: 'Correct', 5: 'Correct'}}
    ]

    current_quiz_df = pd.DataFrame(current_quiz_data)
    historical_quiz_df = pd.DataFrame(historical_quiz_data)

    return current_quiz_df, historical_quiz_df

# Analyze performance trends
def analyze_data(current_df, historical_df):
    # Average Score
    avg_score = historical_df['Scores'].mean()

    # Topic-wise Accuracy
    topic_accuracy = current_df.groupby('Topic')['Response'].apply(lambda x: (x == 'Correct').mean())

    # Difficulty-level Accuracy
    difficulty_accuracy = current_df.groupby('Difficulty')['Response'].apply(lambda x: (x == 'Correct').mean())

    return topic_accuracy, difficulty_accuracy, avg_score

# Generate recommendations
def generate_recommendations(topic_accuracy, difficulty_accuracy, avg_score):
    recommendations = []

    # Weak topics
    for topic, accuracy in topic_accuracy.items():
        if accuracy < 0.7:
            recommendations.append(f"Focus more on the topic: {topic}.")

    # Difficulty levels
    for difficulty, accuracy in difficulty_accuracy.items():
        if accuracy < 0.7:
            recommendations.append(f"Practice more {difficulty}-level questions.")

    # General advice
    if avg_score < 75:
        recommendations.append("Overall performance can be improved by revising key concepts.")

    return recommendations

# Visualization
def visualize_data(current_df, historical_df):
    # Topic-wise Accuracy Plot
    topic_accuracy = current_df.groupby('Topic')['Response'].apply(lambda x: (x == 'Correct').mean())
    topic_accuracy.plot(kind='bar', color='skyblue', title='Topic-Wise Accuracy')
    plt.xlabel('Topic')
    plt.ylabel('Accuracy')
    plt.show()

    # Historical Scores Trend
    historical_df.plot(x='Quiz ID', y='Scores', marker='o', title='Historical Performance', color='orange')
    plt.xlabel('Quiz ID')
    plt.ylabel('Scores')
    plt.show()

# Main function
def main():
    current_quiz_df, historical_quiz_df = load_data()
    topic_accuracy, difficulty_accuracy, avg_score = analyze_data(current_quiz_df, historical_quiz_df)
    recommendations = generate_recommendations(topic_accuracy, difficulty_accuracy, avg_score)

    print("\nPersonalized Recommendations:")
    for rec in recommendations:
        print(f"- {rec}")

    visualize_data(current_quiz_df, historical_quiz_df)

if __name__ == "__main__":
    main()
