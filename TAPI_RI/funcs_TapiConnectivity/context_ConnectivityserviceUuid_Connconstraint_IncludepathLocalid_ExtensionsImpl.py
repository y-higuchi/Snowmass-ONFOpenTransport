import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_ConnectivityserviceUuid_Connconstraint_IncludepathLocalid_ExtensionsImpl:

    @classmethod
    def get(cls, uuid, localId):
        print 'handling get'
        if uuid in be.Context._connectivityService:
            if localId in be.Context._connectivityService[uuid]._connConstraint._includePath:
                return be.Context._connectivityService[uuid]._connConstraint._includePath[localId]._extensions
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')
