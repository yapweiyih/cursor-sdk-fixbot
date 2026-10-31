"""preToolUse hook: the agent may change code, never the tests."""

import json
import sys
from pathlib import Path

event = json.load(sys.stdin)
path = Path(event["tool_input"].get("file_path", ""))
if path.name.startswith("test_"):
    print(json.dumps({"permission": "deny", "agent_message": "Tests are read-only. Fix the code."}))
else:
    print(json.dumps({"permission": "allow"}))
