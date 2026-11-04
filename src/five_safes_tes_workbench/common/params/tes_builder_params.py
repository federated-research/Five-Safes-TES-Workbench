from typing import Literal

from pydantic import BaseModel
import tes


class InputTESParams(BaseModel):
    name: str | None = None
    description: str | None = None
    url: str | None = None
    path: str
    type: Literal["FILE", "DIRECTORY"] | None = "DIRECTORY"
    content: str | None = None
    streamable: bool | None = None

    def make_tes_inputs(self) -> tes.Input:
        return tes.Input(
                name=self.name,
                description=self.description,
                url=self.url,
                path=self.path,
                type=str(self.type),
                content=self.content,
                streamable=self.streamable
                )


class OutputTESParams(BaseModel):
    name: str | None = None
    description: str | None = None
    url: str
    path: str
    type: Literal["FILE", "DIRECTORY"] = "DIRECTORY"
    path_prefix: str | None = None

    def make_tes_outputs(self) -> tes.Output:
        return tes.Output(
                name=self.name,
                description=self.description,
                url=self.url,
                path=self.path,
                type=str(self.type),
                path_prefix=self.path_prefix
                )


class ExecutorTESParams(BaseModel):
    image: str
    command: list[str]
    workdir: str | None = None
    stdin: str | None = None
    stdout: str | None = None
    stderr: str | None = None
    env: dict[str, str] | None = None
    ignore_error: bool | None = None

    def make_tes_executor(self) -> tes.Executor:
        return tes.Executor(
                image=self.image,
                command=self.command,
                workdir=self.workdir,
                stdin=self.stdin,
                stderr=self.stderr,
                env=self.env,
                ignore_error=self.ignore_error
                )


class TESTaskParams(BaseModel):
    """
    Parameters for building a TES task
    """

    name: str
    executors: list[ExecutorTESParams]
    description: str | None = None
    inputs: list[InputTESParams] | None = None
    outputs: list[OutputTESParams] | None = None
    volumes: list[str] | None = None
