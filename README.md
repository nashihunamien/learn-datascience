## Learning Data Science

A repository dedicated to various data science projects and exercises aimed at enhancing data science skills and understanding.

### Current Projects:
- **Property Analysis in Yogyakarta**: Analyzing and visualizing property listings in Yogyakarta, Indonesia.

### Prerequisites:
- Python 3.x
- Poetry (Dependency Manager)

### Libraries Used:
- Pandas: For data manipulation and analysis.
- Folium: For creating interactive maps.
- Nominatim from Geopy: For geocoding locations to get their coordinates.

### Setup and Installation:
1. **Clone the Repository**:
    ```
    git clone [repo-link]
    cd [repo-directory]
    ```

2. **Setup Environment with Poetry**:
    ```
    poetry install
    ```

3. **Activate the Poetry Environment**:
    ```
    poetry shell
    ```

4. **Run Jupyter Notebook (Optional)**:
    If you're planning to use Jupyter Notebook for the analysis:
    ```
    poetry run jupyter notebook
    ```

### Contribution Flow:
1. **Checkout the Development Branch**:
    ```
    git checkout development
    ```

2. **Pull the Latest Changes**:
    ```
    git pull origin development
    ```

3. **Create a New Branch for Your Work**:
    ```
    git checkout -b [name_of_your_new_branch]
    ```

4. **Make Changes and Commit**:
    Commit your changes after you've finished.
    ```
    git commit -m "Description of changes"
    ```

5. **Push Your Branch**:
    ```
    git push origin [name_of_your_new_branch]
    ```

6. **Create a Pull Request**:
    Open a pull request on GitHub to merge your branch into the `development` branch. Ensure you provide a comprehensive description of the changes made.

### Contributing:
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Remember, always make a pull request to the `development` branch.