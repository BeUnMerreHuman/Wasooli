# Student Data Viewer Web App

A Flask-based web application that fetches, filters, and displays real-time student data from an external API. The app is deployed live at [https://wasooli.onrender.com](https://wasooli.onrender.com).

## Features

- Fetches real-time data from a REST API
- Displays a searchable, filterable table of student records
- Filters by:
  - Student ID or Name
  - Class
  - Status
  - General text search
- Built using Flask and Pandas for backend processing
- Interactive frontend with filtering interface
- Responsive and easy to use

## Tech Stack

- **Backend**: Python, Flask, Pandas, Requests
- **Frontend**: HTML, JavaScript
- **Deployment**: Render.com

## Project Structure

```
Wasooli/
├── static/            # Static assets like images
│   └── logo.png
├── templates/         # HTML templates
│   └── index.html
├── app.py             # Main Flask application
├── requirements.txt   # Python dependencies
├── render.yaml        # Deployment config for Render
└── .gitignore
```

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/BeUnMerreHuman/Wasooli.git
   cd Wasooli
2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
5. **Run the application**
   ```bash
   python app.py
6. **Open http://localhost:5000 in your browser.**

**The app fetches data from this external API:**
```bash
https://sms.ilmwasooli.com/temp/gettestingdata
```

The app is deployed on Render using the render.yaml configuration.

## License
This project is licensed under the [MIT License](LICENSE).

## Author
- Muneeb Ur Rehman Siddiqui
- Email: muneeburrehmansiddiqui98@gmail.com
