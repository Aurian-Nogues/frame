import iw_parse

class WifiUtilities:
    
    def scan_ssids(self, dBm_limit = -70):
        """
            This will return a list of SSID ordered by signal strenghth

            Args:
                dBm_limit: None will return all SSIDs
                        if passing an integer, this is the DB limit that will be used to filter returned networks
                        -30 dBm: amazong
                        -67 dBm: very good (voip, streaming, video)
                        -70 dBm: minimum acceptable for reliable packet delivery (email / web)
                        -80 dBm: unreliable packet delivery
                        -90 dBm: unusable, any functionality is highly unlikely

        """

        my_networks = dict()

        #get all networks
        networks = iw_parse.get_interfaces(interface='wlan0')
        if len(networks) == 0:
            return list()
        # only keep networks above required noise threshold
        for network in networks:
            if dBm_limit is not None:
                if int(network['Signal Level']) > dBm_limit:
                    my_networks[network['Name']] = int(network['Signal Level'])
        # sort results
        sorted_networks_tuples = sorted(my_networks.items(), key=lambda x: x[1])
        networks_list = list()
        for entry in sorted_networks_tuples:
            networks_list.append(entry[0])
        return networks_list
