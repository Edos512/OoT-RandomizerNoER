class Entrance(object):

    def __init__(self, name='', parent=None):
        self.name = name
        self.parent_region = parent
        self.connected_region = None
        self.target = None
        self.addresses = None
        self.spot_type = 'Entrance'
        self.recursion_count = { 'child': 0, 'adult': 0 }
        self.vanilla = None
        self.access_rule = lambda state: True


    def copy(self, new_region):
        new_entrace = Entrance(self.name, new_region)

        new_entrace.connected_region = self.connected_region.name
        new_entrace.addresses = self.addresses
        new_entrace.spot_type = self.spot_type
        new_entrace.vanilla = self.vanilla
        new_entrace.access_rule = self.access_rule

        return new_entrace


    def can_reach(self, state, age='either'):
        if age == 'either':
            return state.can_reach(self, age='adult') or \
                    state.can_reach(self, age='child')

        elif age == 'child' or age == 'adult':
            return state.as_age(self.access_rule, age=age, spot=self) and \
                    state.can_reach(self.parent_region, age=age)


    def connect(self, region, addresses=None, target=None, vanilla=None):
        self.connected_region = region
        self.target = target
        self.addresses = addresses
        self.vanilla = vanilla
        region.entrances.append(self)


    def __str__(self):
        return str(self.__unicode__())


    def __unicode__(self):
        return '%s' % self.name

