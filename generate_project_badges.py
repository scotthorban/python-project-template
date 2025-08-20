"""A script to generate project badges designed for use in a README.md file."""

import json
import os
import xml.etree.ElementTree as ET
from datetime import datetime

from definitions import PROJECT_ROOT_DIR

IMG_PATH = PROJECT_ROOT_DIR.joinpath("docs/img")


def get_python_version():
    """Return Python version."""
    return "3.11"


def get_ruff_result() -> str:
    """Read and return Ruff result from PROJECT_ROOT_DIR/reports/linting.txt."""
    report_path = PROJECT_ROOT_DIR.joinpath("reports/ruff.json")
    with open(report_path, "r") as linting_file:
        content = json.load(fp=linting_file)

    result = "Passing" if content == [] else "Failing"
    return result


def get_unittest_results() -> str:
    """Read and return test results from PROJECT_ROOT_DIR/reports/unit-tests.xml."""
    test_report_path = PROJECT_ROOT_DIR.joinpath("reports/unit-tests.xml")
    root = ET.parse(test_report_path).getroot()

    failures = 0
    skipped = 0
    tests = 0
    for type_tag in root.findall("testsuite"):
        failures = int(type_tag.get("failures"))
        skipped = int(type_tag.get("skipped"))
        tests = int(type_tag.get("tests"))

    text = ""
    if failures > 0:
        text = f"{failures} skipped {tests - failures} passed"

    if skipped > 0:
        text = f"{skipped} skipped {tests - skipped} passed"

    if failures == 0 and skipped == 0:
        text = f"{tests} passed"

    return text


def get_coverage_score() -> float:
    """Read and return Coverage from PROJECT_ROOT_DIR/reports/coverage.xml."""
    coverage_report_path = PROJECT_ROOT_DIR.joinpath("reports/coverage.xml")
    root = ET.parse(coverage_report_path).getroot()
    coverage_score = root.attrib["line-rate"]
    return round(100.0 * float(coverage_score), 1)


def make_badges() -> None:
    """Create badges from python version, linter score, unittest results, coverage score and latest release month & year."""
    red = "#be403c"
    warn = "#c8991d"
    green = "#00a10b"

    print("Generating Python badge")
    try:
        python_version = get_python_version()
        if python_version:
            if "python.svg" in os.listdir(IMG_PATH):
                os.remove(f"{IMG_PATH}/python.svg")

        os.system(f'uv run anybadge -l python -v "{python_version}" -f "{IMG_PATH}/python.svg" --color="#0f5fa5"')

    except Exception as exception:
        print(str(exception))

    print("Generating Unittest badge")
    try:
        unittest_results = get_unittest_results()
        if unittest_results:
            if "unittest.svg" in os.listdir(IMG_PATH):
                os.remove(f"{IMG_PATH}/unittest.svg")

            if "failed" in unittest_results:
                os.system(
                    f'uv run anybadge -l unittest -v "{unittest_results}" -f "{IMG_PATH}/unittest.svg" --color={red}'
                )
            elif "skipped" in unittest_results:
                os.system(
                    f'uv run anybadge -l unittest -v "{unittest_results}" -f "{IMG_PATH}/unittest.svg" --color={warn}'
                )
            else:
                os.system(
                    f'uv run anybadge -l unittest -v "{unittest_results}" -f "{IMG_PATH}/unittest.svg" --color={green}'
                )

    except Exception as exception:
        print(str(exception))

    print("Generating Coverage badge")
    try:
        coverage_score = get_coverage_score()
        if coverage_score:
            if "coverage.svg" in os.listdir(IMG_PATH):
                os.remove(f"{IMG_PATH}/coverage.svg")

            os.system(f'uv run anybadge --value={coverage_score} -f "{IMG_PATH}/coverage.svg" coverage')

    except Exception as exception:
        print(str(exception))

    print("Generating Ruff badge")
    try:
        ruff_result = get_ruff_result()
        if ruff_result:
            if "pylint.svg" in os.listdir(IMG_PATH):
                os.remove(f"{IMG_PATH}/ruff.svg")

            color = "green" if ruff_result == "Passing" else "red"
            os.system(f'uv run anybadge -l ruff -v "{ruff_result}" -f "{IMG_PATH}/ruff.svg" --color={color}')

    except Exception as exception:
        print(str(exception))

    print("Generating Release badge")
    try:
        if "release.svg" in os.listdir(IMG_PATH):
            os.remove(f"{IMG_PATH}/release.svg")

        current_month = datetime.now().strftime("%b")
        current_year = datetime.now().year

        os.system(
            f'uv run anybadge -l "released" -v "{current_month} {current_year}" -f "{IMG_PATH}/release.svg" --color="#0f5fa5"'
        )

    except Exception as exception:
        print(str(exception))


if __name__ == "__main__":
    make_badges()
