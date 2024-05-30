# Part-of-Speech Tagging System

## Overview
This project involves the development of a Part-of-Speech (POS) tagging system from scratch using the Viterbi algorithm. The system tags each word in a sentence with its corresponding part of speech, leveraging a large dataset that required extensive data cleaning and preprocessing.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Implementation](#implementation)
- [Challenges](#challenges)


## Introduction
The goal of this project is to build a POS tagging system that accurately tags words in a sentence with their respective parts of speech. The system uses the Viterbi algorithm, a dynamic programming algorithm, to determine the most probable sequence of tags.

## Dataset
A large, raw dataset was utilized for this project, which required substantial data cleaning and preprocessing. The dataset contains sentences with corresponding POS tags used to train and test the tagging system.

## Methodology
The Viterbi algorithm was implemented to efficiently find the most probable sequence of POS tags for a given sentence. This involves:
1. **Data Cleaning**: Handling missing values, removing noise, and normalizing the dataset.
2. **Training**: Using the cleaned dataset to train the Viterbi algorithm.
3. **Tagging**: Applying the trained model to tag new sentences.

## Implementation
The implementation details are as follows:
1. **Data Preprocessing**: Scripts to clean and preprocess the dataset.
2. **Viterbi Algorithm**: Core implementation of the Viterbi algorithm in Python.
3. **Evaluation**: Functions to evaluate the accuracy of the POS tagging system.

## Challenges
- **Data Quality**: Ensuring the dataset was clean and free of inconsistencies.
- **Algorithm Efficiency**: Optimizing the Viterbi algorithm for performance.
- **Accuracy**: Achieving high accuracy in tagging across diverse sentence structures.

## Results
The POS tagging system demonstrated high accuracy and performance in tagging words with their correct parts of speech. Detailed results and performance metrics can be found in the [results](results/) directory.

