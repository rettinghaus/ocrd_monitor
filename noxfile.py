import nox


@nox.session
def mypy(session: nox.Session) -> None:
    session.install("-e", ".[dev]")
    session.run("mypy", "--strict", "ocrdbrowser", "ocrdmonitor", "tests")


@nox.session
def pytest(session: nox.Session) -> None:
    session.install("-e", ".[dev]")
    session.install("pytest-clarity")

    session.run("pytest", "-vv", "tests", *session.posargs)
