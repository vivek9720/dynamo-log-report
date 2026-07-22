import json
from pathlib import Path

import pytest

REPORT = Path("/app/report.json")

# Expected values are computed directly from the fixed /app/access.log:
#   6 non-empty request lines
#   3 distinct client IPs (192.168.0.1, 192.168.0.2, 10.0.0.5)
#   /index.html is requested 3 times (more than any other path)
EXPECTED_TOTAL_REQUESTS = 6
EXPECTED_UNIQUE_IPS = 3
EXPECTED_TOP_PATH = "/index.html"


@pytest.fixture(scope="module")
def report():
    """Load /app/report.json once for all value assertions."""
    assert REPORT.exists(), "no report.json found at /app/report.json"
    with REPORT.open() as f:
        return json.load(f)


def test_report_is_json_object_with_exact_keys(report):
    """Criterion 1: /app/report.json is a single JSON object with exactly the
    three keys total_requests, unique_ips, and top_path."""
    assert isinstance(report, dict), "report.json must contain a JSON object"
    assert set(report.keys()) == {"total_requests", "unique_ips", "top_path"}, (
        f"expected exactly keys total_requests/unique_ips/top_path, got {sorted(report.keys())}"
    )


def test_total_requests(report):
    """Criterion 2: total_requests equals the number of requests in the log."""
    assert report["total_requests"] == EXPECTED_TOTAL_REQUESTS, (
        f"total_requests should be {EXPECTED_TOTAL_REQUESTS}, got {report['total_requests']!r}"
    )


def test_unique_ips(report):
    """Criterion 3: unique_ips equals the number of distinct client IPs."""
    assert report["unique_ips"] == EXPECTED_UNIQUE_IPS, (
        f"unique_ips should be {EXPECTED_UNIQUE_IPS}, got {report['unique_ips']!r}"
    )


def test_top_path(report):
    """Criterion 4: top_path is the most frequently requested path."""
    assert report["top_path"] == EXPECTED_TOP_PATH, (
        f"top_path should be {EXPECTED_TOP_PATH!r}, got {report['top_path']!r}"
    )
