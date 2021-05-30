
import py_dss_interface
import numpy as np
import matplotlib.pyplot as plt
import functions

dss = py_dss_interface.DSSDLL()

dss_file = r"D:\Users\Rodolfo\Documentos\.code\OpenDSS\Minicurso_py_dss\8500-Node\Master-unbal.dss"

dss.text("compile [{}]".format(dss_file))

dss.text("New Energymeter.m1 Line.ln5815900-1 1")
dss.text("New Monitor.m1 Line.ln5815900-1 1 mode=1 ppolar=no")
dss.text("Set Maxiterations=100")
dss.text("Set MaxControliter=100")


dss.text("Batchedit Load..* daily=default")

bus = "M1047339"
dss.circuit_setactivebus(bus)
vbase = dss.bus_kVbase()

functions.define_3ph_pvsystem_with_transformer(dss, bus, vbase, 3300, 3000)

dss.text("set number=24")
dss.text("set stepsize=1h")
dss.text("set mode=daily")
dss.text("solve")

if dss.solution_read_converged():

    # Q3 - 1
    dss.monitors_write_name("m1")
    pa_feederhead = dss.monitors_channel(1)
    qa_feederhead = dss.monitors_channel(2)
    pb_feederhead = dss.monitors_channel(3)
    qb_feederhead = dss.monitors_channel(4)
    pc_feederhead = dss.monitors_channel(5)
    qc_feederhead = dss.monitors_channel(6)

    pt = np.array(pa_feederhead) + np.array(pb_feederhead) + \
        np.array(pc_feederhead)
    qt = np.array(qa_feederhead) + np.array(qb_feederhead) + \
        np.array(qc_feederhead)

    # Q3 - 2
    plt.plot(range(1, len(pt) + 1), pt, "g", label="P")
    plt.plot(range(1, len(pt) + 1), qt, "b", label="Q")
    plt.title("Daily Active and Reactive Power at Feeder Head")
    plt.legend()
    plt.ylabel("kW, kvar")
    plt.xlabel("Hour")
    plt.xlim(1, 24)
    plt.grid(True)
    plt.show()

else:
    print("OpenDSS with status: NOT Solved")



print("here")
