# Movie Recommendation System 🎬✨
![Streamlit](https://img.shields.io/badge/Built_with-Streamlit-red)
![Python](https://img.shields.io/badge/Python-3.8%2B-yellow)
![TMDb](https://img.shields.io/badge/API-TMDb-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A movie recommendation system built with Python and Streamlit that uses a similarity matrix to provide suggestions for similar movies. This project includes data preprocessing (in a Jupyter Notebook) and an application that fetches movie posters, genres, and overviews via the TMDb API.

![Project Screenshot](/screenshots/UI.png)

> 🎥 **Discover your next favorite movie** – simply select or search for a movie and get a list of recommendations along with detailed information.

## 🚀 Features

- **Interactive Search:** Use a search bar or select box to find your movie.
- **Movie Recommendations:** Get the top 5 movie recommendations based on similarity.
- **Rich Movie Details:** Displays movie posters, genres, and overviews (retrieved via the TMDb API).
- **Responsive UI:** Built with Streamlit for an engaging and responsive web interface.
- **Data Preprocessing:** Includes a Jupyter Notebook for preprocessing the movie data and generating the similarity matrix.

## 🧰 Technologies Used

| Category                | Library / Tool         | Purpose                                                                 |
|-------------------------|------------------------|-------------------------------------------------------------------------|
| **Backend**             | Python Standard Library| Core scripting and data manipulation                                     |
| **Frontend / UI**       | `streamlit`            | To create an interactive and responsive web interface                   |
| **Data Processing**     | `pickle`, `pandas`     | To load movie data and the similarity matrix                             |
| **HTTP Requests**       | `requests`             | To interact with the TMDb API for movie details                           |
| **Environment Vars**    | `python-dotenv`        | To load environment variables securely (e.g., TMDb API key)               |

## 🗂️ Files

- `app.py`: The main application file containing the recommendation & streamlit code.
- `data_preprocessing.ipynb`: Jupyter Notebook for data preprocessing and generating the similarity matrix, Make sure to execute it to generate the input data.
- `requirements.txt`: List of Python packages needed to run the project.
- `.gitignore`: Specifies files and folders to ignore in the Git repository.

## 📥 Installation & Setup

1. **Clone the Repository:**
```bash
git clone https://github.com/NinaadSawant23/movie-recommendation-system.git
cd movie-recommendation-system
```
2. **Create and Activate a Virtual Environment**
```bash
python -m venv env
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate
```
3. **Install Required Packages:**
```bash
pip install -r requirements.txt
```
4. **Get a TMDb API Key**

- Signup or login at TMDb.
- Create a .env file and initialize TMDB_API_KEY

5. **Data Preparation:**

- Run the data/data_preprocessing.ipynb notebook to process the raw data and generate the movies.pkl and similarity_matrix.pkl files.

## ⚙️ Usage
1. **Running the application**
```bash
streamlit run app.py
```
2. **Interact with the Application:**
- Use the select box to select a movie
- Click on "Recommend" button to generate recommendations

## 🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.


