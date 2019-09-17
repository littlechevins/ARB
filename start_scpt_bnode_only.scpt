tell application "iTerm2"
  tell current window
    set newTab0 to (create tab with default profile)
    tell current session of newTab0
      write text "echo exporting flask app"
      write text "python node.py -n node_1 -ip 5001 -t backbone"
    end tell
    set newTab1 to (create tab with default profile)
    tell current session of newTab1
      write text "echo exporting flask app"
      write text "python node.py -n node_2 -ip 5002 -t backbone"
    end tell
    set newTab2 to (create tab with default profile)
    tell current session of newTab2
      write text "echo exporting flask app"
      write text "python node.py -n node_3 -ip 5003 -t backbone"
    end tell
    set newTab3 to (create tab with default profile)
    tell current session of newTab3
      write text "echo exporting flask app"
      write text "python node.py -n node_4 -ip 5004 -t backbone"
    end tell
    set newTab4 to (create tab with default profile)
    tell current session of newTab4
      write text "echo exporting flask app"
      write text "python node.py -n node_5 -ip 5005 -t end"
    end tell
    set newTab11 to (create tab with default profile)
    tell current session of newTab11
      write text "echo exporting flask app"
      write text "python node.py -n node_11 -ip 5011 -t end"
    end tell
  end tell
end tell
