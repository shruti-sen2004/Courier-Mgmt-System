# Courier Management System
A console-based application designed to manage and streamline courier operations. This system provides a simple, text-based interface for handling shipments, tracking packages, and managing user and admin accounts.

## Features
- **User and Admin Roles:** The system supports two distinct user types: admin and user. Admins have full control over the system, while regular users can manage their own shipments.
- **Login & Authentication:** Secure login and logout functionality to ensure data integrity and privacy.
- **Shipment Management:** Create new shipments with details like sender, receiver, and destination.
- **Search Functionality:** Easily search for shipments using criteria like parcel ID.
- **Data Persistence:** Data is stored in a MySQL database, so it is not lost when the application is closed.

## Technologies Used
- **Language:** Python
- **Database:** MySQL
- **Libraries:** mysql-connector-python

## Getting Started
Follow these instructions to get a copy of the project up and running on your local machine.
### Prerequisites
You will need the following installed on your system:
  - Python 3.x
  - MySQL Server running locally
  - The `mysql-connector-python` library

### Installation
- Clone the repository: `git clone https://github.com/shruti-sen2004/Courier-Mgmt-System.git`
- Navigate into the project directory: `cd Courier-Mgmt-System`
- Create a virtual environment (optional)
- Install the required Python library: `pip install mysql-connector-python`
- Set up the MySQL database:
  - Log in to your MySQL server.
  - Create a database named c_m_system : `CREATE DATABASE c_m_system;`
  - The code will automatically create the necessary tables.

### Update the database connection details:
- Open the main.py file.
- Modify the `mysql.connector.connect()` line with your MySQL username and password.
  ```bash
  mycon=ms.connect(host="localhost",user="your_username",password="your_password",database="c_m_system")
  ```
- Run the application: `python main.py`

## Usage
Once the application is running, you will be greeted by the main menu. Follow the on-screen prompts to log in, register, or perform other actions based on your user role.

- **For Admins**: The employee login ID is hardcoded as `EMD0002` with the password `4321`.
- **For Users**: You can register a new account directly from the customer menu.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
