
import inspect


def opendata():
    module = _whoami()
    day = int(module.split('day')[-1].split('.py')[0])
    datafile = f"./day{day}_input.txt"
    exampledatafile = f"./day{day}_exampleinput.txt"
    return open(exampledatafile, 'r'), open(datafile, 'r')

def _whoami():
    '''Return the module name of where the call came from.'''

    # This will return a list of frame records, [1] is the frame
    # record of the caller.
    frame_records = inspect.stack()[3]

    # Index 1 of frame_records is the full path of the module,
    # we can then use inspect.getmodulename() to get the
    # module name from this path.
    calling_module = inspect.getmodulename(frame_records[1])

    return calling_module