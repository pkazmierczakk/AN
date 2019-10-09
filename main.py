import matplotlib.pyplot as plt
from tqdm import tqdm
from e_power_x import EPowerX

PRECISION = 10**-99

def H1():
    results_def_start = []
    results_def_end = []
    difference = []


    # e_powers = [i / 50000 for i in range(-500000, 500000)]
    e_powers = [i / 500 for i in range(-500, 500)]

    for x in tqdm(e_powers):
        epow = EPowerX(x, True, PRECISION)
        difference.append(abs(epow.compute_exp(method='def', reverse=False)) - abs(epow.compute_exp(method='def', reverse=True)))
        # results_def_start.append(epow.compute_exp(method='def', reverse=False))
        # results_def_end.append(epow.compute_exp(method='def', reverse=True))


    # plt.scatter(e_powers, results_def_start, label='Results from definitions summed from start', s=1)
    # plt.scatter(e_powers, results_def_end, label='Results from definitions summed from end', s=1)

    plt.scatter(e_powers, difference, label='Difference', s=1)

    p = 10 ** -15
    plt.ylim(-p, p)
    plt.yscale('linear')
    plt.ylabel('precision')
    plt.xlabel('x')
    plt.title('e^x')
    plt.legend()
    plt.show()


H1()
# pow = EPowerX(5, False, 10**-10)
# print('pow', pow.compute_exp())