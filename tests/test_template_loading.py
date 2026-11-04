from pathlib import Path

import pytest

from five_safes_tes_workbench.common.params.tes_builder_params import (
    ExecutorTESParams,
    TESTaskParams,
)
from five_safes_tes_workbench.core.tes.templates.load_template import (
    load_template,
)


@pytest.fixture
def task_single_executor() -> TESTaskParams:
    # This is a real task from https://5s-tes.federated-research.com/Submission/GetASubmission/4441
    return load_template(Path("./tests/test_data/single-executor-task.json"))


def test_task_single_executor(task_single_executor):
    assert task_single_executor.name == "intes"

    assert task_single_executor.description is None

    assert len(task_single_executor.executors) == 1

    executor = task_single_executor.executors[0]
    assert isinstance(executor, ExecutorTESParams)
    assert executor.image == "ubuntu"
    assert executor.command == ["cat", "/data/tesdata.txt"]
    assert executor.workdir == "/outputs"


@pytest.fixture
def task_multiple_executor() -> TESTaskParams:
    return load_template(Path("./tests/test_data/multiple-executor-task.json"))


def test_task_multiple_executor(task_multiple_executor):
    assert task_multiple_executor.name == "Test - DrugUtilisation add metrics"
    assert (
        task_multiple_executor.description
        ==  "Generate an acetaminophen cohort, add drug utilisation metrics, "
            "summarise one metric, then clean up"
    )

    assert len(task_multiple_executor.executors) == 4
