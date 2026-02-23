# Blog

A full-featured blog web application built with Python and Flask. Blog features a modern, premium dark-themed UI with glassmorphism effects, secure user authentication, and AI-powered draft generation to help creators write their stories.

## Features

- **Modern & Responsive UI**: Beautiful dark theme built with Bootstrap 5 and custom CSS, featuring glassmorphism cards, smooth animations, and Google Fonts (Inter & Outfit).
- **User Authentication**: Secure registration and sign-in functionality utilizing `bcrypt` for password hashing.
- **Blog Management**: Full CRUD (Create, Read, Update, Delete) capabilities. Authors can easily manage their published stories.
- **AI Draft Generation**: Integrated with the OpenRouter AI API to automatically generate comprehensive blog post drafts based entirely on just a title. 
- **Comments System**: Interactive comment section allowing logged-in users to share their thoughts on posts.
- **Search Engine**: Fast and responsive search functionality to find articles by title, description, or author.

## Technologies Used

- **Backend**: Python, Flask
- **Database**: SQLite3
- **Frontend**: HTML5, Jinja2 Templates, Vanilla CSS, Bootstrap 5
- **Security**: `bcrypt` (password hashing)
- **APIs**: OpenRouter API (for AI text generation)

## Installation & Setup

Follow these instructions to get the project up and running on your local machine.

### Prerequisites
- Python 3.8+ installed on your system.
- An [OpenRouter API key](https://openrouter.ai/) for the AI draft generation feature.

### Step-by-Step Guide

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <repository_url>
   cd blog
   ```

2. **Create a virtual environment**:
   It is recommended to use a virtual environment to manage dependencies.
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install the dependencies**:
   ```bash
   pip install -r requirement.txt
   ```

5. **Set up Environment Variables**:
   Create a `.env` file in the root directory of the project and add your OpenRouter API key:
   ```env
   OPENROUTER_API=your_openrouter_api_key_here
   ```

6. **Run the Application**:
   Start the Flask development server:
   ```bash
   python app.py
   ```

7. **Access the App**:
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Usage

- **Viewing**: Anyone can view the homepage, read blog posts, and use the search functionality without logging in.
- **Writing**: To write a blog or comment, you must create an account and sign in.
- **AI Generation**: On the "Write a Story" page, enter a Title and click the **AI Generate Draft** button. The AI will write the `Description` for you based on your title.
- **Managing**: Head to the "My Blogs" section from the navigation bar to edit or delete your existing posts.
