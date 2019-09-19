tell application "iTerm2"
    set newWindow1 to (create window with default profile)
    tell current session of newWindow1
      write text "osascript start_scpt_enode_only_europe.scpt"
    end tell
end tell
