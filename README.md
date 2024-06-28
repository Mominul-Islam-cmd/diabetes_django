# 🚀 Project Overview

📌 Title: Diabetes Prediction Using KNN and Deployment with Django

🎯 Objective

To predict whether a patient has diabetes using the K-Nearest Neighbors (KNN) machine learning algorithm. The model will be trained on data sourced from Kaggle and deployed using Django, rendered via a web platform.
________________________________________
📊 Data Source and Preprocessing

📂 Dataset

The dataset used for this project is sourced from Kaggle and contains various medical predictor variables and one target variable indicating the presence of diabetes.
## 🧹 Data Preprocessing
- **Handling Missing Values**: Missing values were addressed appropriately in the dataset.
- **One-Hot Encoding**: Categorical features were converted to numerical values using one-hot encoding.
- **Feature Scaling**: The features were scaled to a standard range using StandardScaler from the `sklearn` library.

## 🤖 Machine Learning Model
- **Algorithm Used**: K-Nearest Neighbors (KNN)

### 📊 Steps Involved
1. **Data Splitting**: The dataset was split into training and testing sets.
2. **Model Training**: The KNN model was trained on the processed training data.
3. **Model Evaluation**: The trained model was evaluated on the testing data, achieving an accuracy of 96%.

### 📈 Model Performance
- **Accuracy**: 96%
- **Precision, Recall, F1-Score**: Detailed classification report is included in the notebook, showing high performance for class 0 and relatively lower performance for class 1.

________________________________________
## 🌐 Deployment with Django
- **🖥️ Framework**: Django for web application deployment.

### 📝 Steps
1. **🛠️ Create a Django project**: Set up a new Django project and configure the necessary settings.
2. **🏗️ Build the app**: Create an app within the Django project for handling predictions.
3. **🔗 Integrate the model**: Load the trained KNN model into the Django app to make predictions on user input.
4. **🎨 Create views and templates**: Design the front end to allow users to input data and view predictions.
5. **☁️ Deploy using Render**: Deploy the Django app using Render for seamless web hosting.
