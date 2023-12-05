# from collections

class Almanac:
    def __init__(self, data: str):
        self.seeds = list()
        self.seedtosoil = dict()
        self.soiltofertilizer = dict()
        self.fertilizertowater = dict()
        self.watertolight = dict()
        self.lighttotemperature = dict()
        self.temperaturetohumidity = dict()
        self.humiditytolocation = dict()

        seeds_str, seed_soil_str, soil_fert_str, fert_water_str, water_light_str, light_temp_str, temp_hum_str, hum_loc_str \
            = data.split('\n\n')

        self.seeds = sorted(list(map(int, seeds_str.split(':')[1].split())))

        for string, mapping in zip((seed_soil_str, soil_fert_str, fert_water_str, water_light_str, light_temp_str,
                                    temp_hum_str, hum_loc_str),
                                   (self.seedtosoil, self.soiltofertilizer, self.fertilizertowater, self.watertolight,
                                    self.lighttotemperature, self.temperaturetohumidity, self.humiditytolocation)):
            for line in string.splitlines()[1:]:
                dest, source, length = map(int, line.split())
                mapping[source] = (length, dest)

    def analyze_lowest_location(self) -> int:
        minresult = 1E99
        for seed in self.seeds:
            result = seed
            for mapping in (self.seedtosoil, self.soiltofertilizer, self.fertilizertowater, self.watertolight,
                            self.lighttotemperature, self.temperaturetohumidity, self.humiditytolocation):
                closest_key = Almanac.find_largest_in_list_less_than_num(result, list(mapping.keys()))
                if closest_key is not None and result < closest_key + mapping[closest_key][0]:
                    result = result - closest_key + mapping[closest_key][1]
                else:
                    continue

            minresult = min(result, minresult)
        return minresult

    @staticmethod
    def find_largest_in_list_less_than_num(num, list_of_ints) -> int:
        largest = None
        for i in sorted(list_of_ints):
            if i > num:
                return largest
            else:
                largest = i
        return largest


def part_1(data: str):
    return Almanac(data).analyze_lowest_location()


def part_2(data: str):
    pass


if __name__ == '__main__':
    print(part_1(open('data.txt').read()))
    print(part_2(open('data.txt').read()))
