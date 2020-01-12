# python3

import heapq


class Worker:
    

    def __init__(self, idn, free_t=0):
        self.idn = idn
        self.free_t = free_t

    def __lt__(self, other):
        if self.free_t == other.free_t:
            return self.idn < other.idn
        return self.free_t < other.free_t

    def __gt__(self, other):
        if self.free_t == other.free_t:
            return self.idn > other.idn
        return self.free_t > other.free_t


def assign_jobs(n_workers, jobs):
    worker_queue = [Worker(i) for i in range(n_workers)]
    result = []
    for job in jobs:
        worker = heapq.heappop(worker_queue)
        result.append((worker.idn, worker.free_t))
        worker.free_t += job
        heapq.heappush(worker_queue, worker)
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job[0], job[1])


if __name__ == "__main__":
    main()
