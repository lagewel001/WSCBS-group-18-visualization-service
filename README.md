# Brane NLP for disaster tweets visualization task pipeline
This repository contains the NLP for disaster tweets visualization task pipeline to be deployed on a 
system running the Brane Framework. The classification task was taken from its corresponding Kaggle 
competition: https://www.kaggle.com/competitions/nlp-getting-started.

If you do not have a Kubernetes cluster and/or instance running Brane yet, make sure to follow 
[this](./brane-administrator-setting-up-k8s.md) guide to set up a cluster and brane instance first.

## Publishing the Brane package
1. Make sure you have the following files in the same folder (or just use this repository) on a
   machine/instance running Brane connected to a cluster or local deployment:
   - [visualization.py](./visualization.py): visualization script and entry point for the Brane package
   - [container.yml](./container.yml): Brane package definition
2. Build the package by running `brane build ./container.yml` in said folder.
3. Make sure your Brane instance is logged in to sign the package:
   `brane login http://127.0.0.1 --username <user>`
4. Publish the package using `brane push viz`

## Using the Brane package
1. On an instance running Brane connected to the cluster where this package is deployed (see steps above),
run `brane repl --remote http://127.0.0.1:50053` to start the Brane CLI.
2. Import and use the deployed package:
    ```
    1> import nlp;
    2> import viz;
    3> print(nlp("Luke, I'm your father"));
    Disaster! Panic!! AAAAH!
    4> viz();
    5> _
    ```
