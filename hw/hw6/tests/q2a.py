test = {   'name': 'q2a',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> not training_data['TotalBathrooms'].isnull().any() # Check that missing values are dealt with\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> training_data['TotalBathrooms'].sum() == 4421.5 # Check that the values are as expected\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> training_data.loc[training_data['PID'] == 903230120, 'TotalBathrooms'].iloc[0] == 1.0\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> sum(training_data.loc[:, 'TotalBathrooms'] < 2.5) == 1124\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}