import pytest
import logging

from lesson_11.homework_10 import log_event


@pytest.mark.parametrize("username, status, expected_level", [
    ("Monty Python", "success", logging.INFO),
    ("Benny Hill", "expired", logging.WARNING),
    ("Rowan Atkinson", "failed", logging.ERROR),
    ("Philomena Cunk", "other", logging.ERROR),
])
def test_log_event(caplog, username, status, expected_level):
    with caplog.at_level(logging.INFO):
        log_event(username, status)

        # Перевірка чи містяться логи
        assert len(caplog.records) == 1

        # Отримання першого (і єдиного) запису логів
        log_record = caplog.records[0]

        # Перевірка рівня логування
        assert log_record.levelno == expected_level

        # Перевірка повідомлення логу
        assert log_record.message == f"Login event - Username: {username}, Status: {status}"
