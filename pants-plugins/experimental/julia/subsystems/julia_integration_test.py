from pants.testutil.pants_integration_test import run_pants


def test_subsystem_help_is_registered() -> None:
    pants_run = run_pants(
        [
            "--backend-packages=experimental.julia",
            "help",
            "julia",
        ]
    )
    pants_run.assert_success()
