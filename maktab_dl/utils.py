import os
import json
import pathlib
from lxml.html import Element
import re
from pydantic import BaseModel
from typing import Type, TypeVar
from pydantic import ValidationError


def save_cookies(client, filepath):
    # Convert cookies to a dictionary
    cookies_dict = {cookie.name: cookie.value for cookie in client.cookies.jar}
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(cookies_dict, file)


# Load cookies from a file
def load_cookies(client, filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        cookies_dict = json.load(file)
    # Load cookies into the client
    for name, value in cookies_dict.items():
        client.cookies.set(name, value)


def load_cookies_from_json_file(client, json_file):
    with open(json_file, "r") as file:
        cookies: list = json.load(file)
    # Load cookies into the client
    for cookie in cookies:
        client.cookies.set(cookie["name"], cookie["value"])


def get_xpath_first_element(node: Element, xpath: str) -> str | None:
    tags = node.xpath(xpath)
    if tags and len(tags) > 0:
        output = tags[0]
        if isinstance(output, str):
            return output.strip()
        return output


def remove_extra_spaces(text: str) -> str:
    return " ".join(text.split())


def save_model_to_json(model: BaseModel, filename: str, indent: int = 4) -> None:
    """Saves a Pydantic model to a JSON file with UTF-8 encoding and indentation."""
    with open(filename, "w", encoding="utf-8") as f:
        # Option 1: Directly use the model's json() method with indent
        json_string = model.model_dump_json(indent=indent)
        f.write(json_string)


T = TypeVar("T", bound=BaseModel)


def load_model_from_json(model_type: Type[T], filename: str) -> T:
    """Loads a Pydantic model from a JSON file.

    Args:
        model_type: The Pydantic model class (e.g., MyModel).
        filename: The path to the JSON file.

    Returns:
        An instance of the Pydantic model if loading is successful.

    Raises:
        FileNotFoundError: If the JSON file does not exist.
        json.JSONDecodeError: If the JSON file is not valid JSON.
        ValidationError: If the JSON data doesn't match the model.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            json_data = json.load(f)
            model_instance = model_type(**json_data)
            return model_instance

    except FileNotFoundError:
        raise FileNotFoundError(f"JSON file not found: {filename}")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(
            f"Invalid JSON format in {filename}: {e.msg}", e.doc, e.pos
        )
    except ValidationError as e:
        raise ValidationError(
            f"JSON data does not match the model: {e}", model=model_type
        )


def sanitize_filename(filename, replacement="_"):
    """Replaces or removes characters that are not allowed in filenames, while preserving UTF-8."""
    # # Replace spaces with underscores.
    # filename = re.sub(r'\s+', replacement, filename)

    # Remove or replace problematic characters.
    filename = re.sub(r'[\\/:*?"<>|]', replacement, filename)

    # remove leading and trailing underscores and points
    # filename = filename.strip('_').strip('.')

    # Limit to a maximum length for safety.
    max_length = 255  # Reasonable max for most file systems
    return filename[:max_length]


def get_package_file_path():
    """
    Constructs the full path to package dir.
    """
    package_dir = pathlib.Path(__file__).parent.resolve()
    return package_dir


def get_cookies_default_file_path():
    """
    Constructs the full path to cookie file in package dir.
    """
    package_dir = get_package_file_path()
    return os.path.join(package_dir, "cookies.json")


def get_user_default_path():
    """
    Constructs the full path to  default user account dir.
    """
    return os.path.expanduser("~")


def get_boolean_manual(prompt):
    while True:
        response = input(f"{prompt} (yes/no): ").strip().lower()
        if response in ("yes", "y", "true", "t"):
            return True
        elif response in ("no", "n", "false", "f"):
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
