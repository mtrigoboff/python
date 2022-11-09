"""
Thanks to Spring 2020 student Lauren Edwardsen for pointing out
that the code could be improved by eliminating global variables.
"""

import numpy as np                                  # for Poisson generator
import matplotlib.pyplot as plot                    # for graph display
import statistics as stats                          # for mean() function

class Customer:
    def __init__(self):
        self.wait_time = 0

class Station:                                      # e.g. a cash register station
    def __init__(self):
        self.busy = False
        self.mins_to_go = 0

    def use(self, service_time):                    # occupy a station with a customer
        self.busy = True
        self.mins_to_go = service_time

customer_Interval_RNG = np.random.default_rng()     # random number generator for customer interval
station_service_time_RNG = np.random.default_rng()  # random number generator for station service time

def get_free_station(stations):
    for station in stations:                        # check for free station
        if not station.busy:
            return station                          # found a free station
    return None                                     # no free stations

def run(n_stations, avg_stat_mins, cust_per_hour, run_days):

    # data collection lists
    queue_lgths = []                                # length of queue for each minute
    free_stations = []                              # number of free stations for each minute
    customer_intervals = []                         # times between customers
    service_times = []                              # service time for each customer
    wait_times = []                                 # wait time for each customer

    # list of Station instances of length nStation
    stations = [Station() for _ in range(n_stations)]

    avg_customer_interval = 60 / cust_per_hour      # average minutes till next customer arrives

    queue = []

    customer_interval = customer_Interval_RNG.poisson(avg_customer_interval)
    customer_intervals.append(customer_interval)

    run_minutes = run_days * 24 * 60
    for minute in range(run_minutes):

        # record current number of free stations
        free_stations.append([station.busy for station in stations].count(False))

        queue_lgths.append(len(queue))

        for customer in queue:
            customer.wait_time += 1                 # add 1 minute to wait time

        for station in stations:                    # free station when time is up
            if station.busy:
                if station.mins_to_go == 0:
                    station.busy = False            # station becomes free
                else:
                    station.mins_to_go -= 1         # decrement time for busy station

        while len(queue) != 0:                      # there are customer(s) waiting
            free_station = get_free_station(stations)
            if free_station is not None:            # at least one station not busy
                customer = queue.pop(0)             # first customer comes off queue
                wait_times.append(customer.wait_time)
                svc_time = station_service_time_RNG.poisson(avg_stat_mins)
                service_times.append(svc_time)
                if svc_time != 0:                   # only if non-zero service time ...
                    free_station.use(svc_time)      # ... do we need to use a station
            else:
                break

        if customer_interval == 0:                  # it's time for next customer
            free_station = get_free_station(stations)
            if free_station is not None:
                wait_times.append(0)                # customer was served immediately
                svc_time = station_service_time_RNG.poisson(avg_stat_mins)
                service_times.append(svc_time)
                if svc_time != 0:                   # only if non-zero service time ...
                    free_station.use(svc_time)      # ... do we need to use a station
            else:                                   # all stations busy
                queue.append(Customer())            # place customer on queue
            customer_interval = customer_Interval_RNG.poisson(avg_customer_interval)
            customer_intervals.append(customer_interval)
        else:
            customer_interval -= 1                  # "waiting" for next customer

    return [['queue lengths',       queue_lgths],
            ['free stations',       free_stations],
            ['customer intervals',  customer_intervals],
            ['service times',       service_times],
            ['wait_times',          wait_times]]

def printData(data_lists):
    print(f"{'name':22}{'lgth':>8} {'avg':>7}    first ten items")
    for data_item in data_lists:
        data_name, data_list = data_item
        data_name_str = f'{data_name}:'
        print(f'{data_name_str:22}{len(data_list):8,} {stats.mean(data_list):7.1f}    {data_list[:10]}')

def displayData(queue_lgths, free_stations, customer_intervals, service_times, wait_times):
    title = 'McBurgers Simulation'

    fig, axes = plot.subplots(nrows=2, ncols=3, num=None, figsize=(8, 6))
    fig.canvas.manager.set_window_title(title)
    faxes = axes.flatten()

    faxes[0].hist(queue_lgths, bins='doane', color='red')
    faxes[0].set_title('Queue Lengths')

    faxes[1].hist(free_stations, bins='doane', color='lightgreen')
    faxes[1].set_title('Free Stations')

    faxes[2].hist(customer_intervals, bins='doane', color='blue')
    faxes[2].set_title('Customer Intervals')

    faxes[3].hist(service_times, bins='doane', color='purple')
    faxes[3].set_title('Service Times')

    faxes[4].hist(wait_times, bins='doane', color='orange')
    faxes[4].set_title('Wait Times')

    fig.delaxes(faxes[5])

    plot.suptitle(title)
    plot.tight_layout(h_pad=2, w_pad=2, rect=(0, 0, 1, 0.95))
    plot.show()

# these values produce good graphs
# run(n_stations=4, avg_stat_mins=10, cust_per_hour=30, run_days=30)

run_data = run(n_stations=4, avg_stat_mins=10, cust_per_hour=30, run_days=30)
printData(run_data)
displayData(*[item[1] for item in run_data])