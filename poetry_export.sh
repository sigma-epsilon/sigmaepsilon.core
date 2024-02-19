#!/bin/bash
ECHO "Exporting poetry dependencies to requirements.txt"
poetry export -f requirements.txt --output requirements.txt
ECHO "Exporting poetry dependencies to requirements-test.txt"
poetry export -f requirements.txt --only test --output requirements-test.txt
ECHO "Exporting poetry dependencies to requirements-dev.txt"
poetry export -f requirements.txt --only dev --output requirements-dev.txt
ECHO "Exporting poetry dependencies to docs/requirements.txt"
poetry export -f requirements.txt --only docs --output ./docs/requirements.txt
ECHO "All done!"