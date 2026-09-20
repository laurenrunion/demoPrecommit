import re
import sys

# Matches patterns like ABC-123, PROJ-4567
JIRA_PATTERN = re.compile(r"[A-Z][A-Z0-9]+-\d+")


def main():
    commit_msg_filepath = sys.argv[1]
    with open(commit_msg_filepath, "r") as f:
        commit_msg = f.read()

    if not JIRA_PATTERN.search(commit_msg):
        print("Commit message must contain a Jira ticket number (e.g. ABC-123).")
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
