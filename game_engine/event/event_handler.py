class EventHandler(object):
    def __init__(self):
        self._subscriptions = []

    def subscribe(self, event_type, callback):
        subscription = self.__get_subscription(event_type)
        if subscription:
            subscription.add_callback(callback)
        else:
            subscription = _EventSubscription(event_type, callback)
            self._subscriptions.append(subscription)

    def event(self, event):
        for subscription in self._subscriptions:
            if subscription.event_type == type(event):
                self.__execute_event_callbacks(subscription, event)
                return True
        return False

    def __execute_event_callbacks(self, subscription, event):
        for callback in subscription.callbacks:
            callback(event)

    def __get_subscription(self, event_type):
        try:
            return list(filter(lambda subscription: event_type == subscription.event_type, self._subscriptions))[0]
        except IndexError:
            return None


class _EventSubscription(object):
    def __init__(self, event_type, callback):
        self.__event_type = event_type
        self.__callbacks = [callback]

    @property
    def event_type(self):
        return self.__event_type

    def add_callback(self, callback):
        if callback not in self.__callbacks:
            self.__callbacks.append(callback)

    @property
    def callbacks(self):
        return self.__callbacks




