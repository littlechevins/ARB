tell application "iTerm2"
  tell current window
    set newTab0 to (create tab with default profile)
    tell current session of newTab0
      write text "echo exporting flask app"
      write text "python node.py -n 1 -ip 5001 -t backbone"
    end tell
    set newTab1 to (create tab with default profile)
    tell current session of newTab1
      write text "echo exporting flask app"
      write text "python node.py -n 2 -ip 5002 -t backbone"
    end tell
    set newTab2 to (create tab with default profile)
    tell current session of newTab2
      write text "echo exporting flask app"
      write text "python node.py -n 3 -ip 5003 -t backbone"
    end tell
    set newTab3 to (create tab with default profile)
    tell current session of newTab3
      write text "echo exporting flask app"
      write text "python node.py -n 4 -ip 5004 -t backbone"
    end tell
    set newTab11 to (create tab with default profile)
    tell current session of newTab11
      write text "echo exporting flask app"
      write text "python node.py -n 11 -ip 5011 -t end"
    end tell
    set newTab12 to (create tab with default profile)
    tell current session of newTab12
      write text "echo exporting flask app"
      write text "python node.py -n 12 -ip 5012 -t end"
    end tell
    set newTab13 to (create tab with default profile)
    tell current session of newTab13
      write text "echo exporting flask app"
      write text "python node.py -n 13 -ip 5013 -t end"
    end tell
    set newTab14 to (create tab with default profile)
    tell current session of newTab14
      write text "echo exporting flask app"
      write text "python node.py -n 14 -ip 5014 -t end"
    end tell
    set newTab15 to (create tab with default profile)
    tell current session of newTab15
      write text "echo exporting flask app"
      write text "python node.py -n 15 -ip 5015 -t end"
    end tell
  end tell
end tell
