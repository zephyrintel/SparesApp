# SparesApp

## Overview

**SparesApp** is a web application designed to help users manage spare parts for industrial equipment. It allows users to browse kits, view components (both Level 1 and Level 2), compare different kits, and optimize inventory for efficient parts management. The app is built using Django for the backend and is integrated with an Azure SQL database for data storage. The app aims to streamline the management of industrial parts, improving accessibility and reducing downtime in industrial operations.

---

## Features

### 1. **Kit Browsing and Component Display**
   - Users can browse kits by selecting from a dropdown list or search for a kit by pump model.
   - For each selected kit, the app displays its Level 1 components along with associated Level 2 components if they exist.
   - The components are displayed in a tabular format with collapsible rows to show the hierarchy between Level 1 and Level 2 components.

### 2. **Comparing Kits**
   - A feature is being developed to allow users to compare two kits side by side. This will help identify differences between kits, optimizing decision-making for inventory management.

### 3. **Inventory Optimization**
   - A future feature will help users identify kits they can build with the existing parts on hand. This will enable more effective use of available inventory.

---

## Technologies Used

- **Backend**: Django Framework (Python)
- **Frontend**: HTML, CSS (Bootstrap for styling)
- **Database**: Azure SQL Database
- **Version Control**: Git and GitHub
- **Deployment**: Planned deployment on Azure Static Web Apps

---

## Database Structure

The app uses an Azure SQL Database for managing kits and components. Here’s an overview of the key tables:

- **Kits Table**:
  - `KitID` (Primary Key)
  - `KitName`
  - `PumpModel`

- **Level1Components Table**:
  - `PartID` (Primary Key)
  - `ItemNumber`
  - `Description`
  - `ParentKit` (Foreign Key to Kits Table)
  - `Quantity`
  
- **Level2Components Table**:
  - `PartID` (Primary Key)
  - `ParentPartID` (Foreign Key to Level1Components Table)
  - `ItemNumber`
  - `Description`
  - `Quantity`
  
- **KitParts Table** (Linking Table):
  - `KitPartID` (Primary Key)
  - `KitID` (Foreign Key to Kits Table)
  - `PartID` (Foreign Key to Level1Components Table)
  - `Quantity`

---

## Installation and Setup

### 1. Clone the repository:

```bash
git clone https://github.com/zephyrintel/SparesApp.git
cd SparesApp
```

### 2. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure the database settings:

Update the `DATABASES` settings in the `settings.py` file to point to your Azure SQL Database:

```python
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'your_database_host',
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}
```

## 4. Run database migrations:

```bash
python mange.py migrate
```

## 5. Start the development server
```bash
python mange.py runserver
```
	
## Roadmap

- [ ] Implement kit comparison functionality.
- [ ] Implement inventory optimization feature.
- [ ] Deploy the app on Azure Static Web Apps.
- [ ] Add authentication for user-specific kit and inventory management.

