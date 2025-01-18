import sys
from pylint.lint import Run

THRESHOLD = 9

score = Run(["C:\code\CloudResume\SAM\Lambda\\app.py"], do_exit=False).linter.stats.global_note

if score < THRESHOLD:
    sys.exit(1)
sys.exit(0)
