"""Tests for Nox helper configuration."""

from noxfile import CLIArgs


def test_cli_args_parses_hyphenated_flags() -> None:
    """Hyphenated Nox arguments map to underscore field names."""
    args = CLIArgs.parse(["--ruff-fix"])

    assert args.ruff_fix is True


def test_cli_args_parses_option_values() -> None:
    """Nox arguments with values are preserved."""
    args = CLIArgs.parse(["--junitxml", "junit.xml"])

    assert args.junitxml == "junit.xml"
