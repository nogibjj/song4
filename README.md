Individual Project 4 (Data Engineering Systems)

# Objective
This project is to create a microservice that performs a task of sending an email by using FastAPI through Mailgun platform. It is intended to pursue CI/CD(Continuous Integration/Continuous Delivery) based on Github Actions.

# Contents
<img width="269" alt="image" src="https://user-images.githubusercontent.com/112578065/203455409-b2466420-a883-4bb4-a7fb-1379b7e5240f.png">

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

# Mailgun Email API
Mailgun is an email delivery service for sending, receiving, and tracking emails. Mailgun Email API especially makes integrating email into the existing applications incredibly easy with their RESTFUL API, SMTP relays, and comprehensive documentation.

### Example (Source: https://www.mailgun.com)
<img width="943" alt="image" src="https://user-images.githubusercontent.com/112578065/203453684-5e74a6ad-975b-448a-b0fb-092581e5a83b.png">
