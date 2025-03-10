from typing import Type, TypeAlias, TypedDict

from pydantic import BaseModel

TSchema: TypeAlias = Type[BaseModel]


class SchemaPair(TypedDict):
    input: TSchema
    output: TSchema


class OperationSchemaType(TypedDict):
    get: SchemaPair
    post: SchemaPair
    put: SchemaPair
    delete: SchemaPair
