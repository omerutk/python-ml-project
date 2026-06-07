# YZM1022 Project - ML Preprocessing Pipeline

This is my project for the Advanced Programming Course. It is a Python machine learning library that helps clean up messy datasets. It can fill in missing data, scale numbers, and load files concurrently.

## How to install
To install this library so you can use it in your scripts, open your terminal in this folder and run:

```bash
pip install -e .
```


## How to use it
Here is a quick example of how you can use my code to clean a dataset:

from my_ml_pipeline.data import ConcurrentDataLoader
from my_ml_pipeline.core import MeanStrategy, MissingValueImputer, FeatureScaler, StandardMLPipeline

## 1. Set up the tools
loader = ConcurrentDataLoader()
imputer = MissingValueImputer(strategy=MeanStrategy())
scaler = FeatureScaler(method="minmax")

## 2. Put them in the pipeline
pipeline = StandardMLPipeline(loader, imputer, scaler)

## 3. Run it on your data
cleaned_data = pipeline.execute_pipeline('messy_data.csv', 'Age', ['Salary'])
print(cleaned_data)



## Design Patterns I Used
Strategy Pattern: I used this in the MissingValueImputer. Instead of hardcoding the math inside the imputer, I made separate strategy classes (like MeanStrategy). This lets me easily change how I calculate the missing values without rewriting the main class.

Template Method: I used this for the BasePipelineTemplate. The base class forces the pipeline to always run in the exact same order (load data -> impute missing values -> scale features), and my subclass handles the actual execution.



## How I met each of the 6 Learning Outcomes

1. Object-Oriented Programming (OOP): My whole library is built using classes. I used inheritance to build my strategy classes and my pipeline template.

2. Functional Programming: Inside the FeatureScaler class, I wrote math functions to calculate the scaled values. I used Python's built-in map() function and a lambda to apply that math to the entire column.

3. Concurrency: To speed up the process of reading files, I used the concurrent.futures.ThreadPoolExecutor in my ConcurrentDataLoader. Instead of waiting for one file to finish loading before starting the next, it opens multiple files at the same time.

4. Recursion: I added a parse_pipeline_config function in my core file. If you give it a nested dictionary (like a loaded JSON file), it calls itself over and over again to dig through all the layers and get the settings.

5. SOLID Principles: I focused heavily on the Single Responsibility Principle. Every class does exactly one thing. The imputer only fixes missing data, the scaler only scales numbers, and the loader only reads files.

6. Architectural & Design Patterns: As mentioned above, I used the Strategy and Template Method patterns. The overall architecture is a "Pipeline", where data gets passed through a clear sequence of individual steps.