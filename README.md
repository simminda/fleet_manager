# Fleet Manager

Fleet Manager is a Django-based web application designed to manage and track vehicles and their related financial details. This project includes features for asset management, search functionality, and front-end asset editing.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Asset Management**: View and manage assets with details such as make, model, and VIN.
- **Search Functionality**: Search assets by make, model, or VIN.
- **Front-End Editing**: Edit asset details through a modal window (admin users can also edit asset ID and VIN).

## Installation

To get started with this project, follow these steps:

### Clone the Repository

```sh
git clone https://github.com/simminda/fleet_manager.git
cd fleet_manager
```

## Set Up a Virtual Environment

```python -m venv env```

### Activate the Virtual Environment
- **Windows**
```
.\env\Scripts\activate
```
- **MacOS/Linux**
```
source env/bin/activate
```

### Install Dependencies
```pip install -r requirements.txt```

### Apply Migrations
```python manage.py migrate```

### Create a Superuser (Optional)
Create a superuser to access the Django admin interface:
```
python manage.py createsuperuser
```

### Run the Development Server
Start the Django development server:
```
python manage.py runserver
```
You can now access the application at http://127.0.0.1:8000/

### Usage
- **Search for Vehicles**: Use the search bar in the navigation bar to find vehicles by make, model, or VIN.
- **Edit Assets**: Admin users can edit asset details using the provided modal interface.

### Contributing
Contributions are welcome! Please open an issue or submit a pull request with your changes.

### License
This project is licensed under the MIT License. 

## Screenshots:

### Landing Page
<div align="center">
    <img src="screenshots/0. vehicle_summary.png" width="100%"</img> 
</div>

<br/>

### Login Screen
<div align="center">
    <img src="screenshots/1. login.png" width="100%"</img> 
</div>

<br/>

### Landing Page after login
<div align="center">
    <img src="screenshots/2. vehicle_summary.png" width="100%"</img> 
</div>

<br/>

### Search Assets
<div align="center">
    <img src="screenshots/3. search.png" width="100%"</img> 
</div>

<br/>

### Asset Details
<div align="center">
    <img src="screenshots/4. asset_details.png" width="100%"</img> 
</div>

### Edit Asssets
<div align="center">
    <img src="screenshots/5. asset_edit.png" width="100%"</img> 
</div>
