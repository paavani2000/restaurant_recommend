# 🍽️ Decentralized Restaurant Recommendation System

A cross-platform restaurant recommendation system that combines machine learning, sentiment analysis, and blockchain to provide personalized dining suggestions based on user history and Yelp data. Smart contracts ensure transparency and reward users for authentic reviews.


## 📌 Overview

DineSure integrates multiple components into a unified platform:

- 🔗 **[Web Interface](./WebApp)**: A lightweight Flask API backend with ML and sentiment logic  
- 📱 **[Blockchain Layer](./SmartContracts)**: Ethereum smart contracts for review incentives  
- 🧠 **[Data Engine](./BigDataPipeline)**: Processes and analyzes large-scale Yelp and user-generated data

The system tailors recommendations to user behavior while ensuring data integrity and fair rewards through blockchain.


## 🚀 Core Features

- 🧠 **Personalized Recommendations** : Collaborative filtering using cosine similarity and matrix factorization on user history

- 💬 **Sentiment-Enhanced Suggestions** : NLP analysis of user reviews to improve result relevance

- 🔗 **Verified Reviews** : Solidity smart contracts reward authentic reviews with loyalty points

- 🛡️ **Data Integrity** : Blockchain-backed review tracking to prevent tampering

- 📊 **Big Data Processing** : Scalable ingestion and analysis of Yelp and user-generated data

- 🌐 **Yelp API Integration** : Real-world restaurant metadata and reviews


## 🛠️ Tech Stack

- **Python** – ML modeling and backend logic  
- **Flask** – REST API layer  
- **Scikit-learn, VADER** – Recommendation algorithms and sentiment analysis  
- **Solidity, Ethereum Testnet** – Smart contract development  
- **Web3.py, Ganache** – Blockchain integration and testing  
- **Yelp API** – Restaurant metadata and review content
