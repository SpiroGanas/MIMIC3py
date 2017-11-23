# Project Charter
  
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
|2017-11-23	|???  | Spiro Ganas| MIMIC3py Community |

# Introduction

## Purpose of the document


This document provides the information necessary to frame the project in the context of its scope, purpose, funding, resource requirements and approval. 

## Project Overview
MIMIC3py is a Python library.  It makes the MIMIC III Critical Care Database easily accessible to healthcare data scientists.

## Business Case
State the business case here. If you are creating a document as sophisticated as a Project Charter it is likely that there is a separate Business Case document (and possibly presentation slides and spreadsheets). You should reference any relevant business case documentation here for the audience. 

The business case should state the problem or opportunity that the business is addressing, the likely benefit, the cost associated with achieving the goal(s) and set out the ROI in clear terms. If the project is only a small part of the business case then it should be made clear in the Project Charter that the project is part of a larger strategic initiative, which might be described depending on sensitivity. 

## Project Scope

### Objectives

* Allow authorized users to easily download the MIMIC III data.
* Provide tools to load the MIMIC III data into pandas DataFrames.
* Provide tools to convert the data into formats commomly used for Machine Learning projects.
* Provide sample code demonstrating the analysis of MIMIC III data using machine learning algorithms.

### High-Level Requirements
List the requirements that must be satisfied in order for the project’s goals to be realised.

| Requirement   | Comment                         |   
| ------------- |---------------------------------| 
|Verify physionet.org authorization             |Required to dowload data files|
|Dowload data                                   |                            |
|Load data into pandas DataFrames               |                             |
|Convert data into machine learning format      |                             |
|Analyze data with machine learning algorithm   |Examples using sk-learn and TensorFlow                             |


 
### Milestones and Deliverables


| Milestone     | Deliverable                                                         |   
| ------------- |---------------------------------------------------------------------| 
|Version 0.1    |Ability to download data                                             |
|Version 0.2    |Ability to load data into pandas Dataframe                           |
|Version 0.3    |One data set in a Machine Learning format                            |
|Version 0.4    |One functioning machine learning example using sk-learn              |
|Version 0.5    |One functioning machine learning example using TensorFlow            |

### Project Plan

#### Timeline
| Milestone     | Target Date                                                       |   
| ------------- |---------------------------------------------------------------------| 
|Version 0.1    |2017-12-01                                            |
|Version 0.2    |2017-12-15                         |
|Version 0.3    |2017-12-31                            |
|Version 0.4    |2017-01-15            |
|Version 0.5    |2017-02-15           |

### Financial Estimates
#### Estimate
This project has no expected financial cost.  

## Risks and Assumptions
### Risk Analysis
N/A

### Assumptions
* MIMIC III data will continue to be publically availible on physionet.org.
* Developers will contribute to this project pro-bono.
* There is no critical need to complete this project by the stated deadlines.



 
## Project Organization
Describe the key roles in the project, who fills them, and the responsibilities of each role.
 
| Name      | Role              | Responsibilities         |   
| --------- |-------------------|--------------------------| 
|Spiro Ganas    | Project Manager	  | PM Responsibilities      |

 



### Project Advisory Board/Steering Committee
N/A
### Project Stakeholders
* MIMIC3py library developers
* Healthcare data scientists
* Students studying healthcare data analytics

## Project Approval

*This project has been reviewed and the Project Charter accepted by the following people, as indicated by signature below:*

List all individuals whose signature is required, along with their titles and/or roles on the project.

**Full Name**  Spiro Ganas

**Title** Project Manager

**Signature** Spiro Ganas

**Date**2017-11-23



## APPENDIX A - REFERENCES
N/A

## APPENDIX B - GLOSSARY
| Term                    | Definition                       |   
| ------------------------|----------------------------------| 
|MIMIC III Critical Care Database|A database containing electronic health records derived from critical care unit EHR systems.     |



