import numpy as np
import py_dss_interface
import matplotlib.pyplot as plt

dss_file = r"D:\Users\Rodolfo\Documentos\.code\OpenDSS\Minicurso_py_dss\8500-Node\Master-unbal.dss"

dss = py_dss_interface.DSSDLL()

dss.text("compile {}".format(dss_file))

dss.text("New Energymeter.m1 Line.ln5815900-1 1")
dss.text("New Monitor.m1 Line.ln5815900-1 terminal=1 mode=1 ppolar=False")
dss.text("Set Maxiterations=20")
dss.text("Set Maxcontrolit=100")

# Q2.1
dss.text("Batchedit Load..* daily=default")

dss.text("set mode=daily")
dss.text("set number=24")
dss.text("set stepsize=1h")
dss.text("solve")

# Q2.2
dss.loads_write_name("328365B0a")
loadshape = dss.loads_read_daily()

# Q2.3
dss.monitors_write_name("m1")
pa = dss.monitors_channel(1)
qa = dss.monitors_channel(2)
pb = dss.monitors_channel(3)
qb = dss.monitors_channel(4)
pc = dss.monitors_channel(5)
qc = dss.monitors_channel(6)

pt = np.array(pa) + np.array(pb) + np.array(pc)
qt = np.array(qa) + np.array(qb) + np.array(qc)

plt.plot(range(len(pt)), pt, "g", label="P")
plt.plot(range(len(qt)), qt, "b", label="Q")
plt.title("Daily Active and Reactive Poer at Feeder Head")
plt.legend()
plt.ylabel("kW, kvar")
plt.xlabel("Hour")
plt.grid(True)
plt.show()


print("Fim")
