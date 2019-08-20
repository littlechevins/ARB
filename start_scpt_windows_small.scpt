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
    set newTab5 to (create tab with default profile)
    tell current session of newTab5
      write text "echo exporting flask app"
      write text "python node.py -n node_6 -ip 5006 -t end"
    end tell
    set newTab6 to (create tab with default profile)
    tell current session of newTab6
      write text "echo exporting flask app"
      write text "python node.py -n node_7 -ip 5007 -t end"
    end tell
    set newTab7 to (create tab with default profile)
    tell current session of newTab7
      write text "echo exporting flask app"
      write text "python node.py -n node_8 -ip 5008 -t end"
    end tell
    set newTab8 to (create tab with default profile)
    tell current session of newTab8
      write text "echo exporting flask app"
      write text "python node.py -n node_9 -ip 5009 -t end"
    end tell
  end tell
end tell
