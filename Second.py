from scipy.integrate import ode
import matplotlib.pyplot as plt


starts = [140, 140]
t1 = 12 * 2


def f(t, N):
    return -0.056 * N + 0.0004 * (N ** 2)

#                    1260
# N(t) = --------------------------
#         -2 * e ^(7 * x / 125) + 9

def solve(N0, t0=0, t1=1, h=0.05):
    r = ode(f).set_integrator('vode', method='bdf')
    r.set_initial_value(N0, t0)

    N = [N0]
    t = [t0]

    while r.successful() and r.t < t1:
        t.append(r.t + h)
        N.append(r.integrate(r.t + h))
    return N, t


plt.figure("Task 2")

for i in range(len(starts)):
    plt.subplot(2, 1, i + 1)
    N, t = solve(starts[i], t0=0, t1=t1, h=0.01)
    plt.title("N(0) = " + str(starts[i]))
    plt.plot(t, N)

figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
plt.show()
