#!/bin/bash
PIPE_PATH="/tmp/clipboard_watcher_pipe"
wl-paste -n > "$PIPE_PATH"

