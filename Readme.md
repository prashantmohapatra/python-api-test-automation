
# Install
pip install requests <br>
pip install pytest <br>
pip install allure-pytest <br>

# Activate virtual environment:
source venv/bin/activate <br>

# Set environment variables
export ENVIRONMENT=dev
export TRACE_API_CALLS=true

# Run the test:
pytest --alluredir=allure_result_folder <br>
allure serve allure_result_folder