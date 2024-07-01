import pytest
from Homework_11.homework_10 import log_event
import logging


@pytest.mark.parametrize("username, status, log_level, log_message", [
    ("test_user_success", "success", logging.INFO, "Login event - Username: test_user_success, Status: success"),
    ("test_user_expired", "expired", logging.WARNING, "Login event - Username: test_user_expired, Status: expired"),
    ("test_user_error", "failed", logging.ERROR, "Login event - Username: test_user_error, Status: error")
])
def test_log_event(username, status, log_level,log_message):

    log_event(username, status)

    expected_log_message = f"Login event - Username: {username}, Status: {status}"

    with open('login_system.log', 'r') as log_file:
        log_contents = log_file.read()

        assert expected_log_message in log_contents, f"Expected log message not found in log file: {expected_log_message}"

        log_level_name = logging.getLevelName(log_level)

        assert log_level_name in log_contents, f"Expected log level {log_level_name} not found in log file"

