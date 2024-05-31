# GEMMA 7B with GROQ - Streamlit PDF to Vector Database API

Welcome to the GEMMA 7B with GROQ repository! This project showcases the integration of the GEMMA 7B language model with GROQ to process a fixed PDF document, convert its content into a vector database, and provide an interactive Q&A interface using Streamlit. Users can ask questions and receive answers, along with the relevant data, all through a user-friendly web application.

## Overview

This repository provides a streamlined solution for converting a PDF document into a searchable vector database using the GROQ language and GEMMA 7B model. The application is built with Streamlit to enable an interactive question-and-answer interface. Users can explore the content of the PDF, ask questions, and view relevant data used to generate responses.

### Features

- **PDF Processing**: Extract text from a fixed PDF document (default is a ViT research paper).
- **Vectorization**: Convert extracted text into vector representations using GEMMA 7B.
- **Interactive Q&A**: Ask questions and receive answers, along with the relevant data, through a Streamlit web app.
- **Data Folder**: Easily change the PDF document by placing a new file in the `data` folder.
- **Environment Configuration**: Manage API keys using a `.env` file.

### Getting Started

#### Prerequisites

- Python 3.8 or higher
- Streamlit
- GROQ library
- GEMMA 7B model
- Required Python packages (listed in `requirements.txt`)
- GROQ and Google API keys

#### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/NevroHelios/gemma7b-groq-streamlit.git
   cd gemma7b-groq-streamlit
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download and set up the GEMMA 7B model.

4. Obtain your GROQ and Google API keys and add them to a `.env` file in the root directory:
   ```
   GROQ_API_KEY=your_groq_api_key
   GOOGLE_API_KEY=your_google_api_key
   ```

#### Usage

1. **Prepare the PDF**:
   - Place your PDF file in the `data` directory (default file is a ViT research paper).

2. **Run the Streamlit App**:
   - Start the Streamlit app:
     ```bash
     streamlit run app.py
     ```

3. **Interact with the App**:
   - Open your browser and navigate to the provided local URL (e.g., `http://localhost:8501`).
   - Ask questions about the PDF content and view relevant data.

### Directory Structure

- **`data/`**: Contains the PDF file to be processed. Default file is a ViT research paper.
- **`app.py`**: Main Streamlit application file.
- **`requirements.txt`**: List of required Python packages.
- **`.env`**: File to store API keys securely.

### Contributing

We welcome contributions to enhance the functionality and performance of this project. Please fork the repository and submit a pull request with your changes. Ensure that your code follows the established style guidelines and passes all tests.

### License

This project is licensed under the MIT License. See the `LICENSE` file for details.

### Acknowledgements

Special thanks to the developers and contributors of GEMMA 7B, GROQ, and Streamlit for their powerful tools and support.

---

Feel free to explore, use, and contribute to this repository. If you have any questions or need assistance, please open an issue.

Happy coding!
