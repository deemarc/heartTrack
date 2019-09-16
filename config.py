import json

class Config(object):
    '''
        General application config details
    '''
    def __init__(self):
        # self.environmentfile = '/data/apps/cs_sched/etc/environment.json'
        self.environmentfile = './environment.json'

        # Read the environment config in.  IF the config read fails, we should die with a traceback.  App can't start.
        with open(self.environmentfile) as data_file:
            self.environment = json.load(data_file)


        # Process the config to ensure proper data is available.  App can't start with bad config.
        # for key in ['connections']:
        #     if key not in self.environment:
        #         err = cs_sched.apierror.ApiError(500, 500, "Bad config format.  Missing '%s'" % (key)) 
        #         raise err

        # for connection in self.environment['connections']:
        #     if 'name' not in connection:
        #         err = cs_sched.apierror.ApiError(500, 500, "Bad config format.  One or more connections missing a name.")
        #         raise err
        #     if 'connection' not in connection:
        #         err = cs_sched.apierror.ApiError(500, 500, "Bad config format.  One or more connections missing a connection string.")
        #         raise err
                