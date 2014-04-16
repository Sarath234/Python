def worker(input_q):
    while True:
        item=input_q.get()
        print item
        input_q.task_done()

def master(sequence,output_q):
    for item in sequence:
        output_q.put(item)

if __name__== "__main__":
    from multiprocessing import Process, JoinableQueue
    q=JoinableQueue()
    con_p=Process(target=worker,args=(q,))
    con_p.daemon=True
    con_p.start()
    sequence=range(100)
    master(sequence,q)
    q.join()
