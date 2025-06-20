#SOLUTION

class Job:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Job(start={self.start}, end={self.end})"

def sortByEnd(jobs):
    return sorted(jobs, key=lambda job: job.end)

def internalSchedulingFinishTime(jobs):
    sortByEnd(jobs)
    endRef = 0
    result = []
    for job in jobs:
        if job.start >= endRef:
            result.append(job)
            endRef = job.end

    return result

# Esempio di utilizzo
if __name__ == "__main__":
    # Creazione di alcuni jobs
    jobs = [
        Job(1, 4),
        Job(2, 6),
        Job(5, 7),
        Job(8, 9),
        Job(3, 5)
    ]

    print(internalSchedulingFinishTime(jobs))

