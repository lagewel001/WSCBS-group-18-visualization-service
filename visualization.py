#!/usr/bin/env python3

"""
Demo visualization script for data pipeline deployed on a K8S cluster controlled
by the Brane Framework. The classification task is based on the NLP with Disaster
Tweets Kaggle competition: https://www.kaggle.com/competitions/nlp-getting-started.
The resulting csv from the corresponding classification task pipeline can be used
as input for this visualization.

Dependencies for installation: dependencies: matplotlib, pandas, seaborn
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import yaml


def visualize(output):
    """
        Simple visualization of the outputted csv by the classification task pipeline.
        Saves a graph.png containing the number of disaster tweets and regular tweets
        with an indication of their corresponding words.
    """
    sns.set()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    tweet_len = output[output['Classification'] == 1]['text'].str.len()
    ax1.hist(tweet_len, color='blue')
    ax1.set_title('disaster tweets')
    ax1.set_xlabel('Number of characters')
    ax1.set_ylabel('Number of tweets')

    tweet_len = output[output['Classification'] == 0]['text'].str.len()
    ax2.hist(tweet_len, color='CRIMSON')
    ax2.set_title('Not disaster tweets')
    ax2.set_xlabel('Number of characters')
    ax2.set_ylabel('Number of tweets')

    fig.suptitle('Characters in tweets')
    fig.savefig('/data/graph.png')
    plt.show()


if __name__ == "__main__":
    output = pd.read_csv('/data/classification.csv')
    visualize(output)
    print(yaml.dump({"output": "Saved image to /data/graph.png"}))
