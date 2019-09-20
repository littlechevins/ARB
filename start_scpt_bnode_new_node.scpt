tell application "iTerm2"
  tell current window
    set newTab0 to (create tab with default profile)
    tell current session of newTab0
      write text "echo exporting flask app"
      write text "python node.py -n NewNode -ip 5021 -t backbone"
    end tell
  end tell
end tell
