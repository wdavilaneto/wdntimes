import requests
import gitlab

requests.packages.urllib3.disable_warnings()
URL = 'https://gitlab.mprj.mp.br'

gl = gitlab.Gitlab(URL, private_token='GyxKCZbYBpRXze55RyAz', ssl_verify=False, per_page=100)
projects = gl.projects.list(starred=True)
for p in projects:
    print(p)

# print(gl.projects.list(name='mprj-consup'))

extrajudicial = gl.projects.get(115)
print(extrajudicial)

# extrajudicial.issues()
# boards = extrajudicial.boards.list()
# for b in boards:R
#     for board in b.lists.list():
#         print(board)
#
# events = extrajudicial.events.list()
# actions = {}
# for event in events:
#     if event.action_name not in actions:
#         actions[event.action_name] = 1
#         print (event.action_name)
#         if event.action_name == 'commented on':
#             print (event)
#
#
# for milestone in extrajudicial.milestones.list():
#     print(milestone)

# epics = extrajudicial.epics.list()
# for epic in epics:
#     print(epic)


# users = gl.users.list()
# for user in users:
#     print(user)
