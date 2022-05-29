#pandas

"""
Loading a DataFrame
We're still working hard to solve the kidnapping of Bayes, the Golden Retriever. 
Previously, we used a license plate spotted at the crime scene to narrow the list of suspects to:

Fred Frequentist
Ronald Aylmer Fisher
Gertrude Cox
Kirstine Smith
We've obtained credit card records for all four suspects. Perhaps some of them made suspicious purchases before the kidnapping?

The records are in a CSV called "credit_records.csv".

"""

# Import pandas under the alias pd
import pandas as pd

# Load the CSV "credit_records.csv"
credit_records = pd.read_csv('credit_records.csv')

# Display the first five rows of credit_records using the .head() method
print(credit_records.head())


"""
Inspecting a DataFrame
We've loaded the credit card records of our four suspects into a DataFrame called credit_records. 
Let's learn more about the structure of this DataFrame.

The pandas module has been imported under the alias pd. The DataFrame credit_records has already been imported.

How many rows are in credit_records?

"""

# Use .info() to inspect the DataFrame credit_records
print(credit_records.info())