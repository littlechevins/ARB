#!/usr/bin/env python

from argparse import ArgumentParser

# from node import app
import node

if __name__ == '__main__':
  # parser = ArgumentParser(
  #   description='A simple distributed hash table')
  # parser.add_argument('-n', '--name', action='store', required=True,
  #                     help='name of node')
  # parser.add_argument('-k', '--host', action='store', default='localhost',
  #                     help='hostname to bind to')
  # parser.add_argument('-p', '--port', action='store', type=int,
  #                     required=True, help='port to bind to')
  #
  # args = parser.parse_args()
  #
  # app.run(host=args.host, port=args.port)

  n1 = node.Node()
  print(n1.ping())
  app = n1
  app.run()


# tell application "iTerm2"
#     set newWindow to (create window with default profile)
#     tell current session of newWindow
#         write text "echo it works!"
#     end tell
# end tell
