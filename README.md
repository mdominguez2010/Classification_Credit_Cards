# Classification of Credit Card Clients

Using random forest to classify credit card defaults potential save the bank money

## Target:
Default payment (Yes = 1, No = 0)

## Features: 
limit_bal: Amount of the given credit (NT dollar): it includes both the individual consumer credit and his/her family (supplementary) credit \
sex: Gender (1 = male; 2 = female) \
X3: Education (1 = graduate school; 2 = university; 3 = high school; 4 = others) \
X4: Marital status (1 = married; 2 = single; 3 = others) \
X5: Age (year) \
X6 - X11: History of past payment. We tracked the past monthly payment records (from April to September, 2005) as follows: The measurement scale for the repayment status is: -1 = pay duly; 1 = payment delay for one month; 2 = payment delay for two months; . . .; 8 = payment delay for eight months; 9 = payment delay for nine months and above \
X12-X17: Amount of bill statement (NT dollar). X12 = amount of bill statement in September, 2005; X13 = amount of bill statement in August, 2005; . . .; X17 = amount of bill statement in April, 2005 \
X18-X23: Amount of previous payment (NT dollar). X18 = amount paid in September, 2005; X19 = amount paid in August, 2005; . . .;X23 = amount paid in April, 2005

## Data Used:
UCI Machine Learning Repo, 'default of credit card clients'

## Tools Used:
Pandas, numpy, sklearn, imblearn, ipywidgets, matplotlib, seaborn, streamlit

## Possible Impacts:
Pevent further losses to a financial institution, automate processes
