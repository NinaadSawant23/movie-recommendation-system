# movie-recommendation-system

A movie recommendation system built with Python and Streamlit that uses a similarity matrix to provide suggestions for similar movies. This project includes data preprocessing (in a Jupyter Notebook) and an application that fetches movie posters, genres, and overviews via the TMDb API.

## Features

- **Search for a Movie:** Enter or select a movie to get recommendations.
- **Display Recommendations:** Shows the recommended movies with their posters, genres, and overviews.
- **API Integration:** Uses the TMDb API to retrieve additional movie details.
- **User-Friendly UI:** Built with Streamlit with responsive design elements.

## Files

- `app.py`: The main application file containing the recommendation & streamlit code.
- `data_preprocessing.ipynb`: Jupyter Notebook for data preprocessing and generating the similarity matrix, Make sure to execute it to generate the input data.
- `requirements.txt`: List of Python packages needed to run the project.
- `.gitignore`: Specifies files and folders to ignore in the Git repository.

## Installation

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

## Usage

1. **Pre-processing**

- Run the data/data_preprocessing.ipynb notebook to generate the processed data and pickle files

2. **Running the application**
```bash
streamlit run app.py
```
3. **Interact with the Application:**
- Use the select box to select a movie
- Click on "Recommend" button to generate recommendations

## Contributing
Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.


