# Reflective Journal CLI App

## Overview
A terminal-based journaling application to support emotional awareness, self-reflection, and goal tracking.

## Features
- Secure login with password hashing
- Journal exercises: feelings, cognitive reframing, goals, wins
- Save and view timestamped entries
- Search/filter past entries by type or keyword

## Setup Instructions

### 1. Clone the repository:
In your terminal enter:
```bash
git clone 
cd journaling_app
```

### 2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run the application:
``` bash
python3 main.py
```

### 📦 Third-Party Dependencies and Licensing

| Package             | Purpose                                          | License        | Ethical Use Notes |
|---------------------|--------------------------------------------------|----------------|--------------------|
| `rich`              | Enhanced CLI formatting and prompts              | MIT            | ✅ Permissive, open-source |
| `bcrypt`            | Password hashing for login system                | Apache-2.0     | ✅ Secure and ethically maintained |
| `python-dateutil`   | Advanced date/time parsing and formatting        | BSD-3-Clause   | ✅ Permissive and safe |
| `json` (built-in)   | Data serialization and file storage              | PSF License    | ✅ Standard Python library |

> ✅ **All listed licenses are open-source and ethically aligned with fair, non-restrictive usage in educational and personal projects.**


