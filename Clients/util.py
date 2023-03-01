from uuid import UUID
import typing


def uuid_to_str(data):
    if isinstance(data, str) or isinstance(data, int) or data is None:
        return data
    elif isinstance(data, UUID):
        return str(data)
    elif isinstance(data, list):
        return list(map(uuid_to_str, data))
    elif isinstance(data, dict):
        return {key: uuid_to_str(value) for key, value in data.items()}
    raise TypeError(f"unexpected type: {type(data)}")

