tell application "iTerm2"
  tell current window
    set newTab1 to (create tab with default profile)
    tell current session of newTab1
      write text "echo exporting flask app"
      write text "python node.py -n 1 -ip 6001 -t end"
    end tell
    set newTab2 to (create tab with default profile)
    tell current session of newTab2
      write text "echo exporting flask app"
      write text "python node.py -n 2 -ip 6002 -t end"
    end tell
    set newTab3 to (create tab with default profile)
    tell current session of newTab3
      write text "echo exporting flask app"
      write text "python node.py -n 3 -ip 6003 -t end"
    end tell
    set newTab4 to (create tab with default profile)
    tell current session of newTab4
      write text "echo exporting flask app"
      write text "python node.py -n 4 -ip 6004 -t end"
    end tell
    set newTab5 to (create tab with default profile)
    tell current session of newTab5
      write text "echo exporting flask app"
      write text "python node.py -n 5 -ip 6005 -t end"
    end tell
    set newTab6 to (create tab with default profile)
    tell current session of newTab6
      write text "echo exporting flask app"
      write text "python node.py -n 6 -ip 6006 -t end"
    end tell
    set newTab7 to (create tab with default profile)
    tell current session of newTab7
      write text "echo exporting flask app"
      write text "python node.py -n 7 -ip 6007 -t end"
    end tell
    set newTab8 to (create tab with default profile)
    tell current session of newTab8
      write text "echo exporting flask app"
      write text "python node.py -n 8 -ip 6008 -t end"
    end tell
    set newTab9 to (create tab with default profile)
    tell current session of newTab9
      write text "echo exporting flask app"
      write text "python node.py -n 9 -ip 6009 -t end"
    end tell
    set newTab10 to (create tab with default profile)
    tell current session of newTab10
      write text "echo exporting flask app"
      write text "python node.py -n 10 -ip 6010 -t end"
    end tell
    set newTab11 to (create tab with default profile)
    tell current session of newTab11
      write text "echo exporting flask app"
      write text "python node.py -n 11 -ip 6011 -t end"
    end tell
    set newTab12 to (create tab with default profile)
    tell current session of newTab12
      write text "echo exporting flask app"
      write text "python node.py -n 12 -ip 6012 -t end"
    end tell
    set newTab13 to (create tab with default profile)
    tell current session of newTab13
      write text "echo exporting flask app"
      write text "python node.py -n 13 -ip 6013 -t end"
    end tell
    set newTab14 to (create tab with default profile)
    tell current session of newTab14
      write text "echo exporting flask app"
      write text "python node.py -n 14 -ip 6014 -t end"
    end tell
    set newTab15 to (create tab with default profile)
    tell current session of newTab15
      write text "echo exporting flask app"
      write text "python node.py -n 15 -ip 6015 -t end"
    end tell
    set newTab16 to (create tab with default profile)
    tell current session of newTab16
      write text "echo exporting flask app"
      write text "python node.py -n 16 -ip 6016 -t end"
    end tell
  end tell
end tell
