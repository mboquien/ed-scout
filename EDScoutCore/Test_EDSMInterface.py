from . import EDSMInterface


class TestEDSMInterface:

    def test_get_system(self):
        import sys
        print(f"paths: {sys.path}")

        value = EDSMInterface.get_system("Wolf 397")
        print(f"{value}")
        expected_value = {
            'name': 'Wolf 397',
            'coords': {'x': 40, 'y': 79.21875, 'z': -10.40625},
            'coordsLocked': True,
            'primaryStar': {'type': 'K (Yellow-Orange) Star', 'name': 'Wolf 397', 'isScoopable': True}}

        assert expected_value == value

    def test_get_system_estimated_value(self):
        value = EDSMInterface.get_system_estimated_value("Wolf 397")
        # print(f"{value}")
        assert {'id': 2987,
                'id64': 3107576681170,
                'name': 'Wolf 397',
                'url': 'https://www.edsm.net/en/system/bodies/id/2987/name/Wolf+397',
                'estimatedValue': 345657,
                'estimatedValueMapped': 1148021,
                'valuableBodies': [
                    {'bodyId': 3727,
                     'bodyName': 'Rhodius',
                     'distance': 135,
                     'valueMax': 943143}]
                } == value

    # def test_lookup_system(self):
    #     value = lookup_system("Wolf 397")
    #     print(f"{value}")

    def test_get_bodies(self):
        value = EDSMInterface.get_bodies("Wolf 397")
        print(f"test_get_bodies: actual result - {value}")

        assert {'id': 2987, 'id64': 3107576681170, 'name': 'Wolf 397', 'url': 'https://www.edsm.net/en/system/bodies/id/2987/name/Wolf+397', 'bodyCount': 14, 'bodies': [{'id': 8142382, 'id64': 3107576681170, 'bodyId': 0, 'name': 'Wolf 397', 'discovery': {'commander': 'HulkHoga', 'date': '2017-09-29 21:09:22'}, 'type': 'Star', 'subType': 'K (Yellow-Orange) Star', 'parents': None, 'distanceToArrival': 0, 'isMainStar': True, 'isScoopable': True, 'age': 7454, 'spectralClass': 'K4', 'luminosity': 'V', 'absoluteMagnitude': 8.186981, 'solarMasses': 0.664063, 'solarRadius': 0.7596434680086269, 'surfaceTemperature': 4467, 'orbitalPeriod': None, 'semiMajorAxis': None, 'orbitalEccentricity': None, 'orbitalInclination': None, 'argOfPeriapsis': None, 'rotationalPeriod': 3.018796758298611, 'rotationalPeriodTidallyLocked': False, 'axialTilt': 0.088014, 'belts': [{'name': 'Wolf 397 A Belt', 'type': 'Metal Rich', 'mass': 121460000000000, 'innerRadius': 871750, 'outerRadius': 2225300}], 'updateTime': '2020-08-20 04:30:10'}, {'id': 3727, 'id64': 216175889690464978, 'bodyId': 6, 'name': 'Rhodius', 'discovery': {'commander': 'Redfoxxx', 'date': '2017-09-26 22:44:13'}, 'type': 'Planet', 'subType': 'Earth-like world', 'parents': [{'Star': 0}], 'distanceToArrival': 135, 'isLandable': False, 'gravity': 1.0667730682867584, 'earthMasses': 0.967, 'radius': 6072.419, 'surfaceTemperature': 306, 'surfacePressure': 6.035643350604491, 'volcanismType': 'No volcanism', 'atmosphereType': 'Thick Suitable for water-based life', 'atmosphereComposition': {'Nitrogen': 97.34, 'Oxygen': 2.49, 'Water': 0.16}, 'solidComposition': {'Rock': 70, 'Metal': 30, 'Ice': 0}, 'terraformingState': 'Terraformed', 'orbitalPeriod': 62.875246146215275, 'semiMajorAxis': 0.2700002018992775, 'orbitalEccentricity': 0.003673, 'orbitalInclination': 8.615948, 'argOfPeriapsis': 204.609559, 'rotationalPeriod': 62.8774326383449, 'rotationalPeriodTidallyLocked': False, 'axialTilt': 0.213561, 'updateTime': '2020-08-20 05:12:50'}, {'id': 9349, 'id64': 252204686709428946, 'bodyId': 7, 'name': 'Trus Madi', 'discovery': {'commander': 'Redfoxxx', 'date': '2017-09-26 22:44:13'}, 'type': 'Planet', 'subType': 'Metal-rich body', 'parents': [{'Planet': 6}, {'Star': 0}], 'distanceToArrival': 136, 'isLandable': True, 'gravity': 0.37346660467449816, 'earthMasses': 0.036, 'radius': 1980.20375, 'surfaceTemperature': 222, 'surfacePressure': 0, 'volcanismType': 'No volcanism', 'atmosphereType': 'No atmosphere', 'atmosphereComposition': None, 'solidComposition': {'Metal': 60, 'Rock': 40, 'Ice': 0}, 'terraformingState': 'Not terraformable', 'orbitalPeriod': 31.18041764806713, 'semiMajorAxis': 0.0028000019078351095, 'orbitalEccentricity': 0.004801, 'orbitalInclination': 9.497964, 'argOfPeriapsis': 158.041954, 'rotationalPeriod': 31.755517901898152, 'rotationalPeriodTidallyLocked': True, 'axialTilt': -0.325185, 'materials': {'Iron': 25.96, 'Nickel': 19.64, 'Sulphur': 14.06, 'Carbon': 11.83, 'Manganese': 10.72, 'Phosphorus': 7.57, 'Germanium': 4.18, 'Selenium': 2.2, 'Niobium': 1.77, 'Mercury': 1.13, 'Technetium': 0.93}, 'updateTime': '2020-08-20 04:30:10'}, {'id': 8142383, 'id64': 288233483728392914, 'bodyId': 8, 'name': 'Wolf 397 2', 'discovery': {'commander': 'HulkHoga', 'date': '2017-09-29 21:09:22'}, 'type': 'Planet', 'subType': 'High metal content world', 'parents': [{'Star': 0}], 'distanceToArrival': 280, 'isLandable': False, 'gravity': 0.7972893452962133, 'earthMasses': 0.514747, 'radius': 5124.759, 'surfaceTemperature': 175, 'surfacePressure': 304.09693560325684, 'volcanismType': 'No volcanism', 'atmosphereType': 'Thick Argon-rich', 'atmosphereComposition': {'Nitrogen': 99.02, 'Argon': 0.98}, 'solidComposition': {'Rock': 60.11, 'Metal': 31.76, 'Ice': 8.13}, 'terraformingState': None, 'orbitalPeriod': 187.9427788986111, 'semiMajorAxis': 0.5602665742807862, 'orbitalEccentricity': 3e-05, 'orbitalInclination': 0.393011, 'argOfPeriapsis': 273.702759, 'rotationalPeriod': -187.54562151184027, 'rotationalPeriodTidallyLocked': False, 'axialTilt': -2.017095, 'updateTime': '2020-08-20 04:30:10'}, {'id': 8142374, 'id64': 324262280747356882, 'bodyId': 9, 'name': 'Wolf 397 2 a', 'discovery': {'commander': 'HulkHoga', 'date': '2017-09-29 21:09:22'}, 'type': 'Planet', 'subType': 'Rocky Ice world', 'parents': [{'Planet': 8}, {'Star': 0}], 'distanceToArrival': 280, 'isLandable': False, 'gravity': 0.2633059790274136, 'earthMasses': 0.044802, 'radius': 2630.891, 'surfaceTemperature': 564, 'surfacePressure': 1170.1814162348878, 'volcanismType': 'No volcanism', 'atmosphereType': 'Hot thick Carbon dioxide', 'atmosphereComposition': {'Carbon dioxide': 89.51, 'Ammonia': 8.95, 'Sulphur dioxide': 0.9}, 'solidComposition': {'Rock': 63.43, 'Ice': 26.14, 'Metal': 10.43}, 'terraformingState': None, 'orbitalPeriod': 12.721017830902777, 'semiMajorAxis': 0.0012679361784700188, 'orbitalEccentricity': None, 'orbitalInclination': 83.418374, 'argOfPeriapsis': 306.145082, 'rotationalPeriod': 13.263073616956017, 'rotationalPeriodTidallyLocked': False, 'axialTilt': 0.453857, 'updateTime': '2020-08-20 04:30:10'}, {'id': 8142378, 'id64': 360291077766320850, 'bodyId': 10, 'name': 'Wolf 397 3', 'discovery': {'commander': 'HulkHoga', 'date': '2017-09-29 21:09:22'}, 'type': 'Planet', 'subType': 'High metal content world', 'parents': [{'Star': 0}], 'distanceToArrival': 414, 'isLandable': False, 'gravity': 0.7789700930245281, 'earthMasses': 0.495703, 'radius': 5087.857, 'surfaceTemperature': 127, 'surfacePressure': 42.18688378978534, 'volcanismType': 'No volcanism', 'atmosphereType': 'Thick Argon-rich', 'atmosphereComposition': {'Nitrogen': 99.87, 'Argon': 0.13}, 'solidComposition': {'Rock': 60.24, 'Metal': 30.96, 'Ice': 8.81}, 'terraformingState': None, 'orbitalPeriod': 338.53318956163196, 'semiMajorAxis': 0.8294275698827844, 'orbitalEccentricity': 1.8e-05, 'orbitalInclination': 0.12679, 'argOfPeriapsis': 65.058914, 'rotationalPeriod': 2.287353238877315, 'rotationalPeriodTidallyLocked': False, 'axialTilt': -2.96751, 'updateTime': '2020-08-20 04:30:10'}, {'id': 11529, 'id64': 396319874785284818, 'bodyId': 11, 'name': 'Wolf 397 3 a', 'discovery': {'commander': 'Redfoxxx', 'date': '2017-09-26 22:44:13'}, 'type': 'Planet', 'subType': 'Rocky Ice world', 'parents': [{'Planet': 10}, {'Star': 0}], 'distanceToArrival': 413, 'isLandable': True, 'gravity': 0.20785666186973156, 'earthMasses': 0.022822, 'radius': 2113.38875, 'surfaceTemperature': 112, 'surfacePressure': 0, 'volcanismType': 'No volcanism', 'atmosphereType': 'No atmosphere', 'atmosphereComposition': None, 'solidComposition': {'Rock': 63.43, 'Ice': 26.14, 'Metal': 10.43}, 'terraformingState': 'Not terraformable', 'orbitalPeriod': 26.570752401041666, 'semiMajorAxis': 0.0020198967679293978, 'orbitalEccentricity': 0, 'orbitalInclination': -14.939625, 'argOfPeriapsis': 339.488484, 'rotationalPeriod': 27.175517376932874, 'rotationalPeriodTidallyLocked': False, 'axialTilt': -0.392382, 'materials': {'Sulphur': 19.91, 'Iron': 16.99, 'Carbon': 16.74, 'Nickel': 12.85, 'Phosphorus': 10.72, 'Chromium': 7.64, 'Manganese': 7.02, 'Zinc': 4.62, 'Cadmium': 1.32, 'Niobium': 1.16, 'Ruthenium': 1.05}, 'updateTime': '2020-08-20 04:30:10'}, {'id': 8142385, 'id64': 432348671804248786, 'bodyId': 12, 'name': 'Wolf 397 4', 'discovery': {'commander': 'HulkHoga', 'date': '2017-09-29 21:09:22'}, 'type': 'Planet', 'subType': 'Icy body', 'parents': [{'Star': 0}], 'distanceToArrival': 734, 'isLandable': False, 'gravity': 0.934699095893185, 'earthMasses': 2.228786, 'radius': 9848.788, 'surfaceTemperature': 117, 'surfacePressure': 626.9107920059215, 'volcanismType': 'Major Water Geysers', 'atmosphereType': 'Thick Argon-rich', 'atmosphereComposition': {'Nitrogen': 94.5, 'Argon': 5.5}, 'solidComposition': {'Ice': 68.32, 'Rock': 21.15, 'Metal': 10.53}, 'terraformingState': None, 'orbitalPeriod': 799.4040363916666, 'semiMajorAxis': 1.4708053869075557, 'orbitalEccentricity': 0.000214, 'orbitalInclination': -0.004852, 'argOfPeriapsis': 206.781272, 'rotationalPeriod': 0.8125085534953703, 'rotationalPeriodTidallyLocked': False, 'axialTilt': 0.061592, 'updateTime': '2020-08-20 04:30:10'}, {'id': 8142373, 'id64': 468377468823212754, 'bodyId': 13, 'name': 'Wolf 397 5', 'discovery': {'commander': 'HulkHoga', 'date': '2017-09-29 21:09:22'}, 'type': 'Planet', 'subType': 'Icy body', 'parents': [{'Star': 0}], 'distanceToArrival': 978, 'isLandable': False, 'gravity': 0.8468995954576275, 'earthMasses': 1.761551, 'radius': 9198.482, 'surfaceTemperature': 73, 'surfacePressure': 0.12877555977300764, 'volcanismType': 'Major Water Geysers', 'atmosphereType': 'Neon-rich', 'atmosphereComposition': {'Nitrogen': 93.57, 'Neon': 6.42}, 'solidComposition': {'Ice': 68.32, 'Rock': 21.15, 'Metal': 10.53}, 'terraformingState': None, 'orbitalPeriod': 1227.287230668287, 'semiMajorAxis': 1.9573798492397256, 'orbitalEccentricity': 0.005824, 'orbitalInclination': 0.002705, 'argOfPeriapsis': 261.284034, 'rotationalPeriod': 1.5961892744907407, 'rotationalPeriodTidallyLocked': False, 'axialTilt': -0.375748, 'updateTime': '2020-08-20 04:30:10'}, {'id': 8142376, 'id64': 504406265842176722, 'bodyId': 14, 'name': 'Wolf 397 6', 'discovery': {'commander': 'HulkHoga', 'date': '2017-09-29 21:09:22'}, 'type': 'Planet', 'subType': 'Icy body', 'parents': [{'Star': 0}], 'distanceToArrival': 1402, 'isLandable': False, 'gravity': 0.900429282297381, 'earthMasses': 2.023969, 'radius': 9562.284, 'surfaceTemperature': 61, 'surfacePressure': 0.3797578182876881, 'volcanismType': 'Major Water Geysers', 'atmosphereType': 'Neon-rich', 'atmosphereComposition': {'Helium': 97.56, 'Neon': 2.44}, 'solidComposition': {'Ice': 67.82, 'Rock': 21.44, 'Metal': 10.74}, 'terraformingState': None, 'orbitalPeriod': 2109.899013130787, 'semiMajorAxis': 2.809002098242432, 'orbitalEccentricity': 0.000553, 'orbitalInclination': -0.074866, 'argOfPeriapsis': 2.420435, 'rotationalPeriod': 1.3544995283564816, 'rotationalPeriodTidallyLocked': False, 'axialTilt': -2.204139, 'updateTime': '2020-08-20 04:30:10'}, {'id': 8142375, 'id64': 540435062861140690, 'bodyId': 15, 'name': 'Wolf 397 6 a', 'discovery': {'commander': 'HulkHoga', 'date': '2017-09-29 21:09:22'}, 'type': 'Planet', 'subType': 'Icy body', 'parents': [{'Planet': 14}, {'Star': 0}], 'distanceToArrival': 1405, 'isLandable': False, 'gravity': 0.18015751664949903, 'earthMasses': 0.039589, 'radius': 2989.82375, 'surfaceTemperature': 61, 'surfacePressure': 0.00788205146804836, 'volcanismType': 'No volcanism', 'atmosphereType': 'Thin Argon', 'atmosphereComposition': {'Argon': 100}, 'solidComposition': {'Ice': 87.76, 'Rock': 10.51, 'Metal': 1.73}, 'terraformingState': None, 'orbitalPeriod': 174.88319426775465, 'semiMajorAxis': 0.011241933083365739, 'orbitalEccentricity': None, 'orbitalInclination': -52.734245, 'argOfPeriapsis': 133.555709, 'rotationalPeriod': 176.58528011342594, 'rotationalPeriodTidallyLocked': True, 'axialTilt': 0.204942, 'updateTime': '2020-08-20 04:30:10'}, {'id': 8142377, 'id64': 612492656899068626, 'bodyId': 17, 'name': 'Wolf 397 7', 'discovery': {'commander': 'HulkHoga', 'date': '2017-09-29 21:09:22'}, 'type': 'Planet', 'subType': 'Icy body', 'parents': [{'Null': 16}, {'Star': 0}], 'distanceToArrival': 1993, 'isLandable': False, 'gravity': 0.7675887227517685, 'earthMasses': 1.384781, 'radius': 8566.645, 'surfaceTemperature': 51, 'surfacePressure': 0.2775290294201826, 'volcanismType': 'Water Geysers', 'atmosphereType': 'Neon-rich', 'atmosphereComposition': {'Helium': 97.56, 'Neon': 2.44}, 'solidComposition': {'Ice': 68.2, 'Rock': 21.23, 'Metal': 10.57}, 'terraformingState': None, 'orbitalPeriod': 214.70704426368056, 'semiMajorAxis': 0.005934903892954675, 'orbitalEccentricity': 0.141532, 'orbitalInclination': -3.438596, 'argOfPeriapsis': 83.337775, 'rotationalPeriod': 325.6039554864005, 'rotationalPeriodTidallyLocked': False, 'axialTilt': 0.032578, 'updateTime': '2020-08-20 04:30:10'}, {'id': 8142372, 'id64': 648521453918032594, 'bodyId': 18, 'name': 'Wolf 397 8', 'discovery': {'commander': 'HulkHoga', 'date': '2017-09-29 21:09:22'}, 'type': 'Planet', 'subType': 'Icy body', 'parents': [{'Null': 16}, {'Star': 0}], 'distanceToArrival': 1994, 'isLandable': False, 'gravity': 0.6903970327766323, 'earthMasses': 1.065396, 'radius': 7923.017, 'surfaceTemperature': 51, 'surfacePressure': 0.22451683167036762, 'volcanismType': 'Minor Carbon Dioxide Geysers', 'atmosphereType': 'Neon-rich', 'atmosphereComposition': {'Helium': 97.56, 'Neon': 2.44}, 'solidComposition': {'Ice': 68.2, 'Rock': 21.23, 'Metal': 10.57}, 'terraformingState': None, 'orbitalPeriod': 214.70704426368056, 'semiMajorAxis': 0.0077140767846697695, 'orbitalEccentricity': 0.141532, 'orbitalInclination': -3.438596, 'argOfPeriapsis': 263.337769, 'rotationalPeriod': 285.59758701434026, 'rotationalPeriodTidallyLocked': True, 'axialTilt': -0.149227, 'updateTime': '2020-08-20 04:30:10'}, {'id': 8142384, 'id64': 684550250936996562, 'bodyId': 19, 'name': 'Wolf 397 9', 'discovery': {'commander': 'HulkHoga', 'date': '2017-09-29 21:09:22'}, 'type': 'Planet', 'subType': 'Icy body', 'parents': [{'Star': 0}], 'distanceToArrival': 2694, 'isLandable': False, 'gravity': 1.2692748122149822, 'earthMasses': 4.481866, 'radius': 11984.947, 'surfaceTemperature': 45, 'surfacePressure': 0.8287042777004688, 'volcanismType': 'Major Water Geysers', 'atmosphereType': 'Helium', 'atmosphereComposition': {'Helium': 89.33, 'Hydrogen': 8.43, 'Neon': 2.24}, 'solidComposition': {'Ice': 68.2, 'Rock': 21.23, 'Metal': 10.57}, 'terraformingState': None, 'orbitalPeriod': 5583.305325773033, 'semiMajorAxis': 5.374093418548838, 'orbitalEccentricity': 0.007449, 'orbitalInclination': 0.41204, 'argOfPeriapsis': 55.296416, 'rotationalPeriod': 1.9259499189467595, 'rotationalPeriodTidallyLocked': False, 'axialTilt': -0.027903, 'updateTime': '2020-08-20 04:30:10'}]} == value
