# Random client list

This repository generates a random list of users, who own a certain number of tokens.

The list of tokens that a user can have is in the ```currencies_list.json``` file along with the minimum and maximum ranges.

## How does it work?

This script generates users and tokens randomly, balances are also generated randomly but not uniformly.

This means that the probability of obtaining a certain value for a token is based on the actual distribution of the token, taking into account the on-chain data.

In the ```constants.py``` file, you can find the ranges of the different tokens and the probability that the value is in one of those ranges.

## Purpose

The goal is to generate a list of users similar to that of an exchange. To later be able to verify their solvency and check if all users have been taken into account for balance sheet accounting.
