from click.testing import CliRunner
from  task_cli.cli import cli
import pytest

@pytest.mark.skip(reason="Not implemented")
def test_add_task():
    runner = CliRunner()
    result = runner.invoke(cli, ['add', "first task"])
    assert result.exit_code == 0
    assert result.output != "first task"