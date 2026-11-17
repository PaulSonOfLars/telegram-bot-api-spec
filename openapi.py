from typing import Any


def get_type_schema(ss: list[str]) -> dict[str, Any]:
    if not ss:
        return {}

    if len(ss) > 1:
        return {"oneOf": [get_type_schema([s]) for s in ss]}

    s = ss[0]
    if s == "Integer":
        return {"type": "integer", "format": "int64"}
    if s == "Float":
        return {"type": "number", "format": "double"}
    if s == "Boolean":
        return {
            "type": "boolean",
        }
    if s == "String":
        return {
            "type": "string",
        }

    if s.startswith("Array of"):
        return {
            "type": "array",
            "items": get_type_schema([s.removeprefix("Array of ")]),
        }

    return {"$ref": f"#/components/schemas/{s}"}


def method_parameters(method_data: dict) -> list[dict]:
    return [
        {
            "name": param.get("name"),
            "required": param.get("required", False),
            "in": "query",
            "description": param.get("description"),
            "schema": get_type_schema(param.get("types")),
        }
        for param in method_data.get("fields", [])
    ]


def to_openapi(data: dict) -> dict:
    return {
        "openapi": "3.1.0",
        "info": {
            "title": "telegram-bot-api",
            "description": "Unofficial telegram-bot-api OpenAPI spec. "
            "Generated from the Bot API docs at https://core.telegram.org/bots/api",
            "version": data.get("version"),
        },
        "servers": [
            {
                "url": "https://api.telegram.org/bot{token}",
                "description": "The official hosted Bot API server from Telegram.",
                "variables": {
                    "token": {
                        "description": "The bot's API token, as obtained from t.me/botfather.",
                        "default": "123:XYZ",
                    }
                },
            }
        ],
        "paths": openapi_methods(data),
        "components": {
            "schemas": openapi_types(data),
        },
    }


def openapi_methods(data) -> dict[str, Any]:
    methods = {}
    for method, methodData in data.get("methods", {}).items():
        methods[f"/{method}"] = {
            "post": {
                "operationId": method,
                "summary": method,
                "description": "\n".join(methodData.get("description", [])),
                "parameters": method_parameters(methodData),
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "ok": {"type": "boolean"},
                                        "result": get_type_schema(
                                            methodData.get("returns")
                                        ),
                                    },
                                }
                            }
                        },
                    },
                    "4XX": {
                        "description": "Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "ok": {"type": "boolean"},
                                        "error_code": {
                                            "type": "integer",
                                            "format": "int64",
                                        },
                                        "description": {"type": "string"},
                                        "parameters": {
                                            "$ref": "#/components/schemas/ResponseParameters"
                                        },
                                    },
                                }
                            }
                        },
                    },
                    "5XX": {
                        # TODO
                        "description": "Server error",
                    },
                },
            }
        }
    return methods


def field_properties(f) -> dict[str, Any]:
    schema = get_type_schema(f.get("types"))
    if "$ref" not in schema:
        schema["description"] = f.get("description")
    else:
        return {"description": f.get("description"), "allOf": [schema]}

    return schema


def openapi_types(data: dict):
    types = {}
    for name, typeData in data.get("types", {}).items():
        types[name] = {
            "type": "object",
            "description": "\n".join(typeData.get("description", [])),
            "properties": {
                f.get("name"): field_properties(f) for f in typeData.get("fields", [])
            },
        }

        required = [
            f.get("name") for f in typeData.get("fields", []) if f.get("required")
        ]
        if required:
            types[name]["required"] = required

    return types
