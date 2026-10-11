# This is the main file, program execution happens here (run with Windows + F5)

import recycle_bin_actions as rb
import time

check_frequency = 5 # In seconds, how long the program waits before checking the recycle bin again

while True:
    item_count = rb.get_item_count_in_recycle_bin()

    if item_count > 0:
        rb.empty_recycle_bin()
        rb.notify_recycle_bin_emptied(item_count)

    time.sleep(check_frequency)