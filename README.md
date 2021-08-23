# domain_search (run in venv)

Relevant code in 'app' folder:
  1. application.py (routes and actions)
  2. unittests.py (contains 4 tests)
  3. 'static' folder (contains styles.css)
  4. "templates' folder (contains 3 html templates)

# Instructions:

To run application:
  1. 'cd' to the root folder 'domainsearch'
  2. 'flask run' in terminal (the .env file pre-sets the FLASK_APP so don't need to 'export FLASK_APP=application.py' in CLI

To run tests:
  1. 'cd' to the root folder 'domainsearch'
  2. 'python app/unittests.py' in CLI
  
Dependencies:
  1. Flask (framework)
  2. pip (package manager)
  3. jinja (allows embedded code in HTML)
  4. python-dotenv (creates environment variables from .env file)
