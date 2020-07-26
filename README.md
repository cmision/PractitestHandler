# PractitestHandler
by Carlo Mision

This is a piece of code that takes 3 reports from Practitest:
A.  Requirement Tabular Summary
B.  Instance Tabular Summary
C.  Issue Tabular Summary

...and transforms them to a low level overall coverage report on Excel.  Since it's low level, the user can then use a Pivot Table to summarise test progress.
Key advantage with this code is that the test team can use multiple variables on the Test Instance (as opposed to just a report with 1 variable, which comes OOTB with practitest)

Usage:
1.  Produce each of the reports from PRactitest
2.  Rename them A.xlsx, B.xlsx and C.xlsx
3.  Run Handler.py
4.  Pull out output.xlsx and create your pivots
