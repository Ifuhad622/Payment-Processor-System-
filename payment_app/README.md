# Payment Processing Application

This application processes payments for multiple users, stores payment history, and integrates with a SQLite database. It uses Kivy for the user interface and SQLite for data storage.

## Features

- Add and manage multiple users.
- Process payments and track outstanding balances.
- Store and retrieve payment history.
- Cross-platform support (desktop and mobile).

## Setup

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Installation

1. **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd payment_app
    ```

2. **Install dependencies:**

    ```bash
    sudo apt update
    sudo apt install python3-pip build-essential libssl-dev libffi-dev python3-dev libsqlite3-dev
    pip3 install kivy
    ```

### Running the Application

To run the application on your desktop:

```bash
python3 main.py
