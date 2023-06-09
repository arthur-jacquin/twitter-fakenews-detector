# Fake News Detector

## Description

Dashboard giving a general overview over the credibility of the most popular tweets on a given topic. In particular, the dashboard highlights the tweets that are the most likely to be fake news, with an advanced credibility analysis breakdown. It is also possible to estimate the credibility of a given user or tweet.


## Usage

This tool is perfect for political campaigns. For a candidate preparing an interview, a query on any topic (in the "Topic analysis" tab) will give:
- the population feelings about the topic (polarity, subjectivity),
- the correlation between virality and credibility,
- the (most probably) fake news to debunk,
- the (most) credible pieces of news to be aware of,
- related topics, to help the candidate moving in a debate.

The credibility estimation of the selected tweets can be explored thanks to the collapsible analysis breakdowns.


To deepen the analysis, one could also target a specific user or tweet, thanks to the associated tabs. The input can either be the object URL or, if already known, the object ID.


## Authors

- Yann Chauvard
- David Houri
- Théo Joret Des Closières
- Eliott Kuhn
- Augustin Tachoires
- Arthur Jacquin


## Projected timeline

See `TIMELINE.md`


## Status

The project is not to be develloped after the Coding Weeks. However, feel free to fork it and make it your own!


## Contributing

The code is well documented with docstrings.

Useful commands:

- Test the code cleanness: `py -m pylint script.py`
- Test the code: `py -m pytest`
- Test the coverage: `py -m pytest --cov=.` in main directory

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
5. `git pull`. If there is a conflict, tell everybody and solve it locally with the team. Then restart the process.

Before pushing:

1. `git pull`. If there is a conflict, tell everybody and solve it locally with the team.
2. Tell everybody that you are going to `push`.


## License

See `LICENSE`.


## Credits and sources

- [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
- [SVC classifier](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)
- Dataset 1:
    - Authors: Veronica Perez-Rosas, Bennett Kleinberg, Alexandra Lefevre, Rada Mihalcea
    - Title: Automatic Detection of Fake News
    - Journal: International Conference on Computational Linguistics (COLING)
    - Year: 2018
- LIAR Dataset:
    - Author: William Wang, william@cs.ucsb.edu


## Links

- [Presentation slideshow](https://docs.google.com/presentation/d/17r5GMkfw078WZiYudzLYgj-E9xjYL0YFxJ5U_GvQ6SQ/edit?usp=sharing)

