from flask import Flask, request
import subprocess
from pathlib import Path


app = Flask(__name__)
TRACE_DIR = Path("test-results/traces").resolve()


def is_valid_trace_file(trace_filename: str) -> Path:
    trace_path = (TRACE_DIR / trace_filename).resolve()
    try:
        trace_path.relative_to(TRACE_DIR)
    except ValueError:
        raise ValueError("Invalid trace file path.")
    if not trace_path.exists():
        raise FileNotFoundError("Trace file not found.")
    return trace_path


@app.route('/show-trace')
def show_report():
    trace_files = request.args.getlist("trace")
    if not trace_files:
        return "Missing trace file parameter.", 400

    for trace_filename in trace_files:
        try:
            trace_path = is_valid_trace_file(trace_filename)
            cmd = ["playwright", "show-trace", str(trace_path)]
            subprocess.Popen(cmd)
            return f"Report command executed for {trace_filename}"
        except (ValueError, FileNotFoundError) as e:
            continue

    return "No valid trace files provided.", 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)