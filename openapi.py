from typing import List


def get_type_schema(s: List[str]) -> dict:
    if not s:
        return {}

    if len(s) > 1:
        return {
            "type": "object",
            "additionalProperties": {
                "oneOf": [
                    get_type_schema([ss])
                    for ss in s
                ]}
        }

    s = s[0]
    if s == "Integer":
        return {
            "type": "integer",
            "format": "int64"
        }
    if s == "Float":
        return {
            "type": "number",
            "format": "float64"
        }
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


def method_parameters(method_data: dict) -> List[dict]:
    return [{
        "name": param.get("name"),
        "required": param.get("required"),
        "in": "query",
        "schema": get_type_schema(param.get("types"))
    } for param in method_data.get("fields", [])]


def to_openapi(data: dict) -> dict:
    return {
        "openapi": "3.0.0",
        "info": {
            "title": "telegram-bot-api",
            "description": "Unofficial telegram-bot-api OpenAPI spec. "
                           "Generated from the Bot API docs at https://core.telegram.org/bots/api",
            "version": data.get("version"),
        },
        "paths": openapi_methods(data),
        "components": {
            "schemas": openapi_types(data),
        }
    }


def openapi_methods(data):
    methods = {}
    for method, methodData in data.get("methods", {}).items():
        methods[f"/{method}"] = {
            "post": {
                "summary": method,
                "description": "\n".join(methodData.get("description")),
                "parameters": method_parameters(methodData),
                "responses": {
                    200: {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "ok": {"type": "boolean"},
                                        "result": get_type_schema(methodData.get("returns")),
                                    },
                                }
                            }
                        }
                    },
                    "4XX": {
                        "description": "Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "ok": {"type": "boolean"},
                                        "error_code": {"type": "integer", "format": "int64"},
                                        "description": {"$ref": "#/components/schemas/ResponseParameters"},
                                    }
                                }
                            }
                        }
                    },
                    "5XX": {
                        # TODO
                        "description": "Server error",
                    }
                }
            }
        }
    return methods


def field_properties(f):
    schema = get_type_schema(f.get("types"))
    if "$ref" not in schema:
        schema["description"] = f.get("description")
    else:
        return {
            "description": f.get("description"),
            "allOf": [schema]
        }

    return schema


def openapi_types(data):
    types = {}
    for name, typeData in data.get("types", {}).items():
        types[name] = {
            "type": "object",
            "description": "\n".join(typeData.get("description", [])),
            "properties": {f.get("name"): field_properties(f) for f in typeData.get("fields", [])},
        }

        required = [f.get("name") for f in typeData.get("fields", []) if f.get("required")]
        if required:
            types[name]["required"] = required

    return types
