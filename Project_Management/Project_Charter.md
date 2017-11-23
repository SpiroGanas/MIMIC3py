[comment]: <> (Template is from: https://github.com/documize/document-templates)
#Project Charter

**Project Charter For:**  MIMIC3py

**Document Created:** 2017-11-23

**Author:** Spiro Ganas

**Distribution:** N/A

<u>**Document Revision History**</u>

| Revised By       | Date           | Comment               |
| -----------------|:--------------:|:---------------------:|
| Spiro Ganas | 2017-11-23  | Initial Version |

		
| Start Date | End Date    | Project Manager | Client      |
| :---------:|:-----------:| :--------------:| ------------|
|2017-11-23	|???  | Spiro Ganas| Spiro Ganas |

#Introduction
##Purpose of the document


This document provides the information necessary to frame the project in the context of its scope, purpose, funding, resource requirements and approval. 

##Project Overview
MIMIC3py is a Python library.  It makes the MIMIC III Critical Care Database easily accessible to healthcare data scientists.

##Business Case
State the business case here. If you are creating a document as sophisticated as a Project Charter it is likely that there is a separate Business Case document (and possibly presentation slides and spreadsheets). You should reference any relevant business case documentation here for the audience. 

The business case should state the problem or opportunity that the business is addressing, the likely benefit, the cost associated with achieving the goal(s) and set out the ROI in clear terms. If the project is only a small part of the business case then it should be made clear in the Project Charter that the project is part of a larger strategic initiative, which might be described depending on sensitivity. 

##Project Scope

###Objectives

* Allow authorized users to easily download the MIMIC III data.
* Provide tools to load the MIMIC III data into pandas DataFrames.
* Provide tools to convert the data into formats commomly used for Machine Learning projects.
* Provide sample code demonstrating the analysis of MIMIC III data using machine learning algorithms.

###High-Level Requirements
List the requirements that must be satisfied in order for the project’s goals to be realised.

| Requirement   | Comment                         |   
| ------------- |---------------------------------| 
|Verify physionet.org authorization             |Required to dowload data files|
|Dowload data                                   |                            |
|Load data into pandas DataFrames               |                             |
|Convert data into machine learning format      |                             |
|Analyze data with machine learning algorithm   |Examples using sk-learn and TensorFlow                             |


 
###Milestones and Deliverables
*List the major project milestones and the deliverables from them*

| Milestone     | Deliverable                                                         |   
| ------------- |---------------------------------------------------------------------| 
|Version 0.1    |Ability to download data                                             |
|Version 0.2    |Ability to load data into pandas Dataframe                           |
|Version 0.3    |One data set in a Machine Learning format                            |
|Version 0.4    |One functioning machine learning example using sk-learn              |
|Version 0.5    |One functioning machine learning example using TensorFlow            |

###Project Plan

####Timeline
Lay out the project plan at a very high level, possibly in the form of a Gantt chart image. 

###Financial Estimates
####Estimate
Provide a summary of the estimated costs to deliver the project. If the project is broken into phases then you should cost each phase separately.

##Risks and Assumptions
###Risk Analysis
If you are creating a document as sophisticated as a Project Charter it is likely that there is a separate Risk Register (and possibly presentation slides and spreadsheets). You should reference any relevant business case documentation here for the audience. If not, call out the risks in a table with the column headings below (you should ideally use a spreadsheet):

**Risk Id** – A unique identification number used to identify and track the risk in the risk register. There are different possible ways of classifying the Id but what is clear is that it is best if this is codified. For example, Risk Id RF### could relate to a Financial risk, which Risk Id RC### could relate to a Compliance risk. 

**Category** –Is the risk financial (cost and/or revenue), regulatory or compliance, timeline, resource, environment, or some other key category? Categorising risks groups them and aligns them with stakeholders who are best placed to assess/mitigate and stakeholders for whom the risk is greatest.

**Description** – Describe the potential risk. For instance: Item A cannot be completed until Item B has been purchased but approval has been delayed, or Item A requires resources that have not been identified and the project is currently resource constrained.

**Potential Impact** – A quantitative rating of the potential impact on the project if the risk should materialize. Impact in a Risk Register should be scored on a scale of 1 – 10 with 10 being the highest impact.

**Probability** – The likelihood that the risk will occur at some point in the duration of the project. This should be quantitative like Potential Impact not qualitative (high, medium or low). If you use qualitative measures you cannot calculate a Risk Score, which is done by multiplying Probability and Impact and you can easily convert a number to a descriptor e.g. 1-3 = “Low”, 4-6 = “Medium” and 7-10 = “High”.

**Likely Outcome** – The likely consequence or impact of the risk if it materialises. 

**Ranking** – This is the relative ranking of one risk in comparison to all others that have been assessed. This can be qualitative e.g. high, medium, or low, or it can be quantitative, especially if Rank is used as a sorting mechanism to decide what items most require mitigation. Remember that qualitative ranking will produce duplicate values; if you have two “High” ranking items then you should consider how you might decide which is more important?

**Mitigation** – What signs or outcomes indicate the need to implement contingency plans and what are those contingency plans. It is likely that you will need to create a separate Contingency Planning document for each high impact risk.

**Prevention Plan** – An action plan to prevent a given risk from occurring, often combined with the Contingency Plan described above. You should try to establish a prevention plan for every risk that you categorize, starting with those risks that have the greatest potential impact.

**RACI Matrix** – For every risk, try to establish a RACI matrix.
Who is **R**esponsible?
Who is **A**ccountable?
Who should be **C**onsulted?
Who should be **I**nformed?

###Assumptions
List all of the assumptions that are being made. For example: “to successfully meet its goals in a timely manner with benefits reflected in the current financial year, all parties have signed-off the budget and the project will begin on the scheduled start date.”
 
##Project Organization
Describe the key roles in the project, who fills them, and the responsibilities of each role.
 
| Name      | Role              | Responsibilities         |   
| --------- |-------------------|--------------------------| 
|Spiro Ganas    | Project Manager	  | PM Responsibilities      |

 



###Project Advisory Board/Steering Committee
N/A
###Project Stakeholders
* MIMIC3py library developers
* Healthcare data scientists
* Students studying healthcare data analytics

##Project Approval

*This project has been reviewed and the Project Charter accepted by the following people, as indicated by signature below:*

List all individuals whose signature is required, along with their titles and/or roles on the project.

**Full Name**  Spiro Ganas

**Title** Project Manager

**Signature** Spiro Ganas

**Date**2017-11-23



#APPENDIX A - REFERENCES
N/A

#APPENDIX B - GLOSSARY
| Term                    | Definition                       |   
| ------------------------|----------------------------------| 
|MIMIC III Critical Care Database|A database containing electronic health records derived from Critical Care Unit systems.     |



