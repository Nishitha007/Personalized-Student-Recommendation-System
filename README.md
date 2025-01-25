# Personalized Student Recommendations

This project provides a Python-based solution to analyze student quiz performance and generate personalized recommendations for improving their preparation. The solution processes both current and historical quiz data, identifies weak areas, and proposes actionable steps for improvement.

## Features
- **Data Analysis**: Identifies performance trends by topic, difficulty, and accuracy.
- **Insights Generation**: Highlights strengths, weaknesses, and improvement trends.
- **Personalized Recommendations**: Suggests specific topics and question types to focus on.
- **Visualization**: Includes graphical insights for performance tracking.

## Data Overview
### Current Quiz Data
Details about the latest quiz submission, including:
- Question ID
- Topic
- Difficulty level
- Response (Correct/Incorrect)

### Historical Quiz Data
Performance data from the last 5 quizzes, including:
- Scores
- Response maps (Key: Question ID, Value: Selected option)

## How to Run the Project
### Prerequisites
1. Install Python (>= 3.8).
2. Install required libraries:
   ```bash
   pip install pandas matplotlib seaborn
   ```

### Running the Script
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <repository_name>
   ```
3. Run the script:
   ```bash
   python script.py
   ```

### Expected Output
- **Textual Insights**: Summary of weak areas and improvement suggestions.
- **Visualizations**: Graphical representation of topic-wise accuracy and performance trends.

## Approach
1. **Data Loading**: Simulated datasets are used to represent API data for current and historical quizzes.
2. **Analysis**:
   - Calculate topic-wise and difficulty-level accuracy.
   - Compute average historical scores.
3. **Recommendations**:
   - Highlight topics and difficulty levels requiring improvement.
   - Provide general advice based on average performance.
4. **Visualization**:
   - Bar charts for topic accuracy.
   - Line charts for historical scores.

## Sample Output
### Insights
- Weak topics: Geometry, Chemistry
- Suggested focus areas: Medium-difficulty questions
- General advice: "Revise key concepts for overall improvement."

### Visualizations
- **Topic-Wise Accuracy**: ![Topic Accuracy](visualizations/topic_accuracy.png)
- **Historical Scores**: ![Historical Scores](visualizations/historical_scores.png)

## Demo Video
A 2-5 minute demonstration of the script in action is available in the `demo/` folder.

## Submission Checklist
- [x] Python script with analysis and recommendations.
- [x] README file with project details.
- [x] Visualizations for key insights.
- [x] Demo video showcasing the solution.

## License
This project is licensed under the MIT License.

