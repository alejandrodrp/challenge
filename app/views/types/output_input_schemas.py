from typing import Generic, Type, TypeVar, TypedDict

TInput = TypeVar("TInput")
TOutput = TypeVar("TOutput")


class SchemaPair(Generic[TInput, TOutput], TypedDict):
    input: Type[TInput]
    output: Type[TOutput]


class OperationSchemaType(Generic[TInput, TOutput], TypedDict):
    get: SchemaPair[TInput, TOutput]
    post: SchemaPair[TInput, TOutput]
    put: SchemaPair[TInput, TOutput]
    delete: SchemaPair[TInput, TOutput]
