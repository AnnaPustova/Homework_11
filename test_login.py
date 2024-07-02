import pytest
from Homework_11.homework_10 import log_event
import logging

@pytest.mark.parametrize("username, status, log_message", [
    ("test_user_success", "success","Login event - Username: test_user_success, Status: success"),
    ("test_user_expired", "expired", "Login event - Username: test_user_expired, Status: expired"),
    ("test_user_error", "failed",  "Login event - Username: test_user_error, Status: failed")
])
def test_log_event(username, status,  log_message):
    log_event(username, status)

    expected_log_message = f"Login event - Username: {username}, Status: {status}"

    with open('login_system.log', 'r') as log_file:
        log_contents = log_file.readlines()

    last_line = log_contents[-1]
    assert expected_log_message in last_line, f"Expected log message not found in log file: {expected_log_message}"


