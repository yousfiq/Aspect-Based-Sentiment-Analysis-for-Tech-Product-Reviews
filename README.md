# Aspect-Based-Sentiment-Analysis-for-Tech-Product-Reviews# Aspect-Based Sentiment Analysis (ABSA)

## Overview
This project implements a simple Aspect-Based Sentiment Analysis system using a pre-trained NLP model.  
The system analyzes product reviews and determines the sentiment (positive or negative) for specific aspects such as performance, battery, design, and more.

---

## Objective
The goal of this project is to:
- Analyze customer reviews automatically  
- Extract sentiment for predefined aspects  
- Convert unstructured text into meaningful insights  

---

## Technologies Used
- Python  
- Hugging Face Transformers  
- Pre-trained sentiment analysis model  

---

## How It Works
1. A list of product reviews is provided  
2. A list of aspects is defined (e.g., battery, performance)  
3. Each review is analyzed for every aspect  
4. The system assigns sentiment (POSITIVE / NEGATIVE)  
5. Results are printed in a structured format  

---

## Installation
Make sure you have Python installed, then install the required library:

bash id="p1k2x9" pip install transformers 

---

## Usage
Run the Python script:

bash id="k9d2lm" python your_file_name.py 

---

## Example Output
id="z8q4nr" Review: The battery is amazing but the screen is bad  battery: POSITIVE (0.98) screen: NEGATIVE (0.95) performance: N/A

---

## Limitations
- This is a basic implementation (not full ABSA)  
- The model analyzes full sentences, not true aspect-level understanding  
- Results may be inaccurate for complex reviews  

---

## Future Improvements
- Use advanced models like BERT for true ABSA  
- Automatically extract aspects from text  
- Support multiple languages (including Arabic)  
- Build a web interface  

---

## Author
Yousif Basheer  
Computer Engineering Student
