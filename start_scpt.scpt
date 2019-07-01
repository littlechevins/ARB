tell application "iTerm2"
    set newWindow to (create window with default profile)
    tell current session of newWindow
      write text "osascript start_scpt_windows.scpt"
    end tell
end tell
