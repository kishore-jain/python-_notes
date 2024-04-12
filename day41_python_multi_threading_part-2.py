Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# TCB - Thread control block
# --------------------------

# TID - Thread identifier(name to be given to each pgm instructions)
# PID - Process identifier (regulation scheme and area where all threads are present)
# TRS - Thread Register Set(common log book of threading process)
# TPC - Thread Program counter(overall details about thread counts)
# TSP - Thread Stack pointer (tokenising threads/priotize threads)
# TIP - Thread instrcution pointer
# P2cP - Parent process control pointer (overall monitor)


# Realtime applications
# ---------------------
# social media
# upi- payment gateway interface
# share market / online trading services
# digital broking / digital marketing
# RAM boosters / Grammarly /gmaps
# Google Earth services / realtime tracking

#Threading life cycle
# -------------------

# New / init
# Runnable
# Running
# Blocked
# Waiting
# Terminated

# new/init
# --------

# creates thread name and thread object gives memory allocation to threads


# Runnable
# --------

>>> # Memory alloted threads are scheduled for execution and eligible to run but in concurrent fashion
>>> 
>>> # Running
>>> # -------
>>> 
>>> # started too execute the code (start() , run() )
>>> # started to utilise the shared memory
>>> 
>>> 
>>> # Blocked
>>> # -------
>>> 
>>> # even though thread is already in running state , but if it will wait for a resource that is being  used by another thread has to be released soon
>>> 
>>> 
>>> # Waiting
>>> # -------
>>> 
>>> # a thread is already completed its execution but it with wait in the queue so that the remaining    threads might notify it.
>>> 
>>> #
>>> 
>>> # Terminated
>>> # ----------
>>> 
>>> # Deque process of completed thread to be happen after completion of process execution
