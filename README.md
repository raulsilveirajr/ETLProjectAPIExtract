# ETL Project - API Data Extraction

## Overview
This project implements an ETL (Extract, Transform, Load) pipeline that extracts data from various APIs, transforms it according to business rules, and loads it into a target database.

## Features
- API data extraction with error handling and retry mechanisms
- Data transformation and cleaning
- Configurable data loading to different destinations
- Logging and monitoring capabilities
- Rate limiting support for API calls

## Prerequisites
- Python 3.8+
- pip (Python package installer)
- poetry (Python package manager)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/raulsilveirajr/ETLProjectAPIExtract
cd ETLProjectAPIExtract
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Configuration
1. Copy the `.env.example` file to `.env`
2. Fill in your API credentials and database connection details:
```env
API_KEY=your_api_key
API_SECRET=your_api_secret
DB_CONNECTION_STRING=your_db_connection_string
```

## Usage
Run the ETL pipeline:
```bash
python src/main.py
```

### Command-line Arguments
- `--date`: Process data for a specific date (YYYY-MM-DD)
- `--config`: Use a specific configuration file
- `--debug`: Enable debug logging

## Project Structure
```
etl-project/
├── src/
│   ├── extractors/      # API data extraction modules
│   ├── transformers/    # Data transformation logic
│   ├── loaders/         # Database loading modules
│   └── main.py         # Main execution file
├── config/             # Configuration files
├── tests/             # Unit and integration tests
├── logs/              # Log files
└── README.md
```

## Testing
Run the test suite:
```bash
pytest tests/
```

## Logging
Logs are stored in the `logs/` directory. The logging level can be configured in `config/logging.yaml`.

## Error Handling
- The pipeline implements automatic retries for failed API calls
- Failed records are stored in an error queue for later processing
- Email notifications for critical errors (configurable)

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors
- Your Name (@yourusername)

## Acknowledgments
- List any third-party libraries or tools used
- Credit any inspirations or references
```

This README template provides:
1. A clear project overview
2. Installation and setup instructions
3. Usage examples with command-line arguments
4. Project structure explanation
5. Testing and logging information
6. Error handling details
7. Contributing guidelines
8. License and author information

You can customize this template by:
1. Adding specific API details you're working with
2. Including actual configuration examples
3. Adding more detailed usage scenarios
4. Updating the project structure to match your actual implementation
5. Adding specific requirements for your project
