# This is the back end for the marketing site
 

## Brief description of your project.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Configuration](#configuration)


## Overview

This is the main back-end for the marketing website of fira it contains the waitlist api

## Installation

Provide step-by-step instructions on how to install the project and its dependencies.

```bash
pip install -r requirements.txt

```
# Install dependencies
``` 
cd requirements.txt 
```
## usage:
the following are the accepted api end points:

# Waitlist Entry API

## Overview

The Waitlist Entry API provides endpoints for managing waitlist entries.

## Base URL

`https://example.com/api/v1/waitlist/`

## Allowed Methods

- `GET`: Retrieve a list of waitlist entries.
- `POST`: Create a new waitlist entry.

## Waitlist Entry Object

- `id` (Integer, Read-only): Unique identifier for the waitlist entry.
- `email` (String, Required): Email address of the person.
- `name` (String, Optional): Name of the person.
- `phone` (String, Required): Phone number of the person.

## Endpoint: Retrieve Waitlist Entries

### Request

- **Method:** GET
- **URL:** `/`
- **Content Type:** application/json

### Response

#### Successful Response

- **Status Code:** 200 OK
- **Content Type:** application/json

```json
[
    {
        "id": 1,
        "email": "example@example.com",
        "name": "John Doe",
        "phone": "+1234567890"
    },
    {
        "id": 2,
        "email": "another@example.com",
        "name": "Jane Doe",
        "phone": "+9876543210"
    }
]

```
- **Method:** POST
- **URL:** `/`
- **Content Type:** application/json

### Response

#### Successful Response

- **Status Code:** 201 created
- **Content Type:** application/json

```json

{
    "email": "new@example.com",
    "name": "Miera Doe",
    "phone": "+1122334455"
}
```

# Configuration
```
git clone -b <branch name> git url
cd website_api
pip install -r requirements.txt
connect all databse variable in setting.py

run

python manage.py makemigrations
python manage.py migrate

run server
python manage.py runserver

test api using post man and other

```