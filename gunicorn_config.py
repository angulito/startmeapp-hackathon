def child_exit(server, worker):
    multiprocess.mark_process_dead(worker.pid)


bind = "0.0.0.0:5000"
workers = 2
timeout = 120