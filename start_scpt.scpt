tell application "iTerm2"
    set newWindow to (create window with default profile)
    tell current session of newWindow
      write text "osascript start_scpt_bnode_only.scpt"
    end tell
end tell
