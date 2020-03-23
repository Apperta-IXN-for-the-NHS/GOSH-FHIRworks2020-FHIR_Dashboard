# FHIR-Hackathon

## Chosen Task
1. Graphing data from FHIR records.
2. Preparing data for transfer to XML and CSV, and allow users to download them.
3. Then create a dashboard that presents a human-readable representation of the data.

## Stacks / Skills
1. `pip install FHIR-Parser`. Review [FHIR-Parser Docs](https://fhir-parser.readthedocs.io/en/latest/index.html#).  
Special thanks to [greenfrogs](https://github.com/greenfrogs/).
2. Model-View-Controller (MVC)  
3. Front-end (HTML, CSS, Python3)
4. Back-end and DB (Flask, SQLAlchemy)  

## Extensibility
1. After exporting a CSV file, load it onto [SandDance](https://github.com/microsoft/SandDance) and appreciate its wonderful visualisation.  
You can use [online SandDance](https://sanddance.azurewebsites.net/BeachPartyApp/BeachPartyApp.html) by loading your local dataset.  
Or, install [SandDance for VSCode](https://marketplace.visualstudio.com/items?itemName=msrvida.vscode-sanddance).
2. Allow users to choose fields of CSV or XML by UI button.
3. Link Observation data when user clicks patient's name.

## Deployment options
1. [Deploying Flask on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)
2. [Deploying Flask on Google App Engine](https://cloud.google.com/appengine/docs/standard/python3/runtime)
3. [Deploying Flask on AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html)
4. [Deploying Flask on Azure](https://docs.microsoft.com/en-us/azure/app-service/containers/how-to-configure-python)
5. [Deploying Flask on PythonAnywhere](https://help.pythonanywhere.com/pages/Flask/)

## Background
Great Ormond Street Hospital, a specialist children’s centre, has established a digital research unit,
including NHS clinicians, UCL academics and industry partners. The aim is to improve child health
by optimising the use of clinical data for research.
This task, incorporating the two-day FHIRworks Hackathon, will create a library of example
developer packages that use the FHIR (Fast Healthcare Interoperability Resources) standard.
Students will use synthetically generated data retrieved over FHIR from a GOSH gateway to
demonstrate capabilities and advantages of the FHIR standard for the collection and safe handling
of healthcare data. This approach will support the development of various healthcare apps, for
patients, families and healthcare professionals, like existing phone apps used regularly by
millions. There is already a collection of synthetic records on GOSH DRIVE’s FHIR server.
HL7 FHIR is a next generation standards JSON based framework that leverages the latest web
standards and includes a RESTful API. FHIR interoperability ensures data is collected, accessed,
and used in a safe and secure manner.

## Process
Please review the following [deployment guide link](https://github.com/goshdrive/FHIRworks_2020) 
which contains the instructions and source code 
for the FHIR standard access at Great Ormond St Hospital.


## Author
* [To Eun Kim](https://github.com/kimdanny)

## License
This project is licensed under the MIT License- see the [LICENSE.md](LICENSE.md) file for details.