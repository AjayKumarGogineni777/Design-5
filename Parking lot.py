# Time Complexity : O(1) for park and get_next_available, O(log(n)) for unpark and add_parking_spot
# Space Complexity : O(n) to maintain the heap of all available spots

# Code ran on LeetCode
# Miantain a min heap to get the next available spot and keep updating it if a sopt is used or a new spot is available.

import heapq

class ParkingSpot:

    def __init__(self, floor, spot):
        self.floor = floor
        self.spot = spot

    def __lt__(self, other):
        if self.floor == other.floor:
            return self.spot < other.spot
        return self.floor < other.floor

    def __str__(self):
        return 'Parked at Floor: {}, Spot: {}'.format(self.floor, self.spot)

class ParkingLot:
    def __init__(self, max_floors, spots_per_floor):

        self.max_floors = max_floors
        self.spots_per_floor = spots_per_floor
        self.available_spots = []

    def _is_full(self):
        return len(self.available_spots) == 0

    def park(self):                                     
        if self._is_full():
            raise Exception('Parking Lot is full')
        return heapq.heappop(self.available_spots)

    def get_next_available(self):
        if self._is_full():
            raise Exception('Parking Lot is full')
        return self.available_spots[0]

    def unpark(self, floor, spot):                      
        self._add_vacant_spot(floor, spot)

    def add_parking_spot(self, floor, spot):
        if floor > self.max_floors or spot > self.spots_per_floor:
            raise Exception('Input is out of allowed range')
        self._add_vacant_spot(floor, spot)

    def _add_vacant_spot(self, floor, spot):
        parking_spot = ParkingSpot(floor, spot)
        heapq.heappush(self.available_spots, parking_spot)

def main():
    pl = ParkingLot(10, 20)
    pl.add_parking_spot(1, 1)
    pl.add_parking_spot(2, 1)
    pl.add_parking_spot(3, 1)
    pl.add_parking_spot(1, 2)
    pl.add_parking_spot(2, 2)
    pl.add_parking_spot(3, 2)
    print(pl.get_next_available())
    pl.park()
    print(pl.get_next_available())
    pl.unpark(1, 1)
    print(pl.get_next_available())
main()