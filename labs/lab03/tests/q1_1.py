test = {   'name': 'q1_1',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> parks_with_species.shape[0] == 7\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> parks_with_species.shape[1] == 7\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.all(np.sort(parks_with_species.get('count')) == np.sort(np.array([1885, 2294, 1797, 1416, 6310, 1995, 2088])))\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}