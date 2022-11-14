# fakenewsdetector_group13

## Description

Dashboard giving a general overview over the credibility of the most popular tweets on a given topic. In particular, the dashboard highlights the tweets that are the most likely to be fake news, with an advanced credibility analysis breakdown. It is also possible to estimate the credibility of a given user or tweet.


## Members

- Yann Chauvard
- David Houri
- Théo Joret Des Closières
- Eliott Kuhn
- Augustin Tachoires
- Arthur Jacquin


## Projected timeline

See `TIMELINE.md`


## Rules for code management

Use the Test-Driven Development:

1. Identify what you're going to develop next, on which files, and discuss it with the team.
2. Write a test to verify if a code meets the identified goal (it must fail as code shouldn't be written yet).
3. Write the docstrings related to the code you're about to write.
4. Write the code to pass the test, until the test pass.
5. Clean the code, while ensuring the test still pass.
6. Verify the coverage of the tests, add more tests if needed.

Before commiting:

1. Verify that you only added meaningful files to the staging area, and use the `.gitignore` to exclude the unwanted ones, such as large binary files.
2. Verify that the tests you wrote cover all the code, and that they pass.
3. Verify that the set of modifications is related to one and only one logical unit.
4. Provide an explicit comment for the commit, starting with a keyword. Examples:
    - `add: connection_setup.py`
    - `add: query type dropdown menu on dashboard`
    - `fix: typo in filename`
    - `delete: __pycache__ (now ignored thanks to .gitignore)`
    - `modif: change spacing`
    - `cleaning: restructuring file structure`

Before pushing:

1. `git pull`. If there is a conflict, tell everybody and solve it locally with the team.
2. Tell everybody that you are going to `push`.


## Usage

TODO

Perfect for political campaigns.

Input: either
- topic/hashtag
- user name/url of an user profile
- url of a tweet

Output:
- Credibility repartition
- Identification of the most likely false, and true tweets, with an advanced breakdown of the credibility analysis and alerts about suspicious caracteristics
- Fiability-propagation correlation, propagation-subjectivity correlation graphs
- Cloud of vocabulary related to the chosen topic/username/tweet


## License

See `LICENSE`.



## Credits and sources

ML :
- RandomForestClassifier https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
- SVC classifier https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
- Dataset 1,
author : Veronica Perez-Rosas, Bennett Kleinberg, Alexandra Lefevre, Rada Mihalcea,
title : Automatic Detection of Fake News,
journal : International Conference on Computational Linguistics (COLING),
year : 2018
