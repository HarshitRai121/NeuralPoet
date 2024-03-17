# NeuralPoet

NeuralPoet is an innovative project that combines machine learning with web development to create a dynamic platform for text generation. Using a Long Short-Term Memory (LSTM) model, NeuralPoet generates artistic and poetic text based on user-defined parameters.

## Table of Contents
1. [Introduction](#introduction)
2. [System Architecture](#system-architecture)
3. [Backend Implementation](#backend-implementation)
4. [Frontend Design](#frontend-design)
5. [User Interaction](#user-interaction)
6. [Model Training and Data](#model-training-and-data)
7. [Deployment and Running Instructions](#deployment-and-running-instructions)

## Introduction

### Background
NeuralPoet explores the synergy between machine learning and web development by offering a platform where users can experience the creativity of a pre-trained LSTM model. The project utilizes a subset of Shakespeare's text for model training and allows users to input parameters such as length and temperature to generate diverse textual outputs.

### Objectives
- Implement a Flask backend to handle user requests and interact with the LSTM model.
- Develop an LSTM model using TensorFlow and Keras for creative text generation.
- Design a user-friendly frontend with HTML and CSS for user interaction.
- Provide an interactive experience for users interested in exploring the capabilities of the LSTM model.

## System Architecture

### Overview of Components
1. Flask Backend (app.py): Handles HTTP requests, loads the pre-trained LSTM model, and defines routes for user interaction.
2. Model Utilities (model_utils.py): Prepares training data, defines the LSTM model architecture, and provides utility functions for text generation.
3. Frontend (HTML and CSS): User interface allowing users to input parameters and visualize generated text.

### Interaction Between Components
The Flask backend communicates with the LSTM model through the model_utils module. The frontend interacts with the Flask backend through defined routes (/ and /generate_text).

### Data Flow
User input is collected through the frontend, sent as a JSON payload to the /generate_text endpoint, processed by the Flask backend, and the generated text is displayed on the frontend.

## Backend Implementation

### Flask Application (app.py)
- Route Definitions
- Model Loading

### Model Utilities (model_utils.py)
- Text Preparation
- LSTM Model Architecture
- Data Transformation
- Text Generation Function

### LSTM Model (trained_model.h5)
Stores the pre-trained LSTM model details.

## Frontend Design

### HTML Structure (index.html)
- Input Fields
- Button
- Output Section

### Stylesheet (styles.css)
Defines the visual aspects of the webpage for a better user experience.

## User Interaction

### Input Parameters
Users can input desired length and temperature values through the user interface.

### Text Generation Process
Clicking the "Generate Text" button triggers text generation using the LSTM model.

### Backend Processing
The Flask backend processes user input, generates text, and sends it back to the frontend for display.

### Output Display
The generated text is displayed in the output section of the webpage.

## Model Training and Data

### Training Data Source
The LSTM model is trained on a subset of Shakespeare's text.

### Model Architecture
LSTM layer with 128 units followed by a Dense layer with softmax activation.

### Training Process
The model is trained using the RMSprop optimizer and categorical cross-entropy loss.

## Deployment and Running Instructions

### Dependency Installation
Execute `pip install -r requirements.txt` to install required dependencies.

### Running the Flask Application
Run `python app.py` in the terminal to start the Flask application.

### Accessing the Web Application
Navigate to http://localhost:5000 to access the NeuralPoet application.

### Generating Text
Enter desired parameters, click "Generate Text," and view the generated text in the output section.

---

