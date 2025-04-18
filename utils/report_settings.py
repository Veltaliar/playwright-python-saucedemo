import os

from pathlib import Path
from datetime import datetime
from _pytest.runner import TestReport
import pytest

from playwright.sync_api import Page

REPORT_DIR = Path("reports")
TRACE_DIR = REPORT_DIR / "traces"
SCREENSHOT_DIR = REPORT_DIR / "screenshots"


def setup_reporting():
    """ Setup the reporting directory and remove old reports if they exist. """
    REPORT_DIR.mkdir(exist_ok=True)
    TRACE_DIR.mkdir(exist_ok=True)
    SCREENSHOT_DIR.mkdir(exist_ok=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """ Hook to capture the test report and attach extra items. """
    outcome = yield
    rep: TestReport = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
    if hasattr(item, "extra"):
        rep.extra = item.extra


@pytest.fixture(autouse=True)
def capture_trace_on_failure(request, page: Page):
    """ Fixture to capture traces and screenshots on test failure. """
    page.context.tracing.start(title=request.node.name, screenshots=True, snapshots=True, sources=True)
    yield
    if request.node.rep_call.failed:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        safe_name = request.node.name.replace("/", "_").replace("\\", "_").replace(":", "_")
        trace_path = TRACE_DIR / f"{safe_name}_{timestamp}.zip"
        screenshot_path = SCREENSHOT_DIR / f"{safe_name}.png"
        try:
            page.context.tracing.stop(path=str(trace_path))
            page.screenshot(path=str(screenshot_path))
        except Exception as e:
            print(f"Error capturing trace: {e}")
    else:
        page.context.tracing.stop()


def generate_trace_url(traces):
    """ Generate a URL for the traces captured during the test.
    Used with trace_server.py to open Playwright trace viewer. """
    query_params = "&".join([f"trace={trace.name}" for trace in traces])
    return f"http://127.0.0.1:5000/show-trace?{query_params}"


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    """ Hook to add custom HTML to the report summary. """
    attached_html = (
        '<div class="attached-files" style="margin-top: 20px; padding: 10px; '
        'border: 1px solid #ddd; border-radius: 4px;">'
    )
    screenshots = list(SCREENSHOT_DIR.glob("*.png"))
    traces = list(TRACE_DIR.glob("*.zip"))

    if screenshots or traces:
        attached_html += "<h2>Attached Files</h2>"

    browser_name = os.getenv("BROWSER")
    filtered_screenshots = [s for s in screenshots if browser_name in s.name]
    filtered_traces = [t for t in traces if browser_name in t.name]

    if filtered_screenshots:
        attached_html += "<h3>Screenshots</h3>"
        for screenshot in filtered_screenshots:
            relative_path = screenshot.relative_to(REPORT_DIR)
            attached_html += (
                f'<a href="{relative_path}" target="_blank" style="display:inline-block; margin-right:10px;">'
                f'<img src="{relative_path}" alt="Screenshot" height="150"/></a>'
            )

    if filtered_traces:
        attached_html += "<h3>Traces</h3>"
        for trace in filtered_traces:
            trace_url = generate_trace_url([trace])
            trace_name = trace.name
            attached_html += f'<p>{trace_name} - <a href="{trace_url}" target="_blank">Open Trace</a></p>'

    attached_html += "</div>"
    prefix.append(attached_html)
