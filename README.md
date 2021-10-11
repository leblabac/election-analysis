# Overview of Project
The Colorado Board of Elections has given me the following tasks to complete the election audit of a local congressional election.

```
1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the perrcentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
 ```
## Resources
- Data Source: [election_results.csv ](https://github.com/leblabac/election-analysis/blob/main/resources/election_results.csv)
- Software: Python 3.7.6, Visual Studio Code 1.61.0

## Election-Audit Results
The election audit returned the following results:
  - There were **369,711** votes cast in the election. 
  - The candidates were:
    -   Charles Casper Stockham
    -   Diana DeGette
    -   Raymon Anthony Doane
 - The candidates results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
    - Diana DeGette received 73.8% of the vote and 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.

Based on the vote tally, Diana DeGette wins the popular vote with a total of 73.8% of the vote, totaling 272,892 votes.

## Challenge Overview
In addition to performing the election audit, the election commission asked for an analysis of voter turnout for each county that voted in the congressional district.
The findings of the following tasks were added to the final election audit:
```
1. Calculate the voter turnout for each county.
2. Calculate the percentage of votes each county contributed to the election.
3. Determine which county had the largest turnout.
```
The findings were as follows:
There were three counties involved in the election. Voter turnout was as follows:

- Jefferson: 10.5% (38,855)
- Denver: 82.8% (306,055)
- Arapahoe: 6.7% (24,801)

The county with the largest turnout was Denver.

## Challenge Summary
The script written can be re-used with modification as needed for any election. The script uses loops, conditionals and logical operators which can be used in combination to produce further detail.  For example, with modification, the script could also tally the percentage of votes for *each candidate by county*, were that information required by looping through counties and retrieving the vote count for each candidate to determine the popularity of that particular candidate by county. Depending on the data collected about the election, it would likewise be possible to modify the script to identify to *identify the percentage of votes for the different political parties represented on the ballot*. Ultimately, this script can be used for any election, limited only by the data collected.
