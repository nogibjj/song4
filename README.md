Individual Project 4 (Data Engineering Systems)

# Objective
This project is to create a microservice that performs a task of sending an email by using FastAPI through Mailgun platform. It is intended to pursue CI/CD(Continuous Integration/Continuous Delivery) based on Github Actions and using container in the cloud settings (AWS).

# Contents
<img width="268" alt="image" src="https://user-images.githubusercontent.com/112578065/203547153-e4a6229e-4644-4836-aa88-79a4f9841032.png">

## 1. Build a git repo: nogibjj/song4

## 2. Scaffolding
- README.md
- Makefile
- requirements.txt
- .gitignore
- main.py
- test_mail.py

## 3. Structure of Directories
1) apis
  - api_base.py
  - utils (folder)
    - utils.py
  - version1 (folder)
    - route_comm.py
  
2) config
  - config.py
  
3) schemas
  - sch_comm.py
  
4) Dockerfile & buildspec.yaml

# Mailgun Email API
Mailgun is an email delivery service for sending, receiving, and tracking emails. Mailgun Email API especially makes integrating email into the existing applications incredibly easy with their RESTFUL API, SMTP relays, and comprehensive documentation.

### Example (Source: https://www.mailgun.com)
<img width="943" alt="image" src="https://user-images.githubusercontent.com/112578065/203453684-5e74a6ad-975b-448a-b0fb-092581e5a83b.png">
