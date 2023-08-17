from ibmcloud_sdk_core import get_authenticator_from_environment
from ibm_platform_services import ActivityTrackerV1

class ActivityTracker:
    def __init__(self, instance_id, event_type):
        authenticator = get_authenticator_from_environment('ibm')
        self.activity_tracker = ActivityTrackerV1(authenticator=authenticator)
        self.instance_id = instance_id
        self.event_type = event_type

    def track_activity(self, resource_id, details):
        try:
            response = self.activity_tracker.create_event_instance(
                instance_id=self.instance_id,
                event_type_id=self.event_type,
                resource_id=resource_id,
                details=details
            )
            return response
        except ApiException as e:
            print("Error tracking activity: {}".format(e))

